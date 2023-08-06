def catch_errors(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            print(
                "Found 1 error during execution of your function:",
                f"{type(e).__name__} no such key as foo",
            )

    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data["key"])


some_function_with_risky_operation({"foo": "bar"})

some_function_with_risky_operation({"key": "bar"})
