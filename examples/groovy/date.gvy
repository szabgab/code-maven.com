d = new Date()
println(d)

println(d.getTime())  // epoch

d += 1        // increment days by 1
println(d)

println(d.next())    // next day (incement by 1)
println(d)

println(d.seconds)
println(d.minutes)
println(d.hours)
println(d.day)
println(d.month)
println(d.year)

e = d          // create a copy
e += 3         // increment by 3 days
println(e)
println(d)
z = e-d
println(z)     // 3

