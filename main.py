import asyncio
import os

import dearpygui.dearpygui as dpg
import ctypes

from graphic_configs import WIDTH, HEIGHT, FONT_SIZE
from items.about_window import add_about_window, open_about_window
from items.modals.create_modal import CreateModal
from items.modals.delete_modal import DeleteModal
from items.modals.error_modal import ErrorModal
import os_api.config as api_conf
from items.mods_list_window import add_mods_list_window, open_mods_list_window
from items.settings_window import add_settings_window, open_settings_window
from os_api.methods import move_modpack, open_dir
from items.modals.rename_modal import RenameModal
from items.mods_window import ModsWindow


async def activate_modpack(modpack):
    dpg.configure_item("loading_window", show=True)
    try:
        move_modpack(modpack)
        open_dir(api_conf.DESTINATION_DIR)
        await asyncio.sleep(0.5)
    except FileNotFoundError:
        dpg.configure_item("loading_window", show=False)
        ErrorModal.open_modal("Directory not found")

    dpg.configure_item("loading_window", show=False)


def start_app():
    dpg.create_context()
    dpg.create_viewport(width=WIDTH, height=HEIGHT, title="Modpack Switcher")

    mods_window = ModsWindow()
    rename_modal = RenameModal(mods_window)
    create_modal = CreateModal(mods_window)
    delete_modal = DeleteModal(mods_window)

    add_settings_window()
    add_mods_list_window()
    add_about_window()

    with dpg.font_registry():
        with dpg.font("static/fonts/Minecraft.otf", FONT_SIZE) as font1:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    dpg.bind_font(font1)
    dpg.set_global_font_scale(0.7)
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

    with dpg.window(tag="loading_window", pos=(250, 200) , modal=True, no_title_bar=True, show=False):
        with dpg.group(horizontal=True):
            dpg.add_loading_indicator(circle_count=8)
            dpg.add_text("Moving mods, please wait...")

    with dpg.viewport_menu_bar():
        dpg.add_menu_item(tag="settings_button", label="Settings", callback=open_settings_window)
        dpg.add_menu_item(tag="about_button", label="About", callback=open_about_window)
        dpg.add_menu_item(label="Debug", callback=dpg.show_item_registry)

    # rename_modal.submit() - ???
    with dpg.window(tag="main_window"):
        dpg.add_text("")
        with dpg.group(horizontal=True):
            dpg.add_text("Mods:")
            dpg.add_button(label="Update", callback=mods_window.update)
            dpg.add_button(label="Create", callback=create_modal.open_modal)

        with dpg.group(horizontal=True):
            mods_window.submit()

            with dpg.group(tag="buttons_group", enabled=False):
                dpg.add_button(label="Accept", width=WIDTH // 6, callback=lambda: asyncio.run(activate_modpack(mods_window.selected)))
                dpg.add_button(label="Show mods", width=WIDTH // 6, callback=lambda: open_mods_list_window(mods_window.selected))
                dpg.add_button(label="Rename", width=WIDTH // 6, callback=rename_modal.open_modal)
                dpg.add_button(label="Delete", width=WIDTH // 6, callback=delete_modal.open_modal)

    dpg.set_primary_window("main_window", True)
    dpg.set_viewport_small_icon(os.path.join(api_conf.BASE_DIR, "images\\logo.ico"))
    dpg.set_viewport_large_icon(os.path.join(api_conf.BASE_DIR, "images\\logo.ico"))
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    start_app()
