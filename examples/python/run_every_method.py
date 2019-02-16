python - run every method (in abc order)
method_list = [func for func in dir(self) if callable(getattr(self, func)) and func != "Run"]
for method in method_list:
  eval("self." + method + "()")


