import sys
import os
import re

# Convert .txt articles to .md files that can be published on DEV.to

# <a href= links
# <h2> subtitles
# <include file
# <screencast



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
                line = re.sub(r'<b>([^<]+)</b>', r"`\1`", line)
                line = re.sub(r'<h2>([^<]+)</h2>', r"## \1", line)
                line = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r"[\2](\1)", line)
                if re.search('^=abstract (start|end)', line):
                    continue

                match = re.search(r'<include file="([^"]+)">', line)
                if match:
                    include_file = match.group(1)
                    with open(include_file) as ifh:
                        content = ifh.read()
                        lang = ''
                        if include_file.endswith('yml'):
                            lang = 'yaml'
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
