from __future__ import print_function
import urllib, os, pickle
from HTMLParser import HTMLParser



class ArchiveHTMLParser(HTMLParser):
    # def __init__():
    #     pass

    def handle_starttag(self, tag, attrs):
        # <span class=date title="2015-04-12T08:11:49-05:00">
        if tag != 'a':
            return
        attr = dict(attrs)
        print(attr)
        # if attr.get('class') == 'date' and 'title' in attr:
        #     date = attr['title']
        #     print(date)


class Collector(object):
    def __init__(self):
        self.cache_file = 'python_weekly.pickle'
        self.data = { 'issue': 0}
        self.read_cache()

    def read_cache(self):
        if os.path.exists(self.cache_file):
            fh = open(self.cache_file, 'r')
            self.data = pickle.load(fh)
            fh.close()
    def save_cache(self):
        print(self.cache_file)
        fh = open(self.cache_file, 'w')
        pickle.dump(self.data, fh)
        fh.close()

    def collect(self):
        base_url = 'http://www.pythonweekly.com/archive/'
        while (True):
            self.data['issue'] += 1
            url = base_url + str(self.data['issue']) + '.html'
            print(url)
            f = urllib.urlopen(url)
            html = f.read()
            f.close()
            #print(html)
            parser = ArchiveHTMLParser()
            parser.feed(html)
            break
        self.save_cache()


Collector().collect()
