import string

def convert(s):
    result = ""
    for i in range(len(s)):
        result += s[i]
    return result 

length = input()
ary = ["" for i in range(int(length))]
for i in range(int(length)):
    ary[i] = list(input())
ary.sort(key=lambda x:(len(x), x))
for i in range(int(length)):
    print(convert(ary[i]))