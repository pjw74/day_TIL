# 완주하지 못한 선수


def solution(participant, completion):
    answer = ""
    dic = {}  # dict 내부는 해시테이블
    for x in participant:  # O(n)
        dic[x] = dic.get(x, 0) + 1  # get() x가 존재하면 x 그렇지 않으면 0    시간복잡도:O(1)
    for x in completion:  # O(n)
        dic[x] -= 1
    dnf = [k for k, v in dic.items() if v > 0]  # O(n)
    answer = dnf[0]
    return answer
