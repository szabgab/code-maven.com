import java.util.TimeZone

tz = TimeZone.getTimeZone("Asia/Jerusalem")
print(tz)

def ts = new Date()
println(ts)
println(ts.format("HH:mm"))
println(ts.format("HH:mm", timezone=tz))
