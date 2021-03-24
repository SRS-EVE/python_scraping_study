import requests
import re
from bs4 import BeautifulSoup #스크래핑을 하기 위한 패키지

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    #유저 에이전트 값

for i in range(1, 6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_wow%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=36&rocketAll=true".format(i)
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    # print(res.text)
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:

        #광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("<광고상품제외>")
            continue
        name = item.find("div", attrs={"class":"name"}).get_text()
        
        #애플 제품 제외
        if "Apple" in name:
            print("Apple 상품 제외")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()#가격
        
        #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회

        rate = item.find("em", attrs={"class":"rating"})#평점
        if rate:
            rate = rate.get_text()
        else:
            print("평점이 없는 상품 제외")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})#평점개수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            print("평점 수 없는 상품 제외")
            continue

        if float(rate) >= 4.5 and int(rate_cnt) >= 50:
            print(name, price, rate, rate_cnt)
        