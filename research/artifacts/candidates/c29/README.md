# C29 mixed-core candidate: exact values and replay

Status: NONTERMINAL_CHECKPOINT; verdict=candidate_only; best_verified_result=none.

`proof.md` supplies general arguments and all-order scope. `seed27.json` contains the finite row-saturated mixed seed. `checker.py` checks actual edges and budgets using Fraction/integer arithmetic. Different LP implementations still share the generator trust domain.

## Reproduce the frozen checks

From the repository root, use a supported Linux CPython environment with the standard library. The recorded run was CPython 3.13.5. No numerical solver or external package is needed for replay. The checker enforces a 1 GiB address-space limit, CPU 39 seconds (hard 40) and an internal 36-second wall deadline. Each output path must not exist.

```sh
python research/artifacts/candidates/c29/checker.py --mode nine --out c29-nine-new.json
python research/artifacts/candidates/c29/checker.py --mode oneone --out c29-oneone-new.json
python research/artifacts/candidates/c29/checker.py --mode lift --out c29-lift-new.json
python research/artifacts/candidates/c29/checker.py --mode mutations --out c29-mutations-new.json
```

Use an outer process timeout of 43 seconds and one thread. Runtime measurements differ on a new execution, so whole-output byte digests are not expected to repeat: compare the mathematical result fields, dependency hashes and code version, and record a new process receipt. The published output files retain their original byte identities.

Only `nine` imports the pre-existing C25 exact module and reads the pre-existing C27 twelfth-point certificate, checking each SHA-256 first. Neither dependency is duplicated. The other modes need just checker.py and seed27.json. Missing dependencies or unsupported resource facilities fail explicitly, not as successful verification.

## Literal recorded scope

The nine-core instance has eleven total graph vertices. Its global Q value is proved by the parity-capacity inequality and matching witness, not a claimed exhaustive Q solver. Two rational LPs solve the symmetry quotient for L; a separately verified full edge primal/dual lifts it. Both rational LPs also solve the forced-zero-reduced residual leaf problem.

The p=q=1 replay covers all 114 cardinality parameters with r=9,27,81 and 2<=a<=r, nine named r=243 parameters, and all 502 actual nine-core subsets of size at least two, including the whole core. It does not enumerate all arbitrary two-level graphs.

The growing-budget lift has fifteen finite replay cases: complete extra-budget ranges for fiber orders one and three, plus eight named fiber-order-nine cases. The new all-order formula follows from the proof's Latin and affine constructions, not from those fifteen cases. The seed has L=J=Q=143 but actual nu=142. In the seed lift Q may retain fractional leaf variables. No general J or nu equality is inferred.

All four final modes exited zero. Twelve mutations were detected and nine boundary controls were accepted. An earlier combined full-edge revised-LP probe timed out with unknown child exit; the process record preserves that distinction. Seed discovery used a bounded floating MILP; its status is not a proof input. Replay instead checks the frozen explicit arrays exactly.

## Remaining gap

The whole low-budget uniform-face theorem is open. The saturated-seed lemma does not show existence of a suitable seed for every short proportion and budget, and a positive seed defect would scale quadratically. No arbitrary old support is frozen or protected, and support edit count is not a loss. No nonuniform, multilevel, root or trusted admission result is claimed.

All final new mathematical material and process summaries belong to this single C29 packet. This is not a transportation audit of older uncommitted packages.
