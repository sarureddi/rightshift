aa2,b2 = map(int,input().split())
b2 = b2%aa2
l12 = list(map(int,input().split()))
l22 = l12[-b2:] + l12[:-b2]
print(*l22)
