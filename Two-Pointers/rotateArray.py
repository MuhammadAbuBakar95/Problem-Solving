class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new_arr = []
        k = k % len(nums)
        i = len(nums) - 1
    	first_start = 0
    	second_start = len(nums) - k

    	while first_start != k:
 			tmp = nums[first_start]
 			nums[first_start] = nums[second_start]
 			nums[second_start] = tmp
 			first_start += 1
 			second_start += 1


arr = [1, 2, 3, 4, 4, 5, 6, 7]
	   5, 6, 7, 4, 1, 2, 3
	   5, 6, 7, 1, 2, 3, 4
k = 7

sol = Solution()
sol.rotate(arr, k)
print arr