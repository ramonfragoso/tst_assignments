import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
tem123plus = getattr(undertest, 'tem123plus', None)

class PublicTests(unittest.TestCase):

    def test_1_exemplo1(self):
        assert tem123plus([3,2,1,2,3]) == 2

    def test_2_exemplo2(self):
        assert tem123plus([4,1,1,1,4,2,3]) == 1

    def test_3_exemplo3(self):
        assert tem123plus([1,2,2,3]) == 0

    def test_3_exemplo4(self):
        assert tem123plus([1,2,2,4]) == -1

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
