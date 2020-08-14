from collections import deque

class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		dq = deque()

		for i in xrange(k):
			j = 0
			while j < len(dq): 
				if dq[j] < nums[i]:
					del dq[j]
					j -= 1
				j += 1
			dq.append(nums[i])
		maximums = []
		start = 0
		for i in range(k, len(nums)):
			maximums.append(dq[0])
			if dq[0] == nums[start]:
				dq.popleft()

			j = 0
			while j < len(dq): 
				if dq[j] < nums[i]:
					del dq[j]
					j -= 1
				j += 1
			dq.append(nums[i])
			start += 1
		maximums.append(dq[0])
		return maximums

nums = [1,3,1,2,0,5]
k = 3

sol = Solution()
print sol.maxSlidingWindow(nums, k)