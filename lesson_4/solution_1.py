from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play():
        pass

class Guitar(Instrument):
    def play(self):
        print("Гитара бремчит")

class Piano(Instrument):
    def play(self):
        print("Пианино звучит")

class Flute(Instrument):
    def play(self):
        print("Флейта играет")

instruments = [Guitar(), Piano(), Flute()]

for instrument in instruments:
    instrument.play()