from bs4 import BeautifulSoup
# BeautifulSoup4-4.10.0 soupsieve-2.2.1
# html5lib-1.1

for html in [
    '<a if="{something.length > 0}">remove</a>'
    ]:
    for parser in ["lxml", "html5lib", "html.parser"]:
        soup = BeautifulSoup(html, parser)
        for formatter in [None, "minimal", "html"]:
            prettyHTML = soup.prettify(formatter=formatter)
            print(prettyHTML)

