class Product:
    def __init__(self, name, calories, protein, fat, carbs):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs


class Meal:
    def __init__(self):
        self.products = []

    def add_product(self, product, weight):
        self.products.append((product, weight))

    def total_calories(self):
        total_calories = 0
        for product, weight in self.products:
            total_calories += (product.calories / 100) * weight
        return total_calories

    def print_meal(self):
        print("Meal composition:")
        for product, weight in self.products:
            print(f"{product.name}: {weight}g")


apple = Product("Apple", 52, 0.3, 0.2, 14)
rice = Product("Rice", 130, 2.7, 0.3, 28)
chicken_breast = Product("Chicken Breast", 165, 31, 3.6, 0)

meal = Meal()
meal.add_product(apple, 150)
meal.add_product(rice, 200)
meal.add_product(chicken_breast, 250)


meal.print_meal()
print(f"Total calories: {meal.total_calories()} kcal")
