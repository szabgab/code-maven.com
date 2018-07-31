text = '/abc/def/da/de/abc_def_ge.txt'
def m = (text =~ /[^\/]*$/)
println m[0]     // abc_def_ge.txt
