cart = []

prices = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "eggs": 60
}

try:
    n = int(input("How many items do you want to add? "))
except ValueError:
    print("Invalid number!")
    exit()

for i in range(n):
    item = input("Enter item name: ").lower()
    cart.append(item)

print("Cart items:", cart)

unique_items = set(cart)
print("Unique items:", unique_items)

total = 0

for item in unique_items:
    count = cart.count(item) 
    if item in prices:
        cost = prices[item] * count
        print(f"{item} x {count} = {cost}")
        total += cost
    else:
        print(f"{item} not available in price list")

print("Total cost:", total)

try:
    amount_paid = float(input("Enter amount paid: "))
    if amount_paid < total:
        print("Insufficient amount!")
    else:
        print("Change:", amount_paid - total)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
