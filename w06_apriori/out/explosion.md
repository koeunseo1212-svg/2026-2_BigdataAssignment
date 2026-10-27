# Task 2 — Explosion Curve
## Measurements
| Support | Frequent pairs | Peak counters | Seconds | Peak memory |
|---:|---:|---:|---:|---:|
| 400 | 249 | 10,585 | 0.41 | 1.1 MB |
| 200 | 776 | 58,626 | 0.59 | 6.7 MB |
| 100 | 2,244 | 273,701 | 1.11 | 28.6 MB |
| 50 | 6,397 | 820,259 | 2.16 | 107.7 MB |
| 25 | 17,045 | 893,456 | 2.30 | 107.7 MB |
| 12 | 43,116 | 893,456 | 2.26 | 110.0 MB |
| 6 | 101,938 | 893,456 | 2.34 | 126.5 MB |

## A2 — Where it became difficult
The experiment completed successfully at support 6, with 101,938 frequent pairs and 126.5 MB peak memory. No failure or unbearable slowdown was observed in the tested range, so the failure threshold was not reached.

## A4 — Counter growth
From support 400 to 50, peak counters increased from 10,585 to 820,259, approximately 77.5 times, while support decreased by a factor of eight. From support 50 to 6, the counter count remained at 893,456. The candidate count eventually saturated because only a finite set of pairs formed from frequent singletons was considered.

## A5 — Frequent pairs versus counters
From support 400 to 6, frequent pairs increased from 249 to 101,938, approximately 409 times. Peak counters increased from 10,585 to 893,456, approximately 84.4 times. The number of answers and the number of candidate counters grow differently, and many counters are maintained for pairs that do not meet the support threshold.

## A6 — Machine
- CPU: AMD Ryzen 5 7500F 6-Core Processor (6 cores, 12 logical processors, 3.70 GHz base speed)
- RAM: 32.0 GB DDR5, 5200 MT/s
- Other running applications: PowerShell (running Python experiments), Visual Studio Code
- Python version and platform: Python 3.14.3, Windows-11-10.0.26200-SP0 (AMD64)
