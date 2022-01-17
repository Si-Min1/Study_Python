# 자료형
print(None)
print(type(None))

print( 0 == None)
print( 0 is None)


# 숫자형
금액 = 87_654_321   # 언더바로 숫자세기 편하게 해줌
print(금액)


# 문자열형
bruce_eckel = "Life is short, You need Python"
print(bruce_eckel)

bruce_eckel = "Life is short, \nYou need Python"    # 몇몇문자 입력시 /
print(bruce_eckel)

bruce_eckel = '''Life is short,
\nYou need Python'''        # 적은 대로 나옴 /n같은거 필요없음
print(bruce_eckel)


# 불형 boolean
asdf = 1000
print(asdf == 1000)

asdf_typ = True
print(type(asdf_typ))

print(False is asdf_typ) # is문 가능


# 의미가 있는 bool
print(bool(1))
print(bool(0))


# 리스트
a = [1,2,3,4,5,6,7,8,9,10]
print(a)

arr2 = ['Life', 'is', 'short', 'U', 'need', 'python', '3']
print(arr2)

arr3 = [[1,2,3],[4,5,6]]
print(arr3)

arr4 = list()
print(arr4)


# 튜플
tuple1 = (1,2,3,4)
tuple2 = (2,)

print(tuple1)
print(tuple2)


# 딕셔너리
spiderman = { 'name' : 'Peter Parker'
            , 'age' : '18'
            , 'weapon' : 'web shooter' }

print(spiderman['name'])

# 집합
set_int = set([1,2,3,4,5,6,1,2,2])
print(set_int)                      # 중복 제거

print(set(spiderman))


