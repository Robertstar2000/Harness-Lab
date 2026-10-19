"""Synthetic utility tests, not domain validation. SPDX-License-Identifier: Apache-2.0."""
import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("checks", ROOT / "tools/harness_checks.py")
checks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checks)


def example(name):
    return json.loads((ROOT / "templates" / (name + ".json")).read_text())


class HarnessChecks(unittest.TestCase):
    def test_graph_filters_drafts(self):
        result = checks.graph_context(example("memory-graph"), "claim:power", 2)
        self.assertEqual({n["id"] for n in result["nodes"]}, {"claim:power", "req:power-budget"})

    def test_graph_requires_approved_seed(self):
        with self.assertRaises(ValueError):
            checks.graph_context(example("memory-graph"), "design:power")

    def test_graph_rejects_dangling_edges(self):
        data = example("memory-graph"); data["edges"][0]["to"] = "missing"
        with self.assertRaises(ValueError): checks.change_impact(data, "claim:power")

    def test_impact_includes_draft_dependents(self):
        self.assertEqual(checks.change_impact(example("memory-graph"), "claim:power")["requires_revalidation"],
                         ["design:power", "req:power-budget", "task:review"])

    def test_impact_cycle_terminates(self):
        data = example("memory-graph")
        data["edges"].append({"from": "task:review", "to": "claim:power", "kind": "feedback", "propagates_change": True})
        self.assertEqual(len(checks.change_impact(data, "claim:power")["requires_revalidation"]), 3)

    def test_association_does_not_propagate(self):
        data = example("memory-graph"); data["edges"][0]["propagates_change"] = False
        self.assertEqual(checks.change_impact(data, "claim:power")["requires_revalidation"], [])

    def test_tree_hard_constraints_override_score(self):
        self.assertEqual(checks.rank_tree(example("decision-tree"))["recommended_for_review"], "option-a")

    def test_tree_budget(self):
        data = example("decision-tree"); data["limits"]["max_nodes"] = 1
        with self.assertRaises(ValueError): checks.rank_tree(data)

    def test_tree_cycle(self):
        data = example("decision-tree"); data["nodes"][1]["parent_id"] = "option-a"
        with self.assertRaises(ValueError): checks.rank_tree(data)

    def test_tree_nonfinite_score(self):
        data = example("decision-tree"); data["nodes"][1]["score"] = float("nan")
        with self.assertRaises(ValueError): checks.rank_tree(data)

    def test_pairs_good(self):
        self.assertEqual(checks.reconcile_pairs(example("paired-artifacts"))["reconciled_references"], ["ITEM-001"])

    def test_pairs_quantity_mismatch(self):
        data = example("paired-artifacts"); data["parts"][0]["quantity"] = 3
        with self.assertRaises(ValueError): checks.reconcile_pairs(data)

    def test_pairs_orphan(self):
        data = example("paired-artifacts"); data["parts"][0]["ref"] = "ORPHAN"
        with self.assertRaises(ValueError): checks.reconcile_pairs(data)

    def test_document_good(self):
        self.assertEqual(checks.check_document(example("document-plan"))["section_count"], 2)

    def test_document_fact_drift(self):
        data = example("document-plan"); data["sections"][0]["facts"][0]["unit"] = "days"
        with self.assertRaises(ValueError): checks.check_document(data)

    def test_document_cycle(self):
        data = example("document-plan"); data["sections"][0]["depends_on"] = ["section:method"]
        with self.assertRaises(ValueError): checks.check_document(data)

    def test_document_unknown_source(self):
        data = example("document-plan"); data["sections"][0]["source_ids"] = ["fabricated"]
        with self.assertRaises(ValueError): checks.check_document(data)

    def gate_fixture(self):
        data = example("handoff-packet")
        data.update(packet_id="fixture:1", baseline_id="fixture:base", producer="author:one", reviewer="reviewer:two",
                    status="approved", independent_review_passed=True, blocking_findings=[], artifact_ids=["fixture:artifact"],
                    acceptance_tests=[{"id": "test:1", "passed": True, "evidence_ids": ["fixture:test-log"]}],
                    human_approval={"approved": True, "owner": "fixture:owner", "record_id": "fixture:approval"})
        return data

    def test_gate_draft_template_blocked(self):
        with self.assertRaises(ValueError): checks.check_gate(example("handoff-packet"))

    def test_gate_declared_fields_only(self):
        result = checks.check_gate(self.gate_fixture())
        self.assertFalse(result["identity_and_evidence_authenticated"])

    def test_gate_self_review_blocked(self):
        data = self.gate_fixture(); data["reviewer"] = data["producer"]
        with self.assertRaises(ValueError): checks.check_gate(data)

    def test_gate_empty_tests_blocked(self):
        data = self.gate_fixture(); data["acceptance_tests"] = []
        with self.assertRaises(ValueError): checks.check_gate(data)

    def test_gate_missing_human_approval(self):
        data = self.gate_fixture(); data["human_approval"]["approved"] = False
        with self.assertRaises(ValueError): checks.check_gate(data)

    def test_policy_requires_authority(self):
        with self.assertRaises(ValueError): checks.check_policy(example("run-policy"))

    def test_policy_advisory_only(self):
        data = example("run-policy"); data["explicitly_authorized"] = True
        self.assertFalse(checks.check_policy(data)["authorized_or_executed_by_this_check"])

    def test_policy_projected_budget(self):
        data = example("run-policy"); data["explicitly_authorized"] = True; data["proposed"]["calls"] = 11
        with self.assertRaises(ValueError): checks.check_policy(data)

    def test_policy_external_action_blocked(self):
        data = example("run-policy"); data.update(explicitly_authorized=True, action="purchase", allowed_actions=["purchase"])
        with self.assertRaises(ValueError): checks.check_policy(data)

    def test_replay_good_and_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.txt"; path.write_text("fixture")
            data = {"files": [{"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}]}
            self.assertFalse(checks.check_replay(data, directory)["execution_replayed"])
            data["files"][0]["sha256"] = "0" * 64
            with self.assertRaises(ValueError): checks.check_replay(data, directory)

    def test_replay_escape_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "root"; root.mkdir()
            outside = Path(directory) / "outside"; outside.write_text("fixture")
            data = {"files": [{"path": "../outside", "sha256": hashlib.sha256(outside.read_bytes()).hexdigest()}]}
            with self.assertRaises(ValueError): checks.check_replay(data, root)

    def test_replay_empty_template_rejected(self):
        with self.assertRaises(ValueError): checks.check_replay(example("run-manifest"), ROOT)

    def test_duplicate_ids_rejected(self):
        data = example("memory-graph"); data["nodes"].append(copy.deepcopy(data["nodes"][0]))
        with self.assertRaises(ValueError): checks.graph_context(data, "claim:power")


if __name__ == "__main__":
    unittest.main()
