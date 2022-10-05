import tkinter
import os
import pathlib
from tkinter import Tk,Tcl
from tkinter.filedialog import askdirectory

# codigo para mostrar el gestor de archivos
def gestorDeArchivos():
    Tk().withdraw()
    filename = askdirectory(
        initialdir="D://"
    )
    path = pathlib.Path(filename).absolute()
    videos = os.listdir(path)

    videos = list(
        filter(
            lambda name: ".mp4" in name,
            videos
        )
    )

    for index, content in enumerate(videos):
        print(
            f"Video {index}: {content}"
        )
gestorDeArchivos()
# fin codigo de gestor de archivos