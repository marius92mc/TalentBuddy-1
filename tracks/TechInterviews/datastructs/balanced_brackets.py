def balanced_brackets(s):
    open = 0
    for i in range(len(s)):
        if s[i] == "(":
            open+=1
        elif s[i] == ")":
            open-=1
        if open < 0:
            break
    if open == 0:
        print "Balanced"
    else:
        print "Unbalanced"
