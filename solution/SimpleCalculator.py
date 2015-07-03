__author__ = 'freddie'

class Solution:
    # @param {string} s
    # @return {integer}
    validToken = "+-()"
    num = "0123456789"

    def __init__(self):
        self.numStack = []
        self.leftParenthesisCount = 0

    def calculate(self, s):
        result = 0
        for operand in s:
            if operand == " ":
                continue
            if operand in self.validToken:
                if operand == "(":
                    self.leftParenthesisCount += 1
                elif operand == ")":
                    self.numStack.append(self.doOperation())
                    continue
                self.numStack.append(operand)
            else:
                if len(self.numStack) > 0 and type(self.numStack[-1]) == int:
                    previousValue = self.numStack.pop()
                    self.numStack.append(previousValue * 10 + int(operand))
                else:
                    self.numStack.append(int(operand))

        if len(self.numStack) > 0:
            result = self.doOperation()

        return result

    def doOperation(self):
        result = 0
        operationStack = []
        item = self.numStack.pop()
        while item != "(":
            operationStack.append(item)
            try:
                item = self.numStack.pop()
            except:
                break

        if self.leftParenthesisCount > 1:
            self.leftParenthesisCount -= 1

        while len(operationStack) > 0:
            item = operationStack.pop()
            if type(item) == int:
                result = item
            elif item == "+":
                rval = operationStack.pop()
                result = result + rval

            elif item == "-":
                rval = operationStack.pop()
                result = result - rval

        return result


def test1():
    solution = Solution()
    result = solution.calculate("(1+(40+5+2)-3)+(6+8)")
    print result

def test2():
    solution = Solution()
    result = solution.calculate(" 2-1 + 2 ")
    print result

if __name__ == "__main__":
    test1()
    test2()
