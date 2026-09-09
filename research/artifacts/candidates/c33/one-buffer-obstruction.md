# C33 one-buffer midpoint-fan obstruction

This is a strict failure signature for one construction route, not a counterexample to the host theorem.

Let `U` be a wholly short fiber of order `m`, let `B` be the `b` short vertices in a second fiber, and put `D=floor(p/2)`. Consider any short-resource construction in which every resource triangle meeting `B` has type `UUB`, every point of `B` has exactly `D` resource-triangle incidences, and no `UUU` resource triangle is used.

There are exactly `bD` selected `UUB` triangles. Each contributes two triangle incidences to `U`, so the total triangle incidence on `U` is exactly `2bD`. A core vertex receives two short-resource edges per resource-triangle incidence. Hence the aggregate short-resource degree on `U` is exactly `4bD`.

For even `p=2D`, the total available short endpoint budget on `U` is `2Dm`. Before any edge-color repair, the unused short endpoint capacity on `U` is therefore

\[
 2Dm-4bD=2D(m-2b).
\]

For odd `p=2D+1`, it is

\[
 (2D+1)m-4bD=2D(m-2b)+m.
\]

Thus, whenever `b<m/2` and `D` is a positive linear fraction of `m`, this route has quadratic endpoint defect. Coloring cannot reduce endpoint deficit, and deleting a color only increases total defect. The mechanical midpoint choice may balance the incidences among vertices of `U`, but it cannot change their conserved total `2bD`.

A successful one-buffer construction must therefore introduce genuine `UUU` resource triangles and trade them against the surrounding Steiner decomposition while preserving pair ownership. Repeating midpoint fans, per-layer boundary deletion, or aggregate-degree coloring alone cannot close this regime.
