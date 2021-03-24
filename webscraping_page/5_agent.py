import requests#문서정보를 추출하는 라이브러리

url = "http://nadocoding.tistory.com"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
#유저 에이전트 값

#ctrl+/ = 선택한 코드 전부 주석처리
#구글에 user agent string 검색 후 https://www.whatismybrowser.com/detect/what-is-my-user-agent진입

#res = requests.get("http://naver.com")
res = requests.get(url, headers=headers)#headers 는 페이지에 접속할때 유저 에이전트값을 넘겨줌
res.raise_for_status()#웹스크래핑중 문제 발생시 종료

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)#w는 읽기모드, nadocoding.html 파일생성하는 코드
