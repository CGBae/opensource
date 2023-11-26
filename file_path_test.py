import os

abspathTest = os.path.dirname(os.path.abspath(__file__))
print("os.path.dirname(os.path.abspath(__file__))로 구한 절대경로->>", abspathTest)

relpathTest = os.getcwd()
print("os.getcwd()로 구한 현재 폴더 경로->>", relpathTest)

print("현재파일의 VS Code [경로복사] ->> C:\\Users\\skuniv\\Documents\\My_Python_VS_1123\\file_path_test.py")
print("현재파일의 VS Code [상대경로복사]->> file_path_test.py")