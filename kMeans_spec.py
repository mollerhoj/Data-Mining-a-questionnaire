import unittest
import numpy as np
import pandas as pd
import random
import kMeans as k

class kMeans_spec(unittest.TestCase):

  def setUp(self):
    return 0

  def test_random_element(self):
    df = pd.DataFrame([[1,0,2],
                       [2,0,2.5],
                       [3,6,1.5]],None,['a1','a2','a3'])
    result = k.random_sample(df,2)
    #print(result)

  def test_create_clusters(self):
    df = pd.DataFrame([[1,0,2],
                       [2,0,2.5],
                       [3,6,1.5]],None,['a1','a2','a3'])
    result = k.create_clusters(df)
    #print(result)

  def test_distance_equal(self):
    e1 = pd.Series([2,1,2])
    e2 = pd.Series([2,1,2])
    result = k.distance(e1,e2)
    self.assertEqual(0,result)

  def test_distance_different(self):
    e1 = pd.Series([2,1])
    e2 = pd.Series([1,3])
    result = k.distance(e1,e2)
    self.assertEqual(np.sqrt(5),result)

  def test_closest(self):
    element = pd.Series([2,1,2],['a1','a2','a3'])

    centers = pd.DataFrame([[1,0,2],
                       [2,0,2.5],
                       [3,6,1.5]],None,['a1','a2','a3'])
    result = k.closest(element,centers)
    expected = pd.Series([2,0,2.5])
    assert ((expected == result).all())

  def test_find_center(self):
    df = pd.DataFrame([[1,0,2],
                            [2,0,2.5],
                            [3,6,1.5]],None,['a1','a2','a3'])
    result = df.mean(axis=0)
    #print(result)

  def test_find_centers(self):
    clusters = [pd.DataFrame([[2,0,2.5],
                              [3,6,1.5]],None,['a1','a2','a3']),
                pd.DataFrame([[1,0,2  ]],None,['a1','a2','a3'])]
    result = k.find_centers(clusters)
    #print(result)

  def test_assign_clusters(self):
    df = pd.DataFrame([[1,0,2],
                       [2,0,2.5],
                       [3,6,1.5]],None,['a1','a2','a3'])
    centers = pd.DataFrame([[1,0.5,2  ],
                            [2,0.5,2.5]],None,['a1','a2','a3'])
    clusters = [pd.DataFrame(),
                pd.DataFrame()]

    result = k.assign_clusters(df,clusters,centers)
    #print(result)

  def test_train(self):
    df = pd.DataFrame([[1,1,0],
                       [2,2,0],
                       [3,2,0],
                       [4,3,0],
                       [4,6,0], 
                       [5,6,0], 
                       [6,5,0], 
                       [7,4,0],
                       [7,3,0]],None,['a1','a2','a3'])
    result = k.train(df,2,5)
    #print(result)

unittest.main()
