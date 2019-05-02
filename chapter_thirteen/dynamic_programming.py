# A recursive implementation of the Fibonacci function
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(n-2)
