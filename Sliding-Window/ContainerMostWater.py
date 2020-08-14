class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        start = 0
        end = 0
        maximum_water = 0
        curr_water = 0
        n = len(height)
        while end < len(height):
            maximum_water = max(min(height[start], height[end]) * (end - start), maximum_water)
            print height[start], height[end], height[start] * (n - start - 1), height[end] * (n - end - 1), maximum_water
            if height[start] * (n - start - 1) < height[end] * (n - end - 1):
                start = end
            end += 1
        return maximum_water

h = [9,6,14,11,2,2,4,9,3,8]
sol = Solution()
print sol.maxArea(h)