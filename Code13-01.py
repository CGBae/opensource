import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

con = sqlite3.connect("C:\\sqlite-tools-win-x64-3440200\\naverDB")
cur = con.cursor()

while (True) :
    data1 = input("사용자ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    print("완성된 sql 확인용 출력>> ", sql)
    cur.execute(sql)

con.commit()
con.close()