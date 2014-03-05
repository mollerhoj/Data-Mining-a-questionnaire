import unittest
from Preprocesser import Preprocesser

class Preprocesser_spec(unittest.TestCase):
  
  def setUp(self):
    self.p = Preprocesser()

  def test_should_clean_float(self):
    text = '2,34'
    number = self.p.clean_float(text)
    self.assertEqual(2.34,number)

unittest.main()
