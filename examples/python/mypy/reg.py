import re

def check(regex, text) -> None:
    match = re.search(regex, text)
    print(match)
    z = match.group(0)
    print(z)

check('cat', 'Wilde cat')
check('dog', 'Wilde cat')
print('done')
