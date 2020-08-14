import sys
class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""


		curr_ptr = 0
		curr_sum = 0
		maximum = -sys.maxint + 1

		while curr_ptr < len(nums):
			curr_sum += nums[curr_ptr]
			maximum = max(maximum, curr_sum)
			if curr_sum < 0:
				curr_sum = 0

			curr_ptr += 1

		return maximum