from tkinter import *
from tkinter import ttk
import random
from Пузырьком import bubble_sort
from Быстрая import quick_sort
root = Tk()
root.title('Сортировка')
root.maxsize(800, 600)
root.configure(background = 'black')
#
selected_alg = StringVar()
data = []

def drawData(data, color):
    canvas.delete(('all'))
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data)+1)
    offset = 30
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i,height in enumerate(normalizedData):
        x0 = i * x_width+offset+spacing
        y0 = c_height - height * 340
        x1 = (i+1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Generate():
    try:
        size = int(sizeEntry.get())
    except:
        size = 6
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 15

    if minVal < 0: minVal = 0
    if maxVal > 100: maxVal = 50
    if size > 30 or size < 3: size = 20
    if minVal > maxVal: minVal, maxVal = maxVal, minVal
    global data
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data, ['red' for x in range(len(data))])

def StartAlg():
    global data
    if not data: return
    if algMenu.get() == 'Быстрая сортировка':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    elif algMenu.get() == 'Сортировка пузырьком':
        bubble_sort(data, drawData, speedScale.get())


#Рамка и холст
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380)
canvas.grid(row=1, column=0, padx=10, pady=5)
#Интерфейс

#Ряд 0
Label(UI_frame, text='Алгоритм', bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Сортировка пузырьком', 'Быстрая сортировка'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=130, resolution=0.2, orient=HORIZONTAL, label='Выберете скорость [s]')
speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text='Старт', command=StartAlg, bg='red').grid(row=0, column=3, padx=5, pady=5)
Button(UI_frame, text='Сгенерировать', command=Generate, bg='white').grid(row=0, column=4, padx=5, pady=5)

#Ряд 1
Label(UI_frame, text='Размер', bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text='Мин. знач.', bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text='Макс. знач.', bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)






root.mainloop()