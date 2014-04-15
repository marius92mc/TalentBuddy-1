def test(i , li, e):
    count = 0
    for j in li[i::]:
        while e >= j:
            e-=j
            count+=1
    if e == 0:
        return True, count
    else:
        return False, count
    
def minimum_coins(v, e):
    t = 0
    check, c = test(t, v[::-1] ,e)
    while check == False:
        t +=1
        check, c = test(t,v[::-1],e)
    print c
