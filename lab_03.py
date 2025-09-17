year = int(input("Введите год: "))

is_leap = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

print("Да" if is_leap else "Нет")
