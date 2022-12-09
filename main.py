try:
    b = float(input('Введите B: '))
    d = float(input('Введите D: '))
    x = float(input('Введите X: '))
    try:
        if (x >= 8):
            y = (x-2) / pow(x,2)
        else:
            y = pow(b,2) * d    + 4*pow(x,3)
        print('y=', format(y,'.2f'))
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные")