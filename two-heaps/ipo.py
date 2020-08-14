from heapq import heappush, heappop, heappushpop

def customHeapPushMin(heap, val):
    heappush(heap, val)

def customHeapPushMax(heap, val):
    heappush(heap, -val)

def customHeapPushPopMin(heap, val):
    return heappushpop(heap, val)

def customHeapPushPopMax(heap, val):
    return -heappushpop(heap, -val)

def customHeapPopMin(heap):
    return heappop(heap, val)

def customHeapPopMax(heap):
    return -heappop(heap)

def customHeapPeakMin(heap):
    return heap[0]

def customHeapPeakMax(heap):
    return -heap[0]

class Solution(object):
    def addProfits(self, heap, capital_profits, W, start_idx):
        while start_idx < len(capital_profits):
            c, p = capital_profits[start_idx]
            if c > W:
                break
            customHeapPushMax(heap, p)
            start_idx += 1
        return start_idx

    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        
        capital_profits = zip(Capital, Profits)
        capital_profits.sort()
        heap = []
        start_idx = 0
        
        for i in xrange(k):
            start_idx = self.addProfits(heap, capital_profits, W, start_idx)
            if len(heap) == 0:
                break
            p = customHeapPopMax(heap)
            W += p
        return W

k = 10
W = 0
Profits = [1,2,3]
Capital = [0,1,2]

sol = Solution()
print sol.findMaximizedCapital(k, W, Profits, Capital)