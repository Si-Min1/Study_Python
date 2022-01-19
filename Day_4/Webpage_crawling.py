# 웹페이지 크롤링
# from urllib.request import Request, urlopen

# req = Request('https://www.naver.com')
# res = urlopen(req)

# print(res.status)




# 외부 리퀘스트 패키지 추가 설지 requests
import requests
url = 'https://www.naver.com'
res = requests.get(url)



# print(res.status_code)

print(res.text)






























