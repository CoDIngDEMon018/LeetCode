# 1857. Largest Color Value in a Directed Graph

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a directed graph of `n` colored nodes (indexed `0` to `n-1`) and `m` edges, find the maximum number of occurrences of any single color along a valid path. If the graph contains a cycle, return `-1`.

- `colors[i]` is a lowercase letter for node `i`.
- `edges[j] = [u, v]` means there is a directed edge from `u` to `v`.
- A valid path is a sequence of nodes connected by edges.
- The path’s **color value** is the count of the most frequent color on that path.

## Approach

We combine **topological sorting** (to detect cycles and impose an order) with a **dynamic-programming**-like “color count” propagation:

1. **Topological Sort with Kahn’s algorithm**  
   - Maintain an **in-degree** array; nodes with in-degree `0` go into a queue.
   - Pop nodes one by one, reducing in-degree of their neighbors.  
   - If at the end some nodes were never popped, there’s a cycle ⇒ return `-1`.

2. **Per-node color-count maps**  
   - For each node `u`, maintain a `count[u]` map: `color → max occurrences of that color along any path ending at u`.
   - When processing `u`, first increment `count[u][ colors[u] ]` (to include itself).
   - Update a global `answer` with this new count.
   - Then push all entries of `count[u]` to each neighbor `v`, taking the **maximum** for each color:
     ```python
     count[v][c] = max(count[v].get(c, 0), count[u][c])
     ```

This visits each edge and each node once (plus a constant factor of ≤26 colors), so it runs in O((n + m)·26) ≈ O(n + m).
