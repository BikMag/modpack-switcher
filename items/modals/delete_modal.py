import dearpygui.dearpygui as dpg

from os_api.methods import remove_dir
from items.mods_window import ModsWindow


class DeleteModal:
    def __init__(self, mods_window: ModsWindow):
        with dpg.stage() as stage:
            with dpg.window(label="Delete modpack", modal=True, show=False, tag="delete_modal_id",
                            no_title_bar=False, no_resize=True, no_move=True,
                            width=220, pos=(200, 200)
                            ):
                dpg.add_text(default_value="Are you sure you want to delete this modpack?",
                             wrap=200)
                with dpg.group(horizontal=True):
                    dpg.add_button(label="OK", width=75, callback=self.delete_modpack)
                    dpg.add_button(label="Cancel", width=75,
                                   callback=lambda: dpg.configure_item("delete_modal_id", show=False))

        self.stage = stage
        self.mods_window = mods_window

    def submit(self):
        dpg.unstage(self.stage)

    def open_modal(self):
        dpg.configure_item("delete_modal_id", show=True)

    def delete_modpack(self):
        remove_dir(self.mods_window.selected)
        self.mods_window.selected = None
        self.mods_window.update()
        dpg.configure_item("delete_modal_id", show=False)
        dpg.configure_item("buttons_group", enabled=False)
