def relative_sort(v):
    start = 0
    negs = []
    pos = []
    
    for i in xrange(len(v)):
        if(v[i] > 0):
            pos += [v[i]]
        else:
            negs += [v[i]]
            
    print " ".join(str(x) for x in (negs + pos))
