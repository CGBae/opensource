def get_terms(txt) :
    results = []
    terms = txt.split()
    for term in terms :
        results.append(term[:-1])

    return results

def get_termCount(terms) :
    tCnt = {}
    for term in terms :
        if not term in tCnt.keys() :
            tCnt[term] = 1
        else :
            tCnt[term] += 1

    tCnt = dict(sorted(tCnt.items()))
    return tCnt

def print_termCount(termCount) :
    print("\n")
    for key in termCount :
        print("'%s' -> %s번 등장했음. " % (key, termCount[key]))

txt = """ 오늘은 10월 26일 오픈소스프로그래밍의 시험을 본다.
         오늘도 날씨가 좋다. 나도 기분이 좋다. 나는 시험을 잘볼수있겠지.
         나는 어제도 오늘도 내일도 시험을 잘해내고있다. 나는 잘해내고있다. """

terms = get_terms(txt)
print("\n단어 리스트 : ", terms)

termCount = get_termCount(terms)

print_termCount(termCount)
