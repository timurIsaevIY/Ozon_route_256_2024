for i in range(int(input())):
    k = [int(x) for x in input().split()]
    if k[1] == 2:
        if  k[0] == 29 and (k[2] % 4 == 0 and k[2] % 100 != 0 or k[2] % 400 == 0) or k[0] <= 28:
            print("YES")
        else:
            print("NO")
    elif k[1] in {1, 3, 5, 7, 8, 10, 12} and k[0] <= 31 or k[1] in {2, 4, 6, 9, 11} and k[0] <= 30:
        print("YES")
    else:
        print("NO")

