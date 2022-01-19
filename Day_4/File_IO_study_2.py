f = open('newfile.txt','w', encoding='utf-8')  # UTF-8' 인코딩 파일 오픈

f.write('한화의 김성근 감독님 사랑해~\n')

texts = ['반갑다 소년.\n','내 이름은 간지 폭푹이라고 한다.\n']


f.writelines(texts)
f.close()

# 추가
f = open('newfile.txt','a', encoding='utf-8')  # UTF-8' 인코딩 파일 오픈

f.write('내용을 추가합니다.\n 안되잖아?')
f.close()











