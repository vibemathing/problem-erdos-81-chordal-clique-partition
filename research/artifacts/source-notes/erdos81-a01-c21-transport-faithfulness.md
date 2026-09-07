# C21 transport provenance, coverage, and statement-faithfulness note

Status: candidate_only. Reconciliation date: 2026-09-07.
Base for the addendum: 2f7b0122c5df4169822195bb2dac9690fc471e8e.
This note documents transport and content mapping, not mathematical acceptance.

## Read-back sources and duplicate handling

The previously unconfirmed Issue writes really reached GitHub:
- https://github.com/vibemathing/problem-erdos-81-chordal-clique-partition/issues/1#issuecomment-5560952646
  Created and last updated 2026-09-06T17:34:52Z.
- https://github.com/vibemathing/problem-erdos-81-chordal-clique-partition/issues/1#issuecomment-5560997451
  Created and last updated 2026-09-06T17:43:02Z.

Their statements about missing readable receipts describe their earlier interaction, not the current repository state. Both comments were read from the live connected repository before this packaging. Only bounded mathematical arguments and their limitations are preserved, not the full comments or conversation.

| Existing material | Disposition |
|---|---|
| Fractional complete-split domination and exact B(n) extremum | Already in C18; referenced, not resubmitted |
| Fractional edge/triangle values and triangle-packing rounding identities | Already in C18; referenced, not relabeled as new |
| Dual slack and fractional extremizers | Already in C19; unchanged |
| Capacity maximization over feasible attachment vectors | Distinct proof variant preserved in C21 Section 2 |
| Dense-core whole-clique fractional certificate | Preserved in C21 Section 3 |
| All-r,t unrestricted fractional complete-split formula | Preserved in C21 Section 4 with primal and signed-dual certificates |
| J(r,2) integer incidence-rank certificate and near-n gap | Preserved in C21 Section 5 |
| One-vertex sum of J(3,2) blocks | Preserved in C21 Section 6; single-block result references C18 |
| Previously remote C20 candidate/source/packet | Recovered unchanged except PR binding; merged in PR #22 |
| C02 post-merge twelve-vertex draft | Original bytes recovered through PR #23; no duplication of old C02 candidate or packet |

The old C02 tail is the file `research/artifacts/candidates/erdos81-a01-c02-n12-continuation.md`, not a claim inferred from a chat summary. Its original Git blob 2071508db873dce682974bcf232e0979b04552a4 and all 15688 bytes were retained. The prior restricted conclusion remains a pending proof draft, not an executed enumeration.

## Mathematical semantics that are not changed by transport

The root asks for an INTEGER exact edge-clique partition with a uniform linear error. fcp/cp_f is a fractional all-clique relaxation. p3star/lambda restricts fractional pieces to edges and triangles. p3/p23 restricts integer pieces likewise. An equality-constrained fractional partition is not an overlapping cover. A signed dual is not an integer partition.

C21 preserves the separate sufficient rounding conditions without asserting either. Its J(r,2) examples are split graphs, so the gap cannot serve as a counterexample to same-order split domination. The rank argument is a proposed algebraic certificate whose assumptions and correctness still require review under the frozen contract.

C20 uses a weaker little-o quadratic remainder, with the original cited packing-theorem limitations intact. This reconciliation did not obtain or audit a new primary source. C18's existing LP source note, `research/artifacts/source-notes/erdos81-a01-c18-lp-faithfulness.md`, remains the declared LP reuse input; its old failed-screenshot limitation is neither erased nor represented as a successful replay.

## Artifact-class inventory and execution status

Previously generated mathematical material found for this reconciliation consists of proof drafts, symbolic primal/dual or rank certificates inside those drafts, source notes, packets, and Issue checkpoints. No untransported graph-enumerator program, input/output dataset, Lean/SMT source, solver log, or mathematical execution receipt was found in the supplied conversation material or inspected pending branches. None is fabricated to fill an artifact category.

No mathematical computation, enumeration, Lean/SMT run, or proof-audit program was replayed. All mathematical verification remains pending/unverified. Local UTF-8 hashing, Git-blob comparison, JSON preparation, and GitHub's real structural required checks are transport processing only.

Protected records and verifiers were not modified. Historical closed transport-smoke PR #2 and its retained branch are diagnostic, non-mathematical objects, not an unmerged research Candidate requiring resubmission. The branch is not deleted.

## Audit closure protocol

The companion `research/artifacts/source-notes/erdos81-transport-20260907-audit.json` records the reconciled inventory and the completed recovery transactions before this addendum's final merge. Its own hash and the final backfilled packet hash are recorded in the final Issue checkpoint to avoid self-referential hashes.

A claim that transport is current requires a final live read of main, open PRs, retained branch heads, the merged artifact blobs, and the Issue checkpoint. The creation of this note alone does not make that claim. Mathematical best_verified_candidate remains none and both admitted obligations stay open.
