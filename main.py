"""
created by Nagaj at 26/06/2021
"""
import random
from functools import partial
from tkinter import *

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
        title=MILES_TO_KM,
        image=IMAGE_TITLE_BAR,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        is_center=True,
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
    miles.pack(side="left")
    ########################
    change_text = partial(change_me, miles_to_km, miles)
    click_me = Button(text="Click Me", bg="red", fg="green", command=change_text)
    click_me.pack(side="left")

    ############################
    # Text
    text = Text(height=5, width=30)
    # Puts cursor in textbox. to be ready for writing
    text.focus()
    # Adds some text to begin with.
    text.insert(END, "Example of multi-line text entry.")
    text.insert(CURRENT, "test.")
    # Get's current value in textbox at line 1, character 0
    # 1.5 ==> means from line#1 charIndex#5
    print(text.get("1.5", END))
    text.pack()

    ###########################
    # Spinbox
    def spinbox_used():
        # gets the current value in spinbox.
        print(spinbox.get())

    spinbox = Spinbox(from_=1, to=120, width=5, command=spinbox_used)
    spinbox.pack(side="left")

    ##########################
    # Scale
    # Called with current scale value.No need to parse it
    def scale_used(value):
        print(value)

    scale = Scale(from_=1, to=100, command=scale_used)
    scale.pack(side="left")

    ##########################

    # Checkbutton
    def checkbutton_used():
        # Prints 1 if On button checked, otherwise 0.
        print("Value is", checked_state.get())

    # variable to hold on to checked state, 0 is off, 1 is on.
    checked_state = IntVar()
    # checked_state.set(0
    checkbutton = Checkbutton(
        text="Is On?", variable=checked_state, command=checkbutton_used
    )
    print("V is", checked_state.get())
    checkbutton.pack(side="left")
    #########################
    print("#" * 100)

    # Radiobutton
    def radio_used():
        print(radio_state.get())

    # Variable to hold on to which radio button value is checked.
    radio_state = IntVar()
    radiobutton1 = Radiobutton(
        text="Option1", value=100, variable=radio_state, command=radio_used
    )
    radiobutton2 = Radiobutton(
        text="Option2", value=200, variable=radio_state, command=radio_used
    )
    print(radio_state.get())  # default value is 0
    radiobutton1.pack()
    radiobutton2.pack()

    #########################
    def listbox_used(event):
        # Gets current selection from listbox
        print(listbox.get(listbox.curselection()))

    listbox = Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"][::-1]
    for fruit in fruits:
        index = fruits.index(fruit)
        listbox.insert(index, fruit)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()
    #########################
    window.mainloop()  # keep window open while working


if __name__ == "__main__":
    main()
