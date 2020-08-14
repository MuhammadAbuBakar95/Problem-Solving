from numpy import median

class Solution(object):

	def removeIndex(self, ls, idx):
		for i, e in enumerate(ls):
			if e[1] == idx:
				break
		del ls[i]

	def insertSorted(self, ls, val):
		insert_at = -1
		for i, e in enumerate(ls):
			if e > val:
				insert_at = i
				break
		if insert_at >= 0:
			ls.insert(insert_at, val)
		else:
			ls.append(val)

	def getMedian(self, ls):
		if len(ls) % 2 == 1:
			mid = len(ls)/2
			return float(ls[mid][0])
		else:
			mid1 = len(ls)/2 - 1
			mid2 = len(ls)/2
			return (float(ls[mid1][0]) + float(ls[mid2][0]))/2

	def medianSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[float]
		"""

		window = [(val, idx) for (idx, val) in enumerate(nums[:k])]
		window.sort()

		start = 0
		end = k
		medians = []
		while end < len(nums):
			medians.append(self.getMedian(window))
			self.removeIndex(window, start)
			self.insertSorted(window, (nums[end], end))
			start += 1
			end += 1
		medians.append(self.getMedian(window))
		return medians

nums = [1,4,2,3]
k = 4

sol = Solution()
print sol.medianSlidingWindow(nums, k)