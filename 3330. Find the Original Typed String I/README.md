# 3330. Find the Original Typed String I

## Problem Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times consecutively.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string `word`, which represents the final output displayed on Alice's screen.

**Return** the total number of possible original strings that Alice might have intended to type.

---

## Examples

### Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".


---

## Constraints

- `1 <= word.length <= 100`
- `word` consists only of lowercase English letters.

---

## Approach

1. Identify consecutive groups of the same character in the given string.
2. Since Alice may have pressed a key too long at most once, only one group can be shortened to represent the original string.
3. For each group of repeated characters, determine the number of ways to shorten that group from its length down to 1 (as the original string must have at least one character).
4. Sum the number of possible original strings accounting for shortening only one group at a time plus the original string itself if no mistakes were made.

---

## Solution Code (Python)

```python  
def count_original_strings(word: str) -> int:  
    # Find groups of consecutive characters and their lengths  
    groups = []  
    count = 1  
    for i in range(1, len(word)+1):  
        if i < len(word) and word[i] == word[i-1]:  
            count += 1  
        else:  
            groups.append(count)  
            count = 1  

    # Total count of original strings  
    # Basic: original string itself counts as 1  
    total = 1  

    # For each group, calculate how many shorter versions can originate from it  
    for length in groups:  
        # Number of possible original lengths if this group was the one typed too long  
        # It ranges from 1 up to length (exclusive of length itself, since that is original)  
        # So additional options are length - 1  
        total += (length - 1)  

    return total  
