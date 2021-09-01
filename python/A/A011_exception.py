# 예외처리
class Bignumbererror(Exception):    
    def __inint__(self, msg):
        self.msg = msg
   
    def __str__(self):
        return self.msg


try:        # 예외처리 시작
    print('한자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫번째 숫자를 입력하세요'))
    num2 = int(input('첫번째 숫자를 입력하세요'))
    if num1 >= 10 or num2 >=10:       # 예외가 될 조건
        raise Bignumbererror('입력값 : {0}, {1}'.format(num1, num2))    # raise로 예외 지정 및 예외시 출력값
    print('{0} / {1} = {2}'.format(num1, num2, float(num1 / num2)))     # 정상일 경우 출력값
    
except ValueError:      # 숫자외의 값이 입력될 경우
    print('에러! 잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요.')
except Bignumbererror:      # 사용자 정의 예외처리 1자리 숫자가 아닐경우
    print('값이 정확하지 않음.')
except ZeroDivisionError as err:    # 0으로 나누기가 실행될 경우
    print('0으로 나누기 금지! 0을 제외한 한자리 숫자를 입력하세요.')
except Exception:       # 그 외에 예외상황 발생시
    print('알수 없는 에러가 발생하였습니다')
finally:        # 예외처리 끝
    print("끝")




# 동네에 맛있는 치킨집이 있다.
# 대기 손님을 위해 자동 주문 시스템을 제작하였다.
# 시스템 코드를 확인하고 적절하게 예외처리 구문을 넣어보자.

# 조건 1
# 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
# 메세지 "잘못된 값을 입력하였습니다."
# 조건 2
# 총 치킨량이 10마리로 한정
# 치킨 소진 시 사용자 정의 에러[Soldouterror]를 발생시키고 프로그램 종료
# 메시지 "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):
    pass

chicken = 10    # 남은 치킨의 수
waiting = 1     # 매장 안에는 만석, 대기번호는 1번부터 시작


while(True):
    try:
        print("[남은 치킨] : {0}".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까? : "))
        if order > chicken:     # 남은 치킨보다 주문량이 많을 경우
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1        # 정상처리시 대기번호증가
            chicken -= order    # 정상처리시 치킨 감소

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        print("프로그램을 종료합니다.")
        break
        





