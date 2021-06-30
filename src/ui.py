"""
created by Nagaj at 30/06/2021
"""
from tkinter import Tk, Entry, Label, Button, DoubleVar, messagebox
from mile import Mile


KNOW_YOUR_NUMBERS = "KYN"
INPUT_AGE_X = 230
INPUT_AGE_Y = 80
DEFAULT_AGE = "01"
BTN_X = 150
BTN_Y = 150
BTN_GREEN_BG = "#e75e40"
BTN_WHITE_FG = "white"
BTN_BORDER_WIDTH = 0
BTN_TEXT = "Convert"
BTN_WIDTH = 10
BTN_HEIGHT = 2
DEFAULT_FONT_CONFIG = (
    "Arial",
    15,
)
ENTRY_WIDTH = 2
BTN_FONT = ("Arial", 12, "bold")


class WindowWidget(Tk):
    """"
    ui class for app
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mile_as_input = None
        self.km = None

    def config(self, title, image=None, is_center=False, **kwargs):
        """

        :param title: window title
        :param image: image title bar
        :param is_center: window to center ?
        :param kwargs: more options like width, height
        :return:
        """
        self.title(title)
        super().config(**kwargs)
        if is_center:
            self.center()
        if image:
            self.iconbitmap(image)

        self.init_components()

    def init_components(self):
        super().config(padx=170, pady=100)
        default_miles = DoubleVar()
        default_miles.set(1.00)
        self.mile_as_input = Entry(
            textvariable=default_miles, font=DEFAULT_FONT_CONFIG, width=10
        )
        self.mile_as_input.grid(row=0, column=0)
        # mile label
        miles = Label(text="Miles", font=DEFAULT_FONT_CONFIG, padx=5)
        miles.grid(row=0, column=1)

        # result
        self.km = Label(text="0.0", font=DEFAULT_FONT_CONFIG)
        self.km.grid(row=1, column=0)

        # km label
        miles = Label(text="KM", font=DEFAULT_FONT_CONFIG)
        miles.grid(row=1, column=1)

        # calc btn
        btn = Button(
            text=BTN_TEXT,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            bg=BTN_GREEN_BG,
            fg=BTN_WHITE_FG,
            borderwidth=BTN_BORDER_WIDTH,
            font=BTN_FONT,
            command=self.show_conversion_result,
        )
        btn.grid(row=2, column=0, pady=10)

    def show_conversion_result(self):
        value = self.mile_as_input.get()
        mile = Mile(value)
        if mile.is_valid():
            self.km.config(text=mile.to_km())
        else:
            messagebox.showerror(
                title="Invalid Number", message=f"Must be Number Not [{value}]"
            )

    def center(self) -> None:
        """
        add window to the center of screen
        :return:
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self["width"] / 2))
        y_cordinate = int((screen_height / 2) - (self["height"] / 2))
        self.geometry(f'{self["width"]}x{self["height"]}+{x_cordinate}+{y_cordinate}')

    def run(self):
        """
        keep app opened
        :return:
        """
        self.mainloop()
