def max_n_activities(s, f):
    picked = 0
    print(s[picked], " ", f[picked])

    for i in range(len(f)):
        if s[i] >= f[picked]:
            print(s[i]," ",f[i])
            picked = i


s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
max_n_activities(s , f)
