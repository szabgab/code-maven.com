import os
import pytest

articles = [filename for filename in os.listdir("md") if filename.endswith(".txt")]

@pytest.mark.parametrize("article", articles)
def test_articles(article, tmpdir):
    assert os.system(f'./bin/txt2md.py sites/en/pages/{article} > {tmpdir}/{article}') == 0
    assert os.system(f'diff md/{article} {tmpdir}/{article}') == 0
    #print(article)


if __name__ == '__main__':
    print('generate')
    for article in articles:
        os.system(f'./bin/txt2md.py sites/en/pages/{article} > md/{article}')
