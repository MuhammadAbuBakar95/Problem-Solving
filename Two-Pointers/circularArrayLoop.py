class Solution(object):
    
    def checkSign(self, num, sign):
        if sign == "pos" and num >= 0:
            return True
        if sign == "neg" and num < 0:
            return True
        return False
    
    def createGraph(self, nums, sign):
        nodes = set([x for x in xrange(len(nums))])
        edges = {}
        
        for idx, num in enumerate(nums):

            if not self.checkSign(num, sign):
                edges[idx] = None
                continue

            edges[idx] = (idx + num) % len(nums)
        return nodes, edges
    
    def isCyclic(self, node, edges, stack, not_visited):
		if edges[node] == None or edges[node] == node:
			return False

		if edges[node] in stack:
			return True

		if not edges[node] in not_visited:
			return False

		not_visited.remove(edges[node])
		stack.add(edges[node])

		return self.isCyclic(edges[node], edges, stack, not_visited)
        
    def circularArrayLoopSign(self, nums, sign):
        nodes, edges = self.createGraph(nums, sign)
        not_visited = nodes
        while len(not_visited):
            node = not_visited.pop()
            stack = set([node])
            if self.isCyclic(node, edges, stack, not_visited):
                return True
        return False
            
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return self.circularArrayLoopSign(nums, "pos") or self.circularArrayLoopSign(nums, "neg") 

arr = [2,-1,1,2,2]
sol = Solution()
print sol.circularArrayLoop(arr)