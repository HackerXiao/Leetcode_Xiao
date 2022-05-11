# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.


import collections

# 1. substing 2. window长度确定 
class Solution:
    def findAnagrams(self, s: str, pattern: str) -> list[int]:
        if len(s) == 0:
            return []

        match_indices = []  # the global state
        pattern_counter = collections.Counter()
        for char in pattern:
            pattern_counter[char] += 1

        # window state variables
        start_idx = 0
        window_counter = collections.Counter()

        for end_idx in range(len(s)):
            char = s[end_idx]
            window_counter[char] += 1

            # shrink window until it meets requirement
            while start_idx < len(s) and window_counter[s[start_idx]] > pattern_counter[s[start_idx]]:
                window_counter[s[start_idx]] -= 1
                if window_counter[s[start_idx]] == 0:
                    window_counter.pop(s[start_idx])
                start_idx += 1

            # and meets requirement
            if window_counter == pattern_counter:
                match_indices.append(start_idx)

        return match_indices


