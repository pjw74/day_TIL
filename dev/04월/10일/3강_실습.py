def solution(L, x):
    answer = []
    idx = 0
    if x not in L:
        answer.append(-1)
    else:
        while x in L[idx:]:
            answer.append(L[idx:].index(x) + idx)
            idx = L[idx:].index(x) + idx + 1

            # if x in L[idx:]:
            #     break

    return answer


L = [64, 72, 83, 72, 54]
x = 72
print(solution(L, x))
# result = [1, 3]
