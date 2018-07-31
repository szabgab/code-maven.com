text = 'Some 42 number #12 more'
def ma = (text =~ /\d+/)
println ma              // java.util.regex.Matcher[pattern=\d+ region=0,23 lastmatch=]
println ma[0]           // 42

def mb = (text =~ /#\d+/)
println mb              // java.util.regex.Matcher[pattern=#\d+ region=0,23 lastmatch=]
println mb[0]           //  #12

def mc = (text =~ /#(\d+)/)
println mc[0]          // [#12, 12]
println mc[0][0]       // #12
println mc[0][1]       // 12
