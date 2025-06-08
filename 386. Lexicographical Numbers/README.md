# 386. Lexicographical Numbers

## Problem Description

Given an integer `n`, return all the numbers in the range `[1, n]` sorted in **lexicographical order**.

You must write an algorithm that runs in **O(n)** time and uses **O(1)** extra space.

---

## Examples

**Example 1:**

 `Input: n = 13`

`Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]`


**Example 2:**

`Input: n = 2`

`Output: [1, 2]`


---

## Constraints

- `1 <= n <= 5 * 10^4`

---

## Solution Overview

To efficiently generate lexicographical numbers from `1` to `n`:

- Use a DFS-like iterative approach to traverse the numbers as if navigating a lexicographical tree.
- Start from 1 and try to multiply by 10 to go deeper (e.g., from 1 to 10).
- If you cannot go deeper (either out of range or no children), increment the current number.
- If incrementing leads to trailing zeros, remove those zeros to keep the number valid.
- This approach ensures time complexity of O(n) and uses constant extra space besides the output list.

---
