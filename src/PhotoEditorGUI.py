from typing import Optional, Dict, Callable
from tkinter import Tk
from src.PhotoEditorFunc import PhotoEditorFunc
import tkinter


class ComponentContainer:
    def __init__(self):
        self._menu = {}

    @property
    def Menu(self) -> Dict[str, tkinter.Menu]:
        return self._menu

    @Menu.setter
    def Menu(self, new_menu: Dict[str, tkinter.Menu]):
        self._menu = new_menu


class PhotoEditorGUI:
    def __init__(self):
        self._master = Tk()
        self._photo_editor = PhotoEditorFunc(self._master)
        self._component_container = ComponentContainer()
        self._set_default_window_setting()
        self._set_base_component()
        self._set_menu_component()

    def _set_default_window_setting(self):
        self._master.title("포토 에디터")
        self._master.geometry("500x500")
        self._master.resizable = (False, False)

    def _set_base_component(self):
        base_menu = tkinter.Menu(
            master = self._master
        )
        self._component_container.Menu["base"] = base_menu

    def _create_menu(self,
                     menu_name: str,
                     command_data: Dict[str, Optional[Callable]]):

        base_menu_bar = self._component_container.Menu.get("base")

        menu_obj = tkinter.Menu(
            master = base_menu_bar
        )

        for menu_label, menu_func in command_data.items():
            if menu_func is not None:
                menu_obj.add_command(
                    label = menu_label,
                    command = menu_func
                )
            else:
                menu_obj.add_separator()

        base_menu_bar.add_cascade(
            label = menu_name,
            menu = menu_obj
        )
        self._master.config(menu = base_menu_bar)

    def _set_menu_component(self):
        self._create_menu(
            menu_name = "파일",
            command_data = {
                "파일 열기": self._photo_editor.openfile,
                "파일 저장": self._photo_editor.saveimagefile,
                "sp1": None,
                "프로그램 종료": self._photo_editor.funcexit
            }
        )

        self._create_menu(
            menu_name = "이미지 처리 (1)",
            command_data = {
                "밝게/어둡게": self._photo_editor.bright,
                "sp1": None,
                "엠보싱": self._photo_editor.emboss,
                "블러링": self._photo_editor.blur,
                "sp2": None,
                "연필스케치": self._photo_editor.sketch,
                "경계선 추출": self._photo_editor.edge
            }
        )

        self._create_menu(
            menu_name = "이미지 처리 (2)",
            command_data = {
                "확대": self._photo_editor.zoomin,
                "축소": self._photo_editor.zoomout,
                "sp1": None,
                "상하 반전": self._photo_editor.upsidedown,
                "좌우 반전": self._photo_editor.leftright,
                "회전": self._photo_editor.rotate
            }
        )

    def ShowGUI(self):
        self._master.mainloop()


if __name__ == '__main__':
    PEGUI = PhotoEditorGUI()
    PEGUI.ShowGUI()



