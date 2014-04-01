import collections
import math

class Apriori(object):

  def remove_small(self,col,small):
      return {k:v for k,v in col.items() if v > small}

  def to_list(self,col):
      return [k for k,v in col.items()]

  def slim(self,col,small):
      return self.to_list(self.remove_small(col,small))

  def join(self,col):
      k = []
      c = []
      kol = collections.defaultdict(int)

      for i,s1 in enumerate(col):
          for s2 in col[i:]:
              s3 = s1.union(s2)
              if len(s3)==len(s1)+1:
                  kol[s3] += 1

      x = len(col[0])
      kol2 = [k for k,v in kol.items() if v == x*(x+1)/2]
      return kol2

  def scan(self,data,check):
      col = collections.defaultdict(int)
      for c in check:
          for d in data:
            if c.issubset(d):
              col[c] += 1
      return col

  def split(self,data):
    res = set([])
    for i in data:
      for j in i:
        res.add(frozenset([j]))
    return frozenset(res)

  def find(self,data,minimum):
    a = self.split(data)
    while True:
      b = self.scan(data,a)
      c = self.slim(b,minimum)
      a = self.join(c)
      if len(a) == 0:
        return c
    return 0

