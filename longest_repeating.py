# -*- coding: utf-8 -*-
"""Longest_Repeating

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kzDDHYiA7MmhUoCak8d9W4rMDRUOM9gn
"""

# Time Complexity :  O(n)
# Space Complexity : O(1)
class Solution(object):
    def characterReplacement(self, s, k):
        maxlen, largestCount = 0, 0
        arr = collections.Counter()
        for idx in xrange(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen