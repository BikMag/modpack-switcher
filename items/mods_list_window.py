import dearpygui.dearpygui as dpg

from graphic_configs import WIDTH, HEIGHT
from items.modals.error_modal import ErrorModal
from os_api.methods import get_mods


def add_mods_list_window():
    dpg.add_window(
        tag="mods_list",
        label="Mods", show=False,
        width=WIDTH // 2, height=HEIGHT * 0.8,
        pos=(10, HEIGHT // 10)
    )


def open_mods_list_window(modpack):
    try:
        mods = get_mods(modpack)
    except FileNotFoundError:
        ErrorModal.open_modal("Directory with that name doesn't exist")
    else:
        dpg.delete_item("mods_list", children_only=True)
        dpg.configure_item(
            "mods_list",
            width=WIDTH // 2, height=HEIGHT * 0.5,
            pos=(WIDTH // 3 + 20, HEIGHT // 3.5)
        )

        for i, mod in enumerate(mods):
            dpg.add_text(default_value=f'{i+1}. {mod}', parent="mods_list")

        dpg.show_item("mods_list")