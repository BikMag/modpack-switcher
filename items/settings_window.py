import dearpygui.dearpygui as dpg

import os_api.config as api_conf
from graphic_configs import WIDTH



def change_directory_paths(modpacks_dir, destination_dir):
    api_conf.save_data(modpacks_dir, destination_dir)
    dpg.hide_item("settings_window")


def callback(sender, app_data, user_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)
    dpg.set_value(user_data, app_data["file_path_name"])


def open_file_dialog(item):
    dpg.configure_item("file_dialog_id", default_path=dpg.get_value(item))
    dpg.set_item_user_data("file_dialog_id", item)
    dpg.set_item_callback("file_dialog_id", callback)
    dpg.show_item("file_dialog_id")


def add_settings_window():
    dpg.add_file_dialog(
        directory_selector=True, show=False, callback=callback,
        tag="file_dialog_id", label="Directory selection",
        width=WIDTH * 0.8, height=WIDTH * 0.5,
        file_count=1, modal=True
    )

    with dpg.window(tag="settings_window", label="Settings", width=WIDTH * 0.6, show=False) as settings_window:
        dpg.add_text("Modpacks directory:")
        with dpg.group(horizontal=True):
            dpg.add_button(
                tag="modpack_dir_select",
                label="Select",
                callback=lambda: open_file_dialog(modpacks_dir_input)
            )
            modpacks_dir_input = dpg.add_input_text(
                tag="modpacks_dir_input",
                width=-1,
                default_value=api_conf.MODPACK_DIR,
                enabled=False
            )

        dpg.add_text("Destination directory:")
        with dpg.group(horizontal=True):
            dpg.add_button(
                tag="destination_dir_select",
                label="Select",
                callback=lambda: open_file_dialog(destination_dir_input)
            )
            destination_dir_input = dpg.add_input_text(
                tag="destination_dir_input",
                width=-1,
                default_value=api_conf.DESTINATION_DIR,
                enabled=False
            )

        dpg.add_button(
            label="Save",
            callback=lambda: change_directory_paths(
                dpg.get_value(modpacks_dir_input),
                dpg.get_value(destination_dir_input)
            )
        )

        dpg.add_text("*After changing the directory, press 'Update' button.")


def open_settings_window():
    dpg.configure_item("modpacks_dir_input", default_value=api_conf.MODPACK_DIR)
    dpg.configure_item("destination_dir_input", default_value=api_conf.DESTINATION_DIR)
    dpg.show_item("settings_window")
