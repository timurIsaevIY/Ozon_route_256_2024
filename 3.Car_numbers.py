import re
pattern = re.compile(r'[A-Z]{1}\d{1,2}[A-Z]{2}')
for i in range(int(input())):
    st = input()
    ans = ""
    slide = 0
    while slide < len(st):
        if re.match(pattern, st[slide:]):
            result = re.match(pattern, st[slide:])
            ans += st[slide: slide + result.end()] + ' '
            slide += result.end()


        else:
            print('-')
            ans = 0
            break
    if ans != 0:
        print(ans[: -1])