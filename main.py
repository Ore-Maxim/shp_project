from task1 import reverse_string
from task2 import count_digits

def main():
    print("Выберите действие:")
    print("1 — Развернуть строку")
    print("2 — Подсчитать количество цифр")
    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        s = input("Введите строку: ")
        print("Результат:", reverse_string(s))
    elif choice == "2":
        s = input("Введите строку: ")
        print("Цифр в строке:", count_digits(s))
    else:
        print("Некорректный выбор")

if __name__ == "__main__":
    main()
