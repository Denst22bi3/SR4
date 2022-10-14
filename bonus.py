a = int(input("введите размерность массива"))
first = float(input("Введите первый элемент"))
b = [first]
for i in range (a-1):
    b.append(float(input("Введите следующий элемент")))
    i+= 1
print("Ваш массив", b)
delta = float(input("Теперь введите delta"))
count = 0
minim = float(9999999999999999999999)  
for i in range (a):
    if b[i] < minim:
        minim=b[i]
y = minim+delta
for i in range (a):
    x = b[i]
    if x == y:
        count += 1
print("количество элементов, отличающихся от минимального на delta =", count)
    
    
