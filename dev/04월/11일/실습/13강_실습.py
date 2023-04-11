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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):  # in->post 구현
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []  # 후위표현

    for i in tokenList:
        if len(postfixList) == 0 and '(' != i:
            postfixList.append(i)
        else:
            if i not in prec and ')' != i:
                postfixList.append(i)
            else:
                if opStack.size() == 0:
                    opStack.push(i)
                else:
                    if ')' == i:
                        while True:
                            a = opStack.pop()
                            if '(' != a:
                                postfixList.append(a)
                            else:
                                break
                    else:
                        if prec[i] > prec[opStack.peek()] or '(' == i:
                            opStack.push(i)
                        else:
                            a = opStack.pop()
                            postfixList.append(a)
                            if opStack.size() != 0:
                                if prec[i] > prec[opStack.peek()] or '(' == i:
                                    opStack.push(i)
                                elif prec[i] == prec[opStack.peek()]:
                                    a = opStack.pop()
                                    postfixList.append(a)
                                    opStack.push(i)
                            else:
                                opStack.push(i)

    while opStack.size() != 0:
        b = opStack.pop()
        if '(' != b:
            postfixList.append(b)

    return postfixList


def postfixEval(tokenList):  # 구현
    opStack = ArrayStack()
    ans = 0
    test = []
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    for i in tokenList:
        if i in prec:
            opStack.push(i)
        else:
            test.append(i)
        if opStack.size() != 0:
            a = test.pop()
            b = test.pop()

            c = opStack.pop()
            #d = prec[c]
            if c == '*':
                ans = b*a
            elif c == '/':
                ans = b/a
            elif c == '+':
                ans = b+a
            elif c == '-':
                ans = b-a

            # print(type(d))
            #ans = b+int(c+1)

            test.append(ans)

    while opStack.size() != 0:
        c = opStack.pop()

    return ans


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


expr = "(2-1)*(4-3)"
print(solution(expr))
