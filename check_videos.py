import os
import re
import sys

# TBD fetch all the videos in the youtube channel
# For now we can download files via https://takeout.google.com/

# list the videos that are in none of the playlists
# check if all the videos on youtube have a page in code-maven.

def get_videos_from_code_maven(language):
    pages_dir = os.path.join('sites', language, 'pages')
    files = os.listdir(pages_dir)
    # print(files)
    entries = []
    for file in files:
        if not file.endswith('.txt'):
            continue
        with open(os.path.join(pages_dir, file)) as fh:
            for row in fh:
                match = re.search(r'<screencast file="([^"]+)" youtube="([^"]+)" />', row)
                if match:
                    entries.append(match.group(2))
    return entries

def main():
    language = 'he'
    print(get_videos_from_code_maven(language))

main()


