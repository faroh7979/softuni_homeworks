# a2 = 1010101
# b2 = 111111000
# c2 = 1010110011
# d2 = 1011100010
#
# a = 1*2**6 + 0*2**5 + 1*2**4 + 0*2**3 + 1*2**2 + 0*2**1 + 1*2**0
# b = 1*2**8 +1*2**7 +1*2**6 +1*2**5 +1*2**4 +1*2**3 +0
# c = 1*2**9 +0*2**8 +1*2**7 +0*2**6 +1*2**5 +1*2**4 +0*2**3 +0*2**2 +1*2**1 +1*2**0
# d = 1*2**9 +0*2**8 +1*2**7 +1*2**6 +1*2**5 +0*2**4 +0*2**3 +0*2**2 +1*2**1 +0*2**0
# e= 1**2**8 +1**2**7
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a = input()
# fund = int(input())
# decimal = 0
# length = len(a)
# for position, digit in enumerate(a):
#     decimal += int(digit) * fund ** int(length - position - 1)
# print(decimal)

a = int(input())
fund = int(input())
binary = 0
i = 0
l = []
while a != 0:
    i += 1
    l.append(a % fund)
    a //= fund
for num in range(i):
    print(l[i - num - 1], end= "")

