# 예외처리
def add (a, b):
    return a + b

def minus (a, b):
    return a - b


def multi (a, b):
    return a * b

def div (a, b):
    return a / b

print('테스트 시작')
x, y = 4, 1
num = [3,6,9]

try:
    x = int(input())                    # 문자 넣으면 value 오류남
    print(f'나누기 결과 {div(x, y)}')

    # res = int(num[3] * 3)               # [3]은 없으니 인덱스 오류
    print('오류나면 실행 안되는 부분')  # 예외처리는 필요한 부분만

except ZeroDivisionError as e:
    print(f'{e} 나누기 예외')

except IndexError as e: 
    print(f'{e} 인덱스 예외')

except ValueError as e:
    print(f'{e} type 예외')


except Exception as e:              # Execption이 제일 상위 예외 처리
    print(f'{e} 몰?루')


finally:
    print() # DB닫거나 close() 넣는게 좋음


print(f'빼기 결과 {minus(x, y)}')
print(f'곱하기 결과 {multi(x, y)}')
print(f'더하기 결과 {add(x, y)}')

print('사칙연산 종료')








