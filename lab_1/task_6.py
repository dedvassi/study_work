sum_positive = 0
sum_negative = 0

while True:
    try:
        n = int(input("Введите число: "))
        if n == 0:
            break
        if n > 0:
            sum_positive += n
        else:
            sum_negative += n
    except ValueError:
        print("Вы ввели не число, будьте внимательнее")

print(f"Сумма положительных = {sum_positive}")
print(f"Сумма отрицательных = {sum_negative}")