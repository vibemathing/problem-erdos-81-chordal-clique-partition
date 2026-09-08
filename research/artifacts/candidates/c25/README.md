# C25: replay and statement map

Verdict: candidate_only. best_verified_result: none. No root or two-level target closure.

## Mathematical identity

`proof.md` concerns the capped two-prefix joint LP from C24. The target is an absolute K with nu_star-J<=K*r. That inequality remains open. The positive bound proved here is Q-J<=a+b for Q obtained by optimizing over an integral core packing and a fractional leaf-only allocation. The negative result concerns the additional requirement of permanently keeping the integral core triangles of a particular optimal extreme point. Its frozen-face gap is (8/19)*r*log_19(r), whereas the unrestricted joint gap of the same graph is exactly one. Allowing only s of those triangles to reopen can improve its objective by at most 2s. Temporary subtraction or unrestricted core reselection is not excluded.

The all-order construction is explicit: modulo-19 complete designs, Cartesian products of a fixed rook graph, and two finite triangle lists in `templates.json`. Both lists are checked as exact edge sets. Their historical discovery metadata reports floating MILP search; no floating optimum is used as a proof premise. The recorded new replays use only standard-library exact arithmetic and combinatorial checks.

## Inputs and actual execution

The two executable sources and the template were materialized from the frozen remote file contents and matched against their Git blob SHA-1 and byte length before the recorded executions. Their SHA-256 values are in `artifact-manifest.json` and the process records. No old partial archive or previously unconfirmed execution is used.

From this directory, with fresh output filenames, run:

```text
python extreme_audit.py --seconds 38 --out new-extreme-results.json
python freezing_checker.py --out new-freezing-results.json
```

The recorded runtime is CPython 3.13.5, one thread and a 1 GiB address-space cap. Use a bounded external process timeout as well (42 seconds was used). The first program enforces an internal 38-second wall limit and CPU limits 40/41 seconds; the second uses 32 seconds internally and CPU limits 35/36 seconds. Mathematical source versions are c25-exact-v2 and c25-freezing-exact-v2. Resource ceilings and finite loops are in the source; no network or repository writes are performed by these programs.

Two different exact LP implementations and two differently organized integer optimizers agree on every capped boundary-inclusive tuple with r<=4: counts 1,3,11,43,91, totaling 149 parameter representations. The separate leaf-only test covers 1056 residual graphs/prefix pairs and checks 164 charged fractional groups. The r=5 quarter-valued extreme point is one named extra case, not a complete fifth-order range. The product checker verifies k=1,2 (r=19,361), both local support ranks, the integer witnesses, fractional loads, parity and twelve rejection tests. General proofs, not these finite ranges, justify the all-order statements.

The executed programs, including the two implementations, share a candidate-generator trust domain. They are not two registered trusted verifiers. No continuous optimal face is exhausted and no general gap theorem is established by a successful process.

## Lossless representation of the first process output

The original `extreme-results-replayed.json` had 23313 bytes and SHA-256 `5cdd83711fd2b0f806fff44a8617b4b28819e34fc7afe1ae7ffdf90533bf9d2c`. Its contents are stored without loss as `extreme-table.csv` plus `extreme-report.json`, rather than a compressed archive. The report records all non-table fields, column types and a table digest. This code reconstructs the exact process-output bytes without running a mathematical solver:

```python
import csv, hashlib, io, json
from pathlib import Path
report = json.loads(Path('extreme-report.json').read_text())
raw = Path(report['parameter_table']['path']).read_bytes()
assert hashlib.sha256(raw).hexdigest() == report['parameter_table']['sha256']
rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8'))))
for row in rows:
    for key in report['parameter_table']['integer_columns']:
        row[key] = int(row[key])
assert len(rows) == report['parameter_table']['rows']
result = dict(report['result_without_parameter_rows'], parameter_rows=rows)
output = (json.dumps(result, sort_keys=True, indent=2) + '\n').encode('utf-8')
assert len(output) == report['original_output_bytes']
assert hashlib.sha256(output).hexdigest() == report['original_output_sha256']
with Path('reconstructed-extreme-results.json').open('xb') as handle:
    handle.write(output)
```

`freezing-results-replayed.json` is stored as the original process output. The two sanitized process records under `research/artifacts/source-notes/c25/` contain actual exit codes, budgets, elapsed time and input/output digests. Peak RSS at the inner reporting point and at process exit can differ; both are actual observations. Full output hashes include runtime metadata and need not recur on another machine even when all mathematical entries agree.

## Evidence and continuation

C24's model identity and leaf-color conversion have their own frozen proof. C25 rederives its conditional tangent-rank argument, charging injection, product construction, extreme-point uniqueness, integer upper/lower bounds and clique-partition values. Finite LP extremality/duality facts are standard mathematical inputs; no external design theorem, paper abstract or CI result substitutes for a proof step. Prior C22/C23 weak-asymptotic source audits are not an admission of the stronger statement.

First open obligation: bound nu_star-Q by an absolute constant times r with unrestricted core reselection, equivalently up to the proved 2r allowance bound nu_star-J. Any normal-form potential must charge objective loss, not the count of old integral triangles that are changed. General many-level charging remains unproved. Trusted source/semantic/closure gates and both stronger admitted obligations remain open.
