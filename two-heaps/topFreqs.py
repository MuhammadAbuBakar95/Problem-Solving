from heapq import heappush, heappop, heappushpop

def customHeapPushMin(heap, val):
    heappush(heap, val)

def customHeapPushMax(heap, val):
    if type(val) is tuple:
        heappush(heap, (-val[0], val[1]))
    else:
        heappush(heap, -val)

def customHeapPushPopMin(heap, val):
    return heappushpop(heap, val)

def customHeapPushPopMax(heap, val):
    if type(val) is tuple:
        res = heappushpop(heap, (-val[0], val[1]))
        return (-res[0], res[1])
    else:
        return -heappushpop(heap, val)

def customHeapPopMin(heap):
    return heappop(heap, val)

def customHeapPopMax(heap):
    res = heappop(heap)
    if type(res) is tuple:
        return (-res[0], res[1])
    else:
        return -res

def customHeapPeakMin(heap):
    return heap[0]

def customHeapPeakMax(heap):
    res = heap[0]
    if type(res) is tuple:
        return (-res[0], res[1])
    else:
        return -res

def compareAlphOrder(word1, word2):
    min_word = word1 if len(word1) < len(word2) else word2
    for idx in xrange(len(min_word)):
        if ord(word1[idx]) < ord(word2[idx]):
            return word1
        elif ord(word1[idx]) > ord(word2[idx]):
            return word2
    return min_word
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        freqs = {}
        
        for word in words:
            if not word in freqs:
                freqs[word] = 0
            freqs[word] += 1

        heap = []
        for word in freqs:
            customHeapPushMax(heap, (freqs[word], word))
        sol = []
        for i in xrange(k):
            f, word = customHeapPopMax(heap)
            removed = [word]
            to_pop_idx = 0 
            while len(heap) > 0 and customHeapPeakMax(heap)[0] == f:
                removed.append(customHeapPopMax(heap)[1])
                if compareAlphOrder(removed[to_pop_idx], removed[-1]) == removed[-1]:
                    to_pop_idx = len(removed) - 1

            for idx, word in enumerate(removed):
                if idx == to_pop_idx:
                    sol.append(word)
                else:
                    customHeapPushMax(heap, (f, word))
        return sol


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
sol = Solution()
print sol.topKFrequent(words, k)