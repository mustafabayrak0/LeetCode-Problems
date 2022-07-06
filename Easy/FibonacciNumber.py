class Solution(object):
    def fib(self, n):
        x = Solution()
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return x.fib(n - 1) + x.fib(n - 2)
