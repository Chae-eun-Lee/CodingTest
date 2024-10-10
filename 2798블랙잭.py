
n, m = map(int, input().split())

while(3 <= n <= 100 & 10 <= m <= 300000):
    n, m = map(int, input().split())

cards = list(map(int, input().split()))

def compare(a, b) :
    if(a == m) :
        output = a
    elif(a < m) :
        output = max(a, b)
    elif(a > m) :
        output = min(a, b)
    return output


result = 0
for i in range(0, n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            sum = cards[i] + cards[j] + cards[k]
            result = compare(sum, result)

print(result)

