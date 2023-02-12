import flet as ft

from flet.window_drag_area import WindowDragArea


def main(page: ft.Page):

    def counter(e):
        tf.counter_text = f"{len(tf.value)}/20"
        page.update()

    page.window_width = 400
    page.window_height = 700
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme = ft.Theme(color_scheme_seed="pink")

    tf = ft.TextField(
        hint_text="password",
        # label="username:",
        width=300,
        border_color="pink",
        border_radius=ft.border_radius.all(8),
        focused_border_color="blue",
        color="blue",
        cursor_color="green",
        multiline=False,
        content_padding=20,
        capitalization=ft.TextCapitalization.CHARACTERS,
        counter_text="0/20",
        on_change=counter,
        password=True,
        can_reveal_password=True,
        helper_text="Your password must be at least 20 characters."
    )
    page.add(tf)


ft.app(target=main)
