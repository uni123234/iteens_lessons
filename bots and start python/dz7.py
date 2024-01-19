#зрізи
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_s=list[2:7]
print(my_s)


n1='Це рядок, який потрібно модифікувати'
n2='модифікований рядок'
iv=n1.index(',')
nw=n1[:iv+1] + " " + n2 + "," + n1[iv+1:]
print(nw)
#множини
set1=set(input('строка 1: ').split())
set2=set(input('строка 2: ').split())
print(f'Загальні елементи: {set1 & set2}\nОсобливі елементи:{set1 ^ set2 }\nСпц: { set1 | set2} \nSet 1 різниця: {set2 - set1} \nSet 2 різниця {set2 - set1}')

available_items = {"Манго", "Банани", "Снікерс", "Вода", "Яблука", "Чипси", "Морква"}
user_cart = set()

def add_to_cart(item):
    if item in available_items:
        user_cart.add(item)
        print(f"{item} додано до кошика.")
    else:
        print(f"{item} недоступний для покупки.")

def remove_from_cart(item):
    if item in user_cart:
        user_cart.remove(item)
        print(f"{item} видалено з кошика.")
    else:
        print(f"{item} не знайдено у кошику.")

def view_cart():
    print("Товари у кошику:")
    for item in user_cart:
        print(item)

def end_shopping():
    print("Дякуємо за покупки!")
    exit()

while True:
    print("\nЩо ви хочете зробити?")
    print("1. Додати товар до кошика")
    print("2. Видалити товар з кошика")
    print("3. Переглянути вміст кошика")
    print("4. Завершити покупки")
    choice = input("Ваш вибір: ")

    if choice == "1":
        item = input("Який товар ви хочете додати до кошика? ")
        add_to_cart(item)
    elif choice == "2":
        item = input("Який товар ви хочете видалити з кошика? ")
        remove_from_cart(item)
    elif choice == "3":
        view_cart()
    elif choice == "4":
        end_shopping()
    else:
        print("Невірний вибір. Спробуйте ще раз")
#Словник
# Ввести текст від користувача
text = input("Введіть текст: ")

# Розбити текст на слова
words = text.split()

# Створити словник, де ключі - слова, значення - кількість цього слова в тексті
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

# Знайти слово, яке повторюється найбільшу та найменшу кількість разів
most_common_word = max(word_count, key=word_count.get)
least_common_word = min(word_count, key=word_count.get)

# Вивести результат
print("Слово, яке повторюється найбільшу кількість разів:", most_common_word)
print("Слово, яке повторюється найменшу кількість разів:", least_common_word)

# Приклад використання методу .pop ()
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')  # видаляємо ключ 'b' та повертаємо його значення
print(value)  # 2
print(my_dict)  # {'a': 1, 'c': 3}
# Приклад використання методу .get ()
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')  # повертаємо значення ключа 'b'
print(value)  # 2
value = my_dict.get('d', 'Значення не знайдено')  # повертаємо значення ключа 'd' (який не існує)
print(value)  # Значення не знайдено
# Приклад використання методу .clear ()
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()  # видаляємо всі ключі та значення
print(my_dict)  # {}
# Приклад використання методу .update ()
my_dict = {'a': 1, 'b': 2}
new_dict = {'c': 3, 'd': 4}
my_dict.update(new_dict)  # додаємо ключі та значення з new_dict до my_dict
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Приклад використання методу .copy ()
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()  # створюємо копію my_dict
print(new_dict)  # {'a': 1, 'b': 2, 'c': 3}


