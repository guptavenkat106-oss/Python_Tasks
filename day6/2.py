products = {
    "pen": 10,
    "notebook": 50,
    "pencil": 5
}

categories = {"stationery"}
cart = []


# Recursive function
def recursive_total(cart_items):
    if len(cart_items) == 0:
        return 0
    product, quantity = cart_items[0]
    return (products[product] * quantity) + recursive_total(cart_items[1:])


def display_products():
    print("Available products:")
    for name, price in products.items():
        print(f"{name} : {price}")


def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            return

        item = (name, quantity)
        cart.append(item)
        print("Item added to cart successfully.")

    except NameError:
        print("Product not found in store.")
    except Exception as e:
        print("Error:", e)


def view_bill():
    try:
        if not isinstance(cart, list):
            raise TypeError

        print("Items in cart:")
        for item in cart:
            name, quantity = item
            print(f"{name} x {quantity}")

        try:
            total = recursive_total(cart)
            print("Total bill:", total)
        except ZeroDivisionError:
            print("Calculation error: division by zero.")

    except TypeError:
        print("Cart data type error.")
    except Exception as e:
        print("Error:", e)


def main():
    while True:
        print("\n1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_bill()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


main()
