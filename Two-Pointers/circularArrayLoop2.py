
class Solution(object):
	def checkSign(self, num, sign):
		if sign == "pos" and num >= 0:
			return True
		if sign == "neg" and num < 0:
			return True
		return False

	def circularArrayLoopSign(self, nums, sign):
		slow = 0
		fast = 0
		it = 0

		while True:
			if not self.checkSign(nums[fast], sign) or fast + nums[fast] % len(nums) == fast:
				break
			fast += nums[fast]
			fast = fast % len(nums)
			it += 1
			if it % 2 == 1:
				continue
			slow += nums[slow]
			slow = slow % len(nums)
			if fast == slow:
				return True
		return False

	def circularArrayLoop(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) == 0:
			return False
		return self.circularArrayLoopSign(nums, "pos") or self.circularArrayLoopSign(nums, "neg") 

arr = [3, 1, 2]
sol = Solution()
print sol.circularArrayLoop(arr)