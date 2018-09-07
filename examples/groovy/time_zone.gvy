import java.util.TimeZone

tz = TimeZone.getTimeZone("Asia/Jerusalem")

def ts = new Date()
println(ts)                                 // 12:43:14 UTC 2018
println(ts.format("HH:mm"))                 // 12:43
println(ts.format("HH:mm", timezone=tz))    // 15:43
