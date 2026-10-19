# Task 2 — Convergence Analysis

## A2. Iterations by beta

| Beta | Nodes | Iterations | Time (s) |
|---:|---:|---:|---:|
| 0.50 | 1,200 | 14 | 0.014 |
| 0.70 | 1,200 | 17 | 0.015 |
| 0.85 | 1,200 | 20 | 0.027 |
| 0.95 | 1,200 | 23 | 0.031 |
| 0.99 | 1,200 | 24 | 0.039 |

## A3. Effect of beta

As beta increases toward 1, the iteration count generally increases. A larger beta means the random surfer follows links more often and teleports less often. This weakens the effect of teleportation and generally slows convergence.

## A4. Effect of graph size

For beta = 0.85, the 1,200-node graph converged in 20 iterations and the 20,000-node graph converged in 21 iterations. For beta = 0.95, the counts were 23 and 24 respectively.

The iteration counts remained similar, but execution time increased substantially with graph size because more nodes and edges had to be processed during each iteration.

## A5. Effect of tolerance

For beta = 0.85 on the default graph, tolerance 1e-10 required 20 iterations, while tolerance 1e-6 required 12 iterations. The stricter tolerance required 8 additional iterations.

## A6. Top-10 ranking

The top three nodes were p00009, p00001, and p00006 for all five tested beta values. The complete top-10 lists should also be compared in convergence.json before concluding that the entire ranking remained unchanged.

## A7. Machine and environment

CPU: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
CPU cores: 4 cores, 8 logical processors
RAM: 8.0 GB LPDDR4
Operating system: Windows 11 (10.0.26200, Build 26200)
Python version: Python 3.12.2
Other running applications: Not recorded