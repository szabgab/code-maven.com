import re

author_email = 'foo@bar.com'
if not re.search(r'\A[\w.-]+@bar.com\Z', author_email):
   print("not")
#print(m)

