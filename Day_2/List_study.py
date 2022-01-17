# 리스트 연산
arr = list(range(5))
arr1 = list(range(1, 6))
arr2 = list(range(0, 100, 7))

print(arr)
print(arr1)
print(arr2)
print(arr[1] , '+', arr[2], '=' , arr[1] + arr[2])

# 2차원 배열
arr12 = [1,2,['MY',['kkk','aaa'],'GOD']]
print(arr12[2][1][1])

arr3 = list(range(1,4))
print(arr3 + arr)
print(len(arr3))

# --리스트 함수--
print('-- 리스트 함수 --')
del(arr3[1])            # 배열 번호로 삭제
print(arr3)

arr3.remove(1)          # 입력 값을 찾아 삭제     
print(arr3)

arr4 = [1,3,3,76,21,12,5,42,37]
print(arr4.remove(3))   # 단 처음으로 찾은 3 1개만 지움 (또한 값이 없으면 예외 처리되어 중단됨)

arr4.sort()
print(arr4)

arr4.reverse()          #sort 후 사용 역순 사용
print(arr4)

arr4.insert(2, 10)
print(arr4)

arr4[2] = 100
print(arr4)

# 튜플
tup1 = tuple(range(1,6))
print(tup1)

# tup1[1] = 10  튜플은 값 고정이라 바꿀라카면 뭐라함


# 딕셔너리 연산
dic1 = {1:'a', 2:'b'}
dic1[0] = 'c'
print(dic1)         # 딕셔너리는 순서같은거 상관없이 넣을 수 있음

dic1['a'] = 'asd'
print(dic1)         

del dic1['a']
print(dic1)         

print(dic1.keys())
print(dic1.values())
print(dic1.items())






