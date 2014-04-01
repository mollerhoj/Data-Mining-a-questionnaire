import pandas as pd
import numpy as np
import kNN as kNN
import Preprocesser
import Normalizer

pd.set_option('display.width', 245)

#Is this person fed up with winter?

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
df.FavAnimal = df.FavAnimal.map(Preprocesser.clean_string)
df.MoreMtns = df.MoreMtns.map(Preprocesser.clean_bool)
df.winter = df.winter.map(Preprocesser.clean_bool)
df['rand1-10'] = df['rand1-10'].map(Preprocesser.clean_float)
df['rand0-1'] = df['rand0-1'].map(Preprocesser.clean_float)
df['rand0-1_pt2'] = df['rand0-1_pt2'].map(Preprocesser.clean_float)
df.neuralNetwork = df.neuralNetwork.map(Preprocesser.clean_bool)
df.vectorMachine = df.vectorMachine.map(Preprocesser.clean_bool)
df.sql = df.sql.map(Preprocesser.clean_bool)
df.APriori = df.APriori.map(Preprocesser.clean_bool)

#Drop useless columns
df = df.drop("canteenFood",1)
df = df.drop("SqRoot",1)
df = df.drop("therbforttglag",1)
df = df.drop("Georgios_middleName",1)
df = df.drop("JulianHome",1)

#Categorize
def os_standardize(v):
  v = v.upper()
  if v.find("WIN") != -1:
    return "windows"
  if v.find("LIN") != -1:
    return "linux"
  if v.find("OSX") != -1:
    return "mac"
  if v.find("MAC") != -1:
    return "mac"
  return np.nan

def sql_standardize(v):
  v = v.upper()
  if v.find("MS") != -1:
    return "ms"
  if v.find("MICRO") != -1:
    return "ms"
  if v.find("MY") != -1:
    return "mysql"
  if v.find("POST") != -1:
    return "postgres"
  return v

def color_standardize(v):
  v = v.upper()
  if v.find("BLUE") != -1:
    return "blue"
  if v.find("ORANGE") != -1:
    return "orange"
  if v.find("GREEN") != -1:
    return "green"
  if v.find("PURPLE") != -1:
    return "purple"
  if v.find("RED") != -1:
    return "red"
  if v.find("YELLOW") != -1:
    return "yellow"
  if v.find("BLACK") != -1:
    return "black"
  if v.find("PINK") != -1:
    return "pink"
  if v.find("BROWN") != -1:
    return "brown"
  return v

df.FavSQLServ = df.FavSQLServ.map(sql_standardize)
df.FavColor = df.FavColor.map(color_standardize)
df.OS = df.OS.map(os_standardize)



# Rearrange 'fedup' to be at the end
cols = df.columns.tolist();
cols = cols[0:7] + cols[8:] + cols[7:8]
df = df[cols]

# pick element
element = df.iloc[1]
# pick learning
learn = df.iloc[2:]

# classify
a = kNN.kNN()

k = 6
t1 = 50
t2 = 6

#shuffle

r = a.classify_count(df,t1,t2,k)
print "the output reads: By training with " + str(t1) + " tuples, " + str(r) + " * 100 % of " + str(t2) + " tuples were correctly classified."
print r
