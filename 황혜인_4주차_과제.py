# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점
from re import A


# 1번 문제 반환값 없는 문제랑 2,4번 문제 풀이는 진우 선배가 도와주셨습니다!!


print("Hello")
# 문제 1번
def intervention(queue):
    answer = list() # 요기는 원래 적혀있던 부분
    queue_1 = list(queue[:4]) # 앞 5명의 얼굴을 기억한다고 했으니, 앞 5명의 새로운 리스트
    if '성은' in queue: # 만약 성은이 줄에 존재한다면
        if '성은' in queue_1:
            queue.append('승호')
            answer = queue
        elif '성은' not in queue_1:
            queue.insert(int(queue.index('성은'))+1,'승호')
            answer = queue
    elif '성은' not in queue:
        queue.append('승호')
        answer = queue

    return answer





# 문제 2번
def pascal(n):
    answer = list()
    pas_list = []
    for i in range(n):
        pas_list.append([])
        pas_list[i].append(1)

        for j in range(1, i):
            pas_list[i].append(pas_list[i-1][j-1] + pas_list[i-1][j])

        if n != 0 and len(pas_list) != 1:
            pas_list[i].append(1)

    answer = pas_list[n-1]   
    return answer





# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()

    entry_1 = str(entry)
    new_searchWords = []
    for i in searchWords:
        if entry_1 in i:
            new_searchWords.append(i)

    new_searchWords.sort() # 뭐 대입할때마다 반환값 있는지 없는지 확인
    answer = new_searchWords

    return answer


# 문제 4번
def stock_price(stockChart):
    answer = str() #원래 있던 함수
    stockChart_new = [] # 빈 리스트 _new 하나 만들고
    for i in stockChart: # 수첩에 적은 숫자들을 int 값으로 변환해서 _new 함수에 넣음
        stockChart_new.append(int(i))
    
    sum_list = sum(stockChart_new) #new 함수의 요소들을 싹 다 더한 int 값을 sum_list로 지정
    index_min = 0 #가장 최저값일때의 인덱스값

    if sum_list>0: # new 함수들의 요소를 싹 더한 값이 0보다 크다면 뭔가 주가가 올랐다는거니까
        for j in range(len(stockChart_new)):
            a += stockChart_new[j] #a에다가 하나씩 더해서 저장함
            
            if  stockChart_new_min >= a: #최저값보다 a가 작다면
                stockChart_new_min = a #그때의 a가 새로운 최저값이 되고
                index_min = j #최저값의 인덱스를 저장해놓음
        answer = "%d일 전에 샀어야지 으이구" %(len(stockChart_new) - index_min - 1) 

    else : # 만약 sum함수의 값이 0이거나 0보다 작으면 주가가 올랐던 적이 없는거니까
        answer = "아니야 조금만 더 기다려" #얘를 출력한다
    
    return answer



# 문제 5번
def decryption(letter):
    answer = str()
    list_A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list_B = []
    for i in letter:
        if list_A in letter:
            A = (int(list_A.index(i))+3)%26
            list_B.append(list_A[A])
        elif list_A not in letter:
            list_B.append(i)
    answer = list_B

    return answer
