# Python 3: Fibonacci series up to n

def fib(n=int):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b 
    print()


fib(1000)

# a, b = b, a+b 
# 0 and 1 = 1 and 1
# 1 and 1 = 1 and 2
# 1 and 2 = 2 and 3
# 2 and 3 = 3 and 5
# 3 and 5 = 5 and 8
# ...

a = 1 + 2 + 3 + \
    5 + 6