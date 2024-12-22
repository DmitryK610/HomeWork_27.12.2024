#Конвертация температур
temp = input("Температура в градусах Цельсия: ")
print("Температура в градусах Фаренгейта: ", 9/5 * int(temp) + 32)
#Перевод времени
second = input("Введите колличество секунд: ")
hours = int(second) // 3600
minutes = (int(second) % 3600) // 60
seconds = (int(second) % 3600) % 60
print(f"{hours}:{minutes}:{seconds}")

#Конвертация километров в мили
kilometers = input("Введите километры: ")
miles:int = int( 0.621371 * int(kilometers))
print(f"Миль: {miles}")

#Конвертация футов в метры
foot = input("Введите футы: ")
meters = 0.3048 * int(foot)
print(f"Метры: {meters}")

#Вычисление площади треугольника
a = input("Введите длину онования треугольника: ")
b = input("Введите длину высоты треугольника: ")
s= 0.5 * int(a) * int(b)
print(f"Площадь треугольника: {s}")













