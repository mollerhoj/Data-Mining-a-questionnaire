#kMeans
import random
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

import matplotlib as plt

def random_sample(df,k):
  rindex =  np.array(random.sample(xrange(len(df)), k))
  return df.ix[rindex]

def distance(e1,e2):
  return np.linalg.norm(e1-e2)

def create_clusters(centers):
    clusters = []
    for i in range(len(centers)):
      clusters.append(pd.DataFrame())
    return clusters

def closest(element,centers):
  smallest = None
  for i in range(len(centers)):
    center = centers.iloc[i]
    if smallest == None or distance(element,center) < smallest:
      smallest = distance(element,center)
      closest_center = center
  return closest_center

def assign_clusters(df,clusters,centers):
  for i in range(len(df)):
    element = df.iloc[i]
    center = closest(element,centers)

    # Yes, this is ugly, but damn pandas is hard to grok.
    for c in range(len(centers)):
      if (centers.iloc[c] == center).all():
        clusters[c] = clusters[c].append(element)

  return clusters

def find_center(df):
  return df.mean(axis=0)

def find_centers(clusters):
  centers = pd.DataFrame()
  for cluster in clusters:
    center = find_center(cluster)
    centers = centers.append(center,ignore_index=True)
  return centers

def train(df,k,loop_n):
  init_centers = random_sample(df,k)
  return train_loop(df,k,init_centers,loop_n)

def train_loop(df,k,centers,loop_n):
  step = 1
  for i in range(loop_n):
    clusters = create_clusters(centers)

    clusters = assign_clusters(df,clusters,centers)
    old_centers = centers
    centers = find_centers(clusters)

    #return if we have not moved
    if frames_equal(centers,old_centers):
      return centers

    step += 1
  return centers

def classify(element):
  return 2

def frames_equal(f1,f2):
    try: 
      assert_frame_equal(f1, f2)
    except:
      return False
    return True
