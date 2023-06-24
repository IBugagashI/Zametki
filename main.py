                        # Заметки на Python
from tkinter import *   # tkinter - это кроссплатформенная библиотека для разработки графического интерфейса на языке Python 
from tkinter import messagebox # messagebox - это всплывающее окно, которое появляется на экране для того, чтобы дать вам простую текстовую информацию
from tkinter.filedialog import askopenfile, asksaveasfile # Модуль filedialog предоставляет функциональность файловых диалоговых окон, которые позволяют выбрать файл или каталог для различных задач
                               # askopenfile(): открывает диалоговое окно для выбора файла и возвращает выбранный файл. Если файл не выбран, возвращается None
                               # asksaveasfile(): открывает диалоговое окно для сохранения файла и возвращает сохраненный файл. Если файл не выбран, возвращается None
file_name = NONE

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END) # Удаление всего, что было в заметке. Всё с чистого листа

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.ger('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Нельзя сохранить файл!")

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return file_name == inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

root = Tk() # корневой экземпляр Tk
root.title("Заметки")    # .title - титульное название 
root.geometry("300x300") # .geometry - определяет размер открываемого стикера

text = Text(root, width=300, height=300) # размер поля для ввода текста
text.pack()

menu_bur = Menu(root) 
file_menu = Menu(menu_bur) # переменная, для наполнения Меню функциями действия

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_as)

menu_bur.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bur)
root.mainloop()