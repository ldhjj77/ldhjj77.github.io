

def tr():
    tree = 0
    while tree < 10:   
        tree = tree + 2
        print("나무를 %d번 찍었습니다." % tree)
        if tree == 10:
            print("나무가 넘어갑니다")



def coff():
    coffee = 10
    money = 300
    while money:
        print("돈을 받았으니 커피를 줄께")
        coffee = coffee - 1
        print("남은 커피의 양은 %d 개입니다." % coffee)
        if coffee ==0:
            print("남은 커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break 
        
 
def coff1():
    coffee = 10
    while True:
        money = int(input("돈을 넣어 주세요 : "))
        if money == 300:
            print("커피를 줍니다.")
            coffee = coffee - 1
        elif money > 300:
            print("거스름돈 %d 를 주고 커피를 줍니다." % (money - 300))
            coffee = coffee - 1
        else:
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
            print("남은 커피의 양은 %d개 입니다." % coffee)
        if coffee == 0:
            print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
            break
        


def mark():
    marks = [90, 85, 25, 67, 80]
    number = 0
    for mark in marks:
        number = number + 1
        if mark >= 60:
            print('%d번 학생은 합격 입니다.' % number)
        else:
            print('%d번 학생은 불합격 입니다.'% number)


def mark1():
    marks = [90, 85, 25, 67, 80]
    for number in range(len(marks)):
        if marks[number] < 60:
            continue
        print('%d번 학생은 합격입니다.' %(number+1))


def gugu(): 
    for gugu in range(2, 10):
        for gugugu in range(1, 10):
            print('{0} * {1} = {2}'.format(gugu, gugugu, gugu*gugugu))
       
        
        
 
# while 문을 사용하여 1 ~ 1000 자연수 중 3의 배수의 합을 구하라
def sum3():
    sum = 0
    upcount = 1
    while upcount <= 1000:
        upcount += 1
        if upcount % 3 == 0:
            sum += upcount
    print(sum)
        
    

 
 
 
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100] for문을 사용한 평균점수

def aver():
    a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total = 0
    for score in a:
        total += score
    average = total / len(a)
    print(average)
 



  




if __name__ == '__main__':  # scrape_weather()라는 함수가 같은파일(A020_project.py)안에 있다면 실행하게
    # tr()
    # coff()
    # coff1()
    # mark()
    # mark1()
    # gugu()
    # sum3()
    aver()
    
    
    
    
    
    
    
    
    



