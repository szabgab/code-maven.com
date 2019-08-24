def data = [
    name : 'Foo Bar',
    age : 42,
    email : 'zoo@bor.com',
]

println(data)

my_keys = data.keySet()
println(my_keys.getClass())     // class java.util.LinkedHashMap$LinkedKeySet

our_keys = my_keys as ArrayList
println(our_keys.getClass())    // class java.util.ArrayList
println(our_keys)

