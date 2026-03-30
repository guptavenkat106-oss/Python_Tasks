def is_armstrong(number):
    temp = number
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    
    if total == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
