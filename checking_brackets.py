import re

def insertion():
    text = None #присваиваем значение None, чтобы в конце вернуть переменную
    check = 0 #счетчик проверки
    while True:
        try:
            text = input("Введите исходный текст:") #ввод текста пользователя
            for k in text:
                if k == "(" or k == ")" or k == "{" or k == "}" or k == "[" or k == "]" or k == "<" or k == ">":
                    check += 1 #проверка, если пользователь не указал никаких скобок, то сюда i увеличино не будет
            if check == 0: #если i=0, то пользователь не ввел скобок, вызываем исключение
                raise ValueError
            break
        except ValueError:
            print("Введите строку, содержащую скобки!")
    return text

def checking_brackets(text):
    while True:
        try:
            brackets = input("Введите проверяемые скобки:") #вводим проверяемые скобки
            if re.search('[]}>)]', brackets) or re.search("[0-9a-zA-Zа-яА-Я,./'*`+]", brackets): #если скобки закрывающие или есть другие символы, кроме открывающих скобок, вызываем исключение
               raise ValueError
            elif re.search("[\[({<]", brackets): #если скобки только открывающие, прерываем цикл while
                break
        except ValueError:
            print("Введите только открывающие скобки")

    all_brackets = list(brackets) #записываем открывающие и закрывающие скобки сюда

    for i in range(len(brackets)): #к каждой открывающей скобке мы пишем закрывающую, чтобы можно было сравнивать текст пользователя с нашими скобками
        if (brackets[i] == "("):
            all_brackets.append(")")
        elif (brackets[i] == "["):
            all_brackets.append("]")
        elif (brackets[i] == "{"):
            all_brackets.append("}")
        elif (brackets[i] == "<"):
            all_brackets.append(">")
    #print("Проверяемые скобки:",all_brackets)

    #создаем два списка, open_brackets для окткрывающих скобок, closed_brackets - для закрывающих
    open_brackets = list()
    closed_brackets = list()

    #заполняем данные списки
    for i in range(len(all_brackets)):
        if i < len(all_brackets)//2:
            open_brackets += all_brackets[i]
        else:
            closed_brackets += all_brackets[i]

    print("Open_brackets = ",open_brackets)
    print("Closed_brackets = ",closed_brackets)

    text_brackets = [] #отсекаем сюда только скобки из текста
    for i in text:
        if i == "(" or i == ")" or i == "{" or i == "}" or i == "[" or i == "]" or i == "<" or i == ">":
            text_brackets += i
    #print("text_brackets:",text_brackets)

    n = 0 #переменная для проверки
    flag = 0 #переменная флаг для проверки

    print(text)

    for i in text:
        print("Open_brackets = ", open_brackets)
        if text[0] == ")" or text[0] == "}" or text[0] == "]" or text[0] == ">":
            print("Первая скобка не может быть закрывающей")
            flag += 1 #если строка начнется с закрывающей скобки, то флаг будет 1
            break

        while n == 0:
            if i in open_brackets: #если есть в тексте открытые скобки, то создаем стэк и увеличиваем i на 1, таким образом, в этот цикл while мы больше не зайдем
                stack = []
                n += 1
            else:
                break

        if i in open_brackets:
            stack.append(i) #если нашли одинаковые скобки в тексте и в проверяющих скобках, то записываем в стэк эту скобку
        elif i in closed_brackets:
            position = closed_brackets.index(i)
            try:
                if ((len(stack)>0) and (open_brackets[position] == stack[len(stack)-1])):
                    stack.pop() #если скобка закрылась, удаляем ее из стэка
                else:
                    print(f"Ошибка , {i} , {text.index(i)}") #если скобка не соответствует своей закрывающей, то пишем индекс скобки и саму скобку
                    flag = 1
            except UnboundLocalError:
                break


    if flag == 0:
        if n > 0:
            if len(stack) == 0:
                print("Все верно!")
            else:
                print("Ошибка! Не нашлось закрывающей скобки!")
        else:
            print("Ошибка, не нашлось закрывающей скобки!")
    else: #если флаг не ноль, а например 1, то просто ничего не пишем
        pass

def main():
    text = insertion() #Функция, описывающая ввод текста пользователя
    checking_brackets(text) #Функция, проверяющая скобки в данном тексте

if __name__== '__main__': #Точка входа в программу
    main()
