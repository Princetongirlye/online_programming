# 1001 害死人不偿命的(3*n+1)猜想

def test_1001():
    n = int(input())
    j = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n + 1) / 2
        j = j + 1
    print(j)


# 写出这个数
def test_1002():
    n = input()
    py = ['ling','yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'shi']
    total = 0
    s = []
    for i in n:
        total += int(i)
    for i in str(total):
        s.append(py[int(i)])
    print(" ".join(s))

# 我要通过 --》 审题有误，需要重新考虑
def test_1003():
    n = int(input())
    flag = True
    for i in range(n):
        s = input()
        for j in s:
            if j not in ['P','A','T']:
                flag = False
                break


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

# 继续 3n+1的猜想
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

