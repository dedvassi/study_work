try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a == 0:
        print("Это не квадратное уравнение!")
    else:
        D = b**2 - 4 * a * c
        if D < 0:
            print("Нет вещественных корней")
        else:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            print(f"Корни: {x1:.2f}, {x2:.2f}")
except ValueError:
    print("Ошибка: введено не число!")
