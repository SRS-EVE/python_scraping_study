#정규식
import re#정규식 라이브러리

p = re.compile("ca.e")#p는패턴, 어떤 정규식을 컴파일 할것인지 결정
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case o | caffe x
# ^ (^de)  : 문자열의 시작 > desk, destination o | fade x
# $ (se%)  : 문자열의 끝 > case, base o | face x

def print_match(m):
    if m:
        print("m.group():", m.group())#일치하는 문자열 반환
        print("m.string:", m.string)#입력받은 문자열
        print("m.start():", m.start())#일치하는 문자열의 시작 index
        print("m.end():", m.end())#일치하는 문자열의 끝 index
        print("m.span():", m.span())#일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")

m = p.match("good care")#p와 매칭하는 함수, 주어진 문자열의 처음부터 일치하는지 확인하므로 오류발생 
print_match(m)

#정규식 기본2

m2 = p.search("good care")# search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m2)

lst = p.findall("careless")# findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환