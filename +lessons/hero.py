from datetime import  datetime, timedelta

class Human:
    def __init__(self, title, hp, stamina ,speed, level,attack, reload_time):
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload_time = reload_time
        self.last_attack = None

    def __str__(self):
        return  f"Race {self.title}"

    def check_attack(self):
        if self.last_attack and datetime.now() - self.last_attack < timedelta(microseconds=self.reload_time):
            return False
        else:
            return  True

    def attack_func(self):
        if self.check_attack():
            self.last_attack = datetime.now()
            print(f"Atracking {self.attack}")
            return self.attack
        else:
            print("Pls, wait")
            return 0

    def hell_check(self):
        if self.hp <= 0:
            print(f"enemy dead")

class Archer(Human):
    def __init__(self,level):
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5,3,level,40 + level*5, 300)


class Knight(Human):
    def __init__(self,level):
        self.title = "Knight"
        super().__init__(self.title, 80 + level*20, 95 + level*5,3,level,40 + level*5,200)


class Wizard(Human):
    def __init__(self,level):
        self.title = "Wizard"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*5,200)

