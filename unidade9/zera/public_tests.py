import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
zera_nao_nulos = getattr(undertest, 'zera_nao_nulos', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
        jogo = [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]    
        zera_nao_nulos(jogo, 3, 2)
        assert jogo == [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
        ]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
