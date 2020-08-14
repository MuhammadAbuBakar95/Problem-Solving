import numpy as np
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
     	start = 0
     	end = 0
     	curr_idx = 0
     	minimum = 0
     	arr = np.zeros(len(T))
     	while end < len(S):
     		c = S[end]
     		
     		end += 1
