class Solution(object):
    def isPalindrome(self, x):
        self.x =x
        if str(x) == str(x)[::-1] and x>=0:
            return True
        else:
            return False

        
