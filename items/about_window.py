import dearpygui.dearpygui as dpg


def add_about_window():
    with dpg.window(
        tag="about_window",
        label="About app", show=False
    ):
        with dpg.table(header_row=False):
            dpg.add_table_column()
            dpg.add_table_column()

            with dpg.table_row():
                dpg.add_text("Application name:")
                dpg.add_text("Modpack Switcher")
            with dpg.table_row():
                dpg.add_text("Author:")
                dpg.add_text("Denis Bikmaev (BikMag)")
            with dpg.table_row():
                dpg.add_text("Used GUI tool:")
                dpg.add_text("Dear Pygui 2.0.0")
            with dpg.table_row():
                dpg.add_text("Used font:")
                dpg.add_text("Minecraft RUS NEW")


def open_about_window():
    dpg.show_item("about_window")