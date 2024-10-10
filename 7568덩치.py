n = int(input())
ary = []

# 입력 처리
for i in range(n):
    weight, height = map(int, input().split())
    ary.append([weight, height])

# 등수 리스트 초기화
rank = [1] * n  # 기본 등수는 1 (자신보다 덩치가 큰 사람 0명일 때)

# 모든 사람을 비교하여 등수 계산
for i in range(n):
    for j in range(n):
        if i != j:  # 자기 자신과 비교하지 않음
            # j가 i보다 덩치가 크다면
            if ary[i][0] < ary[j][0] and ary[i][1] < ary[j][1]:
                rank[i] += 1  # 덩치가 더 큰 사람이 있을 때 등수 증가

# 결과 출력
print(*rank)
