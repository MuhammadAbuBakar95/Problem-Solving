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
	def medianSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[float]
		"""	
