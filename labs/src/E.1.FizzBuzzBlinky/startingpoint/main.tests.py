import unittest
try:
    from .main import toColor, getPosition
except:
    from main import toColor, getPosition

class TestToColor(unittest.TestCase):
    def test_3_should_be_green(self):
        (r, g, b) = toColor(3)
        assert r==0
        assert g==255
        assert b==0


class TestGetPosition(unittest.TestCase):
    def test_0_shoud_be_0x0(self):
        row,column = getPosition(0)
        assert row==0
        assert column==0



if __name__ == '__main__':
    unittest.main(verbosity=2)
