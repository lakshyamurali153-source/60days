## recursive function 
A recursive solution is a method where a function solves a problem by calling itself on smaller parts of the same problem.

<img width="678" height="348" alt="image" src="https://github.com/user-attachments/assets/0eae69b7-84d3-4ecc-ac04-a6c6ccf0ac73" />
<img width="868" height="203" alt="image" src="https://github.com/user-attachments/assets/5f15b4c5-2273-444b-a89d-1e1b5f4550e2" />
<img width="787" height="362" alt="image" src="https://github.com/user-attachments/assets/09c509fd-b6bb-4751-b191-f25e63190129" />

# Climbing Stairs: Execution & Recursion Tree Analysis

This guide provides a detailed performance comparison and execution trace between **Naive Recursion** and **Top-Down Memoization** for the Climbing Stairs problem.

---

## ⏱️ Execution Time Comparison

The two approaches differ dramatically in how they scale as the number of stairs (\(n\)) grows.

| Metric | Naive Recursion | Memoized Recursion |
| :--- | :--- | :--- |
| **Time Complexity** | \(O(2^n)\) — Exponential | \(O(n)\) — Linear |
| **Space Complexity** | \(O(n)\) — Call stack depth | \(O(n)\) — Call stack + `help` dictionary |
| **Execution for \(n = 5\)** | 15 recursive calls | 7 recursive calls |
| **Execution for \(n = 45\)** | ~35,184,372,088,832 calls (Timeout) | 87 calls (Runs in < 1ms) |

### Why Memoization Wins
Naive recursion recalculates identical subproblems repeatedly. Memoization caches results in the `help` dictionary. When a previously calculated step is encountered, it is retrieved in \(O(1)\) time, bypassing the remaining recursive branches.

---

## 🌳 Recursion Tree Breakdown (\(n = 5\))

### 1. Naive Recursion Tree
Every single branch must execute fully down to the base cases (\(n=1\) or \(n=2\)). Notice the massive amount of repeated work.

```text
                               climbStairs(5)
                             /                \
               climbStairs(4)                  climbStairs(3)
              /              \                /              \
       climbStairs(3)      climbStairs(2)  climbStairs(2)  climbStairs(1)
       /            \          [Base]          [Base]          [Base]
climbStairs(2)  climbStairs(1)
    [Base]          [Base]
```
* **Total Calls:** 15 calls.
* **Redundancy:** `climbStairs(3)` is completely evaluated twice. `climbStairs(2)` is evaluated 3 separate times.

### 2. Memoized Recursion Tree
With memoization, the tree is heavily pruned. The entire right branch under `climbStairs(5)` turns into an instant lookup.

```text
                               climbStairs(5)
                             /                \
               climbStairs(4)                  climbStairs(3) 🛑 (Cached Hit!)
              /              \                     Returns 3
       climbStairs(3)      climbStairs(2) 🛑 (Cached Hit!)
       /            \          Returns 2
climbStairs(2)  climbStairs(1)
    [Base]          [Base]
```

### Execution Flow Tracker (Memoized)
1. **Diving Left:** $5 \rightarrow 4 \rightarrow 3 \rightarrow 2$ (returns 2) $\rightarrow 1$ (returns 1).
2. **First Cache:** `climbStairs(3)` calculates $2 + 1 = 3$. It saves `{3: 3}`.
3. **Pruning Step 4:** `climbStairs(4)` calls its right child `2`. Instead of recursing, it reads from the base condition and calculates $3 + 2 = 5$. It saves `{3: 3, 4: 5}`.
4. **Pruning Step 5:** `climbStairs(5)` calls its right child `3`. Because `3 in help` evaluates to true, it instantly returns `3` without spawning any child branches.
5. **Final Output:** $5 + 3 = 8$.
