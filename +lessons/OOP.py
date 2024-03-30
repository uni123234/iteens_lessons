class User:
    def __init__(self, frist_name: str, last_name: str, age: int) -> None:
        self.frist_name = frist_name
        self.last_name = last_name
        self.age = age

    def print_info(self):
        print(f"User {self.frist_name} {self.last_name} (age = {self.age})")
