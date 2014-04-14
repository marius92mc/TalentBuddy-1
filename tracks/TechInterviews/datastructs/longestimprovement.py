def longest_improvement(grades):
    count = 0
    max = 0
    for i in range(1,len(grades)):
        if grades[i] >= grades[i-1]:
            count +=1
        else:
            if count > max:
                max = count
            count = 0
    print max+1
