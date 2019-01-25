import random
import sys

def select_names(filename, count):
    with open(filename) as fh:
        names = fh.read().splitlines()

    selected_names = []
    for _ in range(count):
        pick = names[ random.randrange(len(names)) ]
        if pick not in selected_names:
            selected_names.append(pick)
    return selected_names


if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit('Usage: {} FILENAME COUNT'.format(sys.argv[0]))
    names = select_names(sys.argv[1], int(sys.argv[2]))
    for n in names:
        print(n)

