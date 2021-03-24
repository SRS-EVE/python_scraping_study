import requests
from bs4 import BeautifulSoup #스크래핑을 하기 위한 패키지

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")#lxml 모듈을 사용해 html파일을 soup객체로만듬
print(soup.title)
print(soup.title.get_text())#타이틀 밑의 텍스트를 가져옴
print(soup.a)# soup 객체에서 처음발견되는 a태그 정보출력
print(soup.a.attrs)# a element가 가지는 속성정보를 출력
print(soup.a["href"])# a element가 href 속성'값' 정보를 출력

print(soup.find("a", attrs={"class": "Nbtn_upload"}))#a태그에서 첫번째 element값을 가져옴
#print(soup.find(attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element를 찾음

#print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.a.get_text())#a태그의 텍스트만 가져옴
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)

# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")#li 조건에 해당하는 다음항목만 찾음
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))#rank1을 기준으로 li태그들을 전부가져옴

webtoon = soup.find("a", text="바른연애 길잡이-142")
print(webtoon)