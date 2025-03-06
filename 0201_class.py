# Базовый класс для всех видов транспорта
class Transport:
    def __init__(self, speed, max_speed):
        # Инициализация скорости и максимальной скорости
        self._speed = speed  # Приватное свойство: текущая скорость
        self._max_speed = max_speed  # Приватное свойство: максимальная скорость

    # Геттер для скорости
    @property
    def speed(self):
        return self._speed

    # Сеттер для скорости с проверкой на превышение максимальной скорости
    @speed.setter
    def speed(self, value):
        if value > self._max_speed:
            raise ValueError("Скорость не может превышать максимальную")
        self._speed = value

    # Метод для увеличения скорости
    def increase_speed(self, value):
        self.speed += value

    # Метод для уменьшения скорости
    def decrease_speed(self, value):
        self.speed -= value

    # Метод, который вызывается при вызове объекта как функции
    def __call__(self):
        return f"Транспорт движется со скоростью {self._speed} км/ч"


# Класс Автобус, наследующий от Transport
class Bus(Transport):
    def __init__(self, speed, capacity, max_speed):
        # Вызов конструктора родительского класса
        super().__init__(speed, max_speed)
        # Инициализация специфичных для автобуса свойств
        self._capacity = capacity  # Приватное свойство: вместимость автобуса
        self._passengers = []  # Приватное свойство: список пассажиров
        # Словарь мест в автобусе, где ключ — номер места, значение — имя пассажира
        self._seats = {i: None for i in range(1, capacity + 1)}

    # Геттер для проверки наличия свободных мест
    @property
    def has_empty_seats(self):
        return any(seat is None for seat in self._seats.values())

    # Метод для посадки пассажира
    def board_passenger(self, name):
        if not self.has_empty_seats:
            raise ValueError("Нет свободных мест")
        # Находим первое свободное место и сажаем пассажира
        for seat, passenger in self._seats.items():
            if passenger is None:
                self._seats[seat] = name
                self._passengers.append(name)
                break

    # Метод для высадки пассажира
    def disembark_passenger(self, name):
        if name not in self._passengers:
            raise ValueError("Пассажир не найден")
        # Находим место пассажира и освобождаем его
        for seat, passenger in self._seats.items():
            if passenger == name:
                self._seats[seat] = None
                self._passengers.remove(name)
                break

    # Перегрузка оператора "in" для проверки наличия пассажира в автобусе
    def __contains__(self, name):
        return name in self._passengers

    # Перегрузка оператора "+=" для посадки пассажира
    def __iadd__(self, name):
        self.board_passenger(name)
        return self

    # Перегрузка оператора "-=" для высадки пассажира
    def __isub__(self, name):
        self.disembark_passenger(name)
        return self

    # Перегрузка метода __call__ для вывода информации о автобусе
    def __call__(self):
        return (f"Автобус движется со скоростью {self._speed} км/ч, "
                f"пассажиры: {', '.join(self._passengers) if self._passengers else 'нет пассажиров'}")


# Пример использования
bus = Bus(speed=60, capacity=30, max_speed=100)
bus += "Иван Иванов"  # Посадка пассажира
bus += "Петр Петров"  # Посадка пассажира
print(bus())  # Вывод информации о автобусе
print("Иван Иванов" in bus)  # Проверка наличия пассажира
bus -= "Иван Иванов"  # Высадка пассажира
print(bus())  # Вывод обновленной информации о автобусе