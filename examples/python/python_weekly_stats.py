from __future__ import print_function
import urllib
from HTMLParser import HTMLParser



class ArchiveHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # <span class=date title="2015-04-12T08:11:49-05:00">
        if tag != 'a':
            return
        attr = dict(attrs)
        print(attr)
        # if attr.get('class') == 'date' and 'title' in attr:
        #     date = attr['title']
        #     print(date)




def collect():
    base_url = 'http://www.pythonweekly.com/archive/'
    i = 1
    while (True):
        url = base_url + str(i) + '.html'
        print(url)
        f = urllib.urlopen(url)
        html = f.read()
        f.close()
        #print(html)
        parser = ArchiveHTMLParser()
        parser.feed(html)
        break


collect()
