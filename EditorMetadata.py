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

        audios = Variable()
        audio_selected = Variable()

        dir_state = Variable()
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

        def Dir(com):
            match com:
                case "search":
                    return filedialog.askdirectory()

        frm_dir = ttk.Frame(self)
        frm_metadata = ttk.Frame(self)

        lbl_dir_files = ttk.Label(frm_dir, text="Директория:")
        ent_dir_files = ttk.Entry(frm_dir, textvariable=dir_files)
        btn_dir_files = ttk.Button(frm_dir, text="...", command=lambda: dir_files.set(Dir("search")))

        # <<-- Расположение виджетов -->>
        #
        frm_dir.grid(row=0, column=0)

        lbl_dir_files.grid(row=0, column=0)
        ent_dir_files.grid(row=0, column=1)
        btn_dir_files.grid(row=0, column=2)
