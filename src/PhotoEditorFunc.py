from typing import Optional
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.simpledialog import askinteger
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk, ImageEnhance, ImageFilter


class PhotoEditorFunc:
    OutPhoto = None

    def __init__(self, gui_master: Tk):
        self._master = gui_master

    def _display_photo(self, height: int, width: int):
        canvas = Canvas(
            master=self._master,
            width=width,
            height=height
        )
        ChangeImage = ImageTk.PhotoImage(OutPhoto)


        canvas.create_image(0, 0, anchor=NW, image=ChangeImage)
        canvas.pack()

    def _open_file(self):
        file_name = askopenfilename(
            parent=self._master,
            filetypes=(
                (
                    "모든 그림 파일",
                    "*.jpg; *.jpeg; *.bmp; *.png; *.tif"
                ),
                (
                    "모든 파일",
                    " *.* "
                )
            )
        )

        OutPhoto = Image.open(file_name)
        OutX = OutPhoto.width
        OutY = OutPhoto.height
        self._display_photo(OutY, OutX)

    def saveimagefile(self):
        SavePhoto = OutPhoto

        if SavePhoto is None:
            return

        SaveFile = asksaveasfile(
            parent=self._master,
            mode="w",
            defaultextension=".jpg",
            filetypes=(
                (
                    "JPG파일",
                    "*.jpg; *jpeg"
                ),
                (
                    "모든 파일",
                    "*.*"
                )
            )
        )
        SavePhoto.save(SaveFile.name)

    def zoomin(self):
        ZoomInScale = askinteger(
            "확대배수",
            "확대할 배수를 입력하세요",
            minvalue=2,
            maxvalue=8
        )


        OutPhoto = OutPhoto.resize((OutPhoto.height * ZoomInScale, OutPhoto.width * ZoomInScale))
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def zoomout(self):
        ZoomOutScale = askinteger(
            "확대배수",
            "확대할 배수를 입력하세요",
            minvalue=2,
            maxvalue=8
        )

        OutPhoto = OutPhoto.resize((OutPhoto.height / ZoomOutScale, OutPhoto.width / ZoomOutScale))
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def upsidedown(self):
        OutPhoto = OutPhoto.transpose(Image.FLIP_TOP_BOTTOM)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def leftright(self):
        OutPhoto = OutPhoto.transpose(Image.FLIP_LEFT_RIGHT)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def rotate(self):
        angle = askinteger(
            "회전",
            "회전할 각도를 입력하세요",
            minvalue=0,
            maxvalue=360
        )

        OutPhoto = OutPhoto.rotate(angle, expand=True)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def bright(self):
        degree = askfloat(
            "밝게/어둡게",
            "값을 입력하세요(0.0 ~ 5.0)",
            minvalue=0.0,
            maxvalue=5.0
        )

        OutPhoto = ImageEnhance.Brightness(OutPhoto).enhance(degree)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def embos(self):
        OutPhoto = OutPhoto.filter(ImageFilter.EMBOSS)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def blur(self):
        OutPhoto = OutPhoto.filter(ImageFilter.BLUR)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def sketch(self):
        OutPhoto = OutPhoto.filter(ImageFilter.CONTOUR)
        self._display_photo(OutPhoto.height, OutPhoto.width)

    def edge(self):
        OutPhoto = OutPhoto.filter(ImageFilter.FIND_EDGES)
        self._display_photo(OutPhoto.height, OutPhoto.width)

