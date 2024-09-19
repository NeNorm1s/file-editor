import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox


class AppMetadataEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        app_name = "File Editor:\\Configuring File Metadata\\"

        self.title(f'{app_name}')
        self.geometry('800x450')
        self.resizable(False, False)

        file_types = ["mp3"]
        file_type = StringVar(value=file_types[0])
        file_name = StringVar()

        audios = Variable(value=[])
        audio_selected = Variable()

        dir_files = Variable()

        # Метаданные
        md_track_number = StringVar()
        md_title = StringVar()
        md_album = StringVar()
        md_artist = StringVar()
        md_artist_album = StringVar()
        md_organization = StringVar()
        md_copyright = StringVar()
        md_composer = StringVar()
        md_conductor = StringVar()
        md_grouping = StringVar()

        ckb_md_track_number = BooleanVar()
        ckb_md_title = BooleanVar()

        # Адаптация под действия
        def ReloadWidgets():
            def state_machine(widgets, state):
                for widget in widgets.winfo_children():
                    try:
                        widget['state'] = state
                    except TclError:
                        pass
            try:
                os.listdir(dir_files.get())
            except FileNotFoundError:
                state_machine(frm_file, tk.DISABLED)
            else:
                state_machine(frm_file, tk.NORMAL)

        def TypingPathDir(*args):
            Select()

        def Select_type(event):
            Select()

        def Select_file(event):
            pass

        def Select():
            # Обновление списка аудио файлов
            def list_update():
                arr = []
                try:
                    for i in os.listdir(dir_files.get()):
                        if i.endswith(file_type.get()):
                            arr.append(i)
                    audios.set(arr)
                    ReloadWidgets()
                except FileNotFoundError:
                    ReloadWidgets()

            list_update()

        # <<-- Создание виджетов -->>
        frm_dir = ttk.Frame(self)
        frm_file = ttk.Frame(self)
        frm_metadata = ttk.Frame(self)

        lsb_dir_audios = Listbox(frm_dir, listvariable=audios)
        lbl_dir_files = ttk.Label(frm_dir, text="Директория:")
        ent_dir_files = ttk.Entry(frm_dir, textvariable=dir_files)
        btn_dir_files = ttk.Button(frm_dir, text="...", command=lambda: dir_files.set(filedialog.askdirectory()))
        lbl_dir_type = ttk.Label(frm_dir, text="Расширение:")
        cmb_dir_type = ttk.Combobox(frm_dir, textvariable=file_type, values=file_types, width=5)

        lbl_file_title = ttk.Label(frm_file, text="Название:")
        ent_file_title = ttk.Entry(frm_file, textvariable=file_name)

        dir_files.trace('w', TypingPathDir)

        cmb_dir_type.bind('<<ComboboxSelected>>', Select_type)
        lsb_dir_audios.bind('<<ListboxSelect>>', Select_file)

        # <<-- Расположение виджетов -->>
        # Фрейм директории
        frm_dir.grid(row=0, column=0)
        lbl_dir_files.grid(row=0, column=0)
        ent_dir_files.grid(row=0, column=1)
        btn_dir_files.grid(row=0, column=2)
        lbl_dir_type.grid(row=1, column=0)
        cmb_dir_type.grid(row=1, column=1)
        lsb_dir_audios.grid(row=0, column=3, rowspan=2, columnspan=2)
        # Фрейм файла
        frm_file.grid(row=1, column=0)
        lbl_file_title.grid(row=0, column=0)
        ent_file_title.grid(row=0, column=1)

        frm_metadata.grid(row=1, column=1)

        ReloadWidgets()
