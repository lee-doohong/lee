# Taken from mission Army Battles

# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0
        self.vampirism = 0
    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50

# class Rookie(Warrior): #test용 계정
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.health = 50
#         self.attack = 1

def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0 : 
        if unit_1.attack > unit_2.defence :
            dealt_damage_1 = unit_1.attack-unit_2.defence 
            unit_2.health -= dealt_damage_1
            if unit_1.vampirism : unit_1.health += dealt_damage_1 * unit_1.vampirism / 100
            if unit_2.attack > unit_1.defence :
                dealt_damage_2 = unit_2.attack-unit_1.defence
                if unit_2.health > 0 :
                    unit_1.health -= dealt_damage_2
                    if unit_2.vampirism : unit_2.health += dealt_damage_2 * unit_2.vampirism / 100
            else : break
    if unit_1.health > 0 : return True
    else : return False 

class Army:
    def __init__(self):
        self.soldiers = [] #self.soldier 라는 변수 list 선언
    
    def add_units(self, job, n):
        if job == Warrior :
            for i in range(n):
                self.soldiers.append(Warrior())   # 객체를 넣어도 관계가 없구만
        elif job == Knight :
            for i in range(n):
                self.soldiers.append(Knight())
        elif job == Defender :
            for i in range(n):
                self.soldiers.append(Defender())
        elif job == Vampire :
            for i in range(n):
                self.soldiers.append(Vampire())
    
    def __len__(self): # 클래스에서는 len을 따로 설정해줘야 사용 가능하다. 기본적으로 우리가 쓰는게 다 클래스. 그런데 이 클래스에는 len이 없으니까 설정해줘야 사용 가능함.
        return len(self.soldiers) #클래스 안에 list를 넣는다면, list 그 자체로서는 사용할 수 있다. 하지만 list 클래스에 따라오늘 함수들까지 사용할 수 있는 것은 아니다.
print(dir(Army))
print(dir(object))
print(type([]))
print(type(object))
print(type(Army))
class Battle:
    def fight(self, army1, army2):
        while len(army1) and len(army2) : 
            is_soldier1_won = fight(army1.soldiers[0], army2.soldiers[0])
            if is_soldier1_won : army2.soldiers.pop(0)
            else : army1.soldiers.pop(0)
        if len(army1)>0 : return True
        else : return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
