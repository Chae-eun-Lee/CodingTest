def solution(nums):
    array = [[0 for i in range(len(nums))] for j in range(2)]
    count = 0

    for n in nums:
        a = 0
        for k in array[0]:
            if n == k:
                result = True
                break
            else:
                result = False
            a += 1

        if result:
            array[1][a] += 1
        else:
            array[0][count] = n
            array[1][count] += 1
        count += 1
        print(array)
    answer = 0
    for m in array[0]:
        if m > 0:
            answer += 1
    if answer > (len(nums)/2):
        answer = int((len(nums)/2))
        print(answer)
    return answer

solution([3,3,3,2,2,2])

print(set([3,3,3,2,2,2]))