class Greenhouse:
    def __init__(self, temperature = 22, humidity = 40, light_level = 80):
        self.__temperature = temperature
        self.__light_level = light_level
        self.__humidity = humidity
    
    def __str__(self):
        return f'Текущая температура в теплице: {self.__temperature}\n' \
               f'Текущий уровень освещенности в теплице: {self.__light_level}\n' \
               f'Текущий уровень влажности в теплице: {self.__humidity}'
            
    @property
    def temperature(self):
        return self.__temperature
    
    @property
    def light_level(self):
        return self.__light_level
    
    @property
    def humidity(self):
        return self.__humidity
    
    @temperature.setter
    def temperature(self, value):
        if not (15 <= value <= 30):
            print("Ошибка: Температура должна быть в диапазоне от 15 до 30 градусов")
        else:
            self.__temperature = value

    @light_level.setter
    def light_level(self, value):
        if not (60 <= value <= 95):
            print("Ошибка: Освещенность должна быть в диапазоне от 60 до 95")
        else:
            self.__light_level = value

    @humidity.setter
    def humidity(self, value):
        if not (20 <= value <= 50):
            print("Ошибка: Влажность должна быть в диапазоне от 20 до 50")
        else:
            self.__humidity = value
  

# Создаем объект Greenhouse
greenhouse = Greenhouse()
print(greenhouse)

# Демонстрируем установку и получение атрибутов

greenhouse.temperature = 25
print(f'Новая температура в теплице: {greenhouse.temperature}')

greenhouse.humidity = 30
print(f'Новый уровень влажности в теплице: {greenhouse.humidity}')

greenhouse.light_level = 50

greenhouse.light_level = 90
print(f'Новый уровень освещенности в теплице: {greenhouse.light_level}')