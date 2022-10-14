a = int(input("введите размерность массива 1"))
first1 = float(input("Введите первый элемент"))
b = [first1]
for i in range (a-1):
    b.append(float(input("Введите следующий элемент")))
    i+= 1
c = int(input("введите размерность массива 2"))
first2 = float(input("Введите первый элемент"))
d = [first2]
for i in range (c-1):
    d.append(float(input("Введите следующий элемент")))
    i+= 1
print("Массив 1: ", b)
print("Массив 2: ", d)
proverka = 0 #на случай если ни одного элемента не содержится в массиве
for i in range (a):
    for j in range (c):
        if b[i]==d[j]:
            print("Найден общий элемент", b[i])
            proverka +=1
        j+=1
    i+=1
if  proverka == 0:
    print("общих элементов не найдено")

    
