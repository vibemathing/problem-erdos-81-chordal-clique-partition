# C32 affine direction packets

Candidate-only continuation after merged C31.

Main claims:
- actual-host packings, not aggregate Q/J points, for p=3,q=2 and p=q=3 on every actual short set;
- full one-third-face bound `nu_star-nu <= [a+r+2(a mod 3)]/3` for a>=4;
- a period-m affine direction-packet theorem whose full-block defect is below 3r independently of growing p,q;
- an arbitrary-cardinality corollary through `p(p+1)<=r` with defect below 6r;
- exact even edge-color repair, translation-slot ownership, and a quadratic obstruction to selecting near-factor colors first.

Files:
- `candidate.md`: theorem-sized handoff;
- `proof.md`: complete proof draft, dependency DAG, pressure tests, and limits;
- `checker.py`: exact standard-library finite checker;
- `certificates.json`: frozen edge-color and exact repair certificates;
- `construct-results.json`, `controls-results.json`: final bounded outputs.

No trusted verifier, EvidenceLink, Result, Solution, split-domination theorem, or ProblemContract closure is claimed.
