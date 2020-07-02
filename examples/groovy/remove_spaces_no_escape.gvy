def input_text = " hello world "
clean_text = input_text.replaceAll(~/\s/,"")
println("'${input_text}'")   // ' hello world '
println("'${clean_text}'")   // 'helloworld'
