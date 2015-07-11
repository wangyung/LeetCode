__author__ = 'freddie'


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        inputLen = len(s)
        result = []

        if inputLen <= 1 or numRows == 1 or numRows >= inputLen:
            return s

        for i in xrange(numRows):
            j = i
            result += s[i]
            while j < inputLen:
                #calculate downward
                index = self.calculateNext(numRows - i)
                if index >= 0:
                    j += index
                    if j < inputLen:
                        result.append(s[j])

                #calculate upward
                index = self.calculateNext(i + 1)
                if index >= 0:
                    j += index
                    if j < inputLen:
                        result.append(s[j])

        return "".join(result)

    def calculateNext(self, row):
        firstIndex = row - 1
        secondIndex = row - 2
        if secondIndex >= 0:
            return firstIndex + secondIndex + 1
        else:
            return -1


def test1():
    solution = Solution()
    print solution.convert("abcdefghijklmno", 3)


def test2():
    solution = Solution()
    print solution.convert("abcdefghijklmno", 5)

def test3():
    solution = Solution()
    print solution.convert("", 1)

if __name__ == "__main__":
    test1()
    test2()
    test3()