# C30 replay: exact p=1, q=2 fixed-budget slice

Status: NONTERMINAL_CHECKPOINT; verdict=candidate_only; best_verified_result=none.

The proof candidate determines L and Q for every r=3^k, k>=2, and every actual short set of cardinality 2..r. It does not close the whole uniform face or the ProblemContract root.

From a repository checkout with Python 3.13.5 (standard library only), use NEW output paths:

```sh
python research/artifacts/candidates/c30/checker.py construct --out construct-new.json
python research/artifacts/candidates/c30/checker.py lp --out lp-new.json
python research/artifacts/candidates/c30/checker.py controls --out controls-new.json
```

Each mode has a 38-second internal wall limit, 40/41-second CPU limits and a 1 GiB address-space cap. The recorded parent also enforces 43 seconds of wall time; this wrapper is not needed for the mathematical checking code. The outputs refuse overwriting existing files. The exact LP mode imports the immutable `c25/extreme_audit.py` only after SHA-256 checking and also checks the frozen `c27/twelfth-point.json`; neither dependency is duplicated here.

`construct-results.json` contains eight full nine-core witnesses (r core vertices, r+3 host vertices), complete finite range counters, named larger checks and exact support changes. `lp-results.json` contains both-LP agreement and residual primal/dual data; it does not claim a global Q search. `controls-results.json` lists the twelve rejected mutations and nine accepted boundary fixtures. `source-notes/c30/run-record.json` records real exit codes, times and byte identities. These are candidate-generator runs, not trusted attestations.

The full saturated fractional primal is supplied by explicit per-type formulas in proof.md; for every actual edge its incidence equation is checked. The new Q construction uses half short-triple weights and a full long parallel class, with no old support held fixed. The global upper certificate couples local parity charges to the fact that the residual core edge count is divisible by three.
