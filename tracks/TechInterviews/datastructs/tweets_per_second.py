def tweets_per_second(tps, k):
    m = tps[0]
    life = 0
    print m
    for i in xrange(1,len(tps)):
        life = life+1
        if tps[i]>m:
            m = tps[i]
            life = 0
        if life>=k:
            m = tps[i-k+1]
            for j in xrange(i-k+2,i+1):
                if tps[j] > m:
                    m = tps[j]
                    life = i-j
        print m
