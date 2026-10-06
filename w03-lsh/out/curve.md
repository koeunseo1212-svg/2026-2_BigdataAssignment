# Task 2 — Crossover Curve

Measurements on this machine (Windows 11, Python 3.12.2):

| Documents | Brute Force Time | LSH Time | Brute Comparisons | LSH Comparisons |
| --------: | ---------------: | -------: | ----------------: | --------------: |
|       250 |          0.204 s |  2.918 s |            31,125 |             202 |
|       500 |          1.075 s |  4.534 s |           124,750 |             728 |
|     1,000 |          3.667 s |  9.732 s |           499,500 |           3,052 |
|     2,000 |         14.773 s | 20.669 s |         1,999,000 |          12,194 |
|     4,000 |         16.383 s | 22.289 s |         2,246,140 |          13,867 |

## Observation

Brute Force was faster than LSH for every tested input size from 250 to 4,000 documents. However, LSH reduced the number of similarity comparisons dramatically. At 4,000 documents, LSH reduced the comparisons from 2,246,140 to 13,867, avoiding more than 99% of the comparisons.

Despite this reduction, LSH was still slower overall because of the additional overhead from hashing and bucketing. No runtime crossover point was observed within the tested range. At 4,000 documents, the computation became noticeably more expensive, but Brute Force was still faster on this machine.
