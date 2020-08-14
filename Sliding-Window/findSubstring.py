class Solution(object):
    
    def IncFreq(self, word, num_t, freqs):
        if not word in freqs:
            return num_t
        freqs[word] += 1
        if freqs[word] == 1:
            num_t -= 1
        return num_t

    def DecFreq(self, word, num_t, freqs):
        if not word in freqs:
            return num_t
        freqs[word] -= 1
        if freqs[word] == 0:
            num_t += 1
        return num_t
      
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if len(s) == 0:
            return []
        if len(words) == 0:
            return []

        lw = len(words[0])
        if len(s) < len(words) * lw:
            return []

        sol = []
        for start in xrange(lw):
            end = start
            num_t = 0
            freqs = {}
            for word in words:
                if not word in freqs:
                    freqs[word] = 0
                freqs[word] += 1
            while end < len(s):
                num_t = self.DecFreq(s[end : end + lw], num_t, freqs)
                if num_t == len(freqs):
                    sol.append(start)
                end += lw
                if end - start <= (len(words) - 1) * lw:
                    continue
                num_t = self.IncFreq(s[start : start + lw], num_t, freqs)
                start += lw
        return sol

s = "aaaaaaaa"
words = ["aa","aa","aa"]
sol = Solution()
print sol.findSubstring(s, words)