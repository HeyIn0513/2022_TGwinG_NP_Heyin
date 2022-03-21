# 문제 1번
def sum(a,b):
    result_1 = a + b
    return result_1

# 문제 2번
def sub(a,b):
    result_2 = a - b
    return result_2

# 문제 3번
def mul(a,b):
    result_3 = a * b
    return result_3

# 문제 4번
def div(a,b):
    result_4 = a / b
    return result_4

# 문제 5번
def distance(x1,y1,x2,y2):
    a = (sub(x1, x2)**2) + (sub(y1, y2)**2)
    d = a**(1/2)
    return d

# 문제 6번
def short():
    lylic = "life is short art is long"
    return lylic[0:]

# 문제 7번
def myReverse(string):
    return string(::-1)

# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오. : ")
    hobby = input("취미를 입력하시오. : ")
    university = input("재학 중인 대학을 입력하시오. : ")
    birthday = input("생일을 입력하시오. /(단, yymmdd의 형태로/) : ")
    birthday_year = birthday[0:2]
    birthday_month = birthday[2:4]
    birthday_day = birthday[4:6]
    birthday_result = "{0}월 {1}일".format(birthday_month, birthday_day)
    result_8 = "제 이름은 {0}입니다.\n제 취미는 {1}이구요.\n저는 {2}를 다니고 있습니다.\n제 생일은 {3}입니다.".format(name, hobby, university, birthday_result)
    return result_8

# 문제 9번
def calcAI():
    a = input("첫 번째 숫자를 입력하시오 : ")
    b = input("두 번째 숫자를 입력하시오 : ")
    c = a + b
    result_9 = "두 수의 합은 {0}입니다.".format(c)
    return  result_9
