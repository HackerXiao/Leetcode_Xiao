# 76. Minimum Window Substring
# Hard

# 10198

# 535

# Add to List

# Share
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

import typing
from collections import Counter


class Solution:
    def minWindow(self, s: str, pattern: str) -> str:
        if len(s) == 0:
            return ''

        shortest = None  # the global state

        pattern_counter = Counter()
        for char in pattern:
            pattern_counter[char] += 1

        # window state variables
        start_idx = 0
        # 1.  window state用什么记录
        window_counter = Counter()
        effective_count = 0 

        for end_idx in range(len(s)):
            char = s[end_idx]
            window_counter[char] += 1
            if window_counter[char] <= pattern_counter[char]:
                effective_count += 1

            # shrink window until it meets requirement
            # 2. shrink的条件是什么
            while start_idx < len(s) and window_counter[s[start_idx]] > pattern_counter[s[start_idx]]:
                start_char = s[start_idx]
                window_counter[start_char] -= 1
                if window_counter[start_char] == 0:
                    window_counter.pop(start_char)
                start_idx += 1
            
            # 3. window需要满足的条件是什么
            if effective_count == len(pattern):  # and meets requirement
                if shortest is None or (end_idx - start_idx + 1) < len(shortest):
                    shortest = s[start_idx:(end_idx + 1)]

        return shortest if shortest is not None else ''
