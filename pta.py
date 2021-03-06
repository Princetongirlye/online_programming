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
    m, n = input().split()
    m = int(m)
    n = int(n)
    x = []
    flag = True
    k = 0
    i = 2
    while flag:
        if i !=2 and i % 2 == 0:
            pass
        else:
            for j in range(3, int(i**0.5) + 1,  2):
                if i % j == 0:
                    break
            else:
                x.append(i)
        if len(x) == n:
            flag = False
        i += 1

    if m == n:
        print(x[m - 1])
    else:
        j = 0
        print(x)
        for i in x[m - 1:]:
            j += 1
            if j % 10 == 0:
                print(i)
            elif j != n - m + 1:
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


# 德才论

def test_1015():
    n, l, h = input().split()
    n = int(n)
    l = int(l)
    h = int(h)
    for i in range(n):
        pass


# 1016 部分A+B
def test_1016():
    a, b, c, d = input().split()
    t1, t2 = 0, 0
    if b in a:
        t1 = int(a.count(b) * b)
    if d in c:
        t2 = int(c.count(d) * d)
    print(t1 + t2)


# A 除以 B
def test_1017():
    a, b = input().split()

    print(int(a) // int(b), int(a) % int(b))


# 1018 锤子剪刀布 -- 测试点5运行超时
import time


def test_1018():
    # C 代表“锤子”、J 代表“剪刀”、B 代表“布”
    sign = {"C C": 0, "C J": 1, "C B": -1, "B B": 0, "B C": 1, "B J": -1, "J J": 0, "J B": 1, "J C": -1}
    n = int(input())
    res1 = [0, 0, 0, {}]
    res2 = [0, 0, 0, {}]
    for i in range(n):
        a = input()
        value = sign.get(a)
        if value == 0:
            res1[1] += 1
            res2[1] += 1
        elif value == 1:
            res1[0] += 1
            key = a.split()[0]
            res1[3][key] = res1[3].setdefault(key, 0) + 1
            res2[2] += 1
        elif value == -1:
            res2[0] += 1
            key = a.split()[1]
            res2[3][key] = res2[3].setdefault(key, 0) + 1
            res1[2] += 1

    print(" ".join(map(str, res1[:3])))
    print(" ".join(map(str, res2[:3])))
    if res1[3] == {} and res2[3] == {}:
        print("B", "B")
    elif res1[3] != {} and res2[3] == {}:
        res1_a = sorted(res1[3].items(), key=lambda x: (-x[1], x[0]))
        print(res1_a[0][0], "B")
    elif res2[3] != {} and res1[3] == {}:
        res1_b = sorted(res2[3].items(), key=lambda x: (-x[1], x[0]))
        print("B", res1_b[0][0])
    else:
        res1_a = sorted(res1[3].items(), key=lambda x: (-x[1], x[0]))
        res1_b = sorted(res2[3].items(), key=lambda x: (-x[1], x[0]))
        print(res1_a[0][0], res1_b[0][0])


def test_1019():
    n = input().rjust(4, '0')
    j = 0
    if n == n[::-1]:
        print("%s - %s = %s" % (n, n, "0000"))
    else:
        while True:
            a = "".join(sorted(list(n), reverse=True)).rjust(4, '0')
            b = "".join(sorted(list(n))).rjust(4, '0')
            c = str(int(a) - int(b)).rjust(4, '0')
            if n == c and j == 0:
                print("%s - %s = %s" % (a, b, c))
                break
            elif n == c and j != 0:
                break
            elif a == b:
                print("%s - %s = %s" % (a, b, "0000"))
                break
            else:
                print("%s - %s = %s" % (a, b, c))
                n = c
                j += 1


def test_1026():
    c1, c2 = input().split()
    c = (int(c2) - int(c1)) / 100
    res = []
    hh = int(c // 3600)
    c = c - hh * 3600
    mm = int(c // 60)
    ss = round(c - mm * 60)
    print(str(hh).rjust(2, "0") + ":" + str(mm).rjust(2, "0") + ":" + str(ss).rjust(2, "0"))


def test_1027():
    n, b = input().split()
    n = int(n)
    total = 3
    y = 0
    if n < 7:
        print(n)

    else:
        count = 0
        while True:
            if n > 1 + total * 2:
                n = n - (1 + total * 2)
                count += 1
                for i in range(count):
                    total += 2 * i
                    print("total=", total)
            else:
                print("n and total=", n, total)
                break

        print(n)
        print(count)
        if count == 0:
            count += 1
        for i in range(count, -1, -1):
            print(" " * (abs(i - count)) + "*" * (3 + 2 * (i - 1)))
        for i in range(0, count):
            print(" " * (count - i - 1) + "*" * (3 + 2 * i))


# 1032  运行超时
def test_1032():
    n = int(input())
    all = {}
    for i in range(n):
        a, b = input().split()
        b = int(b)
        all[a] = all.setdefault(a, 0) + b
    max_ = sorted(all.items(), key=lambda x:x[1], reverse=True)[0]
    print(max_[0], max_[1])
    #print(all.index(max_) + 1, max_)

    # for i in range(n):
    #     code, score = map(int, input().split())
    #     dic[code] = dic.setdefault(code,0 ) +  score


# 1033 旧键盘打字
def test_1033():
    bad = input()
    real = input()
    res = ""
    for i in real:
        if '+' not in bad and i.lower() in bad.lower():
            pass
        elif '+' in bad:
            if i.isupper():
                pass
            elif i.lower() in bad.lower():
                pass
            else:
                res += i
        else:
            res += i
    print(res)


# 有理数四则运算 1034

# 1036
def test_1036():
    import math
    n, sign = input().split()
    n = int(n)
    rows = math.ceil(n / 2)
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print(sign * n)
        else:
            print(sign + " " * (n - 2) + sign)


def test_1086():
    a, b = input().split()
    c = str(int(a) * int(b))
    print(int(c[::-1]))


# 1091 还有问题
def test_1091():
    n = input()
    nums = map(int, input().split())
    for num in nums:
        for i in range(1, 10):
            tmp = i * num ** 2
            if str(tmp)[-1:-(len(str(num)) + 1):-1][::-1] == str(num):
                print(i, tmp)
                break
            else:
                continue
        if i == 9 and tmp >= num:
            print("No")


# 1061
def test_1061():
    n, m = map(int, input().split())
    scores = input().split()
    right = input().split()
    all = []
    for i in range(n):
        all.append(input())
    for stu in all:
        a = stu.split()
        total = 0
        for i in range(m):
            if a[i] == right[i]:
                total += int(scores[i])
        print(total)


# 1056 组合数的和
def test_1056():
    a = list(input().split())
    total = 0
    for i in range(1, len(a)):
        for j in a[1:]:
            if a[i] != j:
                total += int(a[i] + j)
    print(total)


# 检查密码 1081
def test_1081():
    n = input()
    all = []
    for i in range(int(n)):
        all.append(input())
    for s in all:
        if len(s) < 6:
            print("Your password is tai duan le.")
        else:
            char, digit, special, others = 0, 0, 0, 0
            for i in s:
                if i.isalpha():
                    char += 1
                elif i.isdigit():
                    digit += 1
                elif i == ".":
                    special += 1
                else:
                    others += 1
            if char != 0 and digit != 0 and digit != 0 and others == 0:
                print("Your password is wan mei.")
            elif others != 0:
                print("Your password tai luan le.")
            elif digit == 0 and others == 0:
                print("Your password needs shu zi.")
            elif digit != 0 and char == 0 and others == 0:
                print("Your password needs zimu")


def test_1057():
    s = input().lower()

    total = 0
    chars = "abcdefghijklmnopqrstuvwxyz"
    # dic = {}
    # for i in s:
    #     if i.isalpha():
    #         dic[i] = dic.setdefault(i, 0) + 1
    # for i in chars:
    #     if s.count(i) != 0:
    #         dic[i] = dic.setdefault(i, 0) + s.count(i)
    # for i, v in dic.items():
    #     total += (chars.index(i) + 1) * v
    for i, v in enumerate(chars):
        if s.count(v) != 0:
            total += (i + 1) * s.count(v)
    if total == 0:
        print("0", "0")
    else:
        ss = bin(total).replace("0b", "")
        print(ss.count("0"), ss.count("1"))


def test_1046():
    n = int(input())
    all = []
    for i in range(n):
        all.append(input())
    fail_1 = 0
    fail_2 = 0
    for p in all:
        a, b, c, d = map(int, p.split())
        if b == a + c and d == a + c:
            pass
        elif d == a + c and b != a + c:
            fail_1 += 1
        elif b == a + c and d != a + c:
            fail_2 += 1
        else:
            pass
    print(fail_1, fail_2)


# 输出还是有问题
def test_1051():
    a, b, c, d = map(float, input().split())
    import math
    aa = round((math.cos(b) * math.cos(d) + math.sin(b) * math.sin(d) * -1) * a * c, 2)
    bb = round((math.cos(b) * math.sin(d) + math.sin(b) * math.cos(d)) * a * c, 2)
    if aa == 0.00:
        print("0.00", end="")
    else:
        print("%.2lf" % aa, end="")
    if bb >= 0:
        print("+" + "%.2lfi" % bb)
    else:
        print("%.2lfi" % bb)


# 用set不会超时
def test_1087():
    n = int(input())
    # 用set时间要短一些
    a = set()
    for i in range(1, n + 1):
        tmp = i // 2 + i // 3 + i // 5
        a.add(tmp)
    # a = []
    # for i in range(1, n+1):
    #     tmp = i // 2 + i // 3 + i // 5
    #     if tmp not in a:
    #         a.append(tmp)
    print(len(a))


def test_1076():
    n = int(input())
    a = []
    score = ["A", "B", "C", "D"]
    wifi = ""
    for i in range(n):
        a.append(input())
    for i in a:
        for s in i.split():
            if s.count("T"):
                wifi += str(score.index(s[0]) + 1)
                break
    print(wifi)


# 避免超时，使用str, 或者 join连接
def test_1066():
    m, n, a, b, grey = input().split()
    m = int(m)
    n = int(n)
    a = a.rjust(3, "0")
    b = b.rjust(3, "0")
    grey = grey.rjust(3, "0")
    row = []
    for i in range(m):
        row.append([p.rjust(3, '0') for p in input().split()])
    for i in range(m):
        for j in range(n):
            if row[i][j] <= b and row[i][j] >= a:
                row[i][j] = grey
        print(" ".join(row[i]))


# 1093 字符串A+B
def test_1093():
    a = input()
    b = input()
    c = a + b
    to = list(set(c))
    print("".join(sorted(to, key=c.index)))


# 统计同成绩学生
def test_1038():
    n = input()
    all = list(map(int, input().split()))
    k = list(map(int, input().split()))
    res = []
    for i in k[1:]:
        res.append(str(all.count(i)))
    print(" ".join(res))


def test_1048():
    n, s = input().split()
    len_s = len(s)
    len_n = len(n)
    if len_n > len_s:
        s = s.rjust(len_n, '0')
    else:
        n = n.rjust(len_s, '0')
    s = list(map(int, s))
    n = list(map(int, n))
    index_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
    res = ""
    j = 1
    for v in s[::-1]:
        if j % 2 != 0:
            res += str(index_[(v + n[-j]) % 13])
        else:
            tmp = v - n[-j]
            if tmp < 0:
                res += str(tmp + 10)
            else:
                res += str(tmp)
        j += 1
    other = res[::-1]
    for i, v in enumerate(other):
        if v == '0':
            continue
        else:
            break
    print(other[i:])


# 数列中的所有片段和 -- 运行超时
def test_1049():
    n = int(input())
    nums = list(map(float, input().split()))
    total = 0
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp += nums[j]
            total += tmp
    print("%.2lf" % total)


# 朋友数
def test_1064():
    n = int(input())
    nums = input().split()
    total = set()
    for i in range(n):
        total.add(str(sum(map(int, list(nums[i])))))
    print(len(total))
    print(" ".join(sorted(total, key=lambda x: int(x))))


# 小赌怡情，输入的问题
def test_1071():
    total, k = input().split()
    total = int(total)
    k = int(k)
    for i in range(k):
        if total == 0:
            print("Game Over.")
            break
        else:
            n1, b, t, n2 = input().split()
            t = int(t)
            b = int(b)
            n1 = int(n1)
            n2 = int(n2)
            if t > total:
                print("Not enough tokens.  Total = %d." % total)
            else:
                # 赌小，玩家赢
                if (n1 > n2 and b == 0) or (n1 < n2 and b == 1):
                    total += t
                    print("Win %d!  Total = %d." % (t, total))
                # 赌小，玩家输
                else:
                    total -= t
                    print("Lose %d.  Total = %d." % (t, total))


#
def test_1072():
    n, m = input().split()
    m_code = input().split()
    n = int(n)
    dic = {}
    for i in range(n):
        s = input().split()
        for j in s[2:]:
            if j in m_code:
                dic.setdefault(s[0], [])
                dic[s[0]].append(j)
    i, j = 0, 0
    for key, value in dic.items():
        print(key + ": " + " ".join(value))
        i += 1
        j += len(value)
    print(i, j)


# 用count会增加用时？！
def test_1038():
    # n = input()
    # all = input().split()
    # k = input().split()
    # l = int(k[0])
    # for i, v in enumerate(k[1:]):
    #     if i + 1 == l:
    #         print(all.count(v))
    #     else:
    #         print(all.count(v), end=" ")
    n = int(input())
    grade = {}
    temp = input().split()
    for i in range(n):
        if temp[i] in grade:
            grade[temp[i]] += 1
        else:
            grade[temp[i]] = 1
    temp = input().split()
    x = len(temp)
    for i in range(1, x):
        if temp[i] in grade:
            if i != x - 1:
                print(grade[temp[i]], end=" ")
            else:
                print(grade[temp[i]])
        else:
            if i == x - 1:
                print(0)
            else:
                print(0, end=" ")


def test_1073():
    n, m = input().split()
    n = int(n)
    m = int(m)
    questions = []
    students = []
    scores = [0 for _ in range(n)]
    for i in range(m):
        questions.append(input().split())
    for i in range(n):
        students.append(input())

    for i in range(n):
        stu = students[i].split(") (")
        score = 0
        for j in range(m):
            stu[j] = stu[j].replace("(", "")
            stu[j] = stu[j].replace(")", "")
            s = stu[j].split()
            if s[0] == questions[j][2] and (set(questions[j][3:]) - set(s[1:])) == ():
                score += int(questions[j][0])
            elif s[0] > questions[j][2]:
                score += 0
            elif s[0] <= questions[j][2]:
                pass

    print(questions)
    print(students)


# 能不能好好认真审题呀
def test_1067():
    r_pw, n = input().split()
    n = int(n)
    i = 0
    while True:
        s = input()
        if s == "#":
            break
        else:
            i += 1
            if i <= n:
                if r_pw != s:
                    print("Wrong password: %s" % s)
                else:
                    print("Welcome in")
                    break
                if i == n:
                    print("Account locked")
                    break


def test_1044():
    n = int(input())
    all = []
    low = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
    high = ["tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]
    for i in range(n):
        all.append(input())
    for hh in all:

        if hh.isdigit():
            res = []
            hh = int(hh)
            if hh >= 13:
                res.append(high[hh // 13 - 1])
                if hh % 13 != 0:
                    res.append(low[hh % 13])
            else:
                res.append(low[hh])
            print(" ".join(res))

        else:
            total = 0
            for i in hh.split():
                if i in high:
                    total += (high.index(i) + 1) * 13
                else:
                    total += low.index(i)
            print(total)


def test_1047():
    n = int(input())
    dic = {}
    for i in range(n):
        a, b = input().split()
        b = int(b)
        a = a.split("-")[0]
        dic[a] = dic.setdefault(a, 0) + b
    res = sorted(dic.items(), key=lambda x: x[1], reverse=True)[0]
    for i, v in enumerate(res):
        if i == 0:
            print(v, end=" ")
        else:
            print(v)


def test_1082():
    n = int(input())
    dic = {}
    for i in range(n):
        id, a, b = input().split()
        a = abs(int(a))
        b = abs(int(b))
        dic[id] = dic.setdefault(id, 0) + a * b
    res = sorted(dic.items(), key=lambda x: x[1])
    min_ = res[-1][0]
    max_ = res[0][0]
    print(max_, min_)


def test_1083():
    n = int(input())
    all = [_ for _ in range(1, n + 1)]
    s = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        tmp = abs(all[i] - s[i])
        dic[tmp] = dic.setdefault(tmp, 0) + 1
    res = sorted(dic.items(), key=lambda x: x[0], reverse=True)
    for i in res:
        if i[1] > 1:
            print(i[0], i[1])


def test_1084():
    pass


def test_1069():
    # m 是总转化量 n间隔 s序号
    pass


def test_1078():
    flag = input()
    s = input()
    res = ""
    tag = ""
    if flag == "C":
        tag = s[0]
        cnt = 1
        for i in s[1:]:
            if i == tag:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt) + tag
                else:
                    res += tag
                tag = i
                cnt = 1
        if cnt > 1:
            res += str(cnt) + tag
        else:
            res += tag

    elif flag == "D":
        for i in s:
            if i.isdigit():
                tag += i
                continue
            else:
                if tag:
                    res += int(tag) * i
                else:
                    res += i
            tag = ""

    print(res)


def test_1059():
    pass


# 认真审题啊
def test_1079():
    a = input()
    b = a[::-1]
    flag = True
    for i in range(1, 11):
        if a == b:
            print(a, "is a palindromic number.")
            flag = False
            break
        c = str(int(a) + int(b))
        print("{} + {} = {}".format(a, b, c))
        if c == c[::-1]:
            print(c, "is a palindromic number.")
            flag = False
            break
        else:
            a = c
            b = c[::-1]
    if flag == True:
        print("Not found in 10 iterations.")





def find_prime(num):
    if num != 1 and num != 2 and num % 2 == 0:
        return False
    else:
        flg = 1
        for i in range(3, int(num ** 0.5)+1, 2):
            if num % i == 0:
                flg = 0
                break
        return flg
def test_1059():
    n = int(input())
    res = {}
    for i in range(n):
        name = input()
        res[name] = i + 1
    m = int(input())
    quries = []
    for i in range(m):
        quries.append(input())
    for q in quries:
        if q in res:
            rank = res[q]
            if rank == 1:
                out="Mystery Award"
            elif rank == -1:
                out = "Checked"
            elif find_prime(rank):
                out = "Minion"
            else:
                out="Chocolate"
            res[q] = -1
        else:
            out = "Are you kidding?"
        print("%s: %s" % (q, out))














def test_1039():
    s = input()
    real = input()
    dic = {}
    dic_s = {}
    res = 0
    lack = 0
    for i in real:
        dic[i] = dic.setdefault(i, 0) + 1
    for i in s:
        dic_s[i] = dic_s.setdefault(i, 0) + 1
    s_keys = dic_s.keys()
    keys = dic.keys()
    for k, v in dic.items():
        if k in s_keys:
            temp = dic_s[k]
            if temp >= v:
                res += (temp - v)
            else:
                lack += (v - temp)
        else:
            lack += v
    for k, v in dic_s.items():
        if k not in keys:
            res += v
    if lack > 0:
        print("No %d" % lack)
    else:
        print("Yes %d" % res)


def test_1043():
    s = input()
    seq = "PATest"
    a = []
    for i in seq:
        a.append(s.count(i))


# 1,2,3,4组成4位不同的数字
def test_zsyh_1():
    cnt = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                for l in range(1, 5):
                    if i != j and j != k and k != l and i != l and i != k and j != l:
                        print("%d%d%d%d" % (i, j, k, l))
                        cnt += 1
    print("cnt=", cnt)


def test_zsyh_2():
    a = ['0', '1', 'ABC', 'DEF', 'HI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    n = input()
    res = []
    for i in n:
        res.append(a[int(i)])
    len_s = len(res)
    ss = []
    for i in range(len_s):
        temp = []
        if i == 0:
            for s in res[i]:
                temp.append(s)
        else:
            for j in ss:
                for k in res[i]:
                    temp.append(j+k)
        ss = temp
    print(ss)




# start_time = time.time()

# #print(find_prime(8888))
# end_time = time.time()
# print((end_time - start_time))




n = int(input())

for i in range(2, n):
    t1 = 0
    t2 = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        t1 = i
        t2 = n - t1

        for k in range(2, int(t2 ** 0.5)+1):
            if t2 % k == 0:
                break
        else:
            print("{} = {} + {}".format(n, t1, t2))
            break
