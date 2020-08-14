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
			num_t += 1
		return num_t
    
	def checkInclusion(self, p, s):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""

		if len(s) < len(p):
			return []

		freqs = {}
		for c in p:
			if not c in freqs:
				freqs[c] = 0
			freqs[c] += 1

		start = 0
		end = 0
		num_t = 0
		sol = []

		while end < len(s):
			num_t = self.DecFreq(s[end], num_t, freqs)
			if num_t == len(freqs):
				sol.append(start)
			end += 1
			if end < len(p):
				continue
			num_t = self.IncFreq(s[start], num_t, freqs)
			start += 1
		return sol
