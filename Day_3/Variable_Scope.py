# 변수 라이프 스코프

a = 1               # 전역변수 선언

def vartest(a):     # 지역변수 선언
    a = a + 1
    return a        # 지역변수 반환

a = vartest(a)      # 전역변수 = 지역변수 반환 값
print(a)

# 람다 함수
# 간단하게 한두번 쓸때 유용함
ladd = lambda x, y : x * y
print(ladd(4,3))











