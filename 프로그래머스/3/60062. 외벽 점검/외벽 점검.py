from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)  # 원형을 일자 형태로 변환

    answer = len(dist) + 1  # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    for start in range(length):  # 각 취약 지점에서 시작하는 경우를 고려
        for friends in permutations(dist):  # 친구들을 나열하는 모든 경우의 수에 대해 수행
            count = 1  # 투입할 친구 수
            position = weak[start] + friends[count - 1]  # 현재 친구가 점검할 수 있는 마지막 위치
            for index in range(start, start + length):  # 시작 지점부터 모든 취약 지점을 확인
                if position < weak[index]:  # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1  # 새로운 친구를 투입
                    if count > len(dist):  # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)  # 최소값 계산

    if answer > len(dist):
        return -1

    return answer