name_l = str(input('Ваше прізвище: '))
bal = int(input('Ваші бали за симестер: '))

if int(bal) >= 80:
    print(f"Студент {name_l}"+' здав іспит')
elif int(bal) < 80:
    print(f"Не здав іспит {name_l}")


while True:
    opr = str(input('Ведіть приклад:'))
    print(eval(opr))
    # Чи так while True: print('=', eval(input()))


x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

if x > 0 and y > 0:
    kl = 1
elif x < 0 and y > 0:
    kl = 2
elif x < 0 and y < 0:
    kl = 3
elif x > 0 and y < 0:
    kl = 4
else:
    kl = 0

print(f"x = {x}, y = {y}, {kl} четверть.")
