for i in range(int(input())):
    a = [0]*31
    for j in range(int(input())):
        w = input().split()
        if (w[0]) == '<=' :
            for k in range(15, int(w[1]) + 1):
                a[k] += 1
        else:
            for k in range(int(w[1]), 31):
                a[k] += 1
        if max(a) == j + 1:
            print(a.index(max(a)))
        else:
            print(-1)
    print("")

