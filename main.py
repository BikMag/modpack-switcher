import asyncio

import dearpygui.dearpygui as dpg
import ctypes

from graphic_configs import WIDTH, HEIGHT, FONT_SIZE
from items.modals.create_modal import CreateModal
from items.modals.delete_modal import DeleteModal
from os_api.config import DESTINATION_DIR
from os_api.methods import get_modpacks, get_mods, move_modpack, rename_dir, open_dir
from items.modals.rename_modal import RenameModal
from items.mods_window import ModsWindow


async def activate_modpack(modpack):
    dpg.configure_item("loading_window", show=True)
    move_modpack(modpack)
    open_dir(DESTINATION_DIR)
    await asyncio.sleep(0.5)
    dpg.configure_item("loading_window", show=False)


def show_mods(modpack):
    with dpg.window(label="Mods", width=WIDTH // 2, height=HEIGHT - 100):
        for i, mod in enumerate(get_mods(modpack)):
            dpg.add_text(default_value=f'{i+1}. {mod}')


def start_app():
    dpg.create_context()
    dpg.create_viewport(width=WIDTH, height=HEIGHT, title="Mode Switcher")

    mods_window = ModsWindow()
    rename_modal = RenameModal(mods_window)
    create_modal = CreateModal(mods_window)
    delete_modal = DeleteModal(mods_window)


    with dpg.font_registry():
        with dpg.font("static/fonts/NotoSerifCJKjp-Medium.otf", FONT_SIZE) as font1:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    dpg.bind_font(font1)
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

    with dpg.window(tag="loading_window", pos=(250, 200) , modal=True, no_title_bar=True, show=False):
        with dpg.group(horizontal=True):
            dpg.add_loading_indicator(circle_count=8)
            dpg.add_text("Moving mods, please wait...")

    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Save As")

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Setting 1", check=True)
                dpg.add_menu_item(label="Setting 2")

        dpg.add_menu_item(label="Help")

        with dpg.menu(label="Widget Items"):
            dpg.add_checkbox(label="Pick Me")
            dpg.add_button(label="Press Me")
            dpg.add_color_picker(label="Color Me")

    # rename_modal.submit() - ???
    with dpg.window(tag="main_window"):
        dpg.add_text()
        with dpg.group(horizontal=True):
            mods_window.submit()

            with dpg.group(tag="buttons_group", enabled=False):
                dpg.add_button(label="Accept", callback=lambda: asyncio.run(activate_modpack(mods_window.selected)))
                dpg.add_button(label="Show mods", callback=lambda: show_mods(mods_window.selected))
                dpg.add_button(label="Rename", callback=rename_modal.open_modal)
                dpg.add_button(label="Delete", callback=delete_modal.open_modal)

            dpg.add_button(label="Update", callback=mods_window.update)
            dpg.add_button(label="Create", callback=create_modal.open_modal, tag='btn')

    dpg.show_item_registry()

    dpg.set_primary_window("main_window", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    start_app()
