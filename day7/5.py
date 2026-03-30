def is_perfect(number):
    if number <= 0:
        return False

    total = 0
    
    for i in range(1, number):
        if number % i == 0:
            total += i

    return total == number

num = int(input("Enter a number: "))

if is_perfect(num):  
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")
