import traceback
import sys

data = {}

#name = data['name']
# KeyError: 'name'

def f(n):
   if n > 0:
       f(n-1)
   raise Exception("hello")
  
try:
    #name = data['name']
    f(2)
except Exception as e:
    print("Exception: {}".format(type(e).__name__))
    #print(dir(e))
    #print(e.__traceback__())
    #traceback.print_exc()
    #print(traceback.extract_stack())
    print("Exception: " + ''.join(traceback.format_exception(*sys.exc_info())))


