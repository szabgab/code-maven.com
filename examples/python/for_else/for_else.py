numbers = [3, 5]

for n in numbers:
    if n % 2 == 0:
        even = n
        break
else:
    even = None

print(even)
