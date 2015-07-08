__author__ = 'freddie'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        temp = {}
        for index, value in enumerate(nums, 1):
            if target - value in temp:
                return [temp[target - value], index]

            temp[value] = index


def test1():
    solution = Solution()
    print(solution.twoSum([1, 5, 6, 100], 106))

def test2():
    solution = Solution()
    print(solution.twoSum([1, 12, 6, 100], 18))

if __name__ == "__main__":
    test1()
    test2()