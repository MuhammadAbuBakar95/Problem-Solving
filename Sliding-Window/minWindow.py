from sys import maxint
class Solution(object):

	def IncFreq(self, c, num_t, freqs):
		if not c in freqs:
			return num_t
		freqs[c] += 1
		if freqs[c] == 1:
			num_t -= 1
		return num_t

	def DecFreq(self, c, num_t, freqs):
		if not c in freqs:
			return num_t
		freqs[c] -= 1
		if freqs[c] == 0:
			print c, num_t
			num_t += 1
		return num_t

	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""

		freqs = {}

		for c in t:
			if not c in freqs:
				freqs[c] = 0
			freqs[c] += 1
		minimum = maxint
		min_str = ""
		start = 0
		end = 0
		num_t = 0
		while end < len(s):
			c = s[end]
			num_t = self.DecFreq(c, num_t, freqs)
			while num_t == len(freqs):
				if minimum > end + 1 - start:
					minimum = end + 1 - start
					min_str = s[start : end + 1]
				minimum = min(minimum, end + 1 - start)
				c = s[start]
				num_t = self.IncFreq(c, num_t, freqs)
				start += 1
			end += 1
		return min_str

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print sol.minWindow(s, t)