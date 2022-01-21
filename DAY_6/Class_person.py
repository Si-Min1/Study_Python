# person 클래스

class Person:
    name = ''
    age = 0
    weight = 0
    gender = ''
    blood = ''

    def __init__(self, name = '', age = 0 , weight = 0) -> None:
        self.age = age
        self.name = name
        self.weight = weight

    def greeting(self):
        print(f'나 {self.name} 성별은{self.gender}이오 나이는 {self.age}세 이올시다')

    def eat(self, food):
        print(f'{food} 먹는다')
    
    def run(self):
        print(f'{self.name} 한다 일')



if __name__ == "__main__":
    th = Person('xoxoxo', 31, 24)
    th.weight = 123
    th.gender = 'M'
    th.blood = 'O'
    th.eat('pizza')
    th.run()
    th.greeting()
    

