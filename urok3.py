# Задать список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#x = [2, 3, 6, 10, 12, 16, 5]
#print(x)
#summ = 0
#for i in range(1, len(x), 2):
    #if i % 2 == 1:
        #summ += x[i]       
#print(f"{x} -> сумма элементов на нечётных позициях: {summ}")
# Напиcать программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#def mult_lst(lst):
    #l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    #new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    #print(new_lst)

#lst = [2, 3, 4, 5, 6]
#mult_lst(lst)
#lst = list(map(int, input("Введи числа :\n").split()))
#mult_lst(lst)
# Задать список из вещественных чисел. 
# Написать программу,которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

#my_list = [1.9, 1.8, 45.7, 87, 12.01]
#min = 1
#max = 0
#for i in my_list:
    #if (i - int(i)) <= min:
        #min = i - int(i)
    #if (i - int(i)) >= max:
        #max = i - int(i)  
#print(max-min)
# Написать программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:

 
#def decimalToBinary(n):
    #return bin(n).replace("0b","")
 
# Driver code
#if __name__ == '__main__':
    #print(decimalToBinary(45))
    #print(decimalToBinary(3))
    #print(decimalToBinary(2))
   
# Задать число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#def Fibonacci(n):
    #if n in [1, 2]:                       
        #return 1
    #else:
        #return Fibonacci(n-1) + Fibonacci(n-2)

#def NegaFibonacci(n):
    #if n == 1:                       
        #return 1
    #elif n == 2:                       
        #return -1
    #else:
        #num1, num2 = 1, -1
        #for i in range(2, n):
            #num1, num2 = num2, num1 - num2
        #return num2

#list = [0]
#userNumber = int(input('Введи число: '))
#for e in range(1, userNumber + 1):
    #list.append(Fibonacci(e))
    #list.insert(0, NegaFibonacci(e))
#print(list)