# 클래스 / 함수 / 파일 입출력 / 


class Unit: # 클래스 생성
    def __init__(self, name, hp, damage):
        self.name = name        # 초기화
        self.hp = hp            # 초기화
        self.damage = damage    # 초기화
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격 {1}'.format(self.hp, self.damage))

marine1 = Unit('마린', '40', '5')
marine2 = Unit('마린', '40', '5')
marine3 = Unit('마린', '40', '5')


# 레이스 = 공중 유닛, 비행기,  클로킹
wraith1 = Unit('레이스', '80', '10')
print('유닛 이름 : {0}, 공격력 : {1}.format(wraith1.name, wraith1.damage')

# 마인드 컨트롤 된 레이스
wraith2 = Unit('빼앗은 레이스', 80, 10)
wraith2.clocking = True
if wraith2.clocking == True:
    print('{0} 유닛은 현재 클로킹 상태입니다.'.format(wraith2.name))



# 공격 유닛 클래스
class AttackUnit: # 클래스 생성
    def __init__(self, name, hp, damage):
        self.name = name        # 초기화
        self.hp = hp            # 초기화
        self.damage = damage    # 초기화
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입업습니다.'.format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))
            
# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃', 50, 15)
firebat1.attack('5시')


# 공격 2번 받았다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 공중 유닛 클래스
# 드랍쉽 : 수송기 역할

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))
            
dropship1 = Flyable(100)

# 공중 공격 유닛 클래스 / 상속(단일 / 다중)

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print('[공중 공격 유닛 이동]')
        self.fly(self.name, location)
        
# 발키리 : 공중 공격 유닛, 한번에 14개의 미사일 발사
valkyrie1 = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie1.fly(valkyrie1.name, '3시')

















