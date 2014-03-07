import unittest
import pandas as pd
from kNN import kNN


class kNN_spec(unittest.TestCase):
  
  def setUp(self):
    self.k = kNN()

  def test_should_count_distance(self):
    reference = pd.Series(['a','b'])
    element = pd.Series(['a','a','d'])
    distance = self.k.distance(element,reference)
    self.assertEqual(1,distance)

  def test_equal_elements_has_zero_distance(self):
    reference = pd.Series(['a','b'])
    element = pd.Series(['a','b','d'])
    distance = self.k.distance(element,reference)
    self.assertEqual(0,distance)

  def test_sort(self):
    reference = pd.Series(['a','b','c'])
    df = pd.DataFrame([['a','x','c'],
                       ['a','b','c'],
                       ['x','x','x']],None,['a1','a2','a3'])
    r = self.k.sort(df,reference)
    #print(r)

  def test_head(self):
    df = pd.DataFrame([['a','b','c'],
                       ['a','x','c'],
                       ['x','x','x']],None,['a1','a2','a3'])
    r = self.k.head(df,2)
    #print(r)

  def test_most(self):
    df = pd.DataFrame([['a','b','c'],
                       ['a','x','c'],
                       ['x','x','x']],None,['a1','a2','a3'])
    r = self.k.most(df,'a3')
    self.assertEqual(r,'c')

  def test_classify(self):
    element = ['a','b','c']
    df = pd.DataFrame([['a','x','x'],
                       ['a','b','c'],
                       ['x','x','x']],None,['a1','a2','a3'])
    r = self.k.classify(df,element,1)
    self.assertEqual('c',r)

  def test_read_stuff(self):
    path = 'data/agaricus-lepiotadata.csv'
    df = pd.read_csv(path)

    t1 = 100 #Training tuples
    t2 = 100 #Test tuples
    k = 10 #k

    r = self.k.classify_count(df,t1,t2,k)
    print(r)

unittest.main()
