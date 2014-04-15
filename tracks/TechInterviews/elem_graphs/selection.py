def select_numbers(v, k):
    v.sort()
    print " ".join(str(x) for x in v[:-(len(v) -k)])
