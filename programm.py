import tkinter
from tkinter import *
from app.settings import *
from app.TextEditor import *

app = tkinter.Tk() # создаю окно нашего приложения
app.title(APP_NAME) # указываем названия нашего приложения
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

text = tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap='word')
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) # создали скролл
scroll.pack(side='right',fill='y') # разместили наш скролл
text.configure(yscrollcommand=scroll.set) # связь текста со скроллом
text.pack() # разместили поле с текстом

menuBar = tkinter.Menu(app) # создаем меню
editor = Text_editor(text)

app_menu = tkinter.Menu(menuBar) # выпадающее меню у 'Файл'
app_menu.add_command(label='Новый файл', command=editor.new_file)
app_menu.add_command(label='Открыть файл', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

app_note = tkinter.Menu(menuBar)
app_note.add_command(label='Помощь')
app_note.add_command(label='Советы', command=editor.get_info)
app_note.add_command(label='О программе')

# пункты меню
menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Правка')
menuBar.add_cascade(label='Справка', menu=app_note)
menuBar.add_cascade(label='Выход',command=app.quit)

app.config(menu=menuBar) # публикуем меню

app.mainloop() # бесконечный цикл нашего приложения