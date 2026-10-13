#!/usr/bin/env python3
"""Week 4 · Task 1 — Answer questions about a stream you cannot store.

Textbook §4.3 (sampling), §4.4 (Bloom filter), §4.5 (Flajolet-Martin).

The premise of the whole chapter: the stream is longer than your memory, it
goes past once, and you still have to answer. Every method here trades an exact
answer for a bounded amount of space, and the job is to know exactly what you
traded.

You build three, and the harness checks each against the truth it is
approximating.

    python3 task1_sketches.py --verify
"""
import hashlib
import argparse, random
import math, statistics

class BloomFilter:
    """Membership, with one-sided error.

    A Bloom filter never says "no" about something you inserted. It sometimes
    says "yes" about something you did not. That asymmetry is the entire design
    and it is why it is useful for "have I seen this before" and useless for
    "is this definitely in the set".

    `m` bits, `k` hash functions.
    """
    def __init__(self, m, k, seed=246):
        self.m = m
        self.k = k
        self.seed = seed
        self.bits = bytearray(m)

    def _indexes(self, item):
        data = str(item).encode("utf-8")
        key1 = str(self.seed).encode("utf-8")
        key2 = str(self.seed + 1).encode("utf-8")

        h1 = int.from_bytes(
            hashlib.blake2b(
                data, digest_size=8, key=key1
            ).digest(), "big"
        )
        h2 = int.from_bytes(
            hashlib.blake2b(
                data, digest_size=8, key=key2
            ).digest(), "big"
        ) | 1

        for i in range(self.k):
            yield (h1 + i * h2) % self.m

    def add(self, item):
        for index in self._indexes(item):
            self.bits[index] = 1

    def __contains__(self, item):
        return all(
            self.bits[index]
            for index in self._indexes(item)
        )

    def expected_fp_rate(self, n_inserted):
        return (
            1 - math.exp(-self.k * n_inserted / self.m)
        ) ** self.k


def flajolet_martin(stream, n_hashes=64, seed=246):
    """Estimate how many DISTINCT items went past, in almost no memory."""
    maxima = [0] * n_hashes
    mask = (1 << 64) - 1
    key = str(seed).encode("utf-8")

    for item in stream:
        data = str(item).encode("utf-8")
        base = int.from_bytes(
            hashlib.blake2b(
                data, digest_size=8, key=key
            ).digest(),
            "big"
        )

        for j in range(n_hashes):
            z = (base + 0x9E3779B97F4A7C15 * (j + 1)) & mask
            z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & mask
            z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & mask
            h = z ^ (z >> 31)

            r = 64 if h == 0 else (h & -h).bit_length() - 1
            maxima[j] = max(maxima[j], r)

    estimates = []
    group_size = 4

    for start in range(0, n_hashes, group_size):
        group = maxima[start:start + group_size]
        estimates.append(
            sum(2.0 ** r for r in group) / len(group)
        )

    return statistics.median(estimates) * 0.77351

def reservoir_sample(stream, k, seed=246):
    """Keep k items uniformly at random from a stream of unknown length.

    §4.3. Every item that went past must end up with the same probability k/n
    of being in your sample, and you only ever hold k of them.

    Return a list of k items (or fewer if the stream was shorter).
    """
    
    if k < 0:
        raise ValueError("k must be non-negative")

    rng = random.Random(seed)
    sample = []

    for i, item in enumerate(stream):
        if i < k:
            sample.append(item)
        elif k > 0:
            j = rng.randrange(i + 1)
            if j < k:
                sample[j] = item

    return sample

# ------------------------------------------------------------------- harness
def verify():
    fails = 0
    rng = random.Random(246)

    def check(label, ok, detail=""):
        nonlocal fails
        print(f"  {'ok  ' if ok else 'FAIL'}  {label:<46} {detail}")
        fails += not ok

    # --- Bloom: no false negatives, ever
    try:
        bf = BloomFilter(m=8192, k=5)
    except NotImplementedError:
        print("  BloomFilter is still a stub"); return 1
    inserted = [f"item-{i}" for i in range(800)]
    for x in inserted:
        bf.add(x)
    check("no false negatives", all(x in bf for x in inserted))

    absent = [f"other-{i}" for i in range(20_000)]
    fp = sum(1 for x in absent if x in bf) / len(absent)
    predicted = bf.expected_fp_rate(len(inserted))
    close = abs(fp - predicted) < max(0.02, predicted * 0.5)
    check("measured false-positive rate matches theory", close,
          f"measured {fp:.3%}, predicted {predicted:.3%}")

    # --- Flajolet-Martin: a factor of two is what this method gives you
    try:
        distinct = 20_000
        stream = [f"k{rng.randrange(distinct)}" for _ in range(120_000)]
        est = flajolet_martin(stream)
    except NotImplementedError:
        print("  flajolet_martin is still a stub"); return 1
    true_distinct = len(set(stream))
    ratio = est / true_distinct
    check("distinct estimate within a factor of 2", 0.5 <= ratio <= 2.0,
          f"estimated {est:,.0f}, true {true_distinct:,} ({ratio:.2f}x)")

    # --- Reservoir: uniform over many trials
    try:
        counts = [0] * 20
        trials = 4000
        for t in range(trials):
            s = reservoir_sample(range(20), 5, seed=t)
            for i in s:
                counts[i] += 1
    except NotImplementedError:
        print("  reservoir_sample is still a stub"); return 1
    expected = trials * 5 / 20
    spread = (max(counts) - min(counts)) / expected
    check("reservoir is uniform across items", spread < 0.15,
          f"spread {spread:.1%} around {expected:.0f}")

    print(f"\n  {'all ok' if not fails else str(fails) + ' failed'}")
    return 1 if fails else 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--verify", action="store_true")
    a = p.parse_args()
    raise SystemExit(verify() if a.verify else p.print_help())
