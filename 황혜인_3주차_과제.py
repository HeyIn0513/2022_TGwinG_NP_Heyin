# 문제 1번
def question1():
    정답문자열 = "nextSuwon city"
    return 정답문자열


# 문제 2번
def leapYear(year):
    if (year%4==0 and year%100!=0):
        return "윤년입니다."
    elif (year%4==0 and year%400!=0):
        return "윤년입니다."
    else :
        return "윤년이 아닙니다."


# 문제 3번
def alram(time):
    time = str(time)
    if (len(time)==3):
        a = int(time[:1])
        b = int(time[1:])
        if (b>=45): 
            A_wakeup_h = str(a)
            A_wakeup_m = str(b-45)
            A_wakeup_time = "오전 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time
        elif (b<45):
            A_wakeup_h = str(a-1)
            A_wakeup_m = str(60+(b-45))
            A_wakeup_time = "오전 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time

    elif (len(time)==4):
        a = int(time[:2])
        b = int(time[2:])
        if (a<=12 and b<45):
            A_wakeup_h = str(a-1)
            A_wakeup_m = str(60+(b-45))
            A_wakeup_time = "오전 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time
        elif (a<=12 and b>=45):
            A_wakeup_h = str(a)
            A_wakeup_m = str(b-45)
            A_wakeup_time = "오전 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time

        elif (a==13 and b<45):
            A_wakeup_h = str(12)
            A_wakeup_m = str(60+(b-45))
            A_wakeup_time = "오전 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time
        elif (a==13 and b>=45):
            A_wakeup_h = str(1)
            A_wakeup_m = str(b-45)
            A_wakeup_time = "오후 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time

        elif (a>13 and b<45):
            A_wakeup_h = str(a-13)
            A_wakeup_m = str(60+(b-45))
            A_wakeup_time = "오후 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time
        elif (a>13 and b>=45):
            A_wakeup_h = str(a-12)
            A_wakeup_m = str(b-45)
            A_wakeup_time = "오후 " + A_wakeup_h + "시 " + A_wakeup_m + "분"
            return A_wakeup_time


# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    x1 = int(x1)
    x2 = int(x2)
    r1 = int(r1)
    y1 = int(y1)
    y2 = int(y2)
    r2 = int(r2)
    a = ((x1-x2)**2 + (y1-y2)**2)**0.5 
    b = r1+r2
    if (a>b):
        number = 0
        return number
    elif (a==b):
        number = 1
        return number
    elif (a<r1 or a<r2):
        if (a!=0):
            number = 2
            return number
        else :
            number = 0
            return number
    elif (a+r1==r2 or a+r2==r1):
        number = 1
        return number
    elif (a==0 and r1!=r2):
        number = "어딘지 모르겠다 오바"
        return number
