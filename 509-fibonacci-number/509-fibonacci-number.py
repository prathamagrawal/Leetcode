class Solution:
    def fib(self, n: int) -> int:
        x = 0
        y = 1
        result = x+y
        l=[]
        l.append(x)
        for i in range(n):
            l.append(result)
            result = x+y
            x = y
            y = result

        return l[n]