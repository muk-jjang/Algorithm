n = input()

if len(n) == 2:
    li = list(map(int,n))
    print(sum(li))
elif len(n) == 3:
    n = n.replace('10','')
    print(10+int(n))
else:
    print(20)