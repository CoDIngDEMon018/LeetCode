# 594. Longest Harmonious Subsequence

## Problem Description

We define a **harmonious array** as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array `nums`, the task is to find the length of its longest harmonious subsequence among all possible subsequences.

A **subsequence** is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

---

## Examples

### Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation: The longest harmonious subsequence is [3, 2, 2, 2, 3].


---

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

To solve this problem efficiently:

1. Count the frequency of each number using a hash map (dictionary).
2. For each unique number `num` in the array:
   - If `num + 1` exists in the map, calculate the sum of frequencies of `num` and `num + 1`.
3. Keep track of the maximum sum found.
4. Return the maximum sum found or 0 if none exists.

The algorithm runs in **O(n)** time, where n is the size of the input array, since it performs a single pass to count frequencies and another pass through the unique numbers.

---

## Code Example (Python)

```python  
def findLHS(nums):  
    from collections import Counter  
    freq = Counter(nums)  
    max_length = 0  
    for num in freq:  
        if num + 1 in freq:  
            max_length = max(max_length, freq[num] + freq[num + 1])  
    return max_length  
