import sys


def is_admin(func):
    def wrapper(**kwargs):
        user_type = kwargs.get("user_type")
        sys.tracebacklimit = 0
        if user_type == "admin":
            return func(**kwargs)
        else:
            raise ValueError("Permission denied")

    return wrapper


@is_admin
def show_customer_receipt(**kwargs):
    return "Receipt shown."


print(show_customer_receipt(user_type="admin"))

print(show_customer_receipt(user_type="user"))
