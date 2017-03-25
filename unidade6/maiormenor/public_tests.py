import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
retorna_maior_menor = getattr(undertest, 'retorna_maior_menor', None)

class PublicTests(unittest.TestCase):

    def test_basico1(self):
        assert retorna_maior_menor([10,6,7,15,8]) == [15,6]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
