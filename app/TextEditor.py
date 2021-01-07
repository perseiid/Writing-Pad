import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename# функция сохранить как и открыть файл
from tkinter.messagebox import showerror # показ всех ошибок
import codecs
from tkinter import messagebox

class Text_editor():
    def __init__(self,text):
        self.file_name = tkinter.NONE
        self.text = text

    def new_file(self):
        self.file_name = 'Новый документ'
        self.text.delete('1.0', tkinter.END)

    def open_file(self):
        file = askopenfilename()
        if file is None:
            return
        with codecs.open(file,encoding='utf-8') as inp:
            data = inp.read()
            self.text.delete('1.0', tkinter.END)
            self.text.insert('1.0', data)

    def save_file(self):
        data = self.text.get('1.0', tkinter.END)
        with open(self.file_name, 'w', encoding='utf-8') as output:
            output.write(data)
            output.close()

    def save_as_file(self):
        output = asksaveasfilename()
        data = self.text.get('1.0', tkinter.END)
        try:
            with codecs.open(output+'.txt','w',encoding='utf-8') as file:
                file.write(data.rstrip())
                file.close()
        except Exception:
            showerror(title='Ошибка!',message='Ошибка при сохранения файла!')

    def get_info(self):
        messagebox.showinfo('Справка','Информация о нашем приложении! Спасибо, что его используете :)')