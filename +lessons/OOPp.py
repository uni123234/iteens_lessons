class Car:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"My car is {self.brand}. Model - {self.model}. Create in {self.year}"


myCar = Car("Toyota", "Corolla", 2022)
print(myCar)