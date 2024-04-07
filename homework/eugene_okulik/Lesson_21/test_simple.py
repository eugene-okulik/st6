import pytest
import sys
import random
import allure


class TestOne:
    @allure.feature('simple')
    @allure.story('Test one is one')
    @pytest.mark.simple
    @pytest.mark.skip('Bug #136')
    def test_one(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1

    @allure.feature('simple')
    @allure.story('Test one is one')
    @pytest.mark.simple
    @pytest.mark.skipif(sys.platform == 'linux', reason='Not working on Linux')
    def test_two(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1

    @allure.feature('simple')
    @allure.story('Test one is one')
    @pytest.mark.simple
    def test_three(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 2


@allure.feature('simple')
@allure.story('Test one is one')
@pytest.mark.simple
def test_four(class_process):
    assert 1 == 1


@allure.feature('simple')
@allure.story('Test one random')
def test_random():
    assert 1 == random.randrange(0, 5)
