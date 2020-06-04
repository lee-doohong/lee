# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.life = 50
        self.attack = 5
    @property
    def is_alive(self):
        return self.life > 0

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while unit_1.life > 0 and unit_2.life > 0 : 
        unit_2.life -= unit_1.attack
        if unit_2.life > 0 :
            unit_1.life -= unit_2.attack
        else : break
    if unit_1.life > 0 : return True
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

    def __iter__(self):
        return iter(self.soldiers)
    
    def __str__(self):
        return self.soldiers

    def __len__(self):
        return len(self.soldiers)


class Battle:
    def fight(self, army1, army2):
        while len(army1) and len(army2) : 
            is_soldier1_won = fight(army1.soldiers[0], army2.soldiers[0])
            if is_soldier1_won : army2.soldiers.pop(0)
            else : army1.soldiers.pop(0)
        if len(army1)>0 : return True
        else : return False



my_army = Army()
my_army.add_units(Knight, 3)
for i in my_army:
    print(i)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()


battle.fight(my_army, enemy_army)
battle.fight(army_3, army_4)

        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
