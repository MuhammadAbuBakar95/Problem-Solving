class Solution(object):
    def getNum(self, s, idx):
        num_str = ""
        while True:
            c = s[idx]
            if not c.isdigit():
                break
            num_str += c
            idx += 1
        return int(num_str), idx
        
    def _decodeString(self, s, idx):
        starting_idx = idx
        start_ret_len = len(self.to_ret)
        if starting_idx in self.ht:
            self.to_ret += self.ht[starting_idx][0]
            return self.ht[starting_idx][1]
        while idx < len(s):
            c = s[idx]
            if c.isalpha():
                self.to_ret += c
            elif c.isdigit():
                num, idx = self.getNum(s, idx)
                for i in xrange(num):
                    new_idx = self._decodeString(s, idx)
                idx = new_idx
                continue
            elif c == ']':
                self.ht[starting_idx] = (self.to_ret[start_ret_len : len(self.to_ret)], idx + 1)
                return idx + 1
            idx += 1
        self.ht[starting_idx] = (self.to_ret[start_ret_len : len(self.to_ret)], idx)
        return idx
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.to_ret = ""
        self.ht = {}
        self._decodeString(s, 0)
        return self.to_ret


sol = Solution()
print sol.decodeString("2[2[y]pq4[2[jk]e1[f]]]")
