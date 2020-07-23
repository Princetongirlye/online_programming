class Solution:
    # 正数反转
    # 还可以思考其他方法？
    def reverse(self, x: int) -> int:
        new_x = str(x)
        if new_x[0] == "-":
            new_x = str(x)[1:]
            if int(new_x[::-1]) > 2147483648:
                return 0
            else:
                new_x = "-" +  new_x[::-1]
                return int(new_x)
        else:
            if int(new_x[::-1]) > 2147483647:
                return 0
            else:
                return int(new_x[::-1])

    # 回文数

    def isPalindrome(self, x: int) -> int:
        return str(x)[::-1] == str(x)

    # 罗马数字转正数
    def romanToInt(self, s: str) -> int:
        pass
    # 加 1
    def plusOne(self, digits: list) -> list:
        return list(map(int,str(int("".join(map(str, digits))) + 1)))
    # 只出现了一次的数字
    # 线性复杂度
    def singleNumber(self, nums: list) -> int:
        for i in set(nums):
            if nums.count(i) == 1:
                return i
            else:
                pass
    # 有效的括号
    def isValid(self, s: str) -> bool:
        pass

    # 移除元素
    def removeElement(self, nums: list, val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)




s = Solution()
print(s.isValid("()[]{}"))





