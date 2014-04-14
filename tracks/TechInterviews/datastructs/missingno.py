def find_missing_number(v):
    m = set(range(1,len(v)+2))
    print "".join(str(x) for x in set(v) ^ m)
