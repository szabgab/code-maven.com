
class CB(object):
   def __init__(self, action):
      self.THRESHOLD = 4
      self.errors = 0
      self.action = action

   def run(self, *args, **kw):
       if self.errors > self.THRESHOLD:
           raise Exception("Service Not Available")

       res = self.action(*args, **kw)
       return res
    
