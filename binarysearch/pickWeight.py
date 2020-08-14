import random
import bisect
import numpy
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.s = []
        self.nums = []
        for idx, val in enumerate(w):
            self.s.append(val if idx == 0 else self.s[idx - 1] + val)
            self.nums.append(0)
        
    def pickIndex(self):
        """
        :rtype: int
        """
        x = numpy.random.randint(1, high=self.s[-1] + 1)
        i = bisect.bisect_left(self.s, x)
        self.nums[i] += 1
        return i

w = [3,14,1,7]
solution = Solution(w);
for i in xrange(100000):
    solution.pickIndex()
print w, sum(w)
print solution.nums, sum(solution.nums)