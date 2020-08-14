class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: List[str]
		:rtype: None Do not return anything, modify s in-place instead.
		"""

		if len(s) == 0:
			return s

		words = []


		word_start = len(s) - 1
		word_end = len(s)

		while word_start >= 0:
			if s[word_start] == ' ':
				if word_start < len(s) - 1:
					words.append((word_start + 1, word_end))        
				while s[word_start] == ' ' and word_start >= 0:
					word_start -= 1                
					word_end = word_start + 1
			else:
				word_start -= 1

		if s[0] != ' ':
			words.append((word_start + 1, word_end))
		new_s = ""
		for idx, (start, end) in enumerate(words):
			for i in range(start, end):
				new_s += s[i]
			if idx < len(words) - 1:
				new_s += ' '
		return new_s

s = " 1"
sol = Solution()
print sol.reverseWords(s)