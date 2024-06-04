from enum import Enum
from typing import Optional

class VehicleType(Enum):
    CAR = "car"
    BOAT = "boat"
    BIKE = "bike"

class Moveable:
    def move(self) -> None:
        pass

class Vehicle:
    total_vehicles = 0

    def __init__(self, speed: float) -> None:
        self.speed = speed
        Vehicle.total_vehicles += 1

    @classmethod
    def create_vehicle(cls, vehicle_type: VehicleType, speed: float) -> Optional[type['Vehicle']]:
        if vehicle_type == VehicleType.CAR:
            return Car(speed)
        elif vehicle_type == VehicleType.BOAT:
            return Boat(speed)
        elif vehicle_type == VehicleType.BIKE:
            return Bike(speed)
        else:
            raise ValueError("Неизвестный тип транспортного средства")

    @staticmethod
    def convert_speed_to_kmh(speed_mph: float) -> float:
        return speed_mph * 1.60934

    @classmethod
    def display_total_vehicles(cls) -> None:
        print(f"Всего было создано {cls.total_vehicles} экз. транспортных средств")

class Car(Vehicle):
    def move(self) -> None:
        current_speed = Vehicle.convert_speed_to_kmh(self.speed)
        print(f"Скорость машины {current_speed} км/час")

class Bike(Vehicle):
    def move(self) -> None:
        current_speed = Vehicle.convert_speed_to_kmh(self.speed)
        print(f"Скорость мотоцикла {current_speed} км/час")

class Boat(Vehicle):
    def move(self) -> None:
        print(f"Скорость лодки {self.speed} морских миль")

def move_any_vehicle(vehicle: Moveable) -> None:
    vehicle.move()

# Создание объектов через фабричный метод
car1 = Vehicle.create_vehicle(VehicleType.CAR, 60)
boat1 = Vehicle.create_vehicle(VehicleType.BOAT, 25)
bike1 = Vehicle.create_vehicle(VehicleType.BIKE, 85)

move_any_vehicle(car1)

move_any_vehicle(boat1)

move_any_vehicle(bike1)

Vehicle.display_total_vehicles()

