File tf = File.createTempFile("temp",".tmp")
tf.write("Hello world")   // write to the file
println(tf.absolutePath)  // path to the file
tf.delete()               // delete the file
