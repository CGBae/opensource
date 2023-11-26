outFp = None
outStr = ""

outFp = open("C:\\Uㅇsers\\skuniv\\Documents\\My_Python_VS_1123\\data2.txt", "w", encoding = 'utf-8')

while True :
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break

outFp.close()
print("--- 파일에 정상적으로 써졌음 ---")