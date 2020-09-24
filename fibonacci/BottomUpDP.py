fib_nums = [None] * 10
fib_nums[0]=0
fib_nums[1] = 1
def Fibonacci(n):
    for i in range(2, n+1):
        fib_nums[i] = fib_nums[i-1]+fib_nums[i-2]
    return fib_nums[n]

for i in range(5):
    print(Fibonacci(5-i))
