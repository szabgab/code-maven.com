
hidden = rand(200)
# puts hidden

print "Type in your guess: "
guess = gets.to_i

if guess == hidden
    puts "Hit"
elsif guess < hidden
    puts "Your guess is smaller that the hidden number"
else
    puts "Your guess is bigger that the hidden number"
end
