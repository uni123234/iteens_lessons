products = ["молоко", "хліб", "яйця", "сир", "м'ясо"]

sales = {"молоко": 20, "хліб": 30, "яйця": 50, "сир": 10, "м'ясо": 5}

print("Усі товари:")
for product in products:
    print(product)

products.append("овочі")
products.append("фрукти")

print("\nТовари з новими елементами:")
for product in products:
    print(product)

products.remove("молоко")

print("\nТовари з видаленим елементом:")
for product in products:
    print(product)

products.insert(0, "молоко")

print("\nТовари з новим елементом на початку списку:")
for product in products:
    print(product)

print("\nСписок проданих продуктів за день:")
for product, amount in sales.items():
    print(f"{product}: {amount}")


students = [
    ['Іван', 'Петров'],
    ['Олександр', 'Ковальчук'],
    ['Марія', 'Сидоренко'],
    ['Андрій', 'Іванов'],
    ['Андрій', 'Соколов'],
    ['Олег', 'Петренко'],
    ['Наталія', 'Коваль'],
    ['Андрій', 'Кузьменко'],
    ['Юлія', 'Семенченко']
]

con: int = 0
for students in students:
    if students[0] == 'Андрій':
        con += 1

print("Кількість Андріїв в групі", con)


mas = ['івнічна Америка', 'Південа Америка']
nas = ['Євразія', 'Африка', 'Австралія', 'Антарктида']
cont: list[str] = mas + nas

cont.sort()

for cont in cont:
    print(cont)
