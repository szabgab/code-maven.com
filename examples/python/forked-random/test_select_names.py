import sys
sys.path.append('..')
import selectnames
import random

def test_select_names():
    random.seed(1)
    names = selectnames.select_names('../../data/names.txt', 3)
    print(names)
