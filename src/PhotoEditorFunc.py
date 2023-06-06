from typing import Optional
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.simpledialog import askinteger, askfloat
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageGrab


class PhotoEditorFunc:

    def __init__(self, gui_master: Tk):
        self._master = gui_master
        self._out_photo = None
        self._canvas: Optional[Canvas] = None
        self._color = "black"
        self.start_x, self.start_y = 0, 0
        self.end_x , self.end_y = 0, 0

    def _display_photo(self, height: int, width: int):
        if self._canvas is not None:
            self._canvas.destroy()

        self._canvas = Canvas(
            master=self._master,
            width=width,
            height=height
        )

        ChangeImage = ImageTk.PhotoImage(self._out_photo)

        self._canvas.create_image(0, 0, anchor=NW, image=ChangeImage)
        self._canvas.pack()
        self._master.geometry(f"{width}x{height}")
        self._master.mainloop()

    def openfile(self):
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

        self._out_photo = Image.open(file_name)
        out_x = self._out_photo.width
        out_y = self._out_photo.height
        self._display_photo(out_y, out_x)

    def funcexit(self):
        exit()

    def saveimagefile(self):
        save_photo = self._out_photo

        if save_photo is None:
            return

        save_file = asksaveasfile(
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
        save_photo.save(save_file.name)

    def zoomin(self):
        zoom_in_scale = askinteger(
            "확대배수",
            "확대할 배수를 입력하세요",
            minvalue=2,
            maxvalue=8
        )

        if self._out_photo is not None:
            self._out_photo = self._out_photo.resize(
                (self._out_photo.height * zoom_in_scale, self._out_photo.width * zoom_in_scale))
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def zoomout(self):
        zoom_out_scale = askinteger(
            "확대배수",
            "확대할 배수를 입력하세요",
            minvalue=2,
            maxvalue=8
        )

        if self._out_photo is not None:
            self._out_photo = self._out_photo.resize(
                (self._out_photo.height / zoom_out_scale, self._out_photo.width / zoom_out_scale))
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def upsidedown(self):
        if self._out_photo is not None:
            self._out_photo = self._out_photo.transpose(Image.FLIP_TOP_BOTTOM)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def leftright(self):
        if self._out_photo is not None:
            self._out_photo = self._out_photo.transpose(Image.FLIP_LEFT_RIGHT)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def rotate(self):
        angle = askinteger(
            "회전",
            "회전할 각도를 입력하세요",
            minvalue=0,
            maxvalue=360
        )

        if self._out_photo is not None:
            self._out_photo = self._out_photo.rotate(angle, expand=True)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def bright(self):
        degree = askfloat(
            "밝게/어둡게",
            "값을 입력하세요(0.0 ~ 5.0)",
            minvalue=0.0,
            maxvalue=5.0
        )

        if self._out_photo is not None:
            self._out_photo = ImageEnhance.Brightness(self._out_photo).enhance(degree)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def emboss(self):
        if self._out_photo is not None:
            self._out_photo = self._out_photo.filter(ImageFilter.EMBOSS)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def blur(self):
        if self._out_photo is not None:
            self._out_photo = self._out_photo.filter(ImageFilter.BLUR)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def sketch(self):
        if self._out_photo is not None:
            self._out_photo = self._out_photo.filter(ImageFilter.CONTOUR)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def edge(self):
        if self._out_photo is not None:
            self._out_photo = self._out_photo.filter(ImageFilter.FIND_EDGES)
            self._display_photo(self._out_photo.height, self._out_photo.width)

    def cred(self):
        self._color = "red"

    def cblue(self):
        self._color = "blue"

    def cyellow(self):
        self._color = "yellow"

    def cblack(self):
        self._color = "black"

    def startpoint(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def endpoint(self, event):
        self.end_x = event.x
        self.end_y = event.y

    def reset(self):
        self.start_x, self.start_y, self.end_x, self.end_y = 0, 0, 0, 0

    def setting(self):
        self._master.bind("<Button-1>", self.startpoint)
        self._master.bind("<ButtonRelease-1>", self.endpoint)

    def oval(self):
        self.setting()
        self._canvas.create_oval(
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y,
            outline=self._color
        )

        self.reset()

    def line(self):
        self.setting()
        self._canvas.create_line(
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y,
            width=1,
            fill=self._color
        )

        self.reset()

    def rect(self):
        self.setting()
        self._canvas.create_rectangle(
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y,
            outline=self._color
        )

        self.reset()