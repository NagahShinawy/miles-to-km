"""
created by Nagaj at 26/06/2021
"""

import tkinter


def center(window, window_width, window_height) -> None:
    """
    add window to the center of screen
    :param window: Tk obj
    :param window_width: width of the window
    :param window_height: height of the window
    :return:
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")


def setup(title="", image=None, width=300, height=300, is_center=False) -> tkinter.Tk:
    """
    create tkinter window with title and image title bar
    :param title: title bar
    :param image: image title bar
    :param width: window width
    :param height: window height
    :param is_center: if true center window on screen
    :return: tkinter window
    """
    window = tkinter.Tk()
    window.minsize(width=width, height=height)
    if image is not None:
        window.iconbitmap(image)
    if title:
        window.title(title)

    if is_center:
        center(window, width, height)

    return window
