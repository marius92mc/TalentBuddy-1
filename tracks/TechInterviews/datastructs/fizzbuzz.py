def fizzbuzz(n):
    for i in range(1,n+1):
        s = str()
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if not s:
            print i
        else:
            print s
