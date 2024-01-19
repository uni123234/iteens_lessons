import json

def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)

    with open(file_path, 'r') as file:
        date=file.read()

    return date

file_path='test.txt'
text='Hello, world!'
result=append_to_file(file_path, text)
print(result)


def count_world(file_pach):
    try:
        with open(file_pach, 'r') as f:
           text=f.read()
           words=text.split()
           num_words=len(words)
           print(f"Цей файл  '{file_pach} містить {num_words} слів.")
    except FileNotFoundError:
        print(f"Ошибка: файла '{file_pach}' не знайдено.")



count_world("test.txt")


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        date=json.load(file)
    return date

date=read_json_file('date.json')
print(date)