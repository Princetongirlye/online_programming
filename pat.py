# 1004 成绩排名

def test_1004():
    n = int(input())
    max, min = 0, 100
    max_s = ""
    min_s = ""
    for i in range(n):
        s1, s2, score = input().split()
        if int(score) > max:
            max = int(score)
            max_s = s1 + " " + s2
        if int(score) < min:
            min = int(score)
            min_s = s1 + " " + s2

    print(max_s)
    print(min_s)


# 1005 关键数
def test_1005():
    n = int(input())
    nums = list(map(int, input().split()))
    x = set()
    for k in range(n):
        i = nums[k]
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = (3 * i + 1) / 2
            if i != 1 and i in nums:
                x.add(int(i))
    print(" ".join(map(str, sorted(set(nums) - x, reverse=True))))

test_1005()
