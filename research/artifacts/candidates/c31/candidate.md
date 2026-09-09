# C31 canonical claim artifact

For r=3^k (k>=2), p=q=2, and any actual short set A of size a>=3, let L be the fractional triangle-packing optimum and Q the joint optimum with integral core triangles but aggregated leaf resources.

The merged C28 face criterion (with direct c=0,1,2 boundary formulas recorded in proof.md) gives
L=(C(r,2)+2a+2r)/3.

Write a=3t+b, b in {0,1,2}. Relabel the core by F_3^k, choose two distinct affine parallel classes D0,D1, choose t triples of D1 wholly inside the relabeled A, and mark b further short vertices. Take every affine line except D0 and those t D1 triples as the integer core packing. Put beta=1 on D0 edges and alpha=1 on the chosen D1 edges. Every core edge has one owner, every long endpoint has degree 2, and only the b remainder short vertices miss degree 2. Hence S_core=S_long=0, S_short=2b and L-Q<=2b/3<=4/3.

This aggregate Q point is generally not an actual host packing because each resource graph contains triangles. General continuation lemma: if an integral aggregate resource graph H for m identical leaves has an edge set R such that chi'(H-R)<=m, deleting R and coloring H-R converts it to actual leaf matchings with objective loss exactly |R|; this repair is charged once to H, not once per leaf.

Here both aggregate resource graphs are disjoint unions of triangles. Delete one edge per component. Then |R_beta|=r/3 and |R_alpha|=t, and the remaining paths are 2-edge-colorable. The resulting actual host triangle packing has
S_core=r/3+t, S_short=2t+2b, S_long=2r/3,
so S_total=r+a+b<=2r+2 and therefore
nu_star-nu<=(r+a+b)/3<=(2r+2)/3.

This proves only the fixed p=q=2 atom. The iterative condition for growing multiplicities is to construct aggregate resource graphs with total edge-coloring deficiency sum rho_m(H)=O(r) independently of the number of individual leaves. That growing-layer invariant, the full one-third face, exact split domination, and the ProblemContract root remain open.

Status: candidate_only; best_verified_result=none.
