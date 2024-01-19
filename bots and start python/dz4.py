sum=0

for i in range(1,101,2):
    sum += i

print('Сума всіх чисел неправильних чисел від 1 до 100', sum)

ins = input('Ведіть імя: ')

fname = ins[0]
can = 0
for letter in ins:
    if letter == fname:
        can += 1

print("Кількість воходженя першої букви", can)