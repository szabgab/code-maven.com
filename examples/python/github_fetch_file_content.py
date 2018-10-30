import urllib2
import json
import base64

#print t.tree[1].url
#fh = urllib2.urlopen(t.tree[1].url)

url = 'https://api.github.com/repos/sigmavirus24/github3.py/git/blobs/b5e8c177ca486b518863d9142a45503f7917f99a'
fh = urllib2.urlopen(url)
as_json = fh.read()
file_info = json.loads(as_json)
print base64.b64decode(file_info['content'])


