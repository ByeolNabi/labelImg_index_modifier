import os

def changer(str, sample, target, os):
    if str[0]==sample:
        os.write(target+str[1:])

# 이미지와 라벨파일이 한 곳에 있다는 가정하에 파일의 경로
dir_path = r'C:\Users\AI27\Desktop\program\txtEDITtest\images'

for i in os.walk(dir_path):
    path = i[0]+'\\'
    files = i[2]

    # 파일 가져오기
    for file in files:
        # txt파일만 가져오기
        if '.txt' in file:
            # 파일 내용 가져오기
            with open(path+file, 'r',encoding = 'UTF8') as f:
                lines = f.readlines()

            # 파일 내용 수정하기
            with open(path+file, 'w', encoding='utf-8') as f:
                for line in lines:
                    changer(line, '0','15',f)
                    changer(line, '1','14',f)
                    changer(line, '2','16',f)
                    changer(line, '3','17',f)
                    changer(line, '4','13',f)
                    changer(line, '6','12',f)
                    changer(line, '7','19',f)

