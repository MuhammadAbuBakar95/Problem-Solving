class Solution(object):

	def switchwords(self, s, start_start, start_end, end_start, end_end):
		print s[start_start:start_end], s[end_start + 1:end_end + 1]
		start_len = start_end - start_start + 1
		l = min(start_len, end_end - end_start)
		print l
		for i in xrange(l):
			tmp = s[start_start + i]
			s[start_start + i] = s[end_start + i + 1]
			s[end_end - start_len + 1 + i] = tmp

		print l, s[start_start:start_end], s[end_start:end_end]

		start_waiting = False
		end_waiting = False
		start_start += l
		end_start += l

		if start_end - start_start - 1 <= end_end - end_start:
			end_waiting = True

		elif start_end - start_start - 1 >= end_end - end_start:
			start_waiting = True
			
		print start_waiting, end_waiting, start_start, start_end, end_start, end_end
		print "****************************************************"
		return start_waiting, end_waiting, start_start, start_end, end_start, end_end

	def reverseWords(self, s):
		"""
		:type s: List[str]
		:rtype: None Do not return anything, modify s in-place instead.
		"""
		start_start = 0
		start_end = 0
		start_waiting = False

		end_start = len(s) - 1
		end_end = len(s) - 1
		end_waiting = False

		while start_end < end_start:
			if s[start_end] == ' ':
				start_waiting, end_waiting, start_start, start_end, end_start, end_end = self.switchwords(s, start_start, start_end, end_start, end_end)

			if s[end_start] == ' ':
				end_waiting = True
				if start_waiting:
					start_waiting, end_waiting, start_start, start_end, end_start, end_end = self.switchwords(s, start_start, start_end, end_start, end_end)

			if not start_waiting:
				start_end += 1
			if not end_waiting:
				end_start -= 1
		return s
# s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s = "a good bat is wooden"
arr = []
for c in s:
	arr.append(c)
sol = Solution()
print sol.reverseWords(arr)