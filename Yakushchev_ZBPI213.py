#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задача 1. Напишите рекурсивную функцию fact, которая вычисляет факториал заданного числа x.
def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n * fact(n-1))
#n = int(input("Введите число: "))
#print("Факториал числа равен:",fact(n))


# In[ ]:


#Задача 2. Создайте функцию filter_even, которая принимает на вход список целых чисел, и фильтруя, возвращает список, содержащий только четные числа. Используйте filter для фильтрации и lambda.
def filter_even(li):
    print(list(filter(lambda li: li % 2 == 0, li)))
#filter_even([1, 4, 6, 3, 2, 5, 20, 21, 34, 29, 45])


# In[ ]:


#Задача 3.Напишите функцию square ,которая принимает на вход список целых чисел и возвращает список с возведенными в квадрат элементами. Используйте map.
def square(li):
    res = list(map(lambda x: x*x, li))
    return res
#li=[1,3,6,8,2]
#print(square(li))


# In[ ]:


#Задача 4. Напишите функцию бинарного поиска bin_search, которая принимает на вход отсортированный список и элемент. Функция должна возвращать индекс искомого элемента в списке.
def bin_search(li, element):
    start = 0
    end = len(li)
    while start <= end:
        mid = (start+end)//2
        if li[mid] == element:
            return mid
        if element < li[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1
 
#print(bin_search([2, 5, 7, 9, 11, 17, 222], 11))
#print(bin_search([2, 5, 7, 9, 11, 17, 222], 12))


# In[ ]:


#Задача 5. Напишите функцию is_palindrome определяющую,является ли строка палиндромом.
def is_palindrome(string):
    reversed_string = ""
    forbidden = (',', '.', '!', '?', ';', ':', '-',"'","'")
    s = string.replace(" ","")
    s = s.lower()
    for i in s:
        if i in forbidden:
            s = s.replace(i, '')
    for i in range(len(s), 0, -1):
        reversed_string += s[i-1]
    if s == reversed_string:
        print('YES')
    else:
        print('NO')        
#string="Madam, I'm Adam"
#is_palindrome(string)            


# In[ ]:


#Задача 6. Написать функцию calculate,принимает на вход текстовый файл.Формат файла: арифметическая операция целое число #1 целое число #2
def calculate(path2file):
    operators = {
    '+':lambda a, b: a + b,
    '-':lambda a, b: a - b,
    '*':lambda a, b: a * b,
    '//':lambda a, b: a // b,
    '%':lambda a, b: a % b,
    '**':lambda a, b: a ** b,
    }
    with open(path2file, 'r') as fp:
        for n, line in enumerate(fp, 1):
            line = line.rstrip('\n')
            line = line.split()
            for i in operators:
                if i in line:
                    result=operators[i](int(line[1]), int(line[2]))
                    print(result,end=',')
#calculate('calc.txt')                 


# In[ ]:


#Задание 7. Написать функцию substring_slice,которой на вход поступают два текстовых файла.    
def substring_slice(a,b):
    with open(a, 'r') as fp2, open(b, 'r') as fp1:    
        for line1 in fp1:
            line1 = line1.rstrip('\n')
            for line2 in fp2:
                line2=line2.rstrip('\n').split()
                a=int(line2[0])
                b=int(line2[1])+1
                x=slice(a,b)
                print(line1[x],end=' ')
                if line1!=line1[x]:
                    break
#substring_slice('substring_slice2.txt','substring_slice1.txt')                   


# In[ ]:


#Задание 8. Написать функцию decode_ch,на вход которой поступает строка.В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов. Нужно расшифровать химические символы в название химических элементов.Функция должна вернуть строку - расшифровку
import json
def decode_ch(sting_of_elements):
    with open(sting_of_elements, 'r', encoding='utf-8') as j:
        periodic_table = json.load(j)
        a='NOTiFICaTiON'
        a=list(a)
        c=[]
        for i in range(0,len(a)):                 
            if (a[i-1].isupper()==True) and (a[i].isupper()==True):
                for key in periodic_table.keys():
                       if key == a[i-1]:
                            c.append(str(periodic_table.get(key)))
            elif (a[i-1].isupper()==True) and (a[i].isupper()==False):
                b=str(a[i-1])+str(a[i])
                for key in periodic_table.keys():
                    if key == b:
                        c.append(str(periodic_table.get(key)))
        c.append(c.pop(0))                
        print(''.join(c))
#decode_ch('periodic_table.json')    


# In[ ]:


#Задание 9.Создайте класс с названием Student.
class Student:
    
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.fullname = name+' '+surname
        self.grades=grades
 
    def greetings(self):
        return 'Hello, I am Student'
    
    def mean_grade(self):
        mean_grade = sum(self.grades)/len(self.grades)
        return mean_grade
    
    def is_otlichnik(self):
        if self.mean_grade()>=4.5:
            return 'YES'
        else:
            return 'NO'
        
    def __add__(self,student):
        temp=Student(student.name, student.surname, student.grades)
        return temp 

    def summa_studentov(self):
        return f'{student1.name} is friends with {student2.name}'
    
    def print(self):
        print(self.fullname)
    
#student1=Student('Георгий','Якущев',[3,4,5])
#student2=Student('Иван','Иванов',[5,4,5])
#student3=student1+student2
#student3.summa_studentov()


# In[ ]:


#Задание 10. Определите класс исключений MyError, который принимает строковое сообщение msg в качестве параметра при инициализации и также имеет атрибут msg.
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg        

