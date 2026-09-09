# C32 boundary-completion addendum

This addendum refines, but does not enlarge, the claims of `proof.md`.

## Period-owner correction

In Section 4.2, “changes no old owner” means **changes no owner outside the newly added coset**. Inside that coset, the chosen short-direction core lines are necessarily reassigned to short-leaf resource colors (with the same fixed local coloring and, for even multiplicity, the same deleted color). The period identity is local:

\[
S(a+m)-S(a)=\sigma_m(p),
\]

and no owner outside the new coset is touched.

## Zero short class

In Section 4.3, when `p=0`, choose the period `m=1`. The short packet and the residual term `pb` are both zero; only the long packet remains.

## Explicit small-complement check in the p=3 face proof

In Section 5.2, for the first polynomial

`c^2-4c+x(2c-q-4)+x^2`,

`c>=4` is coefficientwise nonnegative. At `c=3`, `2c+x=r>=9` gives `x>=3`; the values are `x^2-x-3` for `q=3` and `x^2-3` for `q=2`.

For the second polynomial

`c^2+c(q-5)+x(c-q-4)+x^2`,

at `q=2`, the cases `c=3,4,5` are `x(x-3)`, `x^2-2x+4`, and `x^2-x+10`; `c>=6` is coefficientwise nonnegative. At `q=3`, the cases `c=3,4,5,6` are `(x-1)(x-3)`, `x^2-3x+8`, `x^2-2x+15`, and `x^2-x+24`; `c>=7` is coefficientwise nonnegative.

## Exact next boundary object

Let three order-`m` fibers be `U,V,W`, with `U,V` wholly short and only `B subset W`, `|B|=b`, short. Put `d=floor(p/2)`. Removing the residual `pb` term while preserving one-use core ownership reduces to constructing transversal triples such that:

1. all three pair projections are simple;
2. every vertex of `B` has line-degree `d`;
3. vertices of `U,V` have line-degree at most `d` and internal triples complete their remaining degree with total deficiency `O(m)`;
4. the unused cross pairs complete to a transversal design;
5. after the single Vizing repair, the resource graph has `p` actual matching colors.

The three pair projections form a partial Latin square. Balanced proper edge coloring of the `B-U` incidence graph alone does not imply completion to a Latin square of the same order. Conversely, an arbitrary completion need not give balanced column and symbol degrees. This is the precise remaining high-multiplicity, nonperiodic boundary obligation.

Two shortcuts are already excluded by `proof.md`: selecting near-factor colors first has core defect at least `p(m-p)/2`, and an order-`N` fiber has only `N` full translation slots on a shared base edge. These are route obstructions, not counterexamples to the host theorem or root.
