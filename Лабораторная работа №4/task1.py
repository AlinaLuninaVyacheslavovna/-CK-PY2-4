from pydantic import BaseModel

if __name__ == "__main__":

    class Car(BaseModel):
        """ Базовый класс - Автомобиль. """
        def __init__(self, brand: str, speed: int, car_weight: float or int, passenger_weight: float or int):
            """
            Создание и подготовка к работе объекта "Car"
            :param brand: Бренд автомобиля
            :param speed: Текущая скорость автомобиля
            :param car_weight: Вес автомобиля в тоннах
            :param passenger_weight: Вес пассажиров в тоннах
            Примеры:
            >>> car = Car('Volkswagen', 80, 2.5, 2, 0.4)
            """
            self.brand = brand
            self.speed = speed
            self.car_weight = car_weight
            self.passenger_weight = passenger_weight

        def __str__(self):
            """ Магический метод __str__, который наследуется дочерним классом. """
            return f"Автомобиль бренда {self.brand}. Текущая скорость {self.speed}. Вес автомобиля {self.car_weight}. Вес пассажиров {self.passenger_weight}."

        def __repr__(self):
            """ Магический метод __repr__."""
            return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self.speed!r}, car_weight={self.car_weight!r}, passenger_weight={self.passenger_weight!r})"

        def speed(self, speed: int):
            """ Метод проверяет текущую скорость, если она больше, то вызывает ошибку. Наследуется дочерним классом."""
            allowable_speed = 120  # Допустимая скорость автомобиля
            if speed > allowable_speed:
                raise ValueError('Текущая скорость выше допустимой')
            self.speed = speed

        def max_weight(self):
            """Метод, считающий суммарный вес автомобиля"""
            return self.passenger_weight + self.car_weight

    class Truck(Car, BaseModel):
        """ Дочерний класс - Грузовой автомобиль. """
        def __init__(self, brand: str, speed: int, car_weight: float or int, passenger_weight: float or int, color: str, cargo_weight: float or int):
            """
            Расширение конструктора базового класса, так как вводятся дополнительные атрибуты 'color' и 'cargo_weight'
            :param color: цвет грузового автомобиля
            :param cargo_weight: вес груза
            """
            super().__init__(brand, speed, car_weight, passenger_weight)
            self.color = color
            self.cargo_weight = cargo_weight

        def __repr__(self):
            """ Магический метод __repr__, который перегружается, так как добавляются параметры 'color' и 'cargo_weight'."""
            return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self.speed!r}, car_weight={self.car_weight!r}, passenger_weight={self.passenger_weight!r}, color={self.color!r}, cargo_weight={self.cargo_weight!r})"

        def max_weight(self):
            """Метод, считающий суммарный вес автомобиля, перегружается, так как грузовой автомобиль имеет вес груза """
            return self.passenger_weight + self.car_weight + self.cargo_weight
    pass
