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

        # cImage가 ChangeImage로 변경되었지만 의존관계에 있는 코드들의 수정이 이루어지지 않았음
        canvas.create_image(0, 0, anchor = NW, image = cImage)
        canvas.pack()

    def _open_file(self):
        file_name = askopenfilename(
            parent = self._master,
            filetypes = (
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
        InPhoto = Image.open(file_name)

        # InX와 InY는 해당 메소드에서 사용하지 않지만 변수가 생성됨.
        InX = InPhoto.width
        InY = InPhoto.height

        OutPhoto = InPhoto.copy()
        OutX = OutPhoto.width
        OutY = OutPhoto.height
        self._display_photo(OutPhoto, OutY, OutX)

    def saveimagefile(self):
        # PhotoEditorFunc.get_OutPhoto 메소드가 정의되지 않았는데 사용함.
        SavePhoto = PhotoEditorFunc.get_OutPhoto()

        if SavePhoto is None:
            return

        SaveFile = asksaveasfile(
            parent = self._master,
            mode = "w",
            defaultextension = ".jpg",
            filetypes = (
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
        scale = askinteger(
            "확대배수",
            "확대할 배수를 입력하세요",
            minvalue = 2,
            maxvalue = 8
        )

        # PhotoEditorFunc.get_OutPhoto 메소드가 정의되지 않았는데 사용함.
        ShowImage = PhotoEditorFunc.get_OutPhoto()

        # PhotoEditorFunc의 멤버변수로 InX, InY는 존재하지 않음.
        # PhotoEditorFunc에 존재하지 않는 메소드에 접근함.
        # InX, InY, scale 전부 int이지만 int 형변환을 사용함. -> 형변환 필요 없음
        ShowImage = ShowImage.resize((int(PhotoEditorFunc.get_InX * scale), int(PhotoEditorFunc.get(InY * scale))))
        ShowImage
