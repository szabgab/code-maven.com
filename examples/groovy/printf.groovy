def x = 66


def res = sprintf("value: %s", x)   // as string
println(res)
println(sprintf("value: %d", x))    // as decimal
println(sprintf("value: %c", x))    // as character


//  padding with 0
printf('%05d\n', x)
println( sprintf('%05d', x)  )


// indicate location of the value
names = ['First', 'Second', 'Third', 'Fourt']
println( sprintf('%2$s %3$s %3$s %1$s', names) )
