class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        curr = 0
        replace_at = len(nums) - 1
        new_len = len(nums)
        while curr < replace_at + 1:
            print nums, new_len, curr
            if nums[curr] == val:
                new_len -= 1
                tmp = nums[curr]
                nums[curr] = nums[replace_at]
                nums[replace_at] = tmp
                replace_at -= 1
            else:
                curr += 1
        return new_len

nums = [1]
val = 1
sol = Solution()
print sol.removeElement(nums, val)
print nums