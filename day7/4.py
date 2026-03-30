def is_prime(number):
    if number <= 1:
        return False

    for i in range(2,number):
        if number % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a Prime number")
    print("Factors: 1 and", num)
else:
    print(f"{num} is not a Prime number")
