import warnings

def do_something():
    warnings.warn("Some warning")
    warnings.warn("Other warning")

def main():
    print("before")
    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter("always")
        do_something()
        for warn in caught_warnings:
            print("-----")
            print(f"warn: {warn.message}")
            print(warn.category)
            print(str(warn))
    print("-----")
    print("after")

main()
