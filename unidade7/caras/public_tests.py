import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
sequencia_caras = getattr(undertest, 'sequencia_caras', None)

class PublicTests(unittest.TestCase):

    def test_1_exemplo(self):
        jogo1 = [0,1,1,0,1,0,0,0]
        jogo2 = [1,0,1]
        jogo3 = [0,1,1,1,0]

        assert sequencia_caras( jogo1 ) == 2
        assert sequencia_caras( jogo2 ) == 1
        assert sequencia_caras( jogo3 ) == 3

        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
