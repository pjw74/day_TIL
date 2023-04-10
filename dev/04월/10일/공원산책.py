# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3


def solution(park, routes):
    answer = []
    row = len(park[0])
    col = len(park)
    graph = [[0] * row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            if "S" == park[i][j]:
                graph[i][j] = 1  # 1: Start
                c, r = i, j
            if "X" == park[i][j]:
                graph[i][j] = 2  # 2: 장애물
    # print(graph)

    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]

    for i in range(len(routes)):
        if "E" == routes[i][0]:
            for cnt in range(int(routes[i][2])):
                nr = r + dr[3]
                if 0 > nr or nr >= row:
                    r -= 1*cnt
                    break
                if graph[c][nr] == 2:
                    r -= 1*cnt
                    break
                else:
                    r += 1
        if "W" == routes[i][0]:
            for cnt in range(int(routes[i][2])):
                nr = r + dr[2]
                if 0 > nr or nr >= row:
                    r += 1*cnt
                    break
                if graph[c][nr] == 2:
                    r += 1*cnt
                    break
                else:
                    r -= 1
        if "N" == routes[i][0]:
            for cnt in range(int(routes[i][2])):
                nc = c + dc[0]
                if 0 > nc or nc >= col:
                    c += 1*cnt
                    break
                if graph[nc][r] == 2:
                    c += 1*cnt
                    break
                else:
                    c -= 1
        if "S" == routes[i][0]:
            for cnt in range(int(routes[i][2])):
                nc = c + dc[1]
                if 0 > nc or nc >= col:
                    c -= 1*cnt
                    break
                if graph[nc][r] == 2:
                    c -= 1*cnt
                    break
                else:
                    c += 1
    answer = [c, r]

    return answer


park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]
# result = [0,0]
print(solution(park, routes))
