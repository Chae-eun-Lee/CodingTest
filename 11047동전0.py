n, k = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(int(input()))
result = 0
ary.sort(reverse=True)
for a in ary:
    if k >= a and k != 0:
        c = k//a
        result += c
        k -= a*c
    elif k <= 0:
        break
print(result)