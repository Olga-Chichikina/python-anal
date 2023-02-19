
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и 
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов 
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется 
# любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

kol_rows = int(input("Введите количество строк :  "))
kol_columns = int(input("Введите количество столбцов: "))

def fun_proiz(x,y):
    return (x*y)

def print_operation_table(fun, num_rows, num_columns):
    matrix = []
    for i in range(1,num_rows+1):
        temp = []
        for j in range(1,num_columns+1):
            temp.append(fun(i,j))
        matrix.append(temp)   
    return matrix

def print_matrix(my_list):
    for row in my_list:
        for val in row:
            print(val , end=" ")
        print()

              
matr = print_operation_table(fun_proiz,kol_rows,kol_columns)  
print_matrix(matr)
