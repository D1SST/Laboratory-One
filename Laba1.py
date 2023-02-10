print("Введите количество цифр, которое натуральное число не должно превышать: ")
K = int(input())

with open("test2.txt", "r") as f:
    s = "asd"
    number_help = ""
    sequence = []
    while s != "":
        s = f.read(1)
        if (s != " ") and (s != "\n"):
            number_help =  number_help + s
        else:
            sequence.append(number_help)
            number_help = ""
sequence.append(number_help)


for i in range(len(sequence)):
    if (sequence[i].isdigit() == False):
        if (i == (len(sequence) - 1)):
            print("Таких значений нет.")
        i += 1
    else:
        break


numbers_dict = {"0": "ноль ", "1": "один ", "2": "два ", "3": "три ", "4": "четыре ", "5": "пять ", "6": "шесть ", "7": "семь ", "8": "восемь ", "9": "девять "}


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


for i in range(len(sequence)):
    if (sequence[i].isdigit() == True):
        if (int(sequence[i]) != 0) and (int(sequence[i]) % 2 == 0) and (len(str(int(sequence[i]))) <= K):
            if (i % 2 != 0):
                sequence[i] = multiple_replace(str(sequence[i]), numbers_dict)
                print(sequence[i], "| индекс числа -", i)

            else:
                print(sequence[i], "| индекс числа -", i)
        i += 1


