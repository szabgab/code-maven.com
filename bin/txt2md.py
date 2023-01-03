#!/usr/bin/env python
import sys
import os
import re

# Convert .txt articles to .md files that can be published on DEV.to

# remove leading and trailing empty rows from files (and code snippets)
# include the language in the verbatim code read from files
# include the name of the file of the code-snippet
# Convert <ul> and <li>

# <a href= links
# <h2> subtitles
# <include file
# <screencast

ext_to_lang = {
    "yml":  "yaml",
    "yaml": "yaml",
    "PL":   "perl",
    "pl":   "perl",
    "pm":   "perl",
    "py":   "python",
}



def convert(txt_file):
    #print(txt_file)
    filename = os.path.basename(txt_file)[0:-4]
    # md_file =  filename + '.md'
    #print(md_file)
    body = False
    code = False
    with open(txt_file) as fh:
        header = {}
        for line in fh:
            if not body:
                if re.search(r'^\s*$', line):
                    body = True
                    #line = "---\n"
                    line += f"title: {header['title']}\n"
                    line += f"canonical_url: https://code-maven.com/{filename}\n"
                    line += f"series:\n"
                    #line += "---\n"
                    line += "\n"
                    print(line)
                    continue

                match = re.search(r'=([a-z_]+)\s+(.+)$', line)
                if not match:
                    exit(f"ERROR in the header in line '{line}'")
                key = match.group(1)
                value = match.group(2)
                header[key] = value
                continue

            if not code:
                line = re.sub(r'^<screencast file="[^"]*" youtube="([^"]+)" />\s*$', r"{% youtube \1 %}\n", line)
                line = re.sub(r'<b>([^<]+)</b>', r"`\1`", line)
                line = re.sub(r'<hl>([^<]+)</hl>', r"`\1`", line)
                line = re.sub(r'<h2>([^<]+)</h2>', r"## \1", line)
                line = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r"[\2](\1)", line)
                if re.search('^=abstract (start|end)', line):
                    continue

                if re.search(r'^\s*</?ul>\s*$', line):
                    line = ''
                line = re.sub(r'^\s*<li>(.*)</li>$', r"* \1", line)

                match = re.search(r'<include file="([^"]+)">', line)
                if match:
                    include_file = match.group(1)
                    with open(include_file) as ifh:
                        content = ifh.read()
                        extmatch = re.search(r'\.([a-zA-Z0-9]+)$', include_file)
                        lang = ext_to_lang.get(extmatch.group(1), '')
                        line = f"```{lang}\n{content}\n```\n"

                if re.search(r'<code>', line):
                    code = True
                    line = "```\n"

            if re.search(r'</code>', line):
                code = False
                line = "```\n"

            print(line, end='')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} PATH_TO_TXT_FILE")
    convert(sys.argv[1])
