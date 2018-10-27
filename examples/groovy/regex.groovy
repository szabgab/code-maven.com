url = 'https://10.11.12.13/some_name'
def match = url =~ '^https?://([^/]*)/([^/]*)$'
println match
println match[0]
println match[0][1]
println match[0][2]
