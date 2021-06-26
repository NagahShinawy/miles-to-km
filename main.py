"""
created by Nagaj at 26/06/2021
"""
import tkinter

from config import setup
from constants import *


def main():
    """
    entry point
    :return:
    """
    window = setup(
        title=MILES_TO_KM, image=IMAGE_TITLE_BAR, width=WINDOW_WIDTH, is_center=True
    )

    miles_to_km = tkinter.Label(text="Convert Miles to Km", font=("Arial", 15, "bold"))
    # expand=bool, it shows label in the center[center center] of window or make it just top center
    # side one of ==> [top, bottom, left, or right]
    # padding ==> padx, pady
    miles_to_km.pack(
        expand=0, side=TOP, padx=MAIN_TITLE_XPAD, pady=MAIN_TITLE_YPAD
    )  # show and center component(label) with custom features

    # add components to the window and keep me working
    #  keep window opens and listening to the user actions
    window.mainloop()  # keep window open while working


if __name__ == "__main__":
    main()
