class Solution:
    def findTarget(self,root,k):
        bstarr = []
        
        def inorder(nodes):
            if not nodes:
                return
            inorder(nodes.left)
            bstarr.append(nodes.val)
            inorder(nodes.right)
        
        inorder(root)
        
        dic = {}
        for i, node in enumerate(bstarr):
            val = k - node
            if val in dic:
                return True
            dic[node] = i
        return False
        