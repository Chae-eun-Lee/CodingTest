n = int(input())  # 회의의 수 입력
meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

# 회의를 순차적으로 확인하며 겹치지 않는 회의 선택
for s, e in meetings:
    if s >= last_end_time:
        count += 1
        last_end_time = e  # 마지막으로 선택한 회의의 끝나는 시간 갱신

print(count)
