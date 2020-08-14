class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        
        freqs = {}
        for b in barcodes:
        	if not b in freqs:
        		freqs[b] = 0
        	freqs[b] += 1

        max_freq = 0
        for c in freqs:
        	max_freq = max_freq(freqs[c], max_freq)

        