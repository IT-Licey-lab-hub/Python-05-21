# Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B.
a = int(input())
b = int(input())
# a = (2)
# b = (3)

if a < b: 
    print(a + b)

elif a > b:
    print(a + b)

else:
    print(a + 0, b + 0)
