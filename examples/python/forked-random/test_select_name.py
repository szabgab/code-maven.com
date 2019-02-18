import sys
sys.path.append('..')
import selectnames
import random

def test_select_name():
    random.seed(1)
    name = selectnames.select_name('../../data/names.txt')
    assert name  == 'JESSICA'

    random.seed(2)
    name = selectnames.select_name('../../data/names.txt')
    assert name  == 'RUBY'

    random.seed(11)
    name = selectnames.select_name('../../data/names.txt')
    assert name  == 'JOSHUA'
