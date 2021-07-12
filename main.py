import os
import csv

#file_list = os.listdir("/Users/JYW/Desktop/order_file")
team_list = []

com_list = []
# 팀리스트 인자들을 하나씩 파일리스트에 넣어서 비교 대조 한 뒤 출력

def compare(part):
        for a in file_list:
                if part in a:
                        com_list.append({"부서명":part, "파일명":a})
                else:
                        continue

def make_csv():
        with open('결과파일.csv', 'w') as csvfile:
                fieldnames = ['부서명', '파일명']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for a in com_list:
                        writer.writerow(a)

os.system('cls')

input_dir = input("폴더 경로명을 입력해주세요. (폴더 주소창을 복사 후 붙여넣기)\n")
file_list = os.listdir((input_dir))

def input_part():
    init = input("\n\n부서명을 입력해주세요.\n이 단계를 건너뛰시려면 N을 입력해주세요\n")
    if init == "n" or init == 'N':
        for a in team_list:
            compare(a)
        make_csv()
    else:
        team_list.append(init)
        input_part()

input_part()
#make_csv()


#com_list = list(filter(None,com_list))
#com_list = list(set(com_list))
#print(com_list)

# 여기서 나온 com_list 는 파일명 -> 엑셀 뒷줄에 활용


'''
부서명을 앞뒤로 나눠서 비교한다음 부서명 가져오는 함수
해당 파일 명을 리턴하는 함수

두개를 합쳐서 dict형태 만들어준 다음 csv파일 생성 모듈
'''