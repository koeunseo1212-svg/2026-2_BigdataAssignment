# Week 3 Observation

## Task 1
MinHash converts each document's shingle set into a compact signature, while LSH uses banding to generate candidate pairs without comparing every pair. The textbook verification passed all checks, including the Jaccard similarity, MinHash signature, and LSH candidate tests.

## Task 2
On this machine, Brute Force was faster than LSH for all tested input sizes from 250 to 4,000 documents. At 4,000 documents, LSH reduced the number of similarity comparisons from 2,246,140 to 13,867, avoiding more than 99% of the comparisons. However, the additional overhead from hashing and bucketing made LSH slower overall. No runtime crossover point was observed within the tested range.

## Task 3
The LSH-based finder reduced similarity comparisons from 2,246,140 to 13,867, avoiding 99.38% of the comparisons. It achieved 95.9% recall and 100.0% precision, receiving a `strong` result from the benchmark.