# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число a:'))
b = int(input('Введите число b:'))

def proiz_num(a,b):
    if b == 0:
        return 1
    else:
        if b >0:
            return (a * proiz_num(a,b-1))
        else:
            return (a * proiz_num(a,b+1))

print(proiz_num(a,b))



        