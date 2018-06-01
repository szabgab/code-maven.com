def obj = ["question", 42, 'answer']

println obj.getClass()   // class java.util.ArrayList

// Check if obj is the subclass of some class
println (obj instanceof List)                   // true
println (obj instanceof java.util.ArrayList)    // true

// Check the exact type of an object
println (obj.getClass() == List)                // false
println (obj.getClass() == java.util.ArrayList) // true
