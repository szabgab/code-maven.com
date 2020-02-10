from jpype import startJVM, shutdownJVM, java
#startJVM(getDefaultJVMPath(), "-ea")
startJVM(convertStrings=False)
java.lang.System.out.println("hello world")

random = java.util.Random()
number1 = random.nextInt(10)
number2 = random.nextInt(10)
print(number1, number2)
shutdownJVM()
