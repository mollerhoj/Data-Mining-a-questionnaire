import unittest
import pandas as pd
import Normalizer

class Normalizer_spec(unittest.TestCase):

  def test_should_calcualte_mean(self):
    data = pd.Series([None,1.5,2.5,2.2,3.8])
    result = Normalizer.mean(data)
    self.assertEqual(2.5,result)

  def test_should_mean_absolute_deviation(self):
    data = pd.Series([None,None,None,1.5,2.5,2.2,3.8])
    result = Normalizer.mean_absolute_deviation(data)
    self.assertEqual(0.64999999999999991,result)

  def test_should_calcualte_std(self):
    data = pd.Series([None,1,5,2,5,0,7,0,8])
    result = Normalizer.standard_deviation(data)
    self.assertEqual(2.9580398915498081,result)

  def test_should_calcualte_z_score(self):
    data = pd.Series([None,1,-5,-9,1,0,7,0,8])
    result = Normalizer.z_score(data)
    expected = [ 0.1192167, -1.02526359, -1.78825045, 0.1192167, -0.07153002, 1.26369699, -0.07153002, 1.4544437 ]
    #self.assertEqual(expected,result)

unittest.main()
