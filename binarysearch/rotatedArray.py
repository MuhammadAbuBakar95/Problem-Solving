class Solution(object):
    def getRotIdx(self, nums, start, end):
        if start == end:
            return start  
            
        mid = (end + start)/2
        print mid
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        if start == end - 1:
            return 0
        elif nums[mid] > nums[0]:
            return self.getRotIdx(nums, mid, end)
        else:
            return self.getRotIdx(nums, start, mid)

    def searchIdx(self, nums, target, start, end):
        if start == end:
            return start if nums[start] == target else -1 
         
        mid = (end + start)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.searchIdx(nums, target, mid + 1, end)
        else:
            return self.searchIdx(nums, target, start, mid)
               
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        rot_idx = self.getRotIdx(nums, 0, len(nums) - 1)
        if rot_idx == 0:
            return self.searchIdx(nums, target, 0, len(nums) - 1)
        l = self.searchIdx(nums, target, 0, rot_idx - 1)
        if l >= 0:
            return l
        return self.searchIdx(nums, target, rot_idx, len(nums) - 1)

nums = [4,5,6,7,0,1,2]
target = 0
nums = [1]
target = 0
sol = Solution()
print sol.search(nums, target)  