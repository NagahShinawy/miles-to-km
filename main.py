"""
created by Nagaj at 26/06/2021
"""
import random
from tkinter import *
from functools import partial
from config import setup
from constants import *

counter = 1
computer_color = random.choice(COLORS)
print(computer_color)


def change_title_color(label: Label, color, btn):
    label["fg"] = color
    label["text"] = color
    if color == computer_color:
        btn["state"] = DISABLED
        label["text"] = "Got It"


def welcome():
    global counter
    print(f"{counter}-welcome")
    counter += 1


def convert():
    print("Converting ...")


def change_me(label, text):
    label["text"] = text.get()


def main():
    """
    entry point
    :return:
    """
    window = setup(
        title=MILES_TO_KM, image=IMAGE_TITLE_BAR, width=WINDOW_WIDTH, is_center=True
    )

    miles_to_km = Label(text="Convert Miles to Km", font=("Arial", 15, "bold"))
    # expand=bool, it shows label in the center[center center] of window or make it just top center
    # side one of ==> [top, bottom, left, or right]
    # padding ==> padx, pady
    miles_to_km.pack(
        expand=0, side=TOP, padx=MAIN_TITLE_XPAD, pady=MAIN_TITLE_YPAD
    )  # show and center component(label) with custom features

    # add components to the window and keep me working
    #  keep window opens and listening to the user actions
    # todo : update label text, you can update values with label['attr'] = 'value'
    miles_to_km["text"] = "new label"
    miles_to_km["bg"] = "red"
    # todo: or using config method to update attr
    miles_to_km.config(text="test", bg="black", fg="red")

    ##################################################
    convert_btn = Button(
        text="Convert",
        bg="yellow",
        command=lambda: change_title_color(
            miles_to_km, random.choice(COLORS), convert_btn
        ),
    )
    convert_btn.pack(pady=20)
    ########################
    miles = Entry(width=20)
    miles.pack(side="top")
    ########################
    change_text = partial(change_me, miles_to_km, miles)
    click_me = Button(text="Click Me", bg="red", fg="green", command=change_text)
    click_me.pack(side="top")

    ############################
    window.mainloop()  # keep window open while working


if __name__ == "__main__":
    main()
