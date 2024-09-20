import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox, Variable, StringVar, BooleanVar, Listbox

import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC


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
        file_selected = Variable()

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
            # try:
            #     # audio_metadata = MP3(str(f"{dir_files.get()}/{lsb_dir_audios.get(lsb_dir_audios.curselection())}"))
            #     audio_metadata = EasyID3(str(f"{dir_files.get()}/{lsb_dir_audios.get(lsb_dir_audios.curselection())}"))
            #     # audio_metadata = mutagen.File(str(f"{dir_files.get()}/{lsb_dir_audios.get(lsb_dir_audios.curselection())}"))
            #     file_selected.set(lsb_dir_audios.get(lsb_dir_audios.curselection()))
            #     file_name.set(str(lsb_dir_audios.get(lsb_dir_audios.curselection()))[:-4])

#                 # print(mutagen.Metadata(str(f"{dir_files.get()}/{lsb_dir_audios.get(lsb_dir_audios.curselection())}")))

#                 def set(var, tag):
#                     if audio_metadata.get(tag):
#                         var.set(audio_metadata.get(tag))
#                     else:
#                         var.set("")

#                 set(md_track_number, 'tracknumber')
#                 set(md_title, 'title')
#                 set(md_album, 'album')
#                 set(md_artist, 'artist')
#                 set(md_artist_album, 'albumartist')
#                 set(md_organization, 'organization')
#                 set(md_copyright, 'copyright')
#                 set(md_composer, 'composer')
#                 set(md_conductor, 'conductor')
#                 set(md_grouping, 'grouping')
#             except TclError:
#                 pass

        def Select():
            # Обновление списка аудио файлов
            arr = []
            try:
                for i in os.listdir(dir_files.get()):
                    if i.endswith(file_type.get()):
                        arr.append(i)
                audios.set(arr)
                ReloadWidgets()
            except FileNotFoundError:
                ReloadWidgets()

        # <<-- Создание виджетов -->>
        frm_dir = ttk.Frame(self)
        frm_file = ttk.Frame(self)
        # frm_metadata = ttk.Frame(self)

        lsb_dir_audios = Listbox(frm_dir, listvariable=audios)
        lbl_dir_files = ttk.Label(frm_dir, text="Директория:")
        ent_dir_files = ttk.Entry(frm_dir, textvariable=dir_files)
        btn_dir_files = ttk.Button(frm_dir, text="...", command=lambda: dir_files.set(filedialog.askdirectory()))
        lbl_dir_type = ttk.Label(frm_dir, text="Расширение:")
        cmb_dir_type = ttk.Combobox(frm_dir, textvariable=file_type, values=file_types, width=5)

        lbl_file_title = ttk.Label(frm_file, text="Название файла:")
        ent_file_title = ttk.Entry(frm_file, textvariable=file_name)
        lbl_md_track_number = ttk.Label(frm_file, text="Номер трека:")
        ent_md_track_number = ttk.Entry(frm_file, textvariable=md_track_number)
        lbl_md_title = ttk.Label(frm_file, text="Название трека:")
        ent_md_title = ttk.Entry(frm_file, textvariable=md_title)
        lbl_md_album = ttk.Label(frm_file, text="Альбом:")
        ent_md_album = ttk.Entry(frm_file, textvariable=md_album)
        lbl_md_artist = ttk.Label(frm_file, text="Исполнители:")
        ent_md_artist = ttk.Entry(frm_file, textvariable=md_artist)
        lbl_md_artist_album = ttk.Label(frm_file, text="Исполнители альбома:")
        ent_md_artist_album = ttk.Entry(frm_file, textvariable=md_artist_album)
        lbl_md_organization = ttk.Label(frm_file, text="Издатель:")
        ent_md_organization = ttk.Entry(frm_file, textvariable=md_organization)
        lbl_md_copyright = ttk.Label(frm_file, text="Авторские права:")
        ent_md_copyright = ttk.Entry(frm_file, textvariable=md_copyright)
        lbl_md_composer = ttk.Label(frm_file, text="Композитор:")
        ent_md_composer = ttk.Entry(frm_file, textvariable=md_composer)
        lbl_md_conductor = ttk.Label(frm_file, text="Дирижёр:")
        ent_md_conductor = ttk.Entry(frm_file, textvariable=md_conductor)
        lbl_md_grouping = ttk.Label(frm_file, text="Описание группы:")
        ent_md_grouping = ttk.Entry(frm_file, textvariable=md_grouping)

        # Настройка виджетов
        dir_files.trace('w', TypingPathDir)

        cmb_dir_type.bind('<<ComboboxSelected>>', Select_type)
        lsb_dir_audios.bind('<<ListboxSelect>>', Select_file)

        # <<-- Расположение виджетов -->>
        # Фрейм директории
        frm_dir.grid(row=0, column=0, sticky=W)
        lbl_dir_files.grid(row=0, column=0, sticky=W)
        ent_dir_files.grid(row=0, column=1, sticky=W)
        btn_dir_files.grid(row=0, column=2, sticky=W)
        lbl_dir_type.grid(row=1, column=0, sticky=W)
        cmb_dir_type.grid(row=1, column=1, sticky=W)
        lsb_dir_audios.grid(row=5, column=0, rowspan=2, columnspan=3, sticky=NSEW)
        # Фрейм файла
        frm_file.grid(row=0, column=1, sticky=W)
        lbl_file_title.grid(row=0, column=0, sticky=W)
        ent_file_title.grid(row=0, column=1, sticky=W)
        lbl_md_track_number.grid(row=1, column=0, sticky=W)
        ent_md_track_number.grid(row=1, column=1, sticky=W)
        lbl_md_title.grid(row=2, column=0, sticky=W)
        ent_md_title.grid(row=2, column=1, sticky=W)
        lbl_md_album.grid(row=3, column=0, sticky=W)
        ent_md_album.grid(row=3, column=1, sticky=W)
        lbl_md_artist.grid(row=4, column=0, sticky=W)
        ent_md_artist.grid(row=4, column=1, sticky=W)
        lbl_md_artist_album.grid(row=5, column=0, sticky=W)
        ent_md_artist_album.grid(row=5, column=1, sticky=W)
        lbl_md_organization.grid(row=6, column=0, sticky=W)
        ent_md_organization.grid(row=6, column=1, sticky=W)
        lbl_md_copyright.grid(row=7, column=0, sticky=W)
        ent_md_copyright.grid(row=7, column=1, sticky=W)
        lbl_md_composer.grid(row=8, column=0, sticky=W)
        ent_md_composer.grid(row=8, column=1, sticky=W)
        lbl_md_conductor.grid(row=9, column=0, sticky=W)
        ent_md_conductor.grid(row=9, column=1, sticky=W)
        lbl_md_grouping.grid(row=10, column=0, sticky=W)
        ent_md_grouping.grid(row=10, column=1, sticky=W)

        ReloadWidgets()
