#Normalize
import pandas as pd
import numpy as np
import matplotlib as plt

# z_score using standard deviation.
# Could also have used mean absolute deviation, for another kind of measure.
def z_score(series):
  mu = mean(series)
  sigma = standard_deviation(series)
  return (np.array(series)-mu)/sigma

def mean_absolute_deviation(series):
  error("DOES NOT WORK")
  mu = mean(series)
  diff = np.absolute(np.array(series)-mu)
  return mean(diff)

def mean(series):
  return np.mean(series)

def standard_deviation(series):
  return np.std(series)
