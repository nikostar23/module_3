from abc import ABC, abstractmethod

class Fountain(ABC):
    @abstractmethod
    def spray_water(self):
        pass

class SimpleFountain(Fountain):
    def spray_water(self):
        print("Простой фонтан брызгает воду равномерно")

class MusicalFountain(Fountain):
    def spray_water(self):
        print("Музыкальный фонтан брызгает воду в такт музыке")

class LightedFountain(Fountain):
    def spray_water(self):
        print("Фонтан с подсветкой создает игру света и воды")

fountains = [SimpleFountain(), MusicalFountain(), LightedFountain()]

for fountain in fountains:
    fountain.spray_water()