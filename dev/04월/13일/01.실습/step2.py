# 체육복

# 방법 1
"""
def solution(n, lost, reserve):
    u = [1] * (n + 2)
    for i in reserve:  # O(n)
        u[i] += 1
    for i in lost:  # O(n)
        u[i] -= 1
    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1 : i + 1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
            u[i : i + 2] = [1, 1]
    return len([x for x in u[1:-1] if x > 0])  # O(n)

    # 전체 복잡도 O(n)
"""

# 방법 2


def solution(n, lost, reserve):
    # set()은 해시 테이블로 이루어져 키 접근 O(1), dict 비슷하지만 value가 없음
    s = set(lost) & set(reserve)  # O(k)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):  # O(klogk)
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
