class kNN(object):

  def distance(self,element,reference):
    dist = 0
    for i in range(0,len(reference)):
      if element[i] != reference[i]:
        dist += 1
    return dist

  def sort(self,df,reference):
    s = df.apply(lambda row: self.distance(row,reference),axis=1)
    k = df.set_index(s).sort()
    return k

  def head(self,df,n):
    return df[0:n]

  def most(self,df,column):
    return df[column].value_counts().index[0]

  def classify(self,df,element, k):
    df = self.sort(df,element)
    df = self.head(df,k)
    return self.most(df,df.columns[-1])

  # UGLY:
  def classify_count(self,df,t1,t2,k):
    training = df[0:t1]
    test = df[t1:min(3000,t1+t2)]

    correct = 0
    wrong = 0
    for i in range(len(test)):
      element = df.iloc[i]
      r = self.classify(training,element,k)
      if r == element[-1]:
        correct += 1
      else:
        wrong += 1
    return float(correct)/float(wrong+correct)


