from typing import Optional
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.simpledialog import askinteger
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
        ChangeImage = ImageTk.PhotoImage(img)

        canvas.create_image(0, 0, anchor = NW, image = cImage)
        canvas.pack()

    def _open_file(self):
        FileName = askopenfilename(
            parent = self._master,
            filetypes= (("모든 그림 파일", "*.jpg; *.jpeg; *.bmp; *.png; *.tif"), ("모든 파일", " *.* "))
                                   )
        InPhoto = Image.opne(filename)
        InX = InPhoto.width
        InY = InPhoto.height

        OutPhoto = InPhoto.copy()
        OutX = OutPhoto.width
        OutY = OutPhoto.height
        self._display_photo(OutPhoto, OutY, OutX)

    def saveimagefile(self):
        SavePhoto = PhotoEditorFunc.get_OutPhoto()
        if SavePhoto is None:
            return
        SaveFile = asksaveasfile(
            parent=self._master,
            mode="w",
            defaultextension=".jpg",
            filetypes=(("JPG파일", "*.jpg; *jpeg"), ("모든 파일", "*.*"))
        )
        SavePhoto.save(SaveFile.name)
    
    def zoomin(self):
        scale = askinteger(
            "확대배수",
            "확대할 배수를 입력하세요",
            minvalue=2,
            maxvalue=8
        )
        ShowImage = PhotoEditorFunc.get_OutPhoto()
        ShowImage = ShowImage.resize((int(PhotoEditorFunc.get_InX * scale), int(PhotoEditorFunc.get(InY * scale))))
        ShowImage
