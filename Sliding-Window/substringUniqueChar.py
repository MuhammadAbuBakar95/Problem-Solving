import numpy as np

class Solution(object):
    def IncFreq(self, c, k, freqs, curr_unique, num_sat):
        if not c in freqs:
            freqs[c] = 0
        freqs[c] += 1
        if freqs[c] == 1:
            curr_unique += 1    
        if freqs[c] == k:
            num_sat += 1
        return curr_unique, num_sat

    def DecFreq(self, c, k, freqs, curr_unique, num_sat):
        freqs[c] -= 1
        if freqs[c] == 0:
            curr_unique -= 1
        if freqs[c] == k - 1:
            num_sat -= 1
        return curr_unique, num_sat

    def SubstrUniqueChars(self, s, k, total_unique):
        start = 0
        end = 0
        curr_unique = 0
        num_sat = 0
        freqs = {}
        maximum = 0

        while end < len(s):
            c = s[end]
            curr_unique, num_sat = self.IncFreq(c, k, freqs, curr_unique, num_sat)
            while num_sat >= total_unique and num_sat == curr_unique and end < len(s) - 1:
                if num_sat == curr_unique:
                    maximum = max(end + 1 - start, maximum)                
                end += 1
                c = s[end]                
                curr_unique, num_sat = self.IncFreq(c, k, freqs, curr_unique, num_sat)

            while num_sat >= total_unique:
                if num_sat == curr_unique:
                    maximum = max(end + 1 - start, maximum)
                c = s[start]
                curr_unique, num_sat = self.DecFreq(c, k, freqs, curr_unique, num_sat)
                start += 1
            end += 1
        return maximum

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maximum = 0
        for i in xrange(26):
            maximum = max(maximum, self.SubstrUniqueChars(s, k, i + 1))
        return maximum


s = "aacbbbdc"
k = 2
sol = Solution()
print sol.longestSubstring(s, k)