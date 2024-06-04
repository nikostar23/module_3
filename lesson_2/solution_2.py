class Person:
    population: int = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1  

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2024  # Задаем текущий год
        age = current_year - birth_year
        return cls(name, age)
    
    @classmethod
    def total_population(cls) -> None:
        print(f"Всего человек: {cls.population}")


# Создаем экземпляр Person с использованием метода from_birth_year
person = Person.from_birth_year("Иван", 1990)
person = Person.from_birth_year("Николай", 1985)

# Выводим информацию о созданном экземпляре
print(f"Имя: {person.name}")
print(f"Возраст: {person.age} лет")

# Выводим количество человек
Person.total_population()
