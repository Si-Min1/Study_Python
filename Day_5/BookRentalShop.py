# 책 대여 DB
import cx_Oracle as ora

def mydb():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    db = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')
    return db

#1
def getAllDataFromDivtbl(db):
    cur = db.cursor()
    sql = 'SELECT * FROM divtbl'
    for rows in cur.execute(sql):
        print(rows)

    db.close()
    return 0

#2
def setDataIntoDivtbl(db, tup):
    cur = db.cursor()
    sql = '''INSERT INTO divtbl (division, names) 
             VALUES (:0, :1)'''

    cur.execute(sql,tup)
    cur.close()
    db.commit()
    db.close()

#3
def getSomeDateFromMembertbl(db):
    cur = db.cursor()
    sql = '''SELECT names, levels, addr, mobile, email 
            FROM membertbl
            WHERE addr LIKE '서울%'
            AND UPPER(email) LIKE '%@NAVER.COM'
            ORDER BY idx DESC'''

    for rows in cur.execute(sql):
        print(rows)

    cur.close()
    db.close()

#4
def setNewMemberIntoMembertbl(db, tup):
    cur = db.cursor()
    idx = 0;
    sql1 = '''SELECT ROWNUM, idx
                FROM ( SELECT idx FROM membertbl
                    ORDER BY idx DESC) 
                WHERE ROWNUM = 1'''
    cur.execute(sql1)

    if idx is None:                 # 테이플에 값이 없으면 오류나니까
        idx = 0
    else:
        idx = cur.fetchone()[1]

    intup = (idx + 1, tup[0], tup[1], tup[2], tup[3])

    sql = '''INSERT INTO membertbl 
                    (idx, names, levels, userid, password)
            VALUES (:1, :2, :3, :4, :5)'''

    cur.execute(sql, intup)
    cur.close()
    db.commit()
    db.close()
    print('성공')

#5
def setChangememberFromMembertbl(db, tup):
    cur = db.cursor()
    sql = '''UPDATE membertbl
            SET addr = :1
                , mobile = :2
                , email = :3
            WHERE idx = :4'''

    cur.execute(sql, tup)
    cur.close()
    db.commit()
    db.close()

#6
def delDiv(db, divi):
    cur = db.cursor()
    sql = '''DELETE FROM divtbl WHERE DIVISION = :1'''
    cur.execute(sql, (divi,))       # 데이터 1개일시 튜플엔 , 넣어줘야함
    db.commit()

if __name__ == "__main__":
    db = mydb()

    print("책 대여 프로그램")
    qqq = int(input('1. 장르 조회 \n2. 장르추가 \n3. 멤버 조회 \n4. 맴버추가 \n5. 맴버수정 \n6. 장르삭제 \n'))
    if qqq == 1:
        # 1. Divtbl 데이터 조회

        print("장르 조회")
        getAllDataFromDivtbl(db)
    
    elif qqq == 2:
        # 2. Divtbl 새로운 데이터 입력
        print("장르 정보 추가 입력")

        # div = input('구분 코드 입력 :')
        # div_name = input('장르명 입력 :')
        # tup = (div, div_name)

        # setDataIntoDivtbl(db, tup)
    elif qqq == 3:
        # 3. membertbl에서 데이터 조회
        print('데이터 조회')
        #getSomeDateFromMembertbl(db)

    elif qqq == 4:
        # 4. membertbl 새로운 데이터 입력
        print('신규회원 등록')
        # name = input('이름 입력 :')
        # level = input('레벨 입력 :')
        # userid = input('아이디 입력 : (최대 20자)')
        # password = input('비번입력 : (최대 20자)')

        # tup = (name, level, userid, password)

        # setNewMemberIntoMembertbl(db, tup)

        # cur = db.cursor()            # 여긴 idx값 확인용
        # sql1 = '''SELECT ROWNUM, idx
        #             FROM ( SELECT idx FROM membertbl
        #                 ORDER BY idx DESC) 
        #             WHERE ROWNUM = 1'''
        # cur.execute(sql1)
        # idx = cur.fetchone()[1]
        # print(idx)
        # cur.close()
    
    elif qqq == 5:
        # 5. membertbl 새로운 데이터 수정
        print('기존 회원 수정')
        idx = input("회원 번호 :")
        addr = input("주소 입력 :")
        mobile = input("전화 번호(- 포함) :")
        email = input("이메일 입력 :")

        tup = (addr, mobile, email, idx)

        setChangememberFromMembertbl(db, tup)
        print('회원수정 완료')

    elif qqq == 6:
        # 6. divtbl의 임의 데이터 삭제
        divi = input("삭제할 장르코드 입력 :")
        delDiv(db, divi)
        print('삭제 성공')
    else:
        print('찐빠')