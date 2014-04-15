#got lazy
def two_numbers_sum(v, sum):
    for i in xrange(len(v)):
        for j in xrange(len(v)):
            if j != i:
                if (v[j] + v[i]) == sum:
                    print 1
                    return
    print 0
