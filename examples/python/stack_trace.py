import traceback

def g():
   f()

def f():
   raise Exception("hi")


try:
   g()
except Exception as e:
   track = traceback.format_exc()
   print(track)

print("---------------------")


g()



