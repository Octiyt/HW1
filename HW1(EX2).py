def calculator():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        Symbol = input("Введіть дію (+, -, *, /): ")

        if Symbol == "+":
            result = a + b
        elif Symbol == "-":
            result = a - b
        elif Symbol == "*":
            result = a * b
        elif Symbol == "/":
            if b == 0:
                return "Помилка: Ділення на нуль!"
            result = a / b
        else:
            return "Некоректна дія!"

        return f"Результат: {result}"
    except ValueError:
        return "Помилка: Некоректний ввід чисел!"

print(calculator())
