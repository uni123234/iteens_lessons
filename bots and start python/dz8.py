import matplotlib.pyplot as plt
import numpy as np
# from data_module import get_data


def get_data():
    x_values = [1, 2, 3, 4, 5]
    y_values = [10, 8, 6, 4, 2]
    return x_values, y_values


x_values, y_values = get_data()

plt.plot(x_values, y_values)
plt.title("Графік Х від Y")
plt.xlabel("X-ось")
plt.ylabel("Y-ось")

plt.show()


x_values = [1, 2, 3, 4, 5]
y1_values = [10, 8, 6, 4, 2]
y2_values = [2, 4, 6, 8, 10]
y3_values = [5, 5, 5, 5, 5]
y4_values = [4, 5, 6, 7, 8]

plt.plot(x_values, y1_values)
plt.plot(x_values, y2_values)
plt.plot(x_values, y3_values)
plt.plot(x_values, y4_values)

plt.title("A Simple Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()


# Створення масиву x
x = np.arange(0, 20, 0.2)

# Обчислення значень функції y
y = x**4

# Побудова графіку
plt.plot(x, y)

# Додаткові параметри графіку
plt.title("Графік функції y = x^4")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Відображення графіку
plt.show()
