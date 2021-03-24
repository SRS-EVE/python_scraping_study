import requests#문서정보를 추출하는 라이브러리

#ctrl+/ = 선택한 코드 전부 주석처리

#res = requests.get("http://naver.com")
res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()#웹스크래핑중 문제 발생시 종료
print("응답코드 : ", res.status_code) #200이면 정상실행, 문제발생시 확인하는코드, 403=권한없음

# if res.status_code == requests.codes.ok:#requests.codes.ok 는 응답코드 200과 같은뜻
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mystudy.html", "w", encoding="utf-8") as f:
    f.write(res.text)#w는 읽기모드, mystudy.html 파일생성하는 코드
