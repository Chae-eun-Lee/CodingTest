#직원 수 n, 상사번호 boss
n = int(input())
boss = list(map(int, input().split()))

#직원 수 만큼의 행을 가진 이중리스트
children = [[] for _ in range(n)]

#각 직원에 할당된 (직속)부하직원 저장
for i in range(1, n):
    children[boss[i]].append(i)

#재귀함수 이용한 시간계산함수
def mintime(current):
    #부하직원 없을경우 0분 리턴
    if not children[current]:
        return 0

    # 현재 직원 기준 모든 부하직원들에 대해 뉴스를 듣는데 걸리는 시간을 계산
    time = []
    for child in children[current]:
        # 부하 직원이 뉴스를 듣는 데 걸리는 시간에 1분을 더함
        time.append(mintime(child) + 1)

    # 시간이 오래 걸리는 순으로 정렬 (시간이 많이 걸리는 사람에게 먼저 전화를 걸어야 최소화됨)
    time.sort(reverse=True)

    #각 (직속)부하직원이 뉴스를 듣는 시간 계산
    for i in range(len(time)):
        time[i] += i  #각 직속부하직원에게 전화를 거는 순서에 따른 추가 시간

    # 가장 오래 걸리는 시간이 해당 직원이 뉴스를 받는데 걸리는 최종 시간
    return max(time)


print(mintime(0))