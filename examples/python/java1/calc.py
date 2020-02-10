from jpype import startJVM, shutdownJVM, java, addClassPath, JClass, JInt
startJVM(convertStrings=False)
import jpype.imports
#addClassPath("org/pkg")
#from org.pkg import MyMath
#import MyMath
#import org.pkg as p
#print(p)
#print(p.__class__)

try:
    pass
    #print(dir(p))
    #p.MyMath.divide(6, 2)
    #import Calculator
    calc = JClass('Calculator')
    print(calc)
    print(dir(calc))
    res = calc.add(java.lang.Integer(2), java.lang.Integer(2))
    print(res)
    #from org.pkg import Calculator
    math = JClass('org.pkg.MyMath')
    res = math.divide(java.lang.Integer(6), java.lang.Integer(2))
    #res = math.divide(JInt(6), java.lang.Integer(2))
    print(res)

    #calc = Calculator()
    #print(calc)
except Exception as err:
    print(f"Exception: {err}")
