class Solution(object):

	def IncFreqs(self, c, freqs, num_unique):
		if not c in freqs:
			freqs[c] = 0
		freqs[c] += 1
		if freqs[c] == 1:
			num_unique += 1
		return num_unique

	def DecFreqs(self, c, freqs, num_unique):
		freqs[c] -= 1
		if freqs[c] == 0:
			num_unique -= 1
		return num_unique

	def lengthOfLongestSubstringKDistinct(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""

		freqs = {}
		num_unique = 0
		start = 0
		end = 0
		maximum = 0
		for end in xrange(len(s)):
			num_unique = self.IncFreqs(s[end], freqs, num_unique)
			while num_unique > k:
				num_unique = self.DecFreqs(s[start], freqs, num_unique)
				start += 1

			maximum = max(end - start + 1, maximum)
		return maximum

s = "eceba"
k = 2
sol = Solution()
print sol.lengthOfLongestSubstringKDistinct(s, k)