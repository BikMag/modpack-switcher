import dearpygui.dearpygui as dpg

from graphic_configs import WIDTH
from items.modals.error_modal import ErrorModal
from os_api.methods import remove_dir
from items.mods_window import ModsWindow


class DeleteModal:
    def __init__(self, mods_window: ModsWindow):
        with dpg.stage() as stage:
            with dpg.window(label="Delete modpack", modal=True, show=False, tag="delete_modal_id",
                            no_title_bar=False, no_resize=True, no_move=True,
                            width=WIDTH // 4, pos=(200, 200)
                            ):
                dpg.add_text(default_value="Are you sure you want to delete this modpack?",
                             wrap=(WIDTH - 20) // 4)
                with dpg.group(horizontal=True):
                    dpg.add_button(label="OK", callback=self.delete_modpack)
                    dpg.add_button(label="Cancel",
                                   callback=lambda: dpg.configure_item("delete_modal_id", show=False))

        self.stage = stage
        self.mods_window = mods_window

    def submit(self):
        dpg.unstage(self.stage)

    def open_modal(self):
        dpg.configure_item("delete_modal_id", show=True)

    def delete_modpack(self):
        try:
            remove_dir(self.mods_window.selected)
            self.mods_window.selected = None
            self.mods_window.update()
        except FileNotFoundError:
            dpg.configure_item("delete_modal_id", show=False)
            ErrorModal.open_modal("Directory not found")
        except Exception:
            dpg.configure_item("delete_modal_id", show=False)
            ErrorModal.open_modal("Unknown error")

        dpg.configure_item("delete_modal_id", show=False)
        dpg.configure_item("buttons_group", enabled=False)
