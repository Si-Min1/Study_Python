class car:
    num = 0
    __brand = ''    
    color = ''
    fuel = ''
    year = ''

    def __init__(self, color, num, brand):
        self.color = color
        self.num = num
        self.__brand = brand

    def __str__(self) -> str:                   # print(car())하면 나올거
        return f'내차는{self.year}에 만들어 진{self.fuel} 이올시다'

    def go(self, level):
        print(f'{self.color}색 {self.__brand}의 {self.num}번 차가 {level}단으로 간다')
    
    def edit(self, brand):
        self.__brand = brand

    def show(self):
        print(f'{self.__brand}')


    def back(self):
        print('역돌격')
    def left(self):
        print('왼')
    def right(self):
        print('오')
    def stop(self):
        print('멈춰')
        