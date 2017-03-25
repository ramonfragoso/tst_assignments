import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
pre_vogais = getattr(undertest, 'pre_vogais', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
      assert pre_vogais("Andrade") == ['r', 'd']
      assert pre_vogais("exemplo") == ['x', 'l']
      assert pre_vogais("hiaTO") == ['h', 'i', 't']
      assert pre_vogais("Arara") == ['r']

   def test_exemplo_2(self):
      assert pre_vogais("Andrade") == ['r', 'd']
      assert pre_vogais("exemplo") == ['x', 'l']
      assert pre_vogais("hiaTO") == ['h', 'i', 't']
      assert pre_vogais("Arara") == ['r']

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
