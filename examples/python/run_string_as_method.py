method = "hello"

class Joe(object):
   def hello(self):
       print("Hello", end=" ")
   def world(self):
       print("World!")

j = Joe()
j.hello()
j.world()

for method in ['hello', 'world']:
    getattr(j, method)()

# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
# Calling a me
# python string as method name
import foo
method_to_call = getattr(foo, 'bar')
result = method_to_call()

result = getattr(foo, 'bar')()

