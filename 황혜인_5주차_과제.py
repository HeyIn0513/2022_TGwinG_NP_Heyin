# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점

from turtle import end_fill


def calcCircleArea(r):
    import math
    calcircle = math.pi*r**2
    result = round(calcircle,2)
    return result

def calcLog(a, b):
    result = float()
    import math
    if type(a) is str:
        calog = math.log(b)
        result = round(calog,2)
    elif type(a) is int:
        calog = math.log(a,b)
        result = round(calog,2)
    return result

def calcSin(x):
    result = float()
    import math
    calsin = math.sin(x)
    result = round(calsin, 2)
    return result

def calcFactorial(x):
    result = int()
    import math
    fac = math.factorial(x)
    result = fac
    return result

def calcCombination(n, r):
    result = int()
    import math
    com = math.comb(int(n), int(r))
    result = com
    return result

def calculator(order):
    answer = 0

    a_list = []
    for i in order:
        a_list.append(i)

    if  '원넓이' in order:
        answer = calcCircleArea(int(order[5:]))

    elif '로그' in order:
        list_1 = order[4:]
        list_2 = list_1.split()
        a = list_2[0]
        b = int(list_2[1])
        answer = calcLog(a,b)

    elif '사인' in order:
        answer = calcSin(int(order[4:]))

    elif '팩토리얼' in order:
        answer = calcFactorial(int(order[6:]))

    elif '조합' in order:
        list_3 = order[4:]
        list_4 = list_3.split()
        a = list_4[0]
        b = list_4[1]
        answer = calcCombination(a,b)

    return answer