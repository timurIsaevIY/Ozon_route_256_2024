e = []
for i in range(int(input())):
    e.append(input())
for i in range(len(e)):
    s = [[]]
    w = e[i]
    cur_str = 0
    cur_slid = 0
    for j in range(len(w)):
        if w[j].islower() or w[j] in "0123456789":
            s[cur_str].insert(cur_slid, w[j])
            cur_slid += 1
        elif len(s) != 0:
            match w[j]:
                case 'L':
                    if cur_slid > 0:
                        cur_slid -= 1
                case 'R':
                    if cur_slid < len(s[cur_str]):
                        cur_slid += 1
                case 'U':
                    if cur_str > 0:
                        if cur_slid <= len(s[cur_str - 1]):
                            cur_str -= 1
                        else:
                            cur_str -= 1
                            cur_slid = len(s[cur_str])
                case 'D':
                    if cur_str < len(s) - 1:
                        if cur_slid <= len(s[cur_str + 1]):
                            cur_str += 1
                        else:
                            cur_str += 1
                            cur_slid = len(s[cur_str])
                case 'B':
                    cur_slid = 0
                case 'E':
                    cur_slid = len(s[cur_str])
                case 'N':
                    if cur_str == len(s) - 1 and cur_slid == len(s[cur_str]):
                        s.append([])
                        cur_str += 1
                        cur_slid = 0
                    elif cur_slid == len(s[cur_str]):
                        s.insert(cur_str + 1, [])
                        cur_str += 1
                        cur_slid = 0
                    elif cur_str != len(s) - 1:
                        q = s[cur_str][cur_slid : ]
                        del(s[cur_str][cur_slid : ])
                        s.insert(cur_str + 1, q)
                        cur_slid = 0
                        cur_str += 1
                    else:
                        q = s[cur_str][cur_slid:]
                        del (s[cur_str][cur_slid :])
                        s.append(q)
                        cur_slid = 0
                        cur_str += 1
    for p in range(len(s)):
        print(''.join(s[p]))
    print('-')






