is_logged_in = False

def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access Denied! Please log in first.")
    return wrapper


@login_required
def view_account():
    print("Welcome! Accessing your account details...")


view_account()

is_logged_in = True

view_account()
