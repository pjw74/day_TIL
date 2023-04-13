# 큰 수 만들기


def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            # 사전에 순서에 의한 대소관계 성립(1자리일 때만)
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer
