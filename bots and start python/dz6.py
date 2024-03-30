import re
# 1
surname = input("Введіть ваше імя: ")
count = {}

for letter in surname:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

most_common_letter = max(count, key=count.get)

print(f"Літера '{most_common_letter}' зустрічається найчастіше у вашому імя.")
# 2

input_str = input("Введіть рядок: ")

output_str = re.sub(r'\d', '', input_str)

print("Результат: ", output_str)
