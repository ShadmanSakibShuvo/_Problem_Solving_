class Solution:
    def isPalindrome(self,x):
        xs=str(x)
        xi=xs[::-1]
        if xs==xi:
            return True
        else:
            return False