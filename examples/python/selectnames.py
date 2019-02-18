import random
import multiprocessing



def select_name(filename):
    with open(filename) as fh:
        names = fh.read().splitlines()

    return names[ random.randrange(len(names)) ]


def select_names(filename, count):
    selected_names = []
    with multiprocessing.Pool(count) as p:
        selected_names = p.map(select_name, [filename] * count)
    return selected_names

