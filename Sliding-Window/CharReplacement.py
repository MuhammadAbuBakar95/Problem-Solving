class Solution(object):
    def Inc(self, c, exc, num_others):
        if ord(c) != exc:
            num_others += 1
        return num_others
    
    def Dec(self, c, exc, num_others):
        if ord(c) != exc:
            num_others -= 1
        return num_others
    
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        maximum = 0
        for i in xrange(26):
            
            curr_char = i + ord('A')
            
            start = 0
            end = 0
            num_others = 0
            
            for end in xrange(len(s)):
                num_others = self.Inc(s[end], curr_char, num_others)                    
                while num_others > k:
                    num_others = self.Dec(s[start], curr_char, num_others)    
                    start += 1
                maximum = max(end - start + 1, maximum)
        return maximum

s = "ABAB"
k = 2
sol = Solution()
print sol.characterReplacement(s, k)