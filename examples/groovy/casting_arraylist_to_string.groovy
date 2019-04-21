
def names = ['Foo', 'Bar']
z = names as String
println(names)   // [Foo, Bar]
println(z)       // [Foo, Bar]

println(names.getClass())   // class java.util.ArrayList
println(z.getClass())       // class java.lang.String
