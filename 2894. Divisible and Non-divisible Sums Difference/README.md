# 2894. Divisible and Non-divisible Sums Difference

## Problem Statement

You are given two positive integers, `n` and `m`.

Define two integers as follows:

- `num1`: The sum of all integers in the range `[1, n]` (inclusive) that are **not divisible** by `m`.
- `num2`: The sum of all integers in the range `[1, n]` (inclusive) that are **divisible** by `m`.

Return the integer value of `num1 - num2`.

## Example

If `n = 5` and `m = 2`:

- Numbers divisible by 2 are: 2, 4 → sum = 6 (`num2`)
- Numbers not divisible by 2 are: 1, 3, 5 → sum = 9 (`num1`)
- Result = `num1 - num2 = 9 - 6 = 3`

## Constraints

- `1 <= n, m <= 10^9` (assumed, depending on problem constraints)


