Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ss = "파이썬최고"
ss[0]
'파'
ss[1:3]
'이썬'
ss[3:]
'최고'

= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code08-01.py
파$이$썬$짱$!$

= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code08-01-2.py
파$이$썬$짱$!$

= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규self_study_8-1.py
파#썬#완#재#있#요

= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code08-02.py
문자열을 입력하세요 : 즐거운 Python 프로그래밍~~~
내용을 거꾸로 출력 --> ~~~밍래그로프 nohtyP 운거즐
ss = 'Python is Easy. 그래서 programming이 재미있습니다. ^^'
ss.upper()
'PYTHON IS EASY. 그래서 PROGRAMMING이 재미있습니다. ^^'
ss
'Python is Easy. 그래서 programming이 재미있습니다. ^^'
ss.lower()
'python is easy. 그래서 programming이 재미있습니다. ^^'
ss
'Python is Easy. 그래서 programming이 재미있습니다. ^^'
ss.swapcase()
'pYTHON IS eASY. 그래서 PROGRAMMING이 재미있습니다. ^^'
ss.title
<built-in method title of str object at 0x000001FA6C6616B0>
ss.title()
'Python Is Easy. 그래서 Programming이 재미있습니다. ^^'
ss.capitalize()
'Python is easy. 그래서 programming이 재미있습니다. ^^'
ss
'Python is Easy. 그래서 programming이 재미있습니다. ^^'

= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code08-03.py
입력 문자열 ==> 파이썬 열공 중~~
출력 문자열 ==> (파이썬 열공 중~~)

= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규self_study_8-2.py
원래 문자열 ==> [<<<파<<이>>썬>>>]
공백 삭제 문자열 ==> [파이썬]
ss = '열심히 파이썬 공부 중~~'
ss.replace('파이썬', 'Python')
'열심히 Python 공부 중~~'
ss = 'Python을 열심히 공부 중'
ss.split()
['Python을', '열심히', '공부', '중']
ss = '하나:둘:셋'
>>> ss.split(':')
['하나', '둘', '셋']
>>> ss = '하나\n둘\n셋'
>>> ss.splitlines()
['하나', '둘', '셋']
>>> ss = '%'
>>> ss.join('파이썬')
'파%이%썬'
>>> 
= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code08-06.py
날짜(연/월/일) 입력 ==> 2019/12/31
입력한 날짜의 10년 후 ==> 2029년12월31일
>>> before = ['2019', '12', '31']
>>> after = list(map(int, before))
>>> after
[2019, 12, 31]
>>> 
= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code08-07.py
>>> 
= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규code09-04.py
100과 200의 plus() 함수 결과는 300
>>> 
= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규self_study_9-2.py
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /, **) : /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다. ㅠㅠ
계산불가
>>> 
= RESTART: C:\Users\cheol\OneDrive\바탕 화면\오픈소스프로그래밍\1012\1012_2020301035_배철규self_study_9-2.py
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /, **) : /
두 번째 수를 입력하세요 : 2
## 계산기 : 34 / 2 = 17
