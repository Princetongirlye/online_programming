"""
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWE
"""
s = "".join(input().split("\n"))
# s = input()
print(s)
w = 0
l = 0
j = 0
for i in s:
    j += 1
    if i == 'W':
        w += 1
    elif i == 'L':
        l += 1
    elif i == "E":
        print(w, ":", l)
        break
    if j == 11 and i != 'E':
        print(w, ":", l)
        w, l, j = 0, 0, 0
print()
w, l, j = 0, 0, 0
for i in s:
    j += 1
    if i == 'W':
        w += 1
    elif i == 'L':
        l += 1
    elif i == "E":
        print(w, ":", l)
        break
    if j == 21 and i != 'E':
        print(w, ":", l)
        w, l, j = 0, 0, 0