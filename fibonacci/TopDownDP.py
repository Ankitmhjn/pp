fib_nums = [None] * 10
fib_nums[0]=0
fib_nums[1] = 1
fib_nums[2] = 2
def Fibonacci(n):
    if fib_nums[n] is None:
        fib_nums[n] = Fibonacci(n-1)+Fibonacci(n-2)
    return fib_nums[n]

for i in range(5):
    print(Fibonacci(i))
