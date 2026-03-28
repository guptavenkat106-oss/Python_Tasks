def fibonacci(n):
    if n <=0:
        return "invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
    
