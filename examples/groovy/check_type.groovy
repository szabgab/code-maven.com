def obj = ["question", 42, 'answer']

println obj.getClass()   // class java.util.ArrayList

println (obj instanceof List)                   // true
println (obj instanceof java.util.ArrayList)    // true

println (obj.getClass() == List)                // false
println (obj.getClass() == java.util.ArrayList) // true
