from hero import Archer, Wizard, Knight

print("Wellcome to game!")
name = input("Enter your name: ")
answer = 0

while answer not in [1, 2, 3]:
    answer = int(input("Choose your role\n 1:Archer 2:Knight 3:Wizard"))
    if answer == 1:
        hero = Archer(1)
    if answer == 2:
        hero = Knight(1)
    if answer == 3:
        hero = Wizard(1)

    print(hero)

enemy1 = Knight(1)
print(f"Your enemy is {enemy1} \n Hp is {enemy1.hp}")

enemy1.hp = enemy1.hp - hero.attack_func()
enemy1.hell_check()
enemy1.hp = enemy1.hp - hero.attack_func()
enemy1.hell_check()
enemy1.hp = enemy1.hp - hero.attack_func()
enemy1.hell_check()

print(f"Your enemy is {enemy1} \n Hp is {enemy1.hp}")
