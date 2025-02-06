import dearpygui.dearpygui as dpg

from graphic_configs import WIDTH
from os_api.methods import get_modpacks


class ModsWindow:
    def __init__(self):
        self.selected = None
        with dpg.stage() as stage:
            self._window = dpg.add_child_window(tag="mods_window", width=WIDTH // 2)
            self.update()

        self.stage = stage

    def update(self):
        dpg.push_container_stack(self._window)
        dpg.delete_item(self._window, children_only=True)

        items = [dpg.add_selectable(label=modpack) for modpack in get_modpacks()]
        for item in items:
            if dpg.get_item_label(item) == self.selected:
                dpg.set_value(item, True)
            dpg.configure_item(item, callback=self._selection, user_data=items)

        dpg.pop_container_stack()

    def submit(self):
        dpg.unstage(self.stage)

    def _selection(self, sender, app_data, user_data):
        if dpg.get_value(sender):
            self.selected = dpg.get_item_label(sender)
            dpg.configure_item("buttons_group", enabled=True)
        else:
            self.selected = None
            dpg.configure_item("buttons_group", enabled=False)

        print(self.selected)
        for item in user_data:
            if item != sender:
                dpg.set_value(item, False)

