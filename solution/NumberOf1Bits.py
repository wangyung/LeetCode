__author__ = 'freddie'


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            count += 1
            n = n & (n- 1)
        return count


def test1():
    solution = Solution()
    print solution.hammingWeight(65535010)

if __name__ == "__main__":
    test1()
