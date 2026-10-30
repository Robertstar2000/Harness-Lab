# EXT controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-EXT-01

Preserve declarative skills, profiles and packet contracts; hook contract is an additional extension surface.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-02

Preserve SKILL.md frontmatter, phase validation and independent suite checks.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-03

Reside only name/description/path metadata until activation; record path/environment trigger, source hash and loaded instruction token cost.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-04

MCP position: external integrations use host-provided MCP only when configured and tested. This portable package does not ship an MCP server; file packets remain the baseline.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-05

Publish hooks/v1: pre_tool may deny/rewrite only within original scope; post_tool redacts and appends observations; stop requires independent review. Hook timeout/error denies consequential execution. Hosts lacking hooks remain advisory and cannot claim enforced policy.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-06

Marketplace plugin packaging is not adopted; direct versioned downloads include index, license, dependency declarations and hashes. No claim of one-click host plugin installation.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-07

Install gate: verify provenance/license/hash, inspect archive paths and symlinks, declared tool/MCP dependencies, trust tier and injection scan. Unknown source goes to quarantine; human review promotes it. Fail closed on missing metadata.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-08

Agent-authored skills enter quarantine inbox with parent trace, diff, fixtures and reviewer. No self-install or policy relaxation; approved version supersedes prior definition.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-EXT-09

Profiles use deterministic precedence: platform safety floor → managed policy → user narrowing → project narrowing → packet narrowing. Conflicts deny; version/hash all effective configuration.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

