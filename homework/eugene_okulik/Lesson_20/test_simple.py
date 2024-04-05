import pytest
import sys


class TestOne:
    @pytest.mark.simple
    @pytest.mark.skip('Bug #136')
    def test_one(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1

    @pytest.mark.simple
    @pytest.mark.skipif(sys.platform == 'linux', reason='Not working on Linux')
    def test_two(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1

    @pytest.mark.simple
    def test_three(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1


@pytest.mark.simple
def test_four(class_process):
    assert 1 == 1
