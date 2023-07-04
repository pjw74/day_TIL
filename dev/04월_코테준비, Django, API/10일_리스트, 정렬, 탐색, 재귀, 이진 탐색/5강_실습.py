def solution(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)
    else:
        return solution(L, x, mid + 1, u)


L = [2, 3, 5, 6, 9, 11, 15]
# result = 0

x = 15
l = 0
u = 6

print(solution(L, x, l, u))
