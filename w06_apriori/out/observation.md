# Observations
## Task 1 — A-Priori
The implementation passed all verification checks. It found the expected frequent singletons and pairs at support 3, and the confidence of the rule diaper → beer was 0.8.

## Task 2 — Explosion Curve
As the support threshold decreased from 400 to 6, frequent pairs increased from 249 to 101,938. Peak memory increased from 1.1 MB to 126.5 MB, while peak counters reached 893,456. The experiment completed at support 6, so the failure threshold was not reached in the tested range.

## Task 3 — PCY
PCY returned the same 6,397 frequent pairs as the baseline, with no missing or extra pairs. Peak pair counters decreased from 820,259 to 12,959, a reduction of 98.4%. PCY used a fixed array of 1,048,576 buckets and a bitmap, so these structures also consume memory. In this test, the reduction in pair counters was substantial, although execution time was 1.00 s compared with 0.76 s for the baseline. The results suggest that PCY can reduce pair-counting memory substantially, but its extra hashing work may increase runtime.