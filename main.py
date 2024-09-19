import tkinter as tk
from tkinter import *
from tkinter import ttk

from EditorMetadata import AppMetadataEditor


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        app_name = "File Editor:\\"

        self.title(f'{app_name}')
        self.geometry('800x450')
        self.resizable(False, False)

        # <<-- Команды виджитов -->>
        def open_metadata():
            pass

        def open_converting():
            pass

        # <<-- Создание виджетов -->>
        btn_metadata = ttk.Button(self, text="Редактор метаинформации", command=open_metadata)
        btn_converting = ttk.Button(self, text="Конвертация файлов", command=open_converting)

        # <<-- Расположение виджетов -->>
        btn_metadata.grid(row=0, column=0)
        btn_converting.grid(row=0, column=1)


# <<-- Запуск приложения -->>
if __name__ == "__main__":
    app = AppMetadataEditor()
    app.mainloop()
