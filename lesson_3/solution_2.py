class Greenhouse:
    def __init__(self):
        self.__temperature = 22
        self.__humidity = 50
        self.__light_level = 70

    def set_temperature(self, temperature):
        if 15 <= temperature <= 30:
            self.__temperature = temperature
        else:
            print("Ошибка: Температура должна быть в диапазоне от 15 до 30 градусов")

    def get_temperature(self):
        return self.__temperature

    def set_humidity(self, humidity):
        self.__humidity = humidity

    def get_humidity(self):
        return self.__humidity

    def set_light_level(self, light_level):
        self.__light_level = light_level

    def get_light_level(self):
        return self.__light_level

# Создаем объект Greenhouse
greenhouse = Greenhouse()

# Демонстрируем установку и получение атрибутов
print("Текущая температура в теплице:", greenhouse.get_temperature())
greenhouse.set_temperature(25)
print("Новая температура в теплице:", greenhouse.get_temperature())

print("Текущий уровень влажности в теплице:", greenhouse.get_humidity())
greenhouse.set_humidity(60)
print("Новый уровень влажности в теплице:", greenhouse.get_humidity())

print("Текущий уровень освещенности в теплице:", greenhouse.get_light_level())
greenhouse.set_light_level(80)
print("Новый уровень освещенности в теплице:", greenhouse.get_light_level())