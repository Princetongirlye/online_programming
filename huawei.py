# 字符统计

from collections import defaultdict


def chars_count():
    try:
        while True:
            inputs = input()
            ss = defaultdict(list)
            res = ""
            for i in set(inputs):
                if i.isdigit() or i.isspace() or i.isalpha():
                    ss[inputs.count(i)].append(i)
                else:
                    pass
            for i in sorted(ss.keys(), reverse=True):
                res += "".join(sorted(ss[i], key=lambda k: ord(k)))
            print(res)
    except:
        pass


# 求最小公倍数

def get_lcm():
    try:
        while True:
            nums = input().split(" ")
            a, b = int(nums[0]), int(nums[1])
            gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
            print(a * b // gcd(a, b))
    except:
        pass


# 求立方根，不使用库函数

def get_cube_root():
    try:
        while True:
            num = float(input())
            pass
    except:
        pass


# 字符逆序


def get_reverse_chars():
    try:
        while True:
            strs = input()
            print(strs[::-1])
    except:
        pass


# get_reverse_chars()

# 记负均正

def get_pos_neg():
    try:
        while True:
            num, neg, pos = input().split(" "), [], []
            for i in num:
                neg.append(int(i)) if int(i) < 0 else pos.append(int(i))
            print(len(neg))
            print(round(sum(pos) / len(pos)) if pos else "0.0")
    except:
        pass


# 字符串分隔
def get_string_length(strs, new_strs):
    if len(strs) <= 8:
        new_strs.append(strs + "0" * (8 - len(strs)))
    else:
        new_strs.append(strs[0:8])
        strs = strs[8:]
        get_string_length(strs, new_strs)


def cut_strings():
    # 确认输入多少个字符串
    try:
        while True:
            a = int(input())
            for i in range(a):
                s = input()
                while len(s) > 8:
                    print(s[:8])
                    s = s[8:]
                print(s.ljust(8, "0"))
    except:
        pass


# redraiment 走梅花桩的高手 ? 未做出来！！！
def get_result():
    while True:
        try:
            n = int(input())
            nums = list(map(int, input().split()))
            print(nums)
            max_step = 0
            for i in range(len(nums)):
                step = 0
                b = set(nums[i + 1:])
                print(b)
                for j in b:
                    if j >= nums[i]:
                        step += 1
                if step >= max_step:
                    max_step = step
            print(max_step)
        except:
            break


# 输入整型数据和排序表示，对其元素按照升序或降序进行排序

def get_sort_int_array():
    while True:
        try:
            # 输入个数
            n = int(input())
                # 输入正数数组
            nums = list(map(int,input().split()))
                # 输入排序flag 0 表示升序 1 表示降序
            flag = int(input())
            if flag == 0:
                print(" ".join( str(i) for i in sorted(nums, reverse=False)))

            else:
                print(" ".join(str(i) for i in sorted(nums, reverse=True)))
        except:
            break

# 等差数列
def get_numeric_():
    while True:
        try:
            n = int(input())
            sum = 0
            if n <= 0:
                print("-1")
            else:
                a = 2
                b = a + 3
                for i in range(1, n+1):
                    sum += a
                    a = b
                    b = a + 3
                print(sum)
        except:
            break

# 自守数
def get_self_num():
    while True:
        try:
            n = int(input())
            num = 0
            for i in range(1, n+1):
                sqrt_num = i * i
                if int(str(sqrt_num)[-len(str(i)):]) == i:
                    num += 1
            print(num)
        except:
            break


"""
    加密解密密码
"""

def encr_decrpyt():
    while True:
        try:
            s1 = input()
            s2 = input()
            encrpyt_s = []
            decrpyt_s = []
            for i in s1:
                if i.isalpha():
                    if i == 'Z' or i == 'z':
                        encrpyt_s.append('a' if i.isupper() else 'A')
                    else:
                        encrpyt_s.append(chr(ord(i) + 1).lower() if i.isupper() else chr(ord(i) + 1).upper())
                elif i.isdigit():
                    if int(i) < 9:
                        encrpyt_s.append(str(int(i) + 1))
                    else:
                        encrpyt_s.append('0')

                else:
                    encrpyt_s.append(i)
            for i in s2:
                if i.isalpha():
                    if i == 'a' or i == 'A':
                        decrpyt_s.append('Z' if i.islower() else 'z')
                    else:
                        decrpyt_s.append(chr(ord(i) - 1).lower() if i.isupper() else chr(ord(i) - 1).upper())
                elif i.isdigit():
                    if int(i) == 0:
                        decrpyt_s.append('9')
                    else:
                        decrpyt_s.append(str(int(i) - 1))
                else:
                    decrpyt_s.append(i)
            print("".join(encrpyt_s))
            print("".join(decrpyt_s))

        except:
            break

"""
    字符串合并操作 超时了，需要重新写
"""

def merge_strings():

    while True:
        try:
            new_s = input().replace(" ","")
            new_s1 = "".join(sorted(new_s[0::2]))
            new_s2 = "".join(sorted(new_s[1::2]))
            ss = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            news = ""
            for i in range(len(new_s1)):
                news += ss[int(bin(ss.index(new_s1[i])).replace("0b","")[::-1], 2)].upper()
                if i >= len(new_s2):
                    news += ss[int(bin(ss.index(new_s1[i])).replace("0b","")[::-1], 2)].upper()
                else:
                    news += ss[int(bin(ss.index(new_s2[i])).replace("0b","")[::-1], 2)].upper()
            print(news)
        except:
            pass

"""
单词倒序
"""
def words_reverse():
    import re
    while True:
        try:
            s = input()
            new_s = " ".join((" ".join(re.findall(r"[a-zA-Z]{1,}", s))).split(" ")[::-1])
            print(new_s)
        except:
            break

"""
    在字符串中找出连续最长的数字串
"""
def get_the_longest_strings():
    import re
    while True:
        try:
            s = input()
            nums_list = sorted(re.findall(r"[0-9]{1,}", s), key=lambda x: len(x), reverse=True)
            print(nums_list)
            max_len = len(nums_list[0])
            index_ = ""
            for i in range(len(nums_list)):
                if len(nums_list[i]) == max_len:
                    index_ += nums_list[i]
            print(index_ + "," + str(max_len))
        except:
            break

"""
    分组，使得两组中元素和相等
"""


"""
    记票统计
"""
def get_vote_result():
    from collections import OrderedDict
    while True:
        try:
            # 输入候选人的人数
            n = int(input())
            # 输入候选人的名字
            names = input().split()
            # 投票人数
            vote_n = int(input())
            # 投票
            vote_name = input().split()
            dic = OrderedDict()
            others = len(vote_name)
            for i in names:
                if vote_name.count(i):
                    dic[i] = dic.setdefault(i, 0) + vote_name.count(i)
                    others = others - vote_name.count(i)
                else:
                    dic.setdefault(i, 0)
            for i, v in dic.items():
                print(i, ":", v)
            print("Invalid :", others)
        except:
            break

"""
    整数与IP地址之间的转换
"""
def covert_ips_integer():
    while True:
        try:
            ips = input().split(".")
            nums = int(input())
            ips_strings = ""
            for ip in ips:
                ips_strings += bin(int(ip)).replace("0b", "").rjust(8, '0')
            print(int(ips_strings, 2))
            bin_nums = bin(nums).replace("0b", "").rjust(32, "0")
            ips_ = []
            while len(bin_nums) > 8:
                ips_.append(str(int(bin_nums[:8], 2)))
                bin_nums = bin_nums[8:]
            ips_.append(str(int(bin_nums[:8], 2)))
            print(".".join(ips_))
        except:
            break

"""
    图片整理
"""
def deal_pic():
    while True:
        try:
            s = input()
            if len(s) > 1024:
                break
            else:
                print("".join(sorted(s, key=lambda x: ord(x), reverse=False)))
        except:
            break

"""
    蛇形矩阵
"""

def get_sneak_result():
    pass


"""
 字符串加密
"""
def strings_encrypt():
    while True:
        try:
            # 输入的key
            key = input()
            # 要加密的字符串
            ss = input()
            alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            deplicated = []
            # 去重
            for s in key:
                if s.upper() not in deplicated:
                    deplicated.append(s.upper())
            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if i not in deplicated:
                    deplicated.append(i)
            new_s = ""
            for i in ss:
                if i.isalpha():
                    if i.isupper():
                        new_s += deplicated[alphabet.index(i)]
                    else:
                        new_s += deplicated[alphabet.index(i.upper())].lower()
                else:
                    new_s += i
            print(new_s)
        except:
            break

"""
    统计每个月兔子的总数
"""

def get_rabbits_result():
    while True:
        try:
            # 输入月份
            month = int(input())
            if month == 1 or month == 2:
                print(1)
            else:
                a = 1
                b = 1
                c = 0
                for i in range(3, month + 1):
                    c = a + b
                    b = a
                    a = c
                print(c)
        except:
            break


"""
    求小球落地5次后所经历的路程和第5次反弹的高度
"""
def get_rolls_result():
    while True:
        try:
            height = int(input())
            sum = 0.0
            fifth_height = 0.0
            for i in range(5):
                if i == 0:
                    sum += height
                else:
                    sum += height * 2
                height = height / 2
            print(sum)
            fifth_height = height
            print(fifth_height)
        except:
            break

"""
    判断两个IP是否属于同一个之网
"""

def verify_ips():
    while True:
        try:
            ips = input().split()
            subnet_mask,ip_1,ip_2 = ips[0].split("."), ips[1].split("."), ips[2].split(".")
            new_ip_1, new_ip_2 = [],[]
            flag = False
            for i in range(len(ip_1)):
                if int(subnet_mask[i]) > 255  or int(ip_1[i]) > 255 or int(ip_2[i]) > 255:
                    flag = True
                    break
                else:
                    new_ip_1.append(str(int(subnet_mask[i]) & int(ip_1[i])))
                    new_ip_2.append(str(int(subnet_mask[i]) & int(ip_2[i])))
            if ".".join(new_ip_1) == ".".join(new_ip_2) and  flag == False :
                print(0)
            elif flag == True:
                print(1)
            else:
                print(2)
        except:
            pass


"""
    统计字符
"""

def get_chars_count():
    while True:
        try:
            s = input()
            alpha ,space, nums, other = 0,0,0,0
            for i in s:
                if i.isalpha():
                    alpha += 1
                elif i.isspace():
                    space += 1
                elif i.isdigit():
                    nums += 1
                else:
                    other += 1
            print(alpha)
            print(space)
            print(nums)
            print(other)
        except:
            break

"""
    称砝码
"""


"""
    统计大写字母个数
"""
def count_upper_num():
    while True:
        try:
            s = input()
            upper = 0
            for i in s:
                if i.isalpha() and i.isupper():
                    upper += 1
            print(upper)
        except:
            break


"""
    合法IP
"""

def get_valid_ip():
    while True:
        try:
            s = input().split(".")
            flag = True
            for ip in s:
                if int(ip) <= 255 and  int(ip) >= 0:
                    pass
                else:
                    flag = False
                    break
            print('YES' if flag else "NO")
        except:
            pass

"""
    求最大连线的bit
"""
def get_longest_bit():
    import re
    while True:
        try:
            a = int(input())
            print(len(max(re.findall(r"1{1,}", bin(a)[2:]), key=len)))
        except:
            pass


"""
    密码强度等级
"""
# import re
# while True:
#     try:
#         pwd = input()
#         pwd_len = len(pwd)
#         score = 0
#         # 密码长度
#         if pwd_len<= 4:
#             score += 5
#         elif pwd_len <=7:
#             score += 10
#         else:
#             score += 25
#         # 字母
#         alpha = re.findall(r"[a-zA-Z]+", pwd)
#         if alpha == []:
#             score += 0
#         else:
#             flag = True
#             for i in alpha:
#                 if i.isupper() or i.islower():
#                     pass
#                 else:
#                     flag = False
#                     break
#             if flag:
#                 score += 10
#             else:
#                 score += 20
#         # 数字
#         nums = len(max(re.findall(r"[0-9]+", pwd), key=len))
#         if nums > 1:
#             score += 20
#         elif nums == 1:
#             score += 10
#         else:
#             score += 0
#         # 符号
#
#         # 奖励
#
#     except:
#         pass

"""
    查找输入整数二进制中1的个数
"""
def get_binary_1_num():
    while True:
        try:
            s = int(input())
            print(bin(s)[2:].count("1"))
        except:
            break

"""
    DNA序列
"""
def get_dna_series():
    while True:
        try:
            s ,n= input() , int(input())
            max = 0
            ss = ""
            for i in range(len(s)):
                new_i = s[i:i+n].count("C") + s[i:i+n].count("G")
                if new_i > max:
                    max = new_i
                    ss = s[i:i+n]
                else:
                    pass
            print(ss)
        except:
            break


"""
    字符串匹配
"""
def char_match():
    while True:
        try:
            a,b=set(input()),set(input())
            print ("true" if a&b==a else "false")
        except:
            break


"""
    将真分数分解为埃及分数
"""
# while True:
#     try:
#         pass
#     except:
#         break

"""
    输出出现一次字符的第一个字符
"""
def get_first_char():
    from collections import Counter, OrderedDict
    while True:
        try:
            s = input()
            dic = OrderedDict()
            for i in s:
                dic[i] = dic.setdefault(i, 0) + 1
            new_dic =sorted(dic.items(), key=lambda x:x[1])
            if new_dic[0][1] > 1:
                print("-1")
            else:
                print(new_dic[0][0])
        except:
            break

"""
    挑7
"""
def get_seven():
    while True:
        try:
            num = int(input())
            num_7 = 0
            for i in range(7, num + 1):
                if i % 7 == 0 or str(i).__contains__("7"):
                    num_7 += 1
            print(num_7)
        except:
            break


"""
    完全数计算
"""
def get_compliance():
    while True:
        try:
            n = int(input())
            if n < 0 or n > 500000:
                print(-1)
            else:
                cn = 0
                for i in range(2, n+1):
                    sum = 0
                    for j in range(1, i+1):
                        if i % j == 0 and i != j:
                           sum += j
                    if sum == i:
                        cn += 1
                print(cn)
        except:
            break

"""
    成绩排序
"""
def grade_sort():
    while True:
        try:
            people = int(input())
            flag = input()
            dic = []
            new_dic=[]
            for i in range(people):
                score = input().split()
                score[1] = int(score[1])
                dic.append(score)
            if flag == '0':
                new_dic = sorted(dic, key=lambda x: x[1], reverse=True)
            else:
                new_dic =  sorted(dic, key=lambda x:x[1], reverse=False)
            for i in new_dic:
                print(i[0], i[1])
        except:
            break


"""
    矩阵乘法
"""
def maxtrix_times():
    while True:
        try:
            x,y,z = int(input()),int(input()), int(input())
            maxtrix_1 = [[0]*y for _ in range(x)]
            maxtrix_2 = [[0]*z for _ in range(y)]
            maxtrix_3 = [[0]*z for _ in range(x)]
            for i in range(x):
                nums = input().split()
                for j in range(len(nums)):
                    maxtrix_1[i][j] = int(nums[j])
            for i in range(y):
                nums = input().split()
                for j in range(len(nums)):
                    maxtrix_2[i][j] = int(nums[j])
            for i in range(x):
                for j in range(z):
                    for k in range(y):
                        maxtrix_3[i][j] += maxtrix_1[i][k] * maxtrix_2[k][j]
            for i in range(x):
                for j in range(z):
                    print(maxtrix_3[i][j], end=" ")
                print()
        except:
            break

"""
    整形数组合并
"""
def interger_merge():
    while True:
        try:
            n1, nums1 = input(),input()
            n2, nums2 = input(),input()
            new_s =  sorted(list(map(int,set((nums1 + " "+ nums2).split()))),reverse=False)
            print("".join(map(str, new_s)))
        except:
            break


"""
    表示数字
"""

def number_expression():
    import re
    while True:
        try:
            s = input()
            nums = re.findall(r"[0-9]{1,}", s)
            new_s = ""
            index_ = []
            for i in re.finditer(r"[0-9]{1,}", s):
                index_ .append (i.start())
                index_.append(i.start() + len(i.group()))
            t = 0
            for i in range(len(s)):
                if i not in index_:
                    new_s += s[i]
                else:
                    t = index_.pop(0)
                    new_s += "*"
                    new_s += s[i]
            if index_ != [] and index_.pop(0) == len(s):
                new_s += "*"
            print(new_s)
        except:
            break
