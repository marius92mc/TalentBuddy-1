from heapq import nlargest
def nth_number(v, n):
    print v[nlargest(n, range(len(v)), key=lambda i: v[i])[n-1]]
