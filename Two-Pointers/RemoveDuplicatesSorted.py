class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        check_idx = 1
        insert_idx = 1

        while check_idx < len(nums):
        	check_idx += 1
        	if nums[check_idx - 2] == nums[check_idx - 1]:
        		continue
        	nums[insert_idx] = nums[check_idx - 1]
        	insert_idx += 1
        
        return insert_idx