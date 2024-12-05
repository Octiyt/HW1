def procesing():
    if 0 <= mark <= 49:
        print( "Незадовільно")
    elif 50 <= mark <= 69:
        print ("Задовільно")
    elif 70 <= mark <= 89:
        print ("Добре")
    elif 90 <= mark <= 100:
        print ("Відмінно")
    else:
        print ("Некоректні дані")

mark = int(input("Введіть кількість балів (0-100): "))
mark = procesing()
print(f"Оцінка: {mark}")