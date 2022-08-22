def handle_something(value_or_values):
    if isinstance(value_or_values, list):
        return value_or_values
    elif isinstance(value_or_values, str):
        return [value_or_values]
    else:
        raise ValueError(f"expected a string or a list but got {type(value_or_values)}")

print(handle_something("hello"))
print(handle_something(["hi", "there"]))
print(handle_something(42))


