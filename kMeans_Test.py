import pandas as pd
import numpy as np
import kMeans
import Preprocesser
import Normalizer

pd.set_option('display.width', 245)

def load():
  path = './data/survey2014.csv'
  return pd.read_csv(path, delimiter=';')

df = load()

#Remove student 19,45,49, because of fake answers.
df = df.drop([19])
df = df.drop([45])
df = df.drop([49])

#Fix age column, bad name bug:  ?age
df['age'] = df.iloc[:,0]
df = df.iloc[:,1:]

#Clean based on type
df.age = df.age.map(Preprocesser.clean_int)
df.prog_skill = df.prog_skill.map(Preprocesser.clean_float)
df.uni_yrs = df.uni_yrs.map(Preprocesser.clean_float)
df['rand1-10'] = df['rand1-10'].map(Preprocesser.clean_float)
df['rand0-1'] = df['rand0-1'].map(Preprocesser.clean_float)
df['rand0-1_pt2'] = df['rand0-1_pt2'].map(Preprocesser.clean_float)
df.Planets = df.Planets.map(Preprocesser.clean_int)
df.EngSkill = df.EngSkill.map(Preprocesser.clean_int)

#Normalize

df.age = Normalizer.z_score(df.age)
df.prog_skill = Normalizer.z_score(df.prog_skill)
df.uni_yrs = Normalizer.z_score(df.uni_yrs)
df['rand0-1'] = Normalizer.z_score(df['rand0-1'])
df['rand1-10'] = Normalizer.z_score(df['rand1-10'])
df['rand0-1_pt2'] = Normalizer.z_score(df['rand0-1_pt2'])
df.Planets = Normalizer.z_score(df.Planets)
df.EngSkill = Normalizer.z_score(df.EngSkill)

# Fill missing.
df =  df.fillna(df.mean())

#Only look at numeric columns.

df = df[['age', 'prog_skill', 'uni_yrs',  'EngSkill',  'rand1-10', 'rand0-1', 'rand0-1_pt2',  'Planets']]

#calculate clusters
result = kMeans.train(df,10,15)
print "The output reads: These are the ten centers found."
print result
