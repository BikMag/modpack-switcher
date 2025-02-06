import dearpygui.dearpygui as dpg

from os_api.methods import create_dir
from items.mods_window import ModsWindow


class CreateModal:
    def __init__(self, mods_window: ModsWindow):
        with dpg.stage() as stage:
            with dpg.window(label="Create modpack", modal=True, show=False, tag="create_modal_id",
                            no_title_bar=False, no_resize=True, no_move=True,
                            width=220, pos=(200, 200)
                            ):
                dpg.add_text(default_value="modpack name")
                value = dpg.add_input_text(hint="enter modpack name here", width=200,
                                           tag="create_modal_input", on_enter=True,
                                           callback=lambda: self.create_modpack(dpg.get_value(value)),
                                           auto_select_all=True)
                with dpg.group(horizontal=True):
                    dpg.add_button(label="OK", width=75, callback=lambda: self.create_modpack(dpg.get_value(value)))
                    dpg.add_button(label="Cancel", width=75,
                                   callback=lambda: dpg.configure_item("create_modal_id", show=False))

        self.stage = stage
        self.mods_window = mods_window

    def submit(self):
        dpg.unstage(self.stage)

    def open_modal(self):
        dpg.set_value("create_modal_input", "")
        dpg.focus_item("create_modal_input")
        dpg.configure_item("create_modal_id", show=True)

    def create_modpack(self, new_name):
        create_dir(new_name)
        self.mods_window.selected = new_name
        self.mods_window.update()
        dpg.configure_item("create_modal_id", show=False)
        dpg.configure_item("buttons_group", enabled=True)


