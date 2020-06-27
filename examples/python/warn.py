import warnings

def do_something():
    warnings.warn("Some warning")

def main():
    print("before")
    do_something()
    print("after")

main()
