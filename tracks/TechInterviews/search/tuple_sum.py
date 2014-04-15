from itertools import combinations
def tuple_sum(a, s):
    combos = combinations(a,4)
    for combo in combos:
         if sum(combo) == s:
                print " ".join(str(a.index(x)) for x in combo)
                return
