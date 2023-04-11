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

    for c in S:
        if c == '(':
            opStack.push(c)
        elif c == ')':
            while not opStack.isEmpty():
                op = opStack.pop()
                if op == '(':
                    break
                else:
                    answer += op
        elif c.isalpha():
            answer += c
        else:
            if opStack.isEmpty():
                opStack.push(c)
            else:
                if prec[opStack.peek()] >= prec[c]:
                    while not opStack.isEmpty():
                        answer += opStack.pop()
                        if opStack.size() != 0:
                            if prec[opStack.peek()] < prec[c]:
                                opStack.push(c)
                                break
                        else:
                            opStack.push(c)
                            break
                    # opStack.push(c)
                else:
                    opStack.push(c)

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


S = "A+B*C/(D*E-F)+G"


#S = "(A+B)*(C+D)"
# result = "AB+CD+*"

#S = "A*B+C"
# result = "AB*C+"

#S = "A+B*C"
# result = "ABC*+"


print(solution(S))
