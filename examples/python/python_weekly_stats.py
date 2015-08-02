from __future__ import print_function
import urllib2, os, pickle, re, sys
from HTMLParser import HTMLParser


class ArchiveHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        if 'href' in attr:
            self.urls.append(attr["href"])
        else:
            print("Missing href from a with attributes: ", attr)


class Collector(object):
    def __init__(self):
        self.cache_file = 'python_weekly.pickle'
        self.data = { 'issue': 0, 'hosts' : {} }
        self.read_cache()

    def read_cache(self):
        if os.path.exists(self.cache_file):
            fh = open(self.cache_file, 'r')
            self.data = pickle.load(fh)
            fh.close()
    def save_cache(self):
        fh = open(self.cache_file, 'w')
        pickle.dump(self.data, fh)
        fh.close()

    def collect(self):
        base_url = 'http://www.pythonweekly.com/archive/'
        while (True):
            self.data['issue'] += 1
            url = base_url + str(self.data['issue']) + '.html'
            try:
                f = urllib2.urlopen(url)
                html = f.read()
                f.close()
            except urllib2.HTTPError as e:
                print(e, 'while fetching', url)
                break

            parser = ArchiveHTMLParser()
            parser.urls = []
            parser.feed(html)
            for u in parser.urls:
                if u == '#':
                    continue
                if not re.search(r'^https?://', u):
                    print("Unhandled url: " + u)
                    continue
                match = re.search(r'^https?://([^/]+)', u)
                if match:
                    host = match.group(1)
                    if host not in self.data['hosts']:
                        self.data['hosts'][host]  = 0
                    self.data['hosts'][host] += 1
            self.save_cache()

    def report(self):
        hosts, total = 0, 0
        for k in sorted(self.data['hosts'].keys(), key=lambda x: self.data['hosts'][x], reverse=True):
            hosts += 1
            total += int(self.data['hosts'][k])
            #print(k, self.data['hosts'][k])
            print('<li><a href="http://{0}/">{0}</a> {1}</li>'.format(k, self.data['hosts'][k]))
        print("A total of {} links to {} hosts in {} issues.".format(total, hosts, self.data['issue']))

    def run(self):
        if len(sys.argv) == 2:
            if sys.argv[1] == 'collect':
                self.collect()
            if sys.argv[1] == 'report':
                self.report()
        else:
            self.collect()
            self.report()

Collector().run()
