import dearpygui.dearpygui as dpg

from graphic_configs import WIDTH


class ErrorModal:
    @staticmethod
    def open_modal(text):
        dpg.render_dearpygui_frame()
        with dpg.window(label="Error!", modal=True, tag="error_modal_id",
                        no_title_bar=False, no_resize=True, no_move=True,
                        width=WIDTH // 4, pos=(200, 200)
                        ):
            dpg.add_text(default_value=text,
                         wrap=(WIDTH - 20) // 4)
            dpg.add_button(label="OK", width=80,
                           callback=lambda: dpg.delete_item("error_modal_id"))
