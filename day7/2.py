def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
def is_strong(number):
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == number
num = int(input("Enter a number:"))
if is_strong(num):
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a strong number")
        
