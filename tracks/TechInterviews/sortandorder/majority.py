from collections import Counter

def majority(v):
    t = Counter(v).most_common(1)[0]
    if t[1] > len(v)/2:
        print t[0]
    else:
        print "None"
