import dearpygui.dearpygui as dpg

from graphic_configs import WIDTH
from items.modals.error_modal import ErrorModal
from os_api.methods import create_dir
from items.mods_window import ModsWindow


class CreateModal:
    def __init__(self, mods_window: ModsWindow):
        with dpg.stage() as stage:
            with dpg.window(label="Create modpack", modal=True, show=False, tag="create_modal_id",
                            no_title_bar=False, no_resize=True, no_move=True,
                            width=WIDTH // 3, pos=(200, 200)
                            ):
                dpg.add_text(default_value="Modpack name")
                value = dpg.add_input_text(hint="Enter modpack name here",
                                           tag="create_modal_input", on_enter=True,
                                           callback=lambda: self.create_modpack(dpg.get_value(value)),
                                           auto_select_all=True, width=-1)
                with dpg.group(horizontal=True):
                    dpg.add_button(label="OK", callback=lambda: self.create_modpack(dpg.get_value(value)))
                    dpg.add_button(label="Cancel",
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
        try:
            create_dir(new_name)
            self.mods_window.selected = new_name
            self.mods_window.update()
        except FileExistsError:
            dpg.configure_item("create_modal_id", show=False)
            ErrorModal.open_modal("Directory with that name is already exists")
        except ValueError:
            dpg.configure_item("create_modal_id", show=False)
            ErrorModal.open_modal(f"Directory must not be empty and contain characters ^\\/:*?\"<>|")
        except Exception:
            dpg.configure_item("create_modal_id", show=False)
            ErrorModal.open_modal("Unknown error")

        dpg.configure_item("create_modal_id", show=False)
        dpg.configure_item("buttons_group", enabled=True)


