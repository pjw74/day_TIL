"""
def solution(x):
    
    def fibo(n):        
        if n == 1 or n==2:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)
        
    #answer = fibo(x)    
    return fibo(x)
"""


def solution(x):
    def fibo(n):
        a = 1
        b = 1
        if n == 1 or n == 2:
            return 1
        for i in range(1, n):
            a, b = b, b+a
        return a
    return fibo(x)
