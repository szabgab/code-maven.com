import requests
res = requests.get('https://www.lipsum.com/')
text = res.text
words = text.split()

words = ['apple', 'banana', 'peach', 'melon', 'Lorem', 'Ipsum']
words_set = set(words)

first = next(filter(lambda word: word in words_set,  words), None)
print(first)
