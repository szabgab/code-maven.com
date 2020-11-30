import requests
res = requests.get('https://www.lipsum.com/')
text = res.text

stop_words = ['apple', 'banana', 'peach', 'melon', 'Lorem', 'Ipsum']

locations = [] # list of tuples (location, word)

for word in stop_words:
    loc = text.find(word)

    if loc == -1:
        continue  # word not in text

    locations.append( (loc, word) )

if locations:
    locations.sort(reverse=True)
    first = locations[0][1]
else:
    first = None

print(first)
