#!/usr/bin/env ruby
require 'json'

puts JSON.pretty_generate( JSON.parse( STDIN.read ) )

