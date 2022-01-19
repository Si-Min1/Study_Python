# 파일 입출력

# 파일 출력
# f = open('newfile.txt', 'w')
# f.close()                       # 열었으면 닫아라 젭알

# f = open('C:/Sources/Sample/newfile.txt', 'w') # 특정위치 파일 생성
# f.close()
# ascii (영어만 처리)와 cp949 / EUCKR(한글처리), utf-8


#  f = open('newfile.txt','r', encoding='utf-8')  # UTF-8' 인코딩 파일 오픈
# while True:
#     line = f.readline()        # 한줄씩 읽기
#     if not line: break
#     print(line, end= '')

# f.close()   # 파일 닫기



f = open('newfile.txt','r', encoding='utf-8')  # UTF-8' 인코딩 파일 오픈
for line in f:
    print(line,end='')

f.close








