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

# (1+3) * (1+3)
# 13+13+*

    opStack = ArrayStack()
    postfixList = []  # 후위표현
    #numList = []
    for i in tokenList:
        if opStack.size == 0:
            opStack.push(i)
        else:
            if i not in prec:
                postfixList.append(i)
                # opStack.push(i)
            if i in prec and opStack.size != 0:
                if prec[opStack.peek()] < prec[i]:
                    a = opStack.pop()
                    opStack.push(i)
                    opStack.push(a)

            if ')' == i:
                a = opStack.pop()
                postfixList.append(a)

    while not opStack.isEmpty():

    return postfixList


def postfixEval(tokenList):  # 구현
    pass


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


expr = "(1+3) * (1+3)"
print(solution(expr))
