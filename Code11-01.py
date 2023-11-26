import os
current_folder = os.path.dirname(os.path.abspath(__file__))

inFp = None
inStr = ""

inFp = open(current_folder + "/data1.txt", "r", encoding = 'utf-8')

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()