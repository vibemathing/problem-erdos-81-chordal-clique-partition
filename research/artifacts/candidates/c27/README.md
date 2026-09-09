# C27 replay and scope

Verdict: candidate_only. `proof.md` proves a restricted affine-flag theorem on the uniform one-third full-dual face. It does NOT close the arbitrary-size face, the general two-level gap, or either admitted stronger obligation.

The core and prefix sizes in the main constructive theorem are powers of three (or empty prefixes). Budgets may be arbitrary integers satisfying the explicitly proved necessary inequalities. The defect is at most one per tagged endpoint, and equal prefixes admit a sharper combined charge. A separate at-most-two-core-vertex deletion corollary handles specified additional parity boundaries. No generic closeness-to-affine assumption is inferred from the face condition.

## Reproduction

Use a checkout containing the immutable C25 dependency at `research/artifacts/candidates/c25/extreme_audit.py`, whose SHA-256 is checked before import. The programs use standard-library Python, tested with CPython 3.13.5. From this directory:

```text
python uniform_face_checker.py --mode construct --out replay-construct.json
python uniform_face_checker.py --mode lp --out replay-lp.json
python padding_check.py --out replay-padding.json
```

Use new output names. The programs refuse to overwrite an existing output. They enforce CPU, wall and 1 GiB memory limits. Runtime-dependent full-output hashes can differ between machines; deterministic mathematical records should agree. A timeout must not be called a complete run.

The construct run completely covers affine parameter representations at r=1,3,9,27, counts 3,15,102,819 (939 total), including zero/equal prefixes and all admissible p,q for those size choices. It also checks eight named larger inputs, the r=81 support replacement, and twelve negative controls. It does not cover every arbitrary parameter tuple at these orders.

The LP run enumerates all 149 boundary-inclusive capped tuples through r=4 with two rational LP implementations. Exactly 72 of these attain the all-row one-third bound; Q is recomputed on those 72 by two core-mask/residual-LP methods. For r<3, 'all-row one-third bound attained' is the literal numerical test, not an assertion that every possible zero-priced dual has that form. The named r=7 point is outside that complete range: it has 28 positive columns of full rank and denominators through 12. Its Q optimum is NOT computed.

The padding run checks three specified deletion witnesses and their full one-third face membership. It reports feasible Q values, not Q optima. It gives no all-size nonaffine theorem.

The exact twelfth point was found by bounded lexicographic Fraction simplex search and then frozen in `twelfth-point.json`. Proof use is direct verification of the displayed feasible primal, all-one-third dual and support rank; no random search conclusion or floating-point optimum is imported. Earlier exploratory searches did not constitute complete parameter enumerations.

## Trust and previous material

All programs share the generator trust domain. Their success is not a registered verifier receipt. The algebraic line partition and charging proof, not the finite tests, supplies the all-order restricted claim. No source/external design theorem is used to fill the remaining arbitrary-size gap.

The previous C26/value-reservoir recovery package remains distinct from the merged dense-core C26 and from this C27 transaction. Its 14 supplied file hashes were verified and its main path returned 404 at the fresh base. This PR does not claim to have transported that entire earlier package. No old counterexample, code dependency, or previous packet is re-submitted here. The new packet binds only C27.
