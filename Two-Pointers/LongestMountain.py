class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if len(A) < 3:
            return 0
            
        start = 0
        end = 1
        maximum = 0
        
        while True:
            num = 0
            while end < len(A) and A[end] > A[end - 1]:
                end += 1
                num += 1
            if end == len(A):
                break
            if num <= 0:
                start = end
                end += 1
                continue
            num = 0
            while end < len(A) and A[end] < A[end - 1]:
                end += 1
                num += 1
            if num <= 0:
                start = end
                end += 1
                continue          
            maximum = max(maximum, end - start)
            if end == len(A):
                break
            start = end - 1
        return maximum

arr = [0,2, 2]
print Solution().longestMountain(arr)