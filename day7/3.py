def is_palindrome(number):
    temp = number
    reverse = 0

    while temp > 0:
        digit =  temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    return reverse == number

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a palindrome number")
