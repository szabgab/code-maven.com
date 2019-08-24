def data = [
    name : 'Foo Bar',
    age : 42,
    email : 'zoo@bor.com',
]

println(data)

for (field in data.keySet()) {
   println(field)
}

my_keys = data.keySet()
println(my_keys.getClass())     // class java.util.LinkedHashMap$LinkedKeySet

