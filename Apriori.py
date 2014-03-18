import collections
import math

def remove_small(col,small):
    return {k:v for k,v in col.items() if v > small}

def to_list(col):
    return [k for k,v in col.items()]

def slim(col,small):
    return to_list(remove_small(col,small))

def join(col):
    k = []
    c = []
    kol = collections.defaultdict(int)

    for i,s1 in enumerate(col):
        for s2 in col[i:]:
            diff = s1.strip(s2)
            if len(diff)==1:
                q = "".join(sorted(diff+s2))
                kol[q] += 1

    x = len(col[0])
    kol2 = [k for k,v in kol.items() if v == x*(x+1)/2]
    return kol2

def containsAll(str, sub):
    return 0 not in [c in str for c in set(sub)]

def scan(data,check):
    col = collections.defaultdict(int)
    for c in check:
        for d in data:
            if containsAll(d,c):
                col[c] += 1
    return col

data = ["ACD", "BCE", "ABCE", "BE"]

c1 = scan(data,["A","B","C","D","E"])
print c1
l1 = slim(c1,1)
print l1
c2 = join(l1)
print c2
c22 = scan(data,c2)
print c22
l2 = slim(c22,1)
print l2
c3 = join(['BE', 'AC', 'CE', 'CB'])
print c3
cc3 = scan(data,c3)
print cc3

#print join(to_list(remove_small(scan(["ABC","BCD"],["A","B","C","D"]),1)))
