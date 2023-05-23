from typing import Optional
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk


class PhotoEditorFunc:
    def __init__(self, gui_master: Tk):
        self._master = gui_master

    def _display_photo(self, img: Image, height: int, width: int):
        canvas = Canvas(
            master = self._master,
            width = width,
            height = height
        )
        cImage = ImageTk.PhotoImage(img)

        canvas.create_image(0, 0, anchor = NW, image = cImage)
        canvas.pack()

