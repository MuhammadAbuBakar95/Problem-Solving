class Solution(object):
    def twoSum(self, arr, target):
        new_arr = [(val, idx) for (idx, val) in enumerate(arr)]
        new_arr.sort()
        start_pointer = 0
        end_pointer = len(arr) - 1

        while start_pointer < end_pointer:
            sum = new_arr[start_pointer][0] + new_arr[end_pointer][0]
            if sum > target:
                end_pointer -= 1
            elif sum < target:
                start_pointer += 1
            else:
                return [new_arr[start_pointer][1], new_arr[end_pointer][1]]

arr = [3, 2, 4]
target = 6

sol = Solution()
print sol.twoSum(arr, target)