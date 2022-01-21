from Class_vehicle import car
def simsim(num, time):
    if time != 0:
        num = num * 2
        return simsim(num,time -1)
    else:
        print(num)

if __name__ == "__main__":
    mycar = car('red',1010, 'asdf') # 'asdf'처럼 생성자에서 받던가 클래스내의 함수처럼 캡슐 안에서 조작 해야함 *1
    mycar.year = '1234'
    mycar.go(3)

    mycar.fuel = 'Gasoline'         # 가솔린으로 바꿈
    print(mycar.fuel)               # 가솔린 출력함


    # print(mycar.__brand)          캡슐화된 클래스의 변수에 접근불가 출력 안됨 
    mycar.__brand = 'KIA'           # KIA로 바꿨으나
    mycar.show()                    # 접근이 안되서 불발 정규 루트로 들간것만 적용됨 *1 참조


    mycar.edit('KIA')               # 함수로 접근
    mycar.show()                    # 여기선 바뀜

    print(mycar)

    simsim(2,9)

