import os
import csv

#file_list = os.listdir("/Users/JYW/Desktop/order_file")
team_list = []

handed_team = []

not_handed_team = []

file_list = os.listdir()
# 팀리스트 인자들을 하나씩 파일리스트에 넣어서 비교 대조 한 뒤 출력
def get_team_name():
        with open ("team_name.csv") as team_name:
                csv_data = csv.reader(team_name)
                for row in csv_data:
                        value = row[0]
                        team_list.append(value)


def compare():
        for team in team_list:
                for file in file_list:
                        if team in file:
                                handed_team.append(team)
                        else:
                                continue

def make_not_haded_team():
        for team in team_list:
                if team not in handed_team:
                        not_handed_team.append({'부서명':team})
                

def make_csv():
        with open('결과파일.csv', 'w') as csvfile:
                fieldnames = ['부서명']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for a in not_handed_team:
                        writer.writerow(a)

get_team_name()
compare()
make_not_haded_team()
make_csv()
print(team_list)
print(handed_team)
print(not_handed_team)

'''

# 여기서 나온 handed_team 는 파일명 -> 엑셀 뒷줄에 활용

'''
'''
v.2
디렉토리 위치는 현재 실행파일 있는 곳 얻어오기
부서명 직접 입력하지않고 CSV파일에서 직접 가져와서 리스트에 추가.

v.1
부서명을 앞뒤로 나눠서 비교한다음 부서명 가져오는 함수
해당 파일 명을 리턴하는 함수

두개를 합쳐서 dict형태 만들어준 다음 csv파일 생성 모듈
'''