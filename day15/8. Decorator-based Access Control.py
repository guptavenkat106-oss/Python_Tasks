# Store users and their roles
user_roles = {
    "alice": "admin",
    "bob": "editor",
    "charlie": "viewer"
}

def require_role(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):

            role = user_roles.get(user)

            if role == required_role:
                return func(user, *args, **kwargs)
            else:
                return f"Access denied for {user}. Required role: {required_role}"
        
        return wrapper
    return decorator


@require_role("admin")
def delete_post(user):
    return f"{user} deleted a post"

@require_role("editor")
def edit_post(user):
    return f"{user} edited a post"

@require_role("viewer")
def view_post(user):
    return f"{user} viewed a post"


print(delete_post("alice"))    # Allowed
print(delete_post("bob"))      # Denied

print(edit_post("bob"))        # Allowed
print(edit_post("charlie"))    # Denied

print(view_post("charlie"))    # Allowed
