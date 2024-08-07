from datetime import datetime, timedelta
from random import shuffle
from Comunication import loadSpreadSheetData, writeResultData, sendFinalResultData

#아래의 리스트는 앞쪽에 있을 수록 퀄리티가 좋은 로프트의 리스트입니다.
loft = ["HDF LOFT1", "HDF LOFT2", "HDF LOFT3", "MS 1층 작업실", "MS 1층 회의실", "MS 2층 LOFT1", "MS 2층 LOFT3", "메이커스페이스 2층 회의실", "MS 2층 LOFT3"]

def filterTodayApplicants(list): #오늘 날짜에 로프트 배정을 신청한 팀들만 걸러주는 함수
    today = datetime.strptime("2024-06-20", "%Y-%m-%d") #오늘 날짜를 불러옵니다.
    current_year = datetime.now().year #현재 년도를 불러옵니다.
    date_format = "%m. %d" #날짜 형식을 지정합니다.

    filtered_list = [] #걸러낸 값을 저장할 리스트
    for value in list[1:]:
        date_obj = datetime.strptime(f"{current_year}. {value[1]}", f"%Y. {date_format}") #응답 리스트의 날짜 값을 형식에 맞게 변환합니다.
        if date_obj == today: #응답의 날짜가 현재 날짜인지 체크
            filtered_list.append(value) #오늘 날짜이면 리스트에 저장

    return filtered_list

def loftLottery(list): #리스트를 랜덤으로 섞고 로프트를 배정해주는 함수
    shuffle(list) #파이썬 내장 함수인 shuffle을 활용하여 리스트를 섞는다.
    for i in range(0, len(list)):
        list[i].append(loft[i]) #섞인 리스트를 맨 위부터 퀄리티가 좋은 로프트로 배정한다.
    return list

applicantsList = loadSpreadSheetData() #구글 폼 응답 리스트를 불러옵니다.
todayApplicantsList = filterTodayApplicants(applicantsList) #오늘 날짜인 응답만 걸러냅니다.
finalApplicantsList = loftLottery(todayApplicantsList) #로프트를 랜덤 배정합니다.

sendFinalResultData(finalApplicantsList)
writeResultData(finalApplicantsList, True) #최종 배정 결과를 개시합니다.