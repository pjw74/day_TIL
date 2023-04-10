def solution(L, x):
    answer = 0
    if len(L) == 0:
        answer = -1
        return answer
    lo, hi = 0, len(L)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        if L[mid] == x:
            answer = mid
            break
        if L[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1

    if answer == 0:
        answer = -1
    return answer


# L = [2, 3, 5, 6, 9, 11, 15]
# x = 3
L = [1, 2, 3]
x = 3
print(solution(L, x))

# L = [2, 5, 7, 9, 11]
# x = 4
# print(solution(L, x))
