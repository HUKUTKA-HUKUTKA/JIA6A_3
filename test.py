import pytest
import lib

class Test_KAJIbKyJI9TOP:

    @pytest.fixture()
    def CJIOJEHUE(self):
        return 21, 21, '+'

    @pytest.fixture()
    def BbI4UTAHUE(self):
        return 62, 20, '-'

    @pytest.fixture()
    def gEJIEHUE(self):
        return 84, 2, '/'

    @pytest.fixture()
    def yMHOJEHUE(self):
        return 6, 7, '*'

    def test_1(self, CJIOJEHUE):
        assert lib.KAJIbKyJI9TOP(*CJIOJEHUE) == 42

    def test_2(self, BbI4UTAHUE):
        assert lib.KAJIbKyJI9TOP(*BbI4UTAHUE) == 42

    def test_3(self, gEJIEHUE):
        assert lib.KAJIbKyJI9TOP(*gEJIEHUE) == 42

    def test_4(self, yMHOJEHUE):
        assert lib.KAJIbKyJI9TOP(*yMHOJEHUE) == 42