# 부산 버스 노선별 이용건수
import csv
from encodings import utf_8

file_name = '부산버스정보.csv'
# dir_name = r'D:/data'

f = open('부산버스정보.csv', 'r', encoding='utf_8')


reader = csv.reader(f, delimiter=',')
next(reader) # 헤더를 없애주는 역할 여기서는 노선, 건수 등등 행 하나 쓱싹

for line in reader:
    print(line)

f.close()










