# 함수
def sum(a=5, b=1):
    return a+b

print(sum(9,8))


# 함수종류
# 매개변수( 파라미터 ) 없는경우
def test1():
    return 'test1'

print(test1())

# 매개변수 지정
def test2(a,b):
    return a+b

print(test2(a=2,b=5))
# print(test2(2,5))


# 결과값이 없는 경우
def test3(test):
    print(f'넣은거 {test}')

test3('곷장')

# 둘다 없
def test4():
    print('test4')

test4()

# 매개변수가 일정하지 않음
def test(*args):
    res = 0

    for i in args:
        res += i

    return res;

print(test(1,2,3,5))


# 2개 이상 리턴
def testt (x,y):
    tsum = x + y
    tmul = x * y

    return tsum,tmul

print(type(testt(4,5)[0]))

ans1, ans2 = testt(4,5) #이렇게도 값 받을 수 있음
print(ans1,ans2)

































