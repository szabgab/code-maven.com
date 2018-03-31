puts __FILE__                                 #  examples/ruby/current_path.rb

puts File.expand_path(__FILE__)               # /Users/gabor/work/code-maven.com/examples/ruby/current_path.rb
puts File.dirname(File.expand_path(__FILE__)) # /Users/gabor/work/code-maven.com/examples/ruby
puts File.dirname(File.dirname(File.expand_path(__FILE__))) # /Users/gabor/work/code-maven.com/examples
