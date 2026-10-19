# Week 5 Lab — Observations

## Task 1: PageRank and its failures

Without correction, dead ends absorb no outgoing rank, causing the total rank to drain toward zero. I redistributed dead-end rank uniformly across all nodes. Teleportation also prevents a spider trap from retaining all the rank. Beta represents the probability of following a link, while 1 - beta represents the probability of teleporting uniformly to any node.

## Task 2: Convergence

The iteration count generally increased as beta approached 1 because teleportation became less frequent. Increasing graph size had a much greater effect on execution time than on iteration count. The top three nodes remained the same across the five tested beta values, although the complete top-10 lists should be checked before claiming full ranking stability.

## Task 3: Sparse PageRank

The sparse implementation stores the adjacency list and two rank vectors instead of an n × n transition matrix. For 1,200 nodes and 5,877 edges, it used 2,400 reported floats instead of 1,440,000, achieving 600× less float storage and 51.0× faster execution. The maximum difference from the dense result was 1.18e-15, well within the required 1e-9 tolerance.

The teleport term does not require a dense matrix because every node receives the same constant (1 - beta)/n in each iteration. Dead-end redistribution can also be calculated as one constant, beta times the total dead-end rank divided by n, and added to every node. Small numerical differences may arise from floating-point arithmetic and summation order.