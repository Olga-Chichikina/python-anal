# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка;B, C, M, P – 3 очка;F, H, V, W, Y – 4 очка;
# K – 5 очков;J, X – 8 очков;Q, Z – 10 очков.
# А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка;Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#  Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# Пример
# ноутбук
# 12

dict_1 = dict.fromkeys(['a','e','i','o','u','l','n','s','t','r'],1)
dict_2 = dict.fromkeys(['d','g'],2)
dict_3 = dict.fromkeys(['b','c','m','p'],3)
dict_4 = dict.fromkeys(['f','h','v','w','y'],4)
dict_5 = dict.fromkeys(['k'],5)
dict_6 = dict.fromkeys(['x'],8)
dict_7 = dict.fromkeys(['q','z'],10)
dict_11 = dict.fromkeys(['а','в','е','и','н','о','р','с','т'],1)
dict_12 = dict.fromkeys(['д','к','л','м','п','у'],2)
dict_13 = dict.fromkeys(['б','г','ё','ь','я'],3)
dict_14 = dict.fromkeys(['й','ы'],4)
dict_15 = dict.fromkeys(['ж','з','х','ц','ч'],5)
dict_16 = dict.fromkeys(['ш','э','ю'],8)
dict_17 = dict.fromkeys(['ф','щ','ъ'],10)

my_dict = dict_1 | dict_2 | dict_3 | dict_4 | dict_5 | dict_6 | dict_7 | dict_11 | dict_12 | dict_13 | dict_14 | dict_15 | dict_16 | dict_17 
print(my_dict) 
text = input('Введите слово :')
result = 0
for i in range(len(text)):
    result = sum( my_dict[i] for i in text)
print(result)









