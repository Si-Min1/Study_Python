# for i in range(3): 그냥 for문 쓰는 법
# 기본 for 문

# arr = list(range(0,5))

# for i in arr:
#     print(f'{i:2.1f}')


# 튜플  for 문
# arr2 = ('me', 'my', 'friend', 'asdf')

# for i in arr2:
#     print(f'{i:>10}')


# 합계 계산
# nums = list(range(1,11))
# nums2 = list(range(1,24,2))
# res = 0

# for i in nums:
#     res += i


# print(f'{nums[-1]} 까지의 총 합은 {res} 입니다')


# 홀짝 구분
# num = list(range(0,21))


# for i in num:
#     if i > 18:
#         break;
#         # continue; 이 친구도 있음
#     elif(i % 2 == 0):
#        print(f'{i} 는 짝수')
#     else:
#        print(f'{i} 는 홀수')
    

# 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j:2}',end= '    ') # end= ' '로 줄바꿈 막음
    print('')  # 줄바꿈용 print()도 됨


a = [1, 2, 3, 4]

result = [i * 3 for i in a] # inline for문
print(result)

# while
# hit = 0
# while hit < 100:

#     hit += 1

#     if hit > 10:
#         break;
    
#     print(f'나무를 {hit}번 찍습니다')





















