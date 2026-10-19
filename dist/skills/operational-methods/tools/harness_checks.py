#!/usr/bin/env python3
"""Local record checks. No model calls, network, action execution, or authorization.

Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.
"""
import argparse
import hashlib
import json
import math
import re
import sys
from collections import defaultdict, deque
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: nonempty string required")
    return value


def number(value, label, minimum=0):
    require(type(value) in (int, float) and math.isfinite(value) and value >= minimum,
            f"{label}: finite number >= {minimum} required")
    return value


def rows(value, label, nonempty=True):
    require(isinstance(value, list) and (bool(value) or not nonempty), f"{label}: list required")
    require(all(isinstance(row, dict) for row in value), f"{label}: object rows required")
    return value


def ids(value, label, nonempty=True):
    require(isinstance(value, list) and (bool(value) or not nonempty), f"{label}: ID list required")
    for item in value:
        text(item, label)
    require(len(set(value)) == len(value), f"{label}: duplicate IDs")
    return value


def index(value, label, field="id"):
    result = {}
    for row in rows(value, label):
        key = text(row.get(field), f"{label}.{field}")
        require(key not in result, f"{label}: duplicate {key}")
        result[key] = row
    return result


def graph_data(data):
    require(data.get("edge_direction") == "prerequisite_to_dependent", "Declare prerequisite_to_dependent edges")
    nodes = index(data.get("nodes"), "nodes")
    edges = rows(data.get("edges"), "edges", nonempty=False)
    for edge in edges:
        require(edge.get("from") in nodes and edge.get("to") in nodes, "Dangling graph edge")
        text(edge.get("kind"), "edge.kind")
        require(type(edge.get("propagates_change")) is bool, "Edge must declare propagates_change")
    return nodes, edges


def graph_context(data, seed, depth=2):
    nodes, edges = graph_data(data)
    require(seed in nodes, "Unknown seed")
    require(type(depth) is int and 0 <= depth <= 10, "Depth must be 0..10")
    require(nodes[seed].get("status") == "approved", "Context seed is not approved")
    adjacent = defaultdict(set)
    for edge in edges:
        adjacent[edge["from"]].add(edge["to"])
        adjacent[edge["to"]].add(edge["from"])
    seen, queue = {seed}, deque([(seed, 0)])
    while queue:
        item, level = queue.popleft()
        if level == depth:
            continue
        for other in sorted(adjacent[item]):
            if other not in seen and nodes[other].get("status") == "approved":
                seen.add(other)
                queue.append((other, level + 1))
    return {"nodes": [nodes[k] for k in sorted(seen)], "note": "Approved records, not certified facts; enforce access before calling"}


def change_impact(data, seed):
    nodes, edges = graph_data(data)
    require(seed in nodes, "Unknown seed")
    adjacent = defaultdict(set)
    for edge in edges:
        if edge["propagates_change"]:
            adjacent[edge["from"]].add(edge["to"])
    seen, queue = {seed}, deque([seed])
    while queue:
        for other in sorted(adjacent[queue.popleft()]):
            if other not in seen:
                seen.add(other)
                queue.append(other)
    return {"changed_seed": seed, "requires_revalidation": sorted(seen - {seed}), "modified_records": 0}


def rank_tree(data):
    nodes = index(data.get("nodes"), "nodes")
    limits = data.get("limits")
    require(isinstance(limits, dict), "Missing search limits")
    for key in ("max_nodes", "max_depth", "beam_width"):
        require(type(limits.get(key)) is int and 1 <= limits[key] <= 10000, f"Invalid limit: {key}")
    require(len(nodes) <= limits["max_nodes"], "Node budget exceeded")
    roots = [n for n, row in nodes.items() if row.get("parent_id") is None]
    require(len(roots) == 1, "Exactly one root required")
    children = defaultdict(list)
    viable = {}
    for key, row in nodes.items():
        text(row.get("summary"), "candidate.summary")
        score = number(row.get("score"), "candidate.score")
        require(score <= 1, "Scores must be normalized to 0..1")
        require(type(row.get("hard_constraints_pass")) is bool, "Declare hard-constraint result")
        parent = row.get("parent_id")
        if parent is not None:
            require(parent in nodes, "Unknown parent")
            children[parent].append(key)
        visited, cur, depth, passes = set(), key, 0, True
        while cur is not None:
            require(cur not in visited, "Tree cycle")
            require(cur in nodes, "Unknown ancestor")
            visited.add(cur)
            passes = passes and nodes[cur].get("hard_constraints_pass") is True
            cur = nodes[cur].get("parent_id")
            depth += 1
        require(depth - 1 <= limits["max_depth"], "Depth budget exceeded")
        viable[key] = passes
    require(all(len(v) <= limits["beam_width"] for v in children.values()), "Branch-width budget exceeded")
    candidates = [n for n in nodes if n != roots[0] and n not in children and viable[n]]
    require(bool(candidates), "No viable non-root leaf")
    candidates.sort(key=lambda n: (-nodes[n]["score"], n))
    return {"ranked_candidates": candidates, "recommended_for_review": candidates[0], "approved": False,
            "note": "Ranks supplied records; does not generate or validate model reasoning"}


def reconcile_pairs(data):
    text(data.get("configuration_id"), "configuration_id")
    occurrence = index(data.get("occurrences"), "occurrences", "ref")
    parts = index(data.get("parts"), "parts", "ref")
    require(set(occurrence) == set(parts), "Orphan occurrence or parts row")
    for ref in occurrence:
        for row in (occurrence[ref], parts[ref]):
            text(row.get("part_id"), "part_id")
            require(type(row.get("quantity")) is int and row["quantity"] > 0, "Positive integer quantity required")
        require(occurrence[ref]["part_id"] == parts[ref]["part_id"], f"Part mismatch: {ref}")
        require(occurrence[ref]["quantity"] == parts[ref]["quantity"], f"Quantity mismatch: {ref}")
    return {"reconciled_references": sorted(parts), "external_engineering_checks_verified": False}


def check_document(data):
    facts = index(data.get("facts"), "facts")
    sections = index(data.get("sections"), "sections")
    sources = set(ids(data.get("sources"), "sources"))
    dependencies = {}
    for key, row in sections.items():
        text(row.get("title"), "section.title")
        text(row.get("description"), "section.description")
        ids(row.get("acceptance"), "section.acceptance")
        deps = ids(row.get("depends_on"), "depends_on", nonempty=False)
        require(set(deps) <= set(sections), f"Unknown section dependency: {key}")
        dependencies[key] = set(deps)
        require(set(ids(row.get("source_ids"), "source_ids", nonempty=False)) <= sources, "Unknown source")
        for usage in rows(row.get("facts"), "section.facts", nonempty=False):
            require(usage.get("id") in facts, "Unknown fact")
            canonical = facts[usage["id"]]
            require("value" in canonical and "unit" in canonical and "value" in usage and "unit" in usage,
                    "Fact must include value and unit")
            require(type(usage["value"]) is type(canonical["value"]) and usage["value"] == canonical["value"]
                    and usage["unit"] == canonical["unit"], f"Fact conflict: {usage['id']}")
    done = set()
    while len(done) < len(sections):
        ready = {k for k, v in dependencies.items() if k not in done and v <= done}
        require(bool(ready), "Section dependency cycle")
        done.update(ready)
    return {"section_count": len(sections), "plan_consistent": True, "rendered_document_checked": False}


def check_gate(data):
    require(data.get("schema_version") == "mars-harness-handoff/1.0", "Unsupported handoff schema")
    for key in ("packet_id", "baseline_id", "producer", "reviewer"):
        text(data.get(key), key)
    require(data["producer"] != data["reviewer"], "Author cannot be independent reviewer")
    require(data.get("status") == "approved" and data.get("independent_review_passed") is True, "Independent approval not declared")
    require(data.get("blocking_findings") == [], "Blocking findings unresolved or not supplied")
    ids(data.get("artifact_ids"), "artifact_ids")
    for test_id, test in index(data.get("acceptance_tests"), "acceptance_tests").items():
        require(test.get("passed") is True, f"Acceptance test did not pass: {test_id}")
        ids(test.get("evidence_ids"), "test.evidence_ids")
    require(type(data.get("human_approval_required")) is bool, "Declare human approval requirement")
    if data["human_approval_required"]:
        approval = data.get("human_approval")
        require(isinstance(approval, dict) and approval.get("approved") is True, "Human approval not declared")
        text(approval.get("owner"), "approval.owner")
        text(approval.get("record_id"), "approval.record_id")
    return {"declared_gate_fields_complete": True, "identity_and_evidence_authenticated": False,
            "note": "Consumer must authenticate approvals and inspect real evidence before promotion"}


def check_policy(data):
    require(data.get("risk") == "low", "Human review required for non-low-risk action")
    require(data.get("explicitly_authorized") is True, "No explicit authority declared")
    action = text(data.get("action"), "action")
    require(action in {"read_local", "analyze_local", "write_scratch"}, "Action not eligible for local automatic handling")
    require(action in ids(data.get("allowed_actions"), "allowed_actions"), "Action not allowed by policy")
    for key in ("limits", "used", "proposed"):
        require(isinstance(data.get(key), dict), f"Missing {key}")
    for metric in ("calls", "cost_usd", "elapsed_seconds"):
        cap = number(data["limits"].get(metric), f"limits.{metric}")
        used = number(data["used"].get(metric), f"used.{metric}")
        proposed = number(data["proposed"].get(metric), f"proposed.{metric}")
        if metric == "calls":
            require(all(type(v) is int for v in (cap, used, proposed)), "Call counts must be integers")
        require(used + proposed <= cap, f"Budget exceeded: {metric}")
    return {"declared_policy_within_bounds": True, "authorized_or_executed_by_this_check": False,
            "note": "Advisory only; actual runtime permissions and human authority still govern"}


def check_replay(data, root):
    root = Path(root).resolve(strict=True)
    require(root.is_dir(), "Replay root must be a directory")
    manifest = index(data.get("files"), "files", "path")
    for relative, row in manifest.items():
        require(not Path(relative).is_absolute(), "Manifest paths must be relative")
        path = (root / relative).resolve(strict=True)
        require(path.is_relative_to(root) and path.is_file(), "Artifact outside root or not a regular file")
        digest = row.get("sha256")
        require(isinstance(digest, str) and re.fullmatch(r"[a-f0-9]{64}", digest), "Invalid SHA256")
        h = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                h.update(block)
        require(h.hexdigest() == digest, f"Hash mismatch: {relative}")
    return {"verified_files": sorted(manifest), "execution_replayed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["graph", "impact", "tree", "pairs", "document", "gate", "policy", "replay"])
    parser.add_argument("input", type=Path)
    parser.add_argument("--seed")
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as stream:
            data = json.load(stream)
        require(isinstance(data, dict), "Top-level object required")
        if args.command == "graph":
            result = graph_context(data, args.seed, args.depth)
        elif args.command == "impact":
            result = change_impact(data, args.seed)
        elif args.command == "replay":
            result = check_replay(data, args.root)
        else:
            result = {"tree": rank_tree, "pairs": reconcile_pairs, "document": check_document,
                      "gate": check_gate, "policy": check_policy}[args.command](data)
        print(json.dumps({"ok": True, "scope": "local-record-check-only", "result": result}, indent=2))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({"ok": False, "scope": "local-record-check-only", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
