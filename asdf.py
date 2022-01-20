from flask import Flask, render_template, request, session, redirect
import requests
import sys
import time
import os
import pymysql
from PIL import Image as PILImage
# from gensim.summarization.summarizer import summarize
# 질문할거 회원가입 배경 안바뀜, 회원가입할때 이미지 받아오기(까먹음)
upload_url="/workspace/flask/static/upload/"
# http://jason-heo.github.io/mysql/2014/03/05/find-prev-next.html 이전 이후 게시물 찾기
application = Flask(__name__)
application.config['SECRET_KEY'] = 'apptools'



@application.route("/test", methods=['GET', 'POST'])
def test():
    session['ss_ss'] = get_html('https://namu.wiki/w/Hollow%20Knight?from=%ED%95%A0%EB%A1%9C%EC%9A%B0%EB%82%98%EC%9D%B4%ED%8A%B8')
    return render_template('test.html')
    
# 회원가입
@application.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "GET": 
        return render_template('signup.html')
    else:
        # imgfile = request.files['img1']    # 나중에 물어보기 질문
        userid = request.form['userid']
        userpw = request.form['userpw']
        username = request.form['name']
        userhp = request.form['hp']
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = """insert into member set
        userid = '%s',
        userpw = password('%s'),
        name = '%s',
        level = '2',
        hp = '%s',
        img = 'img.jpg'; """ % (userid, userpw, username, userhp)
        cursor.execute(sql)
        db.commit()
        db.close
        return render_template('userlogin.html')

# 유저 로그인
@application.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == "GET":
        return render_template('userlogin.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = "select name, level, img from member where userid = '%s' and userpw = password('%s')" % (userid, userpw)
        cursor.execute(sql)
        rows = cursor.fetchone()
        db.close

        if rows:
            session['ss_id'] = userid;
            session['ss_name'] = rows[0];
            session['ss_level'] = rows[1];
            session['ss_img'] = rows[2];
            return redirect('/')
        else:
            return render_template('userlogin.html', msg='아이디 또는 비밀번호를 잘못 입력하셨습니다.')
        
# 메인 페이지
@application.route("/", methods=['GET'])
def index():
    category = request.args.get("category")
    sql2 = ""
    if category:
        sql2 = " where category = '%s'" % category
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = "select num, img2, category, subject, price from product %s limit 0,20;" % sql2
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close
    return render_template("index.html", rows=rows)

# 관리자 페이지
@application.route('/admin/main')
def admin_main():
    if session['ss_id'] == False:
        return redirect('/admin')
    else:
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = "select num, subject, img3, price from product order by num desc"
        cursor.execute(sql)
        rows = cursor.fetchall()
        member = {
            "ss_name":session['ss_name'],
            "ss_level":session['ss_level'],
            "ss_img":session['ss_img']
        }
        return render_template('/admin/main.html', member=member, rows=rows)

# 관리자 로그인 페이지(스킵함 이젠)
@application.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == "GET":
        return render_template('admin/login.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = "select name, level, img from member where userid = '%s' and userpw = password('%s')" % (userid, userpw)
        cursor.execute(sql)
        rows = cursor.fetchone()
        db.close

        if rows and rows[1] == 10:
            session['ss_id'] = userid;
            session['ss_name'] = rows[0];
            session['ss_level'] = rows[1];
            session['ss_img'] = rows[2];
            return redirect('/admin/main')
        else:
            return render_template('/admin/login.html', msg='아디비번 확인 및 권한 없음.')

# 로그아웃 공용으로 씀
@application.route('/admin/logout')
def admin_logout():
    session['ss_id'] = False
    session['ss_name'] = False
    session['ss_level'] = False
    session['ss_img'] = False
    return redirect('/')

# 관리자 게시물 리스트
@application.route('/admin/news')
def admin_main_news():
    if session['ss_id']==False:
        return redirect('/admin')
    
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = "select num, category, img1, subject, price from product order by num desc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close
    return render_template('/admin/news/list.html', rows=rows)

# 사용자 게시물 리스트
@application.route('/talk')
def user_talk():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = "select num, subject, name, indate from talk order by num desc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close
    return render_template('talk.html', rows=rows)

# 관리자 맴버 보기
@application.route('/admin/mem')
def admin_main_mem():
    if session['ss_id']==False:
        return redirect('/admin')
    
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = "select num, userid, name, level, hp from member order by num desc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close
    return render_template('/admin/news/mem.html', rows=rows)



# 관리자 게시물 작성 페이지
@application.route('/admin/news/write', methods=['GET','POST'])
def admin_news_write():
    if request.method == "GET":
        return render_template('/admin/news/write.html')
    else:
        sql2 = ""
        f = request.files['img1']
        category = request.form['category']
        subject = request.form['subject'].replace("'","\\'").replace('"','\\"')
        content = request.form['content'].replace("'","\\'").replace('"','\\"')
        #comment = summarize(content, ratio=0.1)
        comment = ""
        price = request.form['price']
        indate = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
        nowtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        if f:
            fname, ext = os.path.splitext(f.filename)
            file1 = nowtime + ext
            # 뻐꾸기.jpg -> 20210512130203.jpg
            f.save(upload_url + file1) #원본 이미지
            
            #썸네일이미지 (큰사이즈)
            img1 = nowtime + "_1" + ext
            with PILImage.open(upload_url + file1) as im:
                im.thumbnail((1200,625))
                im.save(upload_url + img1)
                
            #썸네일이미지 (중간사이즈)
            img2 = nowtime + "_2" + ext
            with PILImage.open(upload_url + file1) as im:
                im.thumbnail((600,409))
                im.save(upload_url + img2)
                
            #썸네일이미지 (작은사이즈)
            img3 = nowtime + "_3" + ext
            with PILImage.open(upload_url + file1) as im:
                im.thumbnail((120,90))
                im.save(upload_url + img3)
                
            #원본 이미지 삭제
            os.remove(upload_url + file1)
            
            sql2 = ", img1='%s', img2='%s', img3='%s'" % (img1,img2,img3)
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = """insert into product set 
            category = '%s',
            subject = '%s',
            content = '%s',
            price = '%s',
            name = '%s',
            userid = '%s',
            indate = '%s',
            comment = '%s' """ % (category, subject, content, price, session['ss_name'],session['ss_id'],indate, comment)
        sql = sql + sql2 + ";"
        cursor.execute(sql)
        db.commit()
        db.close
        return redirect('/admin/news')
        #return sql

# 관리자 게시물 수정
@application.route('/admin/news/edit', methods=['GET','POST'])
def admin_news_edit():
    if request.method == "GET":
        num = request.args.get("num")
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = """select num, category, subject, content, img1, price from product where num = %s;""" % (num)
        cursor.execute(sql)
        rows = cursor.fetchone()
        db.close
        member = {"name":session['ss_name'], 
                  "level":session['ss_level']}
        return render_template('/admin/news/edit.html', member=member, 
                              rows=rows)
    else:
        sql2 = ""
        f = request.files['img1']
        num = request.form['num']
        category = request.form['category']
        subject = request.form['subject'].replace("'","\\'").replace('"','\\"')
        content = request.form['content'].replace("'","\\'").replace('"','\\"')
        price = request.form['price']
        nowtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))        
        if f:
            #원래는 기존 파일을 삭제 하도록 기능 추가
            
            fname, ext = os.path.splitext(f.filename)
            file1 = nowtime + ext
            # 뻐꾸기.jpg -> 20210512130203.jpg
            f.save(upload_url + file1) #원본 이미지
            
            #썸네일이미지 (큰사이즈)
            img1 = nowtime + "_1" + ext
            with PILImage.open(upload_url + file1) as im:
                im.thumbnail((1200,625))
                im.save(upload_url + img1)
                
            #썸네일이미지 (중간사이즈)
            img2 = nowtime + "_2" + ext
            with PILImage.open(upload_url + file1) as im:
                im.thumbnail((600,409))
                im.save(upload_url + img2)
                
            #썸네일이미지 (작은사이즈)
            img3 = nowtime + "_3" + ext
            with PILImage.open(upload_url + file1) as im:
                im.thumbnail((120,90))
                im.save(upload_url + img3)
                
            #원본 이미지 삭제
            os.remove(upload_url + file1)
            
            sql2 = ", img1='%s', img2='%s', img3='%s'" % (img1,img2,img3)
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='test',
            passwd='1234',
            db='test',
            charset='utf8'
        )
        cursor = db.cursor()
        sql = """update product set
        category='%s',
        subject='%s',
        content='%s',
        price='%s' """ % (category, subject, content, price)
        sql = sql + sql2 + " where num = '%s';" % num
        cursor.execute(sql)
        db.commit()
        db.close
        return redirect('/admin/news')
        #return sql        

# 제품 페이지
@application.route("/portfolio_detail", methods=['GET'])
def index_detail():
    num = request.args.get("num")
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = """select num, category, subject,
    indate, img1, content, name, price, comment from product 
    where num = %s;""" % (num)
    cursor.execute(sql)
    rows = cursor.fetchone()
    db.close
    member = {"name":session['ss_name'], 
              "level":session['ss_level']}
    return render_template('/portfolio_detail.html', member=member, rows=rows)

# 사용자 글 보기
@application.route('/talkview', methods=['GET','POST'])
def admin_talk_view():
    num = request.args.get("num")
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = """select num, subject,
    indate, content, name from talk
    where num = %s;""" % (num)
    cursor.execute(sql)
    rows = cursor.fetchone()
    db.close
    member = {"name":session['ss_name'], 
              "level":session['ss_level']}
    return render_template('/talkview.html', member=member, rows=rows)

# 관리자 제품 보기
@application.route('/admin/news/view', methods=['GET','POST'])
def admin_news_view():
    if session['ss_id'] == False:
        return redirect('/admin')
    
    num = request.args.get("num")
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = """select num, category, subject,
    indate, img1, content, name, price, comment from product 
    where num = %s;""" % (num)
    cursor.execute(sql)
    rows = cursor.fetchone()
    db.close
    member = {"name":session['ss_name'], 
              "level":session['ss_level']}
    return render_template('/admin/news/view.html', member=member, rows=rows)

# 관리자 제품 삭제
@application.route('/admin/news/delete', methods=['GET','POST'])
def admin_news_delete():
    num = request.args.get("num")
    #파일삭제
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='test',
        passwd='1234',
        db='test',
        charset='utf8'
    )    
    cursor = db.cursor()
    #첨부파일 삭제 우선 처리
    sql = "select img1, img2, img3 from product where num = %s;" % (num)
    cursor.execute(sql)
    rows = cursor.fetchone()
    if rows[0] and os.path.exists(upload_url + rows[0]):
        os.remove(upload_url + rows[0])
    if rows[1] and os.path.exists(upload_url + rows[1]):
        os.remove(upload_url + rows[1])
    if rows[2] and os.path.exists(upload_url + rows[2]):
        os.remove(upload_url + rows[2])
        
    #DB삭제
    sql = "delete from product where num = %s;" % (num)
    cursor.execute(sql)
    db.commit()
    db.close()
    return redirect('/admin/news')



        
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
