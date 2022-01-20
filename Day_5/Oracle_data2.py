# 커서 접근 코드 함수 작성
import cx_Oracle as ora


def mydb():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    db = ora.connect(user='scott ', password='tiger',
                     dsn=dsn, encoding='UTF-8')
    return db


def getAllDate(db): # mydb()의 db값을 파라미터로 받아서 쿼리 스킵
    cur = db.cursor() # 커서 생성
    sql = '''SELECT * FROM emp''' # 쿼리 생성

    for row in cur.execute(sql): # 쿼리문 실행후 데이터 값 1줄씩 끝까지 가져옴
        print(row)               # 1줄 가져온거 출력하고 반복

    cur.close()
    db.close()


def getNameAndJobData(db):    
    cur = db.cursor() # 커서 생성
    sql = '''SELECT ename, fob FROM emp''' # 쿼리 생성

    cur.execute(sql)

    while True:
        row = cur.fetchone()
        if row is None:
            break
        else:
            print(row)
    

def Show_DB_List(db):
    cur = db.cursor()
    sql = '''SELECT * FROM emp'''
    for row in cur.execute(sql):
        print(row)
    cur.close()
    db.close()


def Find(db):
    cur = db.cursor()
    
    num = int(input('지역 번호를 입력하시오. (10,20,30) :'))

    sql = '''SELECT * FROM emp WHERE deptno = %s''' % (num) # 보안상의 문제로 아래의 함수 getDepName에서 쓰는 방식을 추천함
    cur.execute(sql)


    # sql = f'SELECT * FROM emp WHERE deptno = {num}'
    # cur.execute(sql)

    rows = cur.fetchall()
    
    print(rows)
    cur.close()
    db.close()


def getDepName(db, tup):
    cur = db.cursor()

    sql = "SELECT * FROM dept WHERE deptno = :1 AND loc =:2"
    cur.execute(sql,tup)

    # sql = f'SELECT * FROM dept WHERE deptno = {tup[0]} AND loc =\'{tup[1]}\''
    # cur.execute(sql)   
    
    row = cur.fetchone()

    print(row)
    cur.close()
    db.close()

    return 0

if __name__ == "__main__":
    print('프로그램 시작')
    db = mydb()
    # Show_DB_List(db)
    Find(db)

    # no = int(input('1, 부서번호 입력:'))
    # loc = input('2, 지역명 입력:')
    # tup = (no,loc.upper())
    # getDepName(db, tup)


    
