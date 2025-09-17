TO_METERS = {
    "km": 1000.0,
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
}

print("Единицы: km, m, cm, mm, mi, yd")
from_unit = input("Исходная единица: ").strip().lower()
to_unit = input("Целевая единица: ").strip().lower()
value = float(input("Значение: "))

meters = value * TO_METERS[from_unit]
result = meters / TO_METERS[to_unit]

print(result)