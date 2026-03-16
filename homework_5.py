class Distance:
    # коэффициенты перевода в метры
    conversion_dict = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    # метод конвертации в метры
    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    # 1️⃣ инициализация
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    # 2️⃣ строковое представление
    def __str__(self):
        return f"{self.value} {self.unit}"

    # 3️⃣ сложение
    def __add__(self, other):
        result_meters = self.convert() + other.convert()
        result_value = result_meters / Distance.conversion_dict[self.unit]
        return Distance(result_value, self.unit)

    # ➕ доп: вычитание
    def __sub__(self, other):
        result_meters = self.convert() - other.convert()

        if result_meters < 0:
            raise ValueError("Distance не может быть отрицательной!")

        result_value = result_meters / Distance.conversion_dict[self.unit]
        return Distance(result_value, self.unit)

    # ➕ доп: сравнение
    def __eq__(self, other):
        return self.convert() == other.convert()

    def __lt__(self, other):
        return self.convert() < other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()


# 🔥 ТЕСТЫ
d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(300, "cm")

print(d1)
print(d2)

print(d1 + d3)      # сложение````````
print(d2 - d1)      # вычитание

print(d1 == d3)     # сравнение
print(d2 > d1)