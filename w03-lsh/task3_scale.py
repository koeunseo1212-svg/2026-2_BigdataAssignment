#!/usr/bin/env python3
"""Week 3 · Task 3 — Find the same pairs without comparing everything.

Textbook §3.4.

`BruteForce` compares every pair. On 3,000 documents that is 4.5 million
comparisons and it is completely correct. On 3 million documents it is 4.5
trillion and it is completely useless.

Beat it. Find the same near-duplicate pairs while making far fewer comparisons.

    python3 bench.py
    python3 bench.py --yours

The harness counts every call you make to `similarity()`. That is your score.
It also checks **recall** - which of the truly similar pairs you found. Skipping
comparisons is easy; skipping comparisons without losing the pairs is the task.
"""


class BruteForce:
    """Correct, and quadratic."""

    def __init__(self, threshold):
        self.threshold = threshold

    def find(self, docs, similarity):
        """docs is [set_of_shingles, ...]. Return {(i, j), ...} with i < j."""
        out = set()
        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                if similarity(docs[i], docs[j]) >= self.threshold:
                    out.add((i, j))
        return out


class YourFinder:
    def __init__(self, threshold):
        self.threshold = threshold

    def find(self, docs, similarity):
        from task1_minhash import minhash_signatures, lsh_candidates

        hashes = [
            (lambda r, a=a, b=b: (a * r + b) % 100003)
            for a, b in [
                (1, 1), (3, 1), (5, 1), (7, 1), (11, 1),
                (13, 1), (17, 1), (19, 1), (23, 1), (29, 1),
                (31, 1), (37, 1), (41, 1), (43, 1), (47, 1),
                (53, 1), (59, 1), (61, 1), (67, 1), (71, 1),
                (73, 1), (79, 1), (83, 1), (89, 1), (97, 1),
                (101, 1), (103, 1), (107, 1), (109, 1), (113, 1),
                (127, 1), (131, 1), (137, 1), (139, 1), (149, 1),
                (151, 1), (157, 1), (163, 1), (167, 1), (173, 1),
                (179, 1), (181, 1), (191, 1), (193, 1), (197, 1),
                (199, 1), (211, 1), (223, 1), (227, 1), (229, 1),
                (233, 1), (239, 1), (241, 1), (251, 1), (257, 1),
                (263, 1), (269, 1), (271, 1), (277, 1), (281, 1)
            ]
        ]

        max_row = max((max(doc) for doc in docs if doc), default=0)

        signatures = minhash_signatures(
            docs,
            hashes,
            max_row + 1
        )

        candidates = lsh_candidates(signatures, bands=20)

        result = set()

        for i, j in candidates:
            if similarity(docs[i], docs[j]) >= self.threshold:
                result.add((i, j))

        return result