#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new
print cgi.header
 
print "Hello World!\n"
