class Solution:
    def canMeasureWater(self, x: int, y: int, z:int) ->bool:
        pass
    def isSubsequence(self, s: str, t: str) -> bool:
        pass
    #
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        a = Counter(s)
        index_ = -1
        for i, v in a.items():
            if v == 1:
                index_ = s.index(i)
                break
        return index_
    # 两数之和
    def twoSum(self, nums: list, target: int) ->list:
        pass

    # 消失的数字
    def missingNumber(self, nums: list) -> int:
        i = 0
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        nums.sort()
        for k in nums:
            if i != k:
                return i
            else:
                i += 1
        return i

    # 位1的个数
    def hammingWeight(self, n: int) ->int:
        return bin(n).replace("0b","").count("1")

    # 最后一个单词的长度
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
    # 二进制求和
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).replace("0b", "")




s = Solution()
print(s.missingNumber([3,1,0]))




