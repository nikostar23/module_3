import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        today = datetime.date.today()
        current_year = today.year # Задаем текущий год
        age = current_year - birth_year
        return cls(name, age)

# Создаем экземпляр Person с использованием метода from_birth_year
person = Person.from_birth_year("Иван", 1990)

# Выводим информацию о созданном экземпляре
print(f"Имя: {person.name}")
print(f"Возраст: {person.age} лет")