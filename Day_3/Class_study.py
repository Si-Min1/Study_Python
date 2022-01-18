# 클래스
# class Person:
#     pass

# p = Person()
# print(type(p))          # 타입은 클래스
# print(id(Person))       # 주소값이 인스턴트인 p와 다름
# print(id(p))            # id() 함수는 주소값 알려줌






class test:
    name = ''

    def __init__(self, name = '홍길동'):     # 생성자 (그냥 초기 세팅 같은거?)
        self.name = name
        print(f'{name} 생성')
    
    def info(self):
        print(f'{self.name} 입니다')
        print(type(self.name))
    
    def show(self, check):
        print(f'{self.name}은(는) {check} 번')  #자기꺼 쓸려면 파라메터에 자기 자신을 불러야함


t1 = test()
t1.info()
t1.show(4)
t2 = test('앨랠래')
t2.info()











