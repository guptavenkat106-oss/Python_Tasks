numbers = [10, 25, 30, 45, 50]

search = int(input("Enter number to search: "))

for n in numbers:
    if n == search:
        print("Number found:", n)
        break
else:
    print("Number not found")
