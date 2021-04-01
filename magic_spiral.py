turn = 0 #указывает на то, сколько поворотов нужно будет сделать в зависимости от величины массива
s = 1 #начальное число
flag = 0 #необходимо для грамотного перебора всех значений

while True:
    try:
        n = int(input("Введите число N: "))
        if not n >= 4 and n <= 1000:
            raise ValueError
        break
    except (ValueError,NameError):
        print("Некорректный ввод. Введите целое положительное число в диапазоне от 4 до 1000!")

if not n>=4 and n<=1000:
    print()

print("Введеное вами N:",n)
turn = n+n-1 #вычислим кол-во поворотов
print("Количество поворотов будет:",turn)
A = [[0] * n for i in range(n)] #создание двухмерного массива

#цикл заполнения
while turn>=0:

    for k in range (flag,n-flag):
        A[flag][k] = s
        s+=1
    turn-=1

    for k in range(1+flag,n-flag):
        A[k][n-1-flag] = s
        s+=1
    turn -= 1

    for k in range (n-2-flag,-1+flag,-1):
        A[n-1-flag][k] = s
        s+=1
    turn -= 1

    for k in range (n-2-flag,0+flag,-1):
        A[k][flag] = s
        s+=1
    turn -= 1 #условие выхода из цикла
    flag+=1

#вывод массива
print("Итоговый результат:")
for i in range(n):
    for j in range(n):
        print(A[i][j], end="\t")
    print("\n")