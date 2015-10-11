require 'open-uri'
url = 'http://code-maven.com/'
fh = open(url)
html = fh.read
puts html

