color1 = input("Введите цвет: ")
color2 = input("Введите цвет: ")

if (color1 == "красный" or color1 == "желтый" or color1 == "синий") and (color2 == "красный" or color2 == "желтый" or color2 == "синий"):
    if (color1 == "красный" and color2 == "синий") or (color2 == "красный" and color1 == "синий"):
        print("Фиолетовый")
    if (color1 == "красный" and color2 == "желтый") or (color2 == "красный" and color1 == "желтый"):
        print("Ораньжевый")
    if (color1 == "синий" and color2 == "желтый") or (color2 == "синий" and color1 == "желтый"):
        print("Зеленый")
else:
    print("Нельзя такие цвета")