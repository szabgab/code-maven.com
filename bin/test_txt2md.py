import os
import pytest

articles = [
    'sites/en/pages/vanilla-javascript-counter.txt',
]

@pytest.mark.parametrize("article", articles)
def test_articles(article, tmpdir):
    basename = os.path.basename(article)
    assert os.system(f'./bin/txt2md.py {article} > {tmpdir}/{basename}') == 0
    assert os.system(f'diff md/{basename} {tmpdir}/{basename}') == 0
    #print(article)


if __name__ == '__main__':
    print('generate')
    for article in articles:
        basename = os.path.basename(article)
        os.system(f'./bin/txt2md.py {article} > md/{basename}')
