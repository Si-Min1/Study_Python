from datetime import datetime
import math
from posixpath import split

# 연산자

a = 11
b = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)     # 몫
print(a%b)      # 나머지

# 문자열 연산
str1 = 'Hello'
str2 = 'World'

print(str1, str2)
print(str1 + str2)

res1 = str1, str2
res2 = str1 + str2
print(res1)
print(res2)
print(type(res1))
print(type(res2))

print(str1 * 2) # 곱셈까지는 됨


# 문자열 길이
print(len(str1))


# 문자열 인덱스, 리스트와 동일한 작업
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])        # 드래그 해서 ctrl + / 누르면 주석 처리 다시 누르면 해제

print(str1[-1])


# 문자열 자르기, 수정
일시1 = '2022 - 01 - 17 14 : 39 : 25'
일시 = 일시1.replace(" ","")
print(일시)

print(일시[0:4], "년")
print(일시[5:7], "월")
print(일시[8:10], "일")
print(일시[10:12], "시")
print(일시[13:15], "분")
print(일시[-2:], "초")

list_1 = [1,2,3,4,5]
list_1[1] = 9

print(list_1)


# 문자열 포멧팅
num = 21
age1 = "{1}년 올해 내 나이 {0}살".format(num,2022) # 방법1
print(age1)

age1 = f"{일시} 올해 내 나이 {num}살" # 방법2 <- 앞에f 붙혀주기
print(age1)


## 숫자 1,000 단위 콤마
money = 1999999999999
print(format(money,',d'))

now = datetime.now()
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S')) # 관련 함수 import 필요

mypi = math.pi
print(mypi)

print('{0:0.2f}'.format(mypi))
# print(f'{mypi:0.2f}')

full_name = "App Soo Aa"
age = 11
greeting = '''
반갑다 학우들 {0}살 {1}다
'''.format(age, full_name)

print(greeting)

part_name = full_name.split()
print(type(part_name))
print(part_name)

test = "hey~, guys"
part_test = test.split('~') # 여백으로 두면 공백 기준으로 나누고 이렇게 지정 가능
print(part_test)
# ex
code = 'TEST|2002|10|21'
print(code.split('|'))

# 단어 교체
print(code.replace('2002','2022'))

# 공백제거
qwq = "   qqa  "
print(qwq.strip())
print(qwq.lstrip())
print(qwq.rstrip())

# 문자 찾기
print(qwq.index('q')) # 3(개 존재함)
print(bool(qwq.index('a'))) # bool 뺴면 1
# print(qwq.index('t'))

fqwq = qwq.find('a')
print( fqwq ) #위치찾기

print(qwq.count('q')) # 몇개

# 대문자 소문자 대소문자

print('-'.join(qwq))
print(qwq.lower())
print(qwq.upper())


