import unittest
from main import toColor, getPosition

class TestToColor(unittest.TestCase):

    def test_3_should_be_green(self):
        (r, g, b) = toColor(3)
        assert r==0
        assert g==255
        assert b==0

    def test_1_should_be_white(self):
        (r, g, b) = toColor(1)
        assert r==255
        assert g==255
        assert b==255

    def test_15_should_be_red(self):
        (r, g, b) = toColor(15)
        assert r==255
        assert g==0
        assert b==0

    def test_10_should_be_blue(self):
        (r, g, b) = toColor(10)
        assert r==0
        assert g==0
        assert b==255


class TestGetPosition(unittest.TestCase):

    def test_0_shoud_be_0x0(self):
        row,column = getPosition(0)
        assert row==0
        assert column==0

    def test_16_shoud_be_0x1(self):
        row,column = getPosition(16)
        assert row==0
        assert column==1


if __name__ == '__main__':
    unittest.main(verbosity=2)
