class Temperature:
    def __init__(self, temperature_celsius, temperature_fahrenheit):
        self.temperature_celsius = temperature_celsius
        self.temperature_fahrenheit = temperature_fahrenheit

    @staticmethod
    def convert_celsius_to_fahrenheit(temperature_celsius: float) -> float:
        return temperature_celsius * (9 / 5) + 32
    
    @staticmethod
    def convert_fahrenheit_to_celsius(temperature_fahrenheit: float) -> float:
        return (temperature_fahrenheit - 32) * (5 / 9)

    def display_temperature_fahrenheit(self, temperature_celsius: float) -> None:
        temperature_fahrenheit = Temperature.convert_celsius_to_fahrenheit(self.temperature_celsius)
        print(f"{temperature_celsius} градусов по Цельсию = {temperature_fahrenheit} градусов по Фаренгейту")

    def display_temperature_celsius(self, temperature_fahrenheit: float) -> None:
        temperature_celsius = Temperature.convert_fahrenheit_to_celsius(self.temperature_fahrenheit)
        print(f"{temperature_fahrenheit} градусов по Фаренгейту = {temperature_celsius} градусов по Цельсию")

temperature1 = Temperature(36, 42)

# Отображаем температуру, преобразованную в градусы Фаренгейта
temperature1.display_temperature_fahrenheit(36)

# Отображаем температуру, преобразованную в градусы Цельсия
temperature1.display_temperature_celsius(42)

