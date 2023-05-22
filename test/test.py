
import pytest


def test_sample1():
    assert True


def test_sample2():
    assert [1, 2, 3] != [3, 2, 1]


@pytest.mark.xfail()
def test_sample3():
    assert False


@pytest.mark.xfail()
def test_sample4():
    assert True
