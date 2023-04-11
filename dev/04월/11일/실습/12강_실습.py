class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

#result = "ABC*DE*F-/+G+"


def solution(S):
    opStack = ArrayStack()
    answer = ''

    for i in S:
        if len(answer) == 0 and '(' != i:
            answer += i
        else:
            if i not in prec and ')' != i:
                answer += i
            else:
                if opStack.size() == 0:
                    opStack.push(i)
                else:
                    if ')' == i:
                        while True:
                            a = opStack.pop()
                            if '(' != a:
                                answer += a
                            else:
                                break
                    else:
                        if prec[i] > prec[opStack.peek()] or '(' == i:
                            opStack.push(i)
                        else:
                            a = opStack.pop()
                            answer += a
                            if opStack.size() != 0:
                                if prec[i] > prec[opStack.peek()] or '(' == i:
                                    # while opStack.size() != 0:
                                    #     b = opStack.pop()
                                    #     if '(' != b:
                                    #         answer += b
                                    opStack.push(i)
                                elif prec[i] == prec[opStack.peek()]:
                                    a = opStack.pop()
                                    answer += a
                                    opStack.push(i)
                            else:
                                opStack.push(i)

    while opStack.size() != 0:
        b = opStack.pop()
        if '(' != b:
            answer += b

    return answer


S = "A+B*C/(D*E-F)+G"


#S = "(A+B)*(C+D)"
# result = "AB+CD+*"

#S = "A*B+C"
# result = "AB*C+"

#S = "A+B*C"
# result = "ABC*+"


print(solution(S))
