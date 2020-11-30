import requests
res = requests.get('https://www.lipsum.com/')
text = res.text
words = text.split()

stop_words = ['apple', 'banana', 'peach', 'melon', 'Lorem', 'Ipsum']
words_set = set(stop_words)

for word in words:
    if word in words_set:
        first = word
        break
else:
    first = None
print(first)
