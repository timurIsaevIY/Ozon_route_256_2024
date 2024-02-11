for i in range (int(input())):
    k = [0] * (int(input()) + 1)
    st = input().split(',')
    for j in range(len(st)):
        if st[j].find('-') != -1:
            q = st[j].split('-')
            for g in range(int(q[0]), int(q[1]) + 1):
                k[g] += 1
        else:
            k[int(st[j])] += 1
    ans = ''
    p = 1
    while p < len(k):
        while p < len(k) and k[p] != 0:
            p += 1
        t = p
        while p < len(k) - 1 and k[p + 1] == 0:
            p += 1
        if t != p:
            ans += str(t) + '-' + str(p) + ','
            p += 1
        elif p < len(k):
            ans += str(p) + ','
            p += 1
    print(ans[:-1])




