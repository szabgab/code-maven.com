import groovy.time.TimeCategory
import groovy.time.TimeDuration

def start = new Date()
println(start)
print("Press any key ...")
def name = System.in.newReader().readLine()
def stop = new Date()
println(stop)
diff = stop - start
println(diff)


TimeDuration td = TimeCategory.minus( stop, start )
println td


