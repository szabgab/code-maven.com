import pytest


@pytest.mark.skip("This is going to be skipped")
def test_skipper():
    x = 10 / 0


@pytest.mark.xfail(reason="So we can check xfail that fails")
def test_known_bug():
    assert 7 == 8

@pytest.mark.xfail(reason="So we can check xfail that succeeds")
def test_fixed_bug():
    assert 10 == 10
