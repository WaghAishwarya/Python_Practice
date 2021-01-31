
# 0,1,1,2,3,5,8,13,21,34,55

def Fibonacci(n):
    if n<=0:
        print("Incorrect Input")

    elif n==1:
        return 0

    elif n==2:
        return 1

    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print(Fibonacci(5))
print(Fibonacci(8))
print(Fibonacci(7))
print(Fibonacci(6))