def is_in_set(number):
    if (number - 1) % 6 == 0 or (number + 1) % 6 == 0:
        for x in range(1, 1000000):
            for y in range(1, 1000000):
                if (6*x + 1)*(6*y + 1) == number or (6*x - 1)*(6*y - 1) == number or (6*x + 1)*(6*y - 1) == number or (6*x - 1)*(6*y + 1) == number:
                    return False
                if (6*x + 1)*(6*y + 1) > number:
                    break
        return True
    return False

# Ввод числа от пользователя
number = int(input("Введите число для проверки: "))

# Проверка числа на принадлежность множеству (6a+1) или (6a-1), но не принадлежность множествам (6x+1)(6y+1), (6x-1)(6y-1), (6x+1)(6y-1) или (6x-1)(6y+1)
if is_in_set(number):
    print(f"{number} простое")
else:
    print(f"{number} составное")
