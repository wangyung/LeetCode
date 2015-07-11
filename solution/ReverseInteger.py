__author__ = 'freddie'

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        intString = str(x)

        result = 0
        if x != 0:
            if intString[0] == '-':
                result = int(intString[0] + "".join(list(reversed(intString[1:]))))
            else:
                result = int("".join(list(reversed(intString))))

        if not (-2147483647 <= result < 2147483647):
            result = 0
        return result


def test1():
    solution = Solution()
    print solution.reverse(-2147483648)


def test2():
    solution = Solution()
    print solution.reverse(1534236469)


if __name__ == "__main__":
    test1()
    test2()