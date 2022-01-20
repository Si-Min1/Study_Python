# 오라클 접속   설치 pip install cx_oracle (파이썬 버전 확인 후 사용)
import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', 1521, service_name='orcl') # 접속주소
                                                        # 그냥 위에꺼 적어도 무방할듯? 아님 랄로
db = cx_Oracle.connect(user ='scott ', password = 'tiger', dsn = dsn, encoding = 'UTF-8')

cur = db.cursor()

try:
    # for row in cur.execute('SELECT * FROM emp'):
    #     print(row)

    sql = '''SELECT * FROM emp WHERE deptno = 30'''
    cur.execute(sql)
    rows = cur.fetchone()
    print(rows)

# cur.execute('SELECT * FROM emp')
# rows = cur.fetchone()


except cx_Oracle.DatabaseError as e:
    print(f'쿼리문 확인 요망 {e}')


finally:
    cur.close()
    db.close()

















