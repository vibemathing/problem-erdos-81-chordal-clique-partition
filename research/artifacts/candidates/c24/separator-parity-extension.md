# C24 extension: additive separator budget and order-minimal local failure

Candidate ID: `candidate:erdos81-a01-c24-separator-parity-extension`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport obligation: `obligation:erdos81-split-extremal-reduction`
Base: `09c2b6f3e277eb20fc34d0add65ee8d027c5bb37`
Primary owner: math-proof. Verdict: candidate_only. Best verified result: none.

## 1. Statement identities and dependency boundary

Graphs are finite and simple; isolated vertices are allowed. All packings below are EDGE-disjoint. A clique partition partitions edges exactly once, with vertex reuse allowed. Define nu as the maximum integer triangle packing size, nu_star as its nonnegative fractional capacity-one analogue, delta=nu_star-nu, p23 as the integer edge/triangle partition number, and lambda as its fractional equality-constrained version. The empty graph has all these parameters zero. Put B(n)=floor(n(n+1)/6).

The companion `proof.md`, Sections 2-3, gives a complete written re-derivation of cp<=p23=m-2nu, lambda=m-2nu_star, lambda<=B(n) on chordal graphs, and the uniform, source-backed weaker theorem: for every eta>0 there is N_eta such that every n-vertex chordal graph, n>=N_eta, has cp<=(1/6+eta)n^2. It does not assume C22's conclusion. It includes the signed dual, arbitrary-clique-suffix PEO, both split certificates, every small denominator boundary, the fixed-epsilon source interface, and the all-optimal-dual/maximizer low-core argument.

The stronger statement delta(G)<=C*n on ALL chordal graphs is sufficient for the root cp<=n^2/6+C'*n, but is not claimed equivalent to it. Neither statement implies exact same-order split domination by itself. This extension proves restricted linear estimates and excludes two specified local lemmas. It does not close either admitted obligation.

This is generator-authored mathematics and actual finite generator-side execution, not trust-separated verification or admission. The general separator and complete-graph constructions below have direct proofs; their finite tests are not used as substitutes for those proofs.

## 2. An explicit complete-graph packing with linear leave

For every odd positive q construct triples on Z_q times Z_3 as follows. Use the q vertical triples {(x,0),(x,1),(x,2)}. For every unordered distinct pair {x,y} and every i in Z_3, use {(x,i),(y,i),((x+y)/2,i+1)}, where division by two is in Z_q.

This is a pair partition. A same-level pair occurs in its unique displayed nonvertical triple. An unordered pair on different levels has a unique orientation (i,i+1) modulo three. If its first coordinates agree, it occurs only vertically. Otherwise, for ((x,i),(z,i+1)), the unique other first coordinate is y=2z-x, distinct from x. Thus it occurs in one nonvertical triple. No repeated point or missing pair occurs. The q=1 case consists solely of a vertical triple.

For K_b, b>=3, choose v>=b least with v congruent to 3 modulo 6. Then d=v-b satisfies 0<=d<=5 and the construction above supplies a triangle decomposition of K_v. Delete d vertices and retain triples disjoint from them. A retained edge is uncovered exactly when its original triple contained one deleted vertex. For each deleted vertex the retained pairs so arising are a matching and number at most b/2. Therefore the leave L has at most d*b/2 edges. Constant triangle weights 1/(b-2) show nu_star(K_b)=binom(b,2)/3, so

    delta(K_b) <= |L|/3 <= d*b/6 <= 5*b/6.              (S1)

For b=0,1,2 the gap is zero, and (S1) still holds. This is an explicit bounded finite construction at each order; it invokes no external design-existence theorem. The replay checks pair uniqueness and the restricted leave for every b from zero through 64.

## 3. A separator-loss inequality with a consumable budget

Suppose a graph is assembled successively from induced pieces G_1,...,G_p. When adding G_i, its vertex intersection with the previous union is a clique S_i of size k_i, and there are no edges between the new vertices and old vertices outside S_i. The intersection graph is exactly the same clique in both pieces. Empty intersections are allowed. This includes a rooted clique-tree decomposition with its running-intersection property.

Every triangle of the union is contained in some piece. Indeed, a triangle meeting both new vertices and old vertices outside S_i would require a forbidden cross edge; otherwise it is in the new piece or the previous union. Induction proves the assertion. Assign each triangle in a fractional packing to one containing piece. On each piece the assigned weights form a feasible fractional packing. Hence

    nu_star(G) <= sum_i nu_star(G_i).                   (S2)

For every i choose a maximum integer packing in G_i. Initially keep all their triangle occurrences, allowing repeated edges between different pieces. If an edge has at least two occurrences, delete one triangle using it. Charge this deletion to one excess occurrence of that edge. The total excess sum_e max(0,occurrences(e)-1) strictly decreases; the process terminates, and at most its initial value triangles were removed.

If an edge belongs to mu_e pieces, its initial packing multiplicity is at most mu_e. Sequential gluing increases sum_e(mu_e-1) by exactly binom(k_i,2) at step i, because precisely the separator edges are duplicated. Thus the initial excess is at most sum_(i>1) binom(k_i,2). At termination the surviving triangles form a legal packing, giving

    nu(G) >= sum_i nu(G_i) - sum_(i>1) binom(k_i,2).

Together with (S2), this proves

    delta(G) <= sum_i delta(G_i) + sum_(i>1) binom(k_i,2). (S3)

Each discarded triangle is charged once to an actual duplicate-edge token. The proof does not assume separator capacities can be spent independently, and does not discard a quadratic quantity under the name of a linear error. Nonnegative integer excess is the termination monovariant. All internal edges and piece membership remain unchanged.

For complete clique-tree bags of sizes b_i, the vertex identity is sum_i b_i=n+sum_(i>1)k_i. Substituting (S1) into (S3) yields

    delta(G) <= 5*n/6 + sum_(i>1)(k_i^2/2+k_i/3).         (S4)

Consequently, for any FIXED K>=0, all chordal graphs supplied with such a decomposition satisfying sum k_i^2<=K*n obey

    delta(G) <= 5*(1+K)*n/6,
    cp(G) <= n^2/6 + (11+10*K)*n/6.                    (S5)

Here k_i<=k_i^2 for nonnegative integer k_i, and cp<=B(n)+2delta, B(n)<=n^2/6+n/6. The constants are uniform within this explicitly restricted class. No assertion that every chordal graph has linear separator-square budget is made. A chordal graph has a clique-tree representation by the standard induction which attaches a simplicial vertex's clique to a bag containing its later-neighbor clique; alternatively (S3)-(S5) can simply be checked against a supplied decomposition.

There is a more useful mixed-piece variant. The explicit matching constructions in `proof.md` Section 4 show that a piece within d_i edge edits of a low-core complete split graph J(r_i,t_i), t_i>=r_i-1, has delta(G_i)<=gamma_i+d_i. Here gamma_i=0 except at odd r_i,t_i=r_i-1, where gamma_i=(r_i-1)/2<=(n_i-1)/4. Combining with (S3) gives

    delta(G) <= sum_i gamma_i + sum_i d_i
                + sum_(i>1) binom(k_i,2).              (S6)

When all joins are at one vertex, all separator corrections vanish and n-1=sum_i(n_i-1), recovering delta<=(n-1)/4+sum_i d_i. Large repeated separators need grouping or another potential. For example the naive maximal-clique tree of J(r,2r) repeats the same r-clique many times, although the graph as a single split piece has zero gap. This is why (S4) is not a solution of the general problem.

## 4. Order-eight exact failures and full certificates

The unchanged C23 source was run with both rational LP formulations and separate integer optimizers on all 532 chordal isomorphism classes through order seven. The additional `local_step_audit.py` uses that frozen table and generates all 2119 chordal isomorphism classes of order eight by simplicial extension with exact isomorphism canonicalization. Completeness follows inductively from existence of a simplicial vertex; no sampling replaces the level. It computes nu_star by an exact packing LP with matching primal/dual certificates and nu by exhaustive triangle-conflict search on every order-eight graph. It checks all 8901 simplicial-vertex deletions at order eight.

No jump delta(G)-delta(G-v)>1 occurs through order seven. At order eight it finds 15 violating vertex pairs in five isomorphism classes, with maximum jump 5/3. Therefore order eight is the minimum under this finite, exact, generator-side completeness check for the lemma with constant one. The simpler unbounded-constant failure below is a separate symbolic proof.

The simplest witness is K8 versus K7. Their only maximal clique is their full vertex set. All their nonempty-edge cliques are exactly its subsets of size at least two. The values are

    K7: (nu,nu_star,cp)=(7,7,1),
    K8: (nu,nu_star,cp)=(8,28/3,1).

Use vertices 0,...,6 for K7. Its packing 012,034,056,135,146,236,245 covers all 21 edges. On 0,...,7 the eight triangles 012,345,037,256,064,175,136,247 leave exactly 05,14,23,67. Since every degree of K8 is odd, any triangle packing leaves at least four edges; hence eight is maximum. Uniform triangle weights 1/6 attain 28/3, bounded above by total edge capacity divided by three. The full clique gives cp=1. Thus the single simplicial step has gap jump 4/3>1.

A second witness directly excludes uncorrected clique-bag additivity. Let A={1,2,3,4,5,6,7} be a K7 and add vertex 0 adjacent exactly to {3,4,5,6,7}. Its maximal cliques are A and {0,3,4,5,6,7}, with separator {3,4,5,6,7}. The exact values are

    (n,m,nu,nu_star,lambda,p23,cp)=(8,26,7,26/3,26/3,12,6).

The replay certificate gives all cliques, exact fractional primal/dual vectors, integer packings and partitions. It independently solves the equality LP, rather than assigning lambda from nu_star. A direct integer upper bound uses the six odd-degree vertices: a packing leaves at least three edges and hence has at most floor((26-3)/3)=7 triangles. The six-piece upper partition uses K7 and the five spokes at 0. For a direct lower proof, restrict a proposed partition to the induced K7 minus edge 01 on {0,1,3,4,5,6,7}. Write a=5 for its common core size and u,v for the missing pair. If one endpoint belongs to a single piece, that piece contains the entire core and the other endpoint requires a distinct piece for each of its a spokes, giving at least a+1 pieces. Otherwise every vertex has piece-degree d_w>=2 (a core vertex cannot belong to only one piece because its neighbors include the missing pair). For the vertex-piece incidence matrix M, the Gram matrix is J+diag(d_w-1)-e_u e_v^T-e_v e_u^T. On the (a+1)-dimensional subspace x_u=x_v its quadratic form is (sum x_w)^2+sum_core(d_w-1)x_w^2+(d_u+d_v-4)x_u^2, positive for every nonzero vector. Thus M has rank at least a+1 and at least that many columns. Restricting a clique partition to an induced graph never increases its number of nonempty pieces. Hence cp(G)>=6. The exhaustive residual recurrence supplies a separate finite check.

The component bag gaps are delta(K7)=0 and delta(K6)=1, while delta(G)=5/3>1. Thus delta(G)<=sum delta(bag) is false even for two complete bags. This does not contradict (S3), whose separator correction is retained. The incidence proof and the finite recurrence are separate lower-bound checks.

## 5. Unbounded simplicial-step loss on a complete-graph family

Take odd d>=3 and n=2^d. On the nonzero vectors of F_2^d, the triples {a,b,a+b} partition pairs. Thus K_(n-1) has nu=nu_star=(n-1)(n-2)/6 and delta=0. Each unordered pair fixes its unique third, so the construction is explicit.

Now n is congruent to two modulo six; the construction in Section 2 applies to n+1. Delete one point. The triples through that point partition the remaining n points into pairs; hence their retained edges form exactly a perfect matching. All other triples provide a packing of K_n leaving n/2 edges. The odd-degree parity argument gives a matching upper bound. Uniform triangle weights 1/(n-2) attain the fractional optimum. Therefore

    nu(K_n)=n*(n-2)/6,
    nu_star(K_n)=n*(n-1)/6,
    delta(K_n)-delta(K_(n-1))=n/6.                       (F2)

Both cp values are one. This disproves any absolute constant loss for EVERY simplicial-vertex step, on an explicit chordal family. It is not a counterexample to delta(G)=O(|V(G)|): its gap itself is linear. Finite explicit constructions at n=8,32,128 were replayed.

Even restricting to INTEGER near-extremizers and low-core choices does not rescue that per-step lemma. Write k=2^d as above and R=k^2. Take the complete split graph J(R,2R) and identify one of its vertices with one vertex of K_k, with no other cross edges. Before the last simplicial vertex is added, the second block is K_(k-1). Every triangle and every clique containing an edge stays in one block, so nu,nu_star,cp add.

The split block has gap zero and cp=B(3R), by the explicit matching construction and crossing +1/core -1 certificate. Thus the after-graph has n=3k^2+k-1 and cp=B(3k^2)+1, while its predecessor has one fewer vertex and the same cp. Both normalized cp values tend to 1/6. Their gap jump is k/6, unbounded. Their clique number is R+1; any clique inside a vertex neighborhood has r<=R and t=n-r>=2R+k-2>=r-1. Hence all compression choices are low-core already by clique size, without presupposing the asymptotic theorem. One-vertex gluing preserves chordality. This counterexample concerns a local induction lemma, not either global root statement or the restricted additive block estimate (S6).

## 6. Execution scope, provenance, and first open lemma

The run record and lossless replay bundle bind source bytes, sanitized commands, exact versions, output hashes, exit codes, timing and caps. Full two-formulation enumeration stops at n=7. The n=8 run proves only its local-gap finite scope, using one rational packing formulation and the exact integer packing solver; three highlighted witnesses were additionally checked by both formulations and both integer routines. No continuous optimal face was enumerated. General all-choice low-core inequalities use the written graph-invariant proof, not finite dual samples.

One preliminary larger-pin scan hit the declared deadline in the equality LP. Its exit code was not captured and is recorded as null. The bounded scan was redesigned to avoid repeating that expensive equality LP for every larger extra case, while retaining the complete order-seven two-formulation check and checking the displayed pin witness both ways. The final scan completed all 26 orbits of 512 pin patterns, 55 split constructions, 65 complete-padding cases, and affine paired-pin cases m=3,9,27. A tool timeout is not a mathematical counterexample.

First open rounding lemma: obtain a universal linear bound for delta on the integer-near-extremal chordal class WITHOUT the extra linear-edit or linear separator-square budget hypotheses. Equivalently for a root-sufficient route, it is enough to control 2delta-[B(n)-lambda] by Cn, but that is a different, weaker sufficient assertion. No result here proves either. The generic low-core condition alone is not a simplification: padding an arbitrary k-vertex chordal graph with k isolates forces low-core sizes while preserving delta.

Next atomic action: choose a separator-capacity potential with an explicitly amortized loss for large overlapping bags, and test its terminal bound against (F2), its near-extremizer extension, and the paired-pin examples in `proof.md`. The naive constant-per-vertex and no-separator-correction lemmas are excluded; the admitted route is not retired. The source-backed o(n^2) theorem remains separate. Trusted source-document byte capture, registered verification and closure receipts remain absent. Status: NONTERMINAL_CHECKPOINT.
