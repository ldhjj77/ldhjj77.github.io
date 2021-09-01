


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, self.damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))
            
# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        self.name = name
        self.location = location
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
              
              
# 다중 상속

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)  
         
    
valkyrie = FlyableAttackUnit('발키리', 100, 10, 10)
valkyrie1 = FlyableAttackUnit('발키리', 110, 15, 15)
valkyrie1.fly(valkyrie.name, '3시')

# 메소드 값
firebat1 = AttackUnit("파이어뱃", 50, 20)
firebat1.attack("7시")
firebat1.attack("7시")
firebat1.attack("7시")
    

# 오버라이딩 - 같은 함수가 존재 할 경우 구분해서 사용하는 방법
# 배틀크루저 : 공중 유닛, 최강 유닛
battle = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battle.fly(battle.name, "9시")
battle.attack('9시')  

marine = AttackUnit("마린", 40, 10)
marine.attack("3시")  
    
    






