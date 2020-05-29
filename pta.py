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
    py = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu", "shi"]
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
            if j not in ["P", "A", "T"]:
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


# 换个格式输出整数
def test_1006():
    n = input()
    len_n = len(n)
    new_s = ""

    if len_n == 2:
        new_s = "S" * int(n[0])
    elif len_n == 3:
        new_s = "B" * int(n[0])
        new_s += "S" * int(n[1])
    for i in range(int(n[-1])):
        new_s += str(i + 1)
    print(new_s)


# 素数对猜想 1007
def test_1007():
    pass


# 1009 说反话
def test_1009():
    s = input().split()
    print(" ".join(s[::-1]))


# 1010 一元多项式求导

# 1011 A+B>C
def test_1011():
    n = int(input())
    for i in range(1, n + 1):
        a, b, c = input().split()
        if int(a) + int(b) > int(c):
            print("Case #" + str(i) + ": true")
        else:
            print("Case #" + str(i) + ": false")


# 数字分类 1012

def test_1012():
    nums = list(map(int, input().split()))
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    all = []
    for n in nums[1:]:
        if n % 5 == 0 and n % 2 == 0:
            a1.append(n)
        elif n % 5 == 1:
            a2.append(n)
        elif n % 5 == 2:
            a3.append(n)
        elif n % 5 == 3:
            a4.append(n)
        elif n % 5 == 4:
            a5.append(n)
    if a1 == []:
        all.append("N")
    else:
        all.append(str(sum(a1)))
    if a2 == []:
        all.append("N")
    else:
        j = 0
        for i in range(len(a2)):
            j += a2[i] * (-1) ** i
        all.append(str(j))
    if a3 == []:
        all.append("N")
    else:
        all.append(str(len(a3)))
    if a4 == []:
        all.append("N")
    else:
        all.append(str(round(sum(a4) / len(a4), 1)))
    if a5 == []:
        all.append("N")
    else:
        all.append(str(max(a5)))
    print(" ".join(all))


# 1013 数素数 -- 测试点第四个运行超时
def test_1013():
    import math
    m, n = input().split()
    x = []
    flag = True
    k = 0
    i = 2
    while flag:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            x.append(i)
        if len(x) == int(n):
            flag = False
            break
        i += 1
    if int(m) == int(n):
        print(x[int(m) - 1])
    else:
        j = 0
        print(x)
        for i in x[int(m) - 1:]:
            j += 1
            if j % 10 == 0:
                print(i)
            elif j != int(n) - int(m) + 1:
                print(i, end=" ")
            else:
                print(i)


# 1014
def test_1014():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    DAY = {"A": "MON", "B": "TUE", "C": "WED", "D": "THU", "E": "FRI", "F": "SAT", "G": "SUN"}
    HH = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
          "M",
          "N"]
    s = []
    for count in range(min(len(s1), len(s2))):
        if s1[count] == s2[count]:
            if s != [] and s1[count] in HH:
                s.append(str(HH.index(s1[count])).rjust(2, "0"))
                break
            elif s1[count] in DAY.keys():
                s.append(DAY.get(s1[count]))
                continue

    for count in range(min(len(s3), len(s4))):
        if s3[count] == s4[count] and s3[count].isalpha():
            s.append(str(count).rjust(2, "0"))
            break
    print("%s %s:%s" % (s[0], s[1], s[2]))


# 1015  德才论

def test_1015():
    pass


def test_1021():
    n = input()
    from collections import Counter
    r = sorted(Counter(n).items(), key=lambda x: x[0])
    for i in r:
        print(str(i[0]) + ":" + str(i[1]))


def test_1022():
    a, b, n = input().split()
    c = int(a) + int(b)
    n = int(n)

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    res = []

    while True:
        s = c // n
        y = c % n
        res.append(y)
        if s == 0:
            break
        c = s
    for i in res[::-1]:
        print(str(digits[i]), end="")


# test_1023 最小的数
def test_1023():
    num = list(map(int, input().split()))
    ans = []
    for d, n in enumerate(num[1:], 1):
        if n != 0:
            ans.append(str(d))
            num[d] -= 1
            break
    print(ans)
    print(num)
    for d, n in enumerate(num):
        ans.append(n * str(d))
    print(ans)


def test_1024():
    a, b = input().split("E")
    before = a[0]
    after = b[0]
    a = a[1:]
    b = int(b[1:])
    res = ""
    if after == "-":
        n1, n2 = a.split(".")
        res = '0' + "." + '0' * (b - 1) + n1 + n2
    else:
        n1, n2 = a.split(".")
        if b < len(n2):
            res = n1 + n2[:b] + "." + n2[b:]
        else:
            res = n1 + n2 + "0" * (b - len(n2))
    if before == "-":
        print("-" + res)
    else:
        print(res)


def test_1027():
    n, sign = input().split()
    n = int(n)
    total = 3
    if n < 7:
        print(n)
    else:
        count = 1
        j = 1
        while True:
            if n > 1 + total * 2:
                n = n - (1 + total * 2)
                count += 1
                for i in range(count):
                    total += i * 2
            else:
                if count == 2:
                    count -= 1
                break
            count = j
        for i in range(count, -1, -1):
            print(" " * (abs(count - i)) + sign * (3 + 2 * (i - 1)))
        for i in range(count):
            print(" " * (count - 1) + sign * (3 + 2 * i))
        print(n)


# 测试点5-运行超时
def test_1028():
    import datetime

    n = int(input())
    largest = datetime.date(1814, 9, 6)
    youngest = datetime.date(2014, 9, 6)
    max_year = largest
    min_year = youngest
    l = ""
    y = ""
    num = 0
    for i in range(n):
        name, s = input().split()
        year, month, day = s.split("/")
        year = int(year)
        month = int(month)
        day = int(day)
        t = datetime.date(year, month, day)
        if year < 1814 or year > 2014:
            pass
        elif (t - max_year).days < 0 or (t - min_year).days > 0:
            pass
        else:
            num += 1
            if (t - largest).days >= 0:
                largest = datetime.date(year, month, day)
                y = name
            if (t - youngest).days <= 0:
                youngest = datetime.date(year, month, day)
                l = name
    if num == 0:
        print(0)
    else:
        print(num, l, y)


def test_1029():
    real = input()
    s = input()
    bad = []
    for i in real:
        if i.upper() not in s.upper() and i.upper() not in bad:
            bad.append(i.upper())

    print("".join(bad))


def test_1030():
    n, p = input().split()
    nums = sorted(list(map(int, input().split())))
    p = int(p)
    count = 0
    for i in range(len(nums)):
        for j in range(i + count, len(nums)):
            if p * nums[i] < nums[j]:
                break
            count += 1
    print(count)


def test_1031():
    n = int(input())
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    all_passed = 0
    for i in range(n):
        total = 0
        code = input()
        if code[:17].isdigit() is False:
            print(code)
        else:
            for d, j in enumerate(code[:17]):
                total += weight[d] * int(j)
            if code[17] != m[total % 11]:
                print(code)
            else:
                all_passed += 1
    if all_passed == n:
        print("All passed")


def test_1041():
    n = int(input())
    all = []
    for i in range(n):
        all.append(input())
    m = int(input())
    to_be = input().split()
    dic = {}
    for i in all:
        tmp = i.split()
        dic[tmp[1]] = " ".join([tmp[0], tmp[2]])
    for j in to_be:
        print(dic.get(j))


def test_1042():
    s = input().lower()
    dic = {}
    for i in s:
        if i.isalpha():
            dic[i] = dic.setdefault(i, 0) + 1
    new1 = sorted(dic.items(), key=lambda x: (-x[1],x[0]))
    print(new1[0][0],new1[0][1])


test_1042()
