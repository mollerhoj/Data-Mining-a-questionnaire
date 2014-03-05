#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import math 
f = open("data/survey.csv")
titles = []
first_line = True
people = []

class Preprocesser(object):
  def clean_float(self,text):
    return 2.34

def heading(line):
    titles = line.split(';')
    return titles

def parse(line,titles):
    values = line.split(';')
    person = {}
    for i,value in enumerate(values):
        person[titles[i]] = values[i]
    return person
        
for line in f:
    if first_line:
        titles = heading(line)
        first_line = False
    else:
        people.append(parse(line,titles))
f.close()

#Clean

def clean_float(v,*args):
    v = v.replace(',','.')
    v = v.replace('?','')
    v = v.replace("π",'3.14')
    try :
        v = float(v)
    except :
        return None

    if len(args) <= 1:
        return v
    else:
        return min(max(0,v),1)

def clean_int(v,*args):
    v = v.replace(',','.')
    v = v.replace('?','')
    try :
        return int(v)
    except :
        return None

def clean_string(v,*args):
    return v

def clean_bool(v,*args):
    v = v.upper()
    if re.match('YES|YEP',v):
        return True
    if re.match('NO',v):
        return False
    return None

types = {'randReal': [clean_float,0,1], 'yearsUniversity': [clean_float], 'randInt': [clean_int], 'ann': [clean_string], 'englishSpeaker': [clean_int], 'therbfortt': [clean_string], 'danishMountains': [clean_bool], 'solarSystem\n': [clean_int], 'programmingSkill': [clean_int], 'togelius': [clean_string], 'apriori': [clean_bool], 'favAnimal': [clean_string], 'canteenFood': [clean_string], 'favSQLServ': [clean_string], 'sqrt': [clean_float], 'yannakakis': [clean_string], 'fedUpWWinter': [clean_bool], 'sql': [clean_string], 'favProgLang': [clean_string], 'randReal2': [clean_float], 'svm': [clean_bool], 'age': [clean_int], 'favColour': [clean_string], 'favOS': [clean_string]}

#Clean:
for person in people:
    for k, v in person.iteritems():
        if len(types[k]) == 1:
            person[k] = types[k][0](v)
        if len(types[k]) == 3:
            person[k] = types[k][0](v,types[k][1],types[k][2])

#Calc functions
def sum(values):
    sum = 0
    for i in values:
        sum += i
    return sum

def mean(values):
    return sum(values) / len(values)

def variance(values):
    variance = 0
    for i in values:
        variance += (mean(values) - i) ** 2
    return variance/len(values)

def stddev(values):
    return math.sqrt(variance(values))

def correlation(values1,values2):
    cor = 0
    for v1, v2 in zip(values1,values2):
        cor += ((v1-mean(v1s))*(v2-mean(v2s)))
    return cor / (len(values1)*stddev(v1s)*stddev(v2s))

#Run:
v1s = []
v2s = []

for person in people:
    v1 = person['englishSpeaker']
    v2 = person['programmingSkill']
    if v1 and v2:
        v1s.append(v1)
        v2s.append(v2)

print("correlation: " + str(correlation(v1s,v2s)))
