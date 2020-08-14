class Solution(object):
    def searchIdx(self, nums, target, start, end):
        if start == end:
            return nums[start] if ord(nums[start]) > ord(target) else nums[0]
        if start == end - 1:
            if ord(nums[start]) <=  ord(target) and ord(nums[end]) > ord(target):
                return nums[end]
            else:
                return nums[0]

        mid = (end + start)/2
        if ord(nums[mid]) <=  ord(target) and ord(nums[mid + 1]) > ord(target):
            return nums[mid + 1]
        elif ord(nums[mid]) > ord(target):
            return self.searchIdx(nums, target, start, mid)
        else:
            return self.searchIdx(nums, target, mid, end)
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        return self.searchIdx(nums, target, 0, len(nums) - 1)


letters = ["c", "f", "j"]
target = "d"
sol = Solution()
print sol.search(letters, target)