class Solution(object):
    
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        s_end = len(S) - 1
        t_end = len(T) - 1
        s_spaces = 0
        t_spaces = 0
        
        while True:
            print s_end, t_end, s_spaces, t_spaces        
            if s_end >= 0 and S[s_end] == '#':
                s_spaces += 1
                s_end -= 1
                continue
            if t_end >= 0 and T[t_end] == '#':
                t_spaces += 1
                t_end -= 1
                continue
                
            if s_spaces:
                s_spaces -= 1
                s_end -= 1
                continue
            if t_spaces:
                t_spaces -= 1
                t_end -= 1
                continue

            if s_end < 0 or t_end < 0:
                break

            if S[s_end] != T[t_end]:
                return False
            s_end -= 1
            t_end -= 1        
        return s_end < 0 and t_end < 0

S = "ab##"
T = "c#d#"
sol = Solution()
print sol.backspaceCompare(S, T)