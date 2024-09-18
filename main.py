import tkinter as tk
from tkinter import *
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        app_name = "File Editor:\\"

        self.title(f'{app_name}')
        self.geometry('800x450')
        self.resizable(False, False)

        # Создание виджетов
        btn_metadata = ttk.Button(self, text="Редактор метаинформации")
        btn_converting = ttk.Button(self, text="Конвертация файлов")

        # Расположение виджетов
        btn_metadata.grid(row=0, column=0)
        btn_converting.grid(row=0, column=1)


# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.mainloop()
