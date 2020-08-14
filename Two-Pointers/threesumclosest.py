import sys
class Solution(object):
	def twoSumClosest(self, arr, target):
		start_pointer = 0
		end_pointer = len(arr) - 1
		minimum_dist = sys.maxint
		minimum_dist_val = None 

		while start_pointer < end_pointer:
			s = arr[start_pointer] + arr[end_pointer]
			if minimum_dist > abs(s - target):
				minimum_dist = abs(s - target)
				minimum_dist_val = s
			if s > target:
				end_pointer -= 1
			elif s < target:
				start_pointer += 1
			else:
				return s
		return minimum_dist_val
    
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""

		nums.sort()
		minimum_dist = sys.maxint
		minimum_dist_val = None 
		for i in xrange(len(nums)):
			two_target = target - nums[i]
			two_arr = nums[:i]
			if i < len(nums) - 1:
				two_arr += nums[i + 1:]
			two_closest = self.twoSumClosest(two_arr, two_target)
			dist = abs(target - (two_closest + nums[i]))
			if minimum_dist > dist:
				minimum_dist = dist
				minimum_dist_val = two_closest + nums[i]
		return minimum_dist_val
nums = [0,1,2]
target = 3
sol = Solution()
print sol.threeSumClosest(nums, target)