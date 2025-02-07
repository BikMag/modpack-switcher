import dearpygui.dearpygui as dpg

from graphic_configs import WIDTH
from items.modals.error_modal import ErrorModal
from os_api.methods import rename_dir
from items.mods_window import ModsWindow


class RenameModal:
    def __init__(self, mods_window: ModsWindow):
        with dpg.stage() as stage:
            with dpg.window(label="Rename modpack", modal=True, show=False, tag="rename_modal_id",
                            no_title_bar=False, no_resize=True, no_move=True,
                            width=WIDTH // 4, pos=(200, 200)
                            ):
                dpg.add_text(default_value="modpack name")
                value = dpg.add_input_text(hint="enter modpack name here",
                                           tag="rename_modal_input", on_enter=True,
                                           callback=lambda: self.rename_modpack(dpg.get_value(value)),
                                           auto_select_all=True)
                with dpg.group(horizontal=True):
                    dpg.add_button(label="OK", callback=lambda: self.rename_modpack(dpg.get_value(value)))
                    dpg.add_button(label="Cancel",
                                   callback=lambda: dpg.configure_item("rename_modal_id", show=False))

        self.stage = stage
        self.mods_window = mods_window

    def submit(self):
        dpg.unstage(self.stage)

    def open_modal(self):
        dpg.set_value("rename_modal_input", self.mods_window.selected)
        dpg.focus_item("rename_modal_input")
        dpg.configure_item("rename_modal_id", show=True)

    def rename_modpack(self, new_name):
        try:
            rename_dir(self.mods_window.selected, new_name)
            self.mods_window.selected = new_name
        except FileExistsError:
            dpg.configure_item("rename_modal_id", show=False)
            ErrorModal.open_modal("Directory with that name is already exists")
        except ValueError:
            dpg.configure_item("rename_modal_id", show=False)
            ErrorModal.open_modal(f"Directory must not be empty and contain characters ^\\/:*?\"<>|")
        except Exception:
            dpg.configure_item("rename_modal_id", show=False)
            ErrorModal.open_modal("Unknown error")

        self.mods_window.update()
        dpg.configure_item("rename_modal_id", show=False)


