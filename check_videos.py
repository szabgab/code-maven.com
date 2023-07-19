import csv
import os
import re
import sys

# TBD fetch all the videos in the youtube channel
# For now we can download files via https://takeout.google.com/

# list the videos that are in none of the playlists
# check if all the videos on youtube have a page in code-maven.

# All the videos from the Hebrew YouTube channel should be published on the code-maven site in the sites/he/pages folder.
# The videos from the English YouTube channel are divided between the code-maven.com site and the perlmaven.com site

exclude = [
    'Video Id',    # csv title row
    'muliGK6lz0U', # short
    'foR9n0ws1KQ', # short
    'qmmPz6ozNXY', # welcome video
]

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

def get_videos_from_youtube():
    ids = []
    with open('Video Metadata.csv') as fh:
        rd = csv.reader(fh)
        for row in rd:
            if row:
                vid = row[0].strip()
                if vid in exclude:
                    continue
                ids.append(vid)
    return ids

def main():
    language = 'he'
    code_maven = set(get_videos_from_code_maven(language))
    youtube = set(get_videos_from_youtube())

    print(sorted(code_maven - youtube))
    # This is strange it shows that we have videos on the site that are not in the YouTube channel.
    # I checked the first one and it was on YouTube as well so it unclear why does this say

    print(sorted(youtube - code_maven))
main()


