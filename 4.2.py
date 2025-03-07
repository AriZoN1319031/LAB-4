n = int(input("Введите номер места:"))
if n < 1 or n > 54:
    print("Неккоректный номер места")
else:
    if n % 2 == 0:
        position = "верхнее"
    else:
        position ="нижнее"
        if n <= 36:
            slice = "купе"
        else:
            slice = "боковое"
print(position, slice)