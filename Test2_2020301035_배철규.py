score = {}

print("입력할 학생이 몇명입니까? ")
n = int(input())

for i in range(n)
    name = input("이름 입력 : ")
    scr = int(input("점수 입력 : "))
    score.append(name, scr)

get_name_score(score, n) :
    name = input("이름 입력 : ")
    score = input("점수 입력 : ")

    avg = get_avg(score)
    maxScore, name = get_max(score)

print("score : %s" % score)
print("평균점수 = %f" % avg)
print("최고점수 = %s : %d점" % name, score)
    
