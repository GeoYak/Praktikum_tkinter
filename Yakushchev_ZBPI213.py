


#Задача 1. Напишите рекурсивную функцию fact, которая вычисляет факториал заданного числа x.
def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n * fact(n-1))
#n = int(input("Введите число: "))
#print("Факториал числа равен:",fact(n))



#Задача 2. Создайте функцию filter_even, которая принимает на вход список целых чисел, и фильтруя, возвращает список, содержащий только четные числа. Используйте filter для фильтрации и lambda.
def filter_even(li):
    return list(filter(lambda li: li % 2 == 0, li))
#filter_even([1, 4, 6, 3, 2, 5, 20, 21, 34, 29, 45])



#Задача 3.Напишите функцию square ,которая принимает на вход список целых чисел и возвращает список с возведенными в квадрат элементами. Используйте map.
def square(li):
    res = list(map(lambda x: x*x, li))
    return res
#li=[1,3,6,8,2]
#print(square(li))




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



#Задача 5. Напишите функцию is_palindrome определяющую,является ли строка палиндромом.
def is_palindrome(string):
    stringg = []
    for i in string.lower():
        if i.isalpha():
            stringg.append(i)
    low = 0
    high = len(stringg)-1
    while low < high:
        if stringg[low] == stringg[high]:
            low += 1
            high -=1
        else:
            return 'NO'
    return 'YES'        
#string="Madam, I'm Adam"
#is_palindrome(string)            



#Задача 6. Написать функцию calculate,принимает на вход текстовый файл.Формат файла: арифметическая операция целое число #1 целое число #2
def calculate(file_name):

    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '**': lambda x, y: x ** y,
                 '//': lambda x, y: x // y,
                 '%': lambda x, y: x % y
                 }
    
    with open(file_name, 'r', encoding='utf-8') as f:
        
        items = f.read().splitlines()
        res = []
        
        for item in items:
            item = item.split('    ')
            res.append(str(operators[item[0]](int(item[1]), int(item[2]))))
        return ','.join(res)
#calculate('calc.txt')                 



#Задание 7. Написать функцию substring_slice,которой на вход поступают два текстовых файла.    
def substring_slice(first_file, second_file):

    with open(first_file, 'r', encoding="utf-8") as f1, open(second_file, 'r', encoding="utf-8") as f2:

        string_file = f1.read().splitlines()
        nums_file = [[int(i) for i in item.split(' ')] for item in f2.read().split('\n')]
        res = []
        
        for i in range(len(nums_file)):
            string = string_file[i][nums_file[i][0]:nums_file[i][1] + 1]
            res.append(string)
        return ' '.join(res)

#substring_slice('substring_slice2.txt','substring_slice1.txt')                   



#Задание 8. Написать функцию decode_ch,на вход которой поступает строка.В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов. Нужно расшифровать химические символы в название химических элементов.Функция должна вернуть строку - расшифровку
import json
def decode_ch(sting_of_elements):
    with open('periodic_table.json', 'r', encoding='utf-8') as j:
        periodic_table = json.load(j)
        sting_of_elements=list(sting_of_elements)
        c=[]
        for i in range(0,len(sting_of_elements)):                 
            if (sting_of_elements[i-1].isupper()==True) and (sting_of_elements[i].isupper()==True):
                for key in periodic_table.keys():
                       if key == sting_of_elements[i-1]:
                            c.append(str(periodic_table.get(key)))
            elif (sting_of_elements[i-1].isupper()==True) and (sting_of_elements[i].isupper()==False):
                b=str(sting_of_elements[i-1])+str(sting_of_elements[i])
                for key in periodic_table.keys():
                    if key == b:
                        c.append(str(periodic_table.get(key)))
        c.append(c.pop(0))                
        d=''.join(c)
        return d
#decode_ch('NOTiFICaTiON')



#Задание 9.Создайте класс с названием Student.
class Student:
    
    def __init__(self, name, surname, grades=[3,4,5]):
        self.name = name
        self.surname = surname
        self.fullname = f'{name} {surname}'
        self.grades = grades
  
    def greeting(self):
        return f'Hello, I am Student'
    
    def mean_grade(self):
        self.mean_grade = sum(self.grades)/len(self.grades)
        return self.mean_grade
    
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
    
    def polnoe_imya(self):
        return self.fullname
    
#student1=Student('Георгий','Якущев',[3,4,5])
#student2=Student('Иван','Иванов',[5,4,5])
#student3=student1+student2
#student3.summa_studentov()



#Задание 10. Определите класс исключений MyError, который принимает строковое сообщение msg в качестве параметра при инициализации и также имеет атрибут msg.
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg        

