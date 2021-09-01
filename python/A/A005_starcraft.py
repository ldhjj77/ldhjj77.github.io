from random import *

 # 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # 출력문 추가

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage): # AttackUnit 에서 Unit 으로 이동
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    siege_developed = False # 시즈모드 개발여부 (클래스 변수)

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)

    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return

        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시즈 모드 해제

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)

    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True 
    
    
def game_start():
        print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장했습니다.")

# 발키리 : 공중 공격 유닛, 한 번에 14발의 미사일 발사
valkyrie1 = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie1.fly(valkyrie1.name, "3시")

# 게임 시작
game_start()

# 마린 3명 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2대 생성
t1 = Tank()
t2 = Tank()

# 레이스 1대 생성
w1 = Wraith()

# 유닛 관리 - 리스트 생성
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

print(attack_units)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.siege_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비( 스팀팩 / 시즈모드 / 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):       #unit 이 어떤 클레스인지 확인후 Marine이면 stimpack() 시전
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 60))  # 공격은 랜덤으로 5 ~ 20


# 게임 종료
game_over()
