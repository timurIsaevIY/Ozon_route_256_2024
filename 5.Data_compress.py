for i in range(int(input())):
    l = int(input())
    s = [int(x) for x in input().split()]
    s1 = []
    neg = 0
    pos = 0
    for k in range (len(s)):
        if k + 1 < len(s) and s[k] - 1 == s[k + 1]:
            if pos != 0:
                s1.append(s[k - pos])
                s1.append(pos)
                pos = 0
            else:
                neg -= 1
        elif k + 1 < len(s) and s[k] + 1 == s[k + 1]:
            if neg != 0:
                s1.append(s[k + neg])
                s1.append(neg)
                neg = 0
            else:
                pos += 1
        elif (neg != 0 or pos != 0):
            if pos != 0:
                s1.append(s[k - pos])
                s1.append(pos)
                pos = 0
            elif neg != 0:
                s1.append(s[k + neg])
                s1.append(neg)
                neg = 0
        else:
            s1.append(s[k])
            s1.append(0)
    print(len(s1))
    print(" ".join([str(x) for x  in s1]))





