import math


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

p = (a + b + c) / 2

s_sq = p * (p - a) * (p - b) * (p - c)
if s_sq < 0:
	s_sq = 0.0
s = math.sqrt(s_sq)

print(f"{s:.2f}")