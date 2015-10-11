require 'open-uri'
url = 'http://code-maven.com/'
fh = open(url, 
   "User-Agent" => "Code-Maven-Example (see: http://code-maven.com/download-a-page-using-ruby )"
)
html = fh.read
puts html

