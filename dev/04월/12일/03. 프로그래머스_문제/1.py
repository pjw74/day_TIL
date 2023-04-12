# https://school.programmers.co.kr/learn/courses/30/lessons/161988

from sys import maxsize

INF = maxsize


def solution(sequence):
    answer = -INF
    size = len(sequence)
    s1 = s2 = 0
    s1_min = s2_min = 0
    pulse = 1

    for i in range(size):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)
        answer = max(answer, s1 - s1_min, s2 - s2_min)

        s1_min = min(s1_min, s1)
        s2_min = min(s2_min, s2)

        pulse *= -1
    return answer


sequence = [2, 3, -6, 1, 3, -1, 2, 4]
# result = 10

print(solution(sequence))
