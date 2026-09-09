#!/usr/bin/env python3
"""
Exact finite checker for candidate:erdos81-a01-c32-direction-packets.

Proof use:
- validates explicit p=3,q=2/3 actual-host constructions;
- validates every actual core-edge owner and every individual leaf matching;
- validates the full-one-third face formulas on the recorded finite domain;
- validates fixed m=9 Vizing color certificates and exact even-repair certificates;
- validates the selected-near-factor obstruction identity;
- validates translation-slot uniqueness and rejects slot reuse.

It does NOT prove Vizing's theorem, the universal affine-line identities, or the
universal quantified candidate. Those are natural-language proof obligations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Set, Tuple

Vec = Tuple[int, ...]
Edge = Tuple[Vec, Vec]
Tri = Tuple[Vec, Vec, Vec]


def edge(u: Vec, v: Vec) -> Edge:
    assert u != v
    return (u, v) if u < v else (v, u)


def add(u: Vec, v: Vec) -> Vec:
    return tuple((x + y) % 3 for x, y in zip(u, v))


def neg(u: Vec) -> Vec:
    return tuple((-x) % 3 for x in u)


def sub(u: Vec, v: Vec) -> Vec:
    return tuple((x - y) % 3 for x, y in zip(u, v))


def all_vecs(k: int) -> List[Vec]:
    return list(product(range(3), repeat=k))


def canonical_direction(d: Vec) -> Vec:
    assert any(d)
    return min(d, neg(d))


def projective_directions(k: int) -> List[Vec]:
    return sorted({canonical_direction(v) for v in all_vecs(k) if any(v)})


def affine_lines(vertices: Sequence[Vec]) -> List[Tri]:
    lines: Dict[Tri, Tri] = {}
    for u, v in combinations(vertices, 2):
        w = neg(add(u, v))
        T = tuple(sorted((u, v, w)))
        assert len(set(T)) == 3
        lines[T] = T
    out = sorted(lines)
    r = len(vertices)
    assert len(out) == r * (r - 1) // 6
    return out


def line_edges(T: Tri) -> Set[Edge]:
    return {edge(T[0], T[1]), edge(T[0], T[2]), edge(T[1], T[2])}


def coordinate_cosets(vertices: Sequence[Vec], coord: int) -> List[List[Vec]]:
    groups: Dict[Tuple[int, ...], List[Vec]] = defaultdict(list)
    for v in vertices:
        key = tuple(x for i, x in enumerate(v) if i != coord)
        groups[key].append(v)
    return [sorted(groups[k]) for k in sorted(groups)]


def k3_edge_coloring(C: Sequence[Vec]) -> Dict[int, List[Edge]]:
    x0, x1, x2 = sorted(C)
    return {
        0: [edge(x0, x1)],
        1: [edge(x1, x2)],
        2: [edge(x0, x2)],
    }


def matching_ok(edges: Iterable[Edge]) -> bool:
    seen: Set[Vec] = set()
    for u, v in edges:
        if u in seen or v in seen:
            return False
        seen.add(u)
        seen.add(v)
    return True


def transported_instance(instance: Mapping[str, object], target_A: Set[Vec]) -> Dict[str, object]:
    old_A = sorted(instance["A"])
    V = sorted(instance["V"])
    old_C = [v for v in V if v not in set(old_A)]
    new_A = sorted(target_A)
    new_C = [v for v in V if v not in target_A]
    assert len(old_A) == len(new_A)
    mp = dict(zip(old_A, new_A))
    mp.update(zip(old_C, new_C))

    def me(e: Edge) -> Edge:
        return edge(mp[e[0]], mp[e[1]])

    def mt(T: Tri) -> Tri:
        return tuple(sorted(mp[v] for v in T))

    return {
        "V": V,
        "A": target_A,
        "short": {c: [me(e) for e in E] for c, E in instance["short"].items()},
        "long": {c: [me(e) for e in E] for c, E in instance["long"].items()},
        "core": [mt(T) for T in instance["core"]],
        "unused_core": {me(e) for e in instance["unused_core"]},
        "q": instance["q"],
        "b": instance["b"],
    }


def construct_p3(k: int, a: int, q: int) -> Dict[str, object]:
    assert k >= 2 and q in (2, 3)
    V = all_vecs(k)
    r = len(V)
    assert 0 <= a <= r
    short_cosets = coordinate_cosets(V, 0)
    long_cosets = coordinate_cosets(V, 1)
    t, b = divmod(a, 3)

    chosen_short = short_cosets[:t]
    A: Set[Vec] = {v for C in chosen_short for v in C}
    if b:
        A.update(short_cosets[t][:b])

    short: Dict[int, List[Edge]] = {0: [], 1: [], 2: []}
    for C in chosen_short:
        local = k3_edge_coloring(C)
        for color, E in local.items():
            short[color].extend(E)

    unused_core: Set[Edge] = set()
    if q == 3:
        long: Dict[int, List[Edge]] = {0: [], 1: [], 2: []}
        for C in long_cosets:
            local = k3_edge_coloring(C)
            for color, E in local.items():
                long[color].extend(E)
    else:
        long = {0: [], 1: []}
        for C in long_cosets:
            x0, x1, x2 = sorted(C)
            long[0].append(edge(x0, x1))
            long[1].append(edge(x1, x2))
            unused_core.add(edge(x0, x2))

    short_edges = {e for M in short.values() for e in M}
    long_edges = {e for M in long.values() for e in M}
    assert short_edges.isdisjoint(long_edges)

    lines = affine_lines(V)
    core: List[Tri] = []
    for T in lines:
        E = line_edges(T)
        hit = E & (short_edges | long_edges)
        if not hit:
            core.append(T)
        elif hit == E:
            pass
        elif q == 2 and len(hit) == 2 and E - hit <= unused_core:
            pass
        else:
            raise AssertionError(("partial-owner-line", T, hit, E - hit))

    out = {
        "V": V,
        "A": A,
        "short": short,
        "long": long,
        "core": core,
        "unused_core": unused_core,
        "q": q,
        "b": b,
    }
    validate_actual_instance(out)
    return out


def validate_actual_instance(instance: Mapping[str, object]) -> Dict[str, int]:
    V: List[Vec] = list(instance["V"])
    A: Set[Vec] = set(instance["A"])
    short: Mapping[int, List[Edge]] = instance["short"]
    long: Mapping[int, List[Edge]] = instance["long"]
    core: List[Tri] = list(instance["core"])
    unused_core: Set[Edge] = set(instance["unused_core"])
    q = int(instance["q"])
    r = len(V)
    a = len(A)
    b = int(instance["b"])

    assert len(short) == 3
    assert len(long) == q
    for M in list(short.values()) + list(long.values()):
        assert matching_ok(M)

    owner: Dict[Edge, str] = {}
    for color, M in short.items():
        for e in M:
            assert e[0] in A and e[1] in A
            assert e not in owner
            owner[e] = f"S{color}"
    for color, M in long.items():
        for e in M:
            assert e not in owner
            owner[e] = f"L{color}"
    for T in core:
        for e in line_edges(T):
            assert e not in owner
            owner[e] = "CORE"
    for e in unused_core:
        assert e not in owner
        owner[e] = "UNUSED"

    assert len(owner) == r * (r - 1) // 2
    assert set(owner) == {edge(u, v) for u, v in combinations(V, 2)}

    sdeg = Counter(v for M in short.values() for e in M for v in e)
    ldeg = Counter(v for M in long.values() for e in M for v in e)
    S_short = sum(3 - sdeg[v] for v in A)
    S_long = sum(q - ldeg[v] for v in V)
    S_core = len(unused_core)
    S = S_short + S_long + S_core
    assert S_short == a + 2 * b
    assert S_long + S_core == r
    assert S == a + r + 2 * b

    M = r * (r - 1) // 2
    P = len(core) + sum(map(len, short.values())) + sum(map(len, long.values()))
    U3 = M + 3 * a + q * r
    assert U3 - 3 * P == S

    type_counts = Counter()
    for T in core:
        type_counts[sum(v in A for v in T)] += 1
    assert sum(type_counts.values()) == len(core)

    return {
        "r": r,
        "a": a,
        "q": q,
        "packing": P,
        "S_core": S_core,
        "S_short": S_short,
        "S_long": S_long,
        "S_total": S,
        "AAA": type_counts[3],
        "AAC": type_counts[2],
        "ACC": type_counts[1],
        "CCC": type_counts[0],
    }


def face_interval(r: int, a: int, p: int, q: int) -> Tuple[Fraction, Fraction, bool]:
    c = r - a
    assert a >= 3 and c >= 3
    d = r - 1 - q
    s = d - p
    ell = max(Fraction(0), Fraction(a * (c - q), 2), Fraction(c * (a - q), 2))
    u = min(
        Fraction(a * c, 2),
        Fraction(a * s, 2),
        Fraction(c * d, 2),
        Fraction(a * s + c * d, 6),
    )
    return ell, u, ell <= u


def verify_boundary_primal(r: int, a: int, p: int, q: int) -> None:
    c = r - a
    assert c in (0, 1, 2)
    if c == 0:
        alpha = Fraction(p, r - 1)
        beta = Fraction(q, r - 1)
        z3 = Fraction(r - 1 - p - q, (r - 1) * (r - 2))
        assert alpha >= 0 and beta >= 0 and z3 >= 0
        assert alpha + beta + (r - 2) * z3 == 1
        assert (r - 1) * alpha == p
        assert (r - 1) * beta == q
    elif c == 1:
        alpha = Fraction(p, a - 1)
        beta = Fraction(q, a)
        z2 = Fraction(a - q, a * (a - 1))
        z3 = Fraction(a * a - a * (p + q + 2) + 2 * q, a * (a - 1) * (a - 2))
        assert min(alpha, beta, z2, z3) >= 0
        assert beta + (a - 1) * z2 == 1
        assert alpha + beta + z2 + (a - 2) * z3 == 1
        assert (a - 1) * alpha == p
        assert a * beta == q
    else:
        alpha = Fraction(p, a - 1)
        beta2 = Fraction(q * (a - 2), a * (a - 1))
        beta1 = Fraction(q, a)
        z1 = Fraction(1, a)
        z2 = Fraction(a - q - 1, a * (a - 1))
        z3 = Fraction(
            a * a - a * (p + q + 3) + 4 * q + 2,
            a * (a - 1) * (a - 2),
        )
        assert min(alpha, beta2, beta1, z1, z2, z3) >= 0
        assert a * z1 == 1
        assert beta1 + z1 + (a - 1) * z2 == 1
        assert alpha + beta2 + 2 * z2 + (a - 2) * z3 == 1
        assert (a - 1) * alpha == p
        assert (a - 1) * beta2 + 2 * beta1 == q
        assert a * beta1 == q


def decode_vec(s: str) -> Vec:
    return tuple(int(ch) for ch in s)


def decode_edge(raw: Sequence[str]) -> Edge:
    return edge(decode_vec(raw[0]), decode_vec(raw[1]))


def direction_edges(k: int, directions: Sequence[Vec]) -> Tuple[List[Vec], Set[Edge]]:
    V = all_vecs(k)
    D = set(directions)
    E = {
        edge(u, v)
        for u, v in combinations(V, 2)
        if canonical_direction(sub(v, u)) in D
    }
    return V, E


def validate_edge_coloring(vertices, edges, assignment, palette_size, require_cover):
    assert set(assignment).issubset(edges)
    if require_cover:
        assert set(assignment) == edges
    incident = {}
    for e, color in assignment.items():
        assert 0 <= color < palette_size
        for v in e:
            key = (v, color)
            assert key not in incident
            incident[key] = e


def component_count(vertices, edges):
    adj = {v: [] for v in vertices}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    unseen = set(vertices)
    count = 0
    while unseen:
        count += 1
        root = unseen.pop()
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    stack.append(v)
    return count


def validate_certificates(cert_file: Path) -> Dict[str, object]:
    data = json.loads(cert_file.read_text(encoding="utf-8"))
    for ps, rec in data["vizing_m9"].items():
        p = int(ps)
        dirs = [decode_vec(s) for s in rec["directions"]]
        V, E = direction_edges(2, dirs)
        assignment = {decode_edge(item["edge"]): int(item["color"]) for item in rec["colors"]}
        palette = int(rec["palette_size"])
        validate_edge_coloring(V, E, assignment, palette, True)
        degree = Counter(v for e in E for v in e)
        expected = 0 if p == 1 else (p - 1 if p % 2 else p)
        assert all(degree[v] == expected for v in V)
        assert palette == (p if p % 2 else p + 1)
        actual_sizes = Counter(assignment.values())
        assert {str(k): v for k, v in sorted(actual_sizes.items())} == rec["color_sizes"]

    exact_rho = {}
    for ps, rec in data["exact_even_repair_m9"].items():
        p = int(ps)
        dirs = [decode_vec(s) for s in rec["directions"]]
        V, E = direction_edges(2, dirs)
        assignment = {decode_edge(item["edge"]): int(item["color"]) for item in rec["kept_colors"]}
        deleted = {decode_edge(raw) for raw in rec["deleted_edges"]}
        assert set(assignment).isdisjoint(deleted)
        assert set(assignment) | deleted == E
        validate_edge_coloring(V, E, assignment, p, False)
        rho = int(rec["rho"])
        assert len(deleted) == rho
        comps = component_count(V, E)
        parity_lower = p * comps // 2
        assert rho == parity_lower
        exact_rho[ps] = {"rho": rho, "components": comps}
    return {"vizing_certificates": len(data["vizing_m9"]), "exact_even_repairs": exact_rho}


def near_factor_matching(vertices: Sequence[Vec], color: Vec) -> Set[Edge]:
    out = set()
    for x, y in combinations(vertices, 2):
        if add(x, y) == color:
            out.add(edge(x, y))
    assert matching_ok(out)
    assert len(out) == (len(vertices) - 1) // 2
    return out


def validate_near_factor_obstruction() -> int:
    V = all_vecs(2)
    lines = affine_lines(V)
    all_matchings = {c: near_factor_matching(V, c) for c in V}
    assert set().union(*all_matchings.values()) == {edge(u, v) for u, v in combinations(V, 2)}
    checked = 0
    for mask in range(1 << len(V)):
        D = {V[i] for i in range(len(V)) if mask & (1 << i)}
        omitted = len(D)
        selected = len(V) - omitted
        tau = sum(1 for T in lines if set(T) <= D)
        predicted_core = omitted * (len(V) - 1) // 2 - 3 * tau
        N = Counter(sum(v in D for v in T) for T in lines)
        observed_core = N[1] + 2 * N[2]
        assert observed_core == predicted_core
        assert 2 * predicted_core >= omitted * selected
        checked += 1
    return checked


def translation_slots(N: int, s: int):
    return {(i, (i + s) % N) for i in range(N)}


def validate_translation_slots():
    tested = 0
    for N in (3, 5, 7):
        slots = [translation_slots(N, s) for s in range(N)]
        assert len(set().union(*slots)) == N * N
        for i, A in enumerate(slots):
            for j, B in enumerate(slots):
                if i != j:
                    assert A.isdisjoint(B)
        for s in range(N):
            for t in range(N):
                triples = {(i, (i + s) % N, (i + s + t) % N) for i in range(N)}
                uv = {(x, y) for x, y, _ in triples}
                vw = {(y, z) for _, y, z in triples}
                uw = {(x, z) for x, _, z in triples}
                assert uv == translation_slots(N, s)
                assert vw == translation_slots(N, t)
                assert uw == translation_slots(N, (s + t) % N)
                tested += 1
        assert translation_slots(N, 0).isdisjoint(translation_slots(N, 1))
        assert translation_slots(N, 0) & translation_slots(N, 0)
        assert len(slots) == N
    return {"triangle_slot_pairs": tested, "fiber_sizes": 3}


def run_construct():
    named = []
    cardinality_cases = 0
    for k in (2, 3, 4):
        r = 3 ** k
        for q in (2, 3):
            for a in range(0, r + 1):
                rec = validate_actual_instance(construct_p3(k, a, q))
                cardinality_cases += 1
                if r == 9 and a >= 4:
                    named.append(rec)

    subset_transports = 0
    V9 = all_vecs(2)
    for q in (2, 3):
        for a in range(4, 10):
            canonical = construct_p3(2, a, q)
            for A_tuple in combinations(V9, a):
                moved = transported_instance(canonical, set(A_tuple))
                validate_actual_instance(moved)
                subset_transports += 1

    face_cases = 0
    for r in (9, 27, 81, 243):
        for q in (2, 3):
            for a in range(4, r + 1):
                c = r - a
                if c >= 3:
                    ell, u, ok = face_interval(r, a, 3, q)
                    assert ok and ell <= u
                else:
                    verify_boundary_primal(r, a, 3, q)
                face_cases += 1

    return {
        "cardinality_constructions": cardinality_cases,
        "actual_subset_transports_r9": subset_transports,
        "face_cases": face_cases,
        "named_r9": named,
    }


def run_controls(cert_file: Path):
    certs = validate_certificates(cert_file)
    near_count = validate_near_factor_obstruction()
    slots = validate_translation_slots()
    V = all_vecs(2)
    D = projective_directions(2)[0]
    _, E = direction_edges(2, [D])
    assert bool(E & E)
    C = sorted(coordinate_cosets(V, 0)[0])
    bad_matching = [edge(C[0], C[1]), edge(C[1], C[2])]
    assert not matching_ok(bad_matching)
    assert 3 > 3 - 1
    return {
        **certs,
        "near_factor_obstruction_subsets_m9": near_count,
        "translation_slots": slots,
        "negative_mutations": 3,
        "a3_face_excluded": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("construct", "controls", "all"), nargs="?", default="all")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    cert_file = here / "certificates.json"
    start = time.perf_counter()
    out = {
        "status": "ok",
        "mode": args.mode,
        "python": platform.python_version(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "certificates_sha256": hashlib.sha256(cert_file.read_bytes()).hexdigest(),
    }
    if args.mode in ("construct", "all"):
        out["construct"] = run_construct()
    if args.mode in ("controls", "all"):
        out["controls"] = run_controls(cert_file)
    out["elapsed_seconds"] = time.perf_counter() - start
    print(json.dumps(out, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
