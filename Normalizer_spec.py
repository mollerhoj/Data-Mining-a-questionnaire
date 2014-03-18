import unittest
import pandas as pd
from Normalizer import Normalizer

class Normalizer_spec(unittest.TestCase):

  def setUp(self):
    self.n = Normalizer()

  def test_should_say(self):
    result = self.n.say()
    self.assertEqual(2,result)

unittest.main()
