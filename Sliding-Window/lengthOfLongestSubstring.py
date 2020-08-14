class Solution(object):

	def IncFreqs(self, c, freqs, num_repeating):
		if not c in freqs:
			freqs[c] = 0
		freqs[c] += 1
		if freqs[c] == 2:
			num_repeating += 1
		return num_repeating

	def DecFreqs(self, c, freqs, num_repeating):
		freqs[c] -= 1
		if freqs[c] == 1:
			num_repeating -= 1
		return num_repeating

	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		freqs = {}

		start = 0
		end = 0
		num_repeating = 0
		maximum = 0

		for end in xrange(len(s)):
			num_repeating = self.IncFreqs(s[end], freqs, num_repeating)
			while num_repeating:
				num_repeating = self.DecFreqs(s[start], freqs, num_repeating)
				start += 1
			maximum = max(maximum, end + 1 - start)
		return maximum

sol = Solution()
print sol.lengthOfLongestSubstring("abcabcbb")