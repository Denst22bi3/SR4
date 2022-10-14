a = int(input("введите размерность массива"))
first = float(input("Введите первый элемент"))
b = [first]
for i in range (a-1):
    b.append(float(input("Введите следующий элемент")))
    i+= 1
print("Ваш массив", b)
maks = float(-999999999)
num = 0
for i in range (a):
    if b[i] > maks:
        maks=b[i]
        num = i
for i in range (a):
    if i > num:
        b[i]=0
print("Получившийся массив: ", b)
    
    
