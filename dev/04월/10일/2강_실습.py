
def solution(L, x):
    answer = []
    idx = 0
    for i in range(len(L)):
        if x > L[-1]:
            L.append(x)
            answer = L
            break
        if L[i] > x:
            if i+1 == len(L):
                idx = i
                L.insert(idx, x)
                answer = L
                break
            if x < L[i+1]:
                idx = i
                L.insert(idx, x)
                answer = L
                break
            else:
                idx = i+1
                L.insert(idx, x)
                answer = L
                break
        else:
            continue

    return answer


L = [20, 37, 58, 72, 85, 91]
x = 75
print(solution(L, x))

# answer = [20, 37, 58, 65, 72, 91]
