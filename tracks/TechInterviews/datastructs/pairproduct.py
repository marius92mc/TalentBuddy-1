def max_prod(v):
    max = 0
    for i in range(1,len(v)):
        temp = v[i-1] * v[i]
        if temp > max and temp % 3 == 0:
            max = temp
    print max
