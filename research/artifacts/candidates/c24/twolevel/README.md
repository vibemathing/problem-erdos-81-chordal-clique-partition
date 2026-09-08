# Two-level C24 replay and proof map

Verdict: candidate_only. The mathematical proof is `proof.md`. The remaining open inequality is nu_star-J=O(r) for its edge-specific joint integer allocation J. The proven leaf conversion costs at most floor(a/2)+floor(b/2). Neither the full two-level gap theorem nor the root has been closed.

## Complete local text archive

`replay.part-01.b64` through `replay.part-04.b64` form ONE complete, explicitly indexed base64/XZ/UTF-8-JSON-map archive. `bundle-manifest.json` binds the transport bytes, compressed bytes, decoded JSON and all 15 flat member files. This archive is distinct from the older, incomplete `../replay-bundle.part-*.txt` files, which are not inputs to this proof or replay. No source paper, full chat, private reasoning, credential, machine pathname or raw process dump is encoded. The members are authored source code, concise mathematical tables/certificates and sanitized runtime metadata.

From this directory, choose an output directory that does not exist and run:

```text
python unpack.py --out replay-materialized
```

The decoder checks all sizes and hashes, duplicate keys, flat filenames, bounded decompression and exact member names before writing. It does not execute any decoded program. Its own successful unpacking is a byte-integrity check, not mathematics. The decoded JSON has 155710 bytes and SHA-256 5fa20b3eca2e4f412d1277bc6709e93f17663147fd021696edce96d16b370b87.

## Explicit bounded mathematical runs

Use Python 3.13.5 to reproduce the recorded environment; the code otherwise targets standard-library Python >=3.11. Execute inside `replay-materialized`. Programs enforce their declared CPU/wall/memory limits. Run outputs below should have NEW names or be run in a fresh copy so old frozen outputs remain intact.

```text
python twolevel_audit.py --min-n 4 --max-n 8 --seconds 40 --out replay-n4-n8.json
python twolevel_audit.py --min-n 9 --max-n 9 --seconds 40 --out replay-n9.json
python resume_n9.py --start 108 --stop 117 --out replay-n9-108-117.json
python resume_n9.py --start 117 --stop 126 --out replay-n9-117-126.json
python joint_audit.py --seconds 38 --out replay-joint.json
python examples.py
```

`examples.py` writes `examples-result.json`; preserve the supplied frozen file before that command, or run a second fresh decoded copy. Runtime thresholds need not produce the same partial prefix on another machine. The recorded initial order-nine process completed exactly rows 0..107 before its deadline; its outer exit code was not read back. Two separately completed indexed runs closed rows 108..125. A new replay must determine its actual missing indices rather than blindly declaring that these intervals close its own partial run. Each row index maps to the parameter list in `resume_n9.py`; exact tuple identities, not timing, determine completeness.

The stable mathematical summary is: positive-multiplicity two-prefix representations of total order 4..9 have counts 1,5,15,35,70,126 (252 total). `combined-table.csv` is the checked complete table. These are parameter representations, not isomorphism classes. The additional capped-core ranges r=2,3,4,5 have 2,14,42,108 tuples. The fan algorithm was checked on all 1100 labeled simple graphs of order at most five. The new joint audit executes 12 rejection tests and 27 strict improving trades for the previously known bad allocation family. Five degenerate/equal-level controls are in `examples-result.json`.

## Implementations and exact certificates

- `recovery_checker.py`: unchanged, content-hashed dependency from the supplied recovery package. Rational packing tableau, separately implemented equality-partition revised simplex, triangle-conflict integer packing and residual-edge clique partition. It is not the different main C23 source with 14 historical mutations.
- `orbit.py`: nine-edge-type rational LP and integer resource optimization. Fractional type projection/lifting is proved; integer realization is explicitly not presumed.
- `joint.py`: edge-specific fractional revised-basis LP, exact core/leaf matching dynamic program, constructive fan coloring and charged leaf lift.
- `twolevel_audit.py` and `resume_n9.py`: full parameter sweeps and precise partial-range continuation.
- `joint_audit.py`: complete capped-core comparison, fan graph sweep, charged matching checks and twelve newly authored mutations.
- `examples.py`: normalized nine-vertex primal/dual and integer certificate, J=9 allocation and its eight-triangle lifted packing, plus boundary controls.

The comparison uses exact fractions and primal/dual objective equality. Two differently implemented algorithms still share a candidate-generation trust domain; they are not two trusted verifiers. Hashing a certificate is not verification, and finite tests do not establish all-order claims. No continuous optimal face is exhaustively enumerated. The finite outputs contain runtime fields, so their complete file hashes need not repeat across machines even when every mathematical entry agrees.

## Prior materials and admission

C22/C23 remain proof-drafted/source-backed inputs concerning the weaker uniform o(n^2) theorem. This proof's new graph-specific reductions and fan argument are written out instead of taking that theorem as a premise. Prior C24 nested/subclass results and local obstructions are comparisons and regression inputs, not new results of this cycle. The uploaded 15-file earlier nested package was checked against its manifest, but those checks do not assert that every earlier archive was already complete on main. This PR makes no full-history transport-completeness claim.

Required GitHub checks validate only candidate transport. Natural-language mathematical review, statement faithfulness, any source attestation and any formal verification must come from a suitable registered trust-separated gate. No such receipt is manufactured by this package. Issue #1 and both admitted stronger obligations remain open.
