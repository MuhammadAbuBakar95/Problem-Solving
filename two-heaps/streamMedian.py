from heapq import heappush, heappop, heappushpop

def customHeapPushMin(heap, val):
    heappush(heap, val)

def customHeapPushMax(heap, val):
    heappush(heap, -val)

def customHeapPushPopMin(heap, val):
    return heappushpop(heap, val)

def customHeapPushPopMax(heap, val):
    return -heappushpop(heap, -val)

def customHeapPeakMin(heap):
    return heap[0]

def customHeapPeakMax(heap):
    return -heap[0]

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower_heap = []
        self.upper_heap = []
        self.median = None
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.lower_heap) == 0 and len(self.lower_heap) == 0 and self.median == None:
            self.median = num                
        elif self.median != None: # odd elements
            if num < self.median:
                customHeapPushMax(self.lower_heap, num)
                customHeapPushMin(self.upper_heap, self.median)
            else:
                customHeapPushMax(self.lower_heap, self.median)
                customHeapPushMin(self.upper_heap, num)
            self.median = None
        else: # even elements
            lower_peak = customHeapPeakMax(self.lower_heap)
            upper_peak = customHeapPeakMin(self.upper_heap)
            if num >= lower_peak and num <= upper_peak:
                self.median = num
            elif num < lower_peak:
                self.median = customHeapPushPopMax(self.lower_heap, num)
            elif num > upper_peak:
                self.median = customHeapPushPopMin(self.upper_heap, num)
    def findMedian(self):
        """
        :rtype: float
        """
        if self.median == None:
            lower_peak = customHeapPeakMax(self.lower_heap)
            upper_peak = customHeapPeakMin(self.upper_heap)
            return float(lower_peak + upper_peak)/2
        else:
            return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
sol = MedianFinder()
sol.addNum(-1)
print sol.findMedian()
sol.addNum(-2)
print sol.findMedian()
sol.addNum(-3)
print sol.findMedian()
sol.addNum(-4)
print sol.findMedian()
sol.addNum(-5)
print sol.findMedian()


["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]