def compute_sqrt(n):
    seed = 2
    while seed*seed < n:
        seed+=1
    print seed - 1
