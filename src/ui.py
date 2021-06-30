"""
created by Nagaj at 30/06/2021
"""
from tkinter import Tk, Entry, Label, Button, DoubleVar, messagebox
from mile import Mile

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
PADX_WINDOW = 180
PADY_WINDOW = 100
DEFAULT_MILES = 1.00
MILES_ROW = MILES_COL = 0
MILES_WIDTH = 10
PADX_MILES = 5
MILES_LABEL_ROW = 0
MILES_LABEL_COL = 1
RESULT_ROW = 1
RESULT_COL = 0

KM_ROW = KM_COL = 1
BTN_ROW = 2
BTN_COL = 0
PADY_BTN = 10


class WindowWidget(Tk):
    """"
    ui class for app
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mile = None
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
        super().config(padx=PADX_WINDOW, pady=PADY_WINDOW)
        default_miles = DoubleVar()
        default_miles.set(DEFAULT_MILES)
        self.mile = Entry(
            textvariable=default_miles, font=DEFAULT_FONT_CONFIG, width=MILES_WIDTH
        )
        self.mile.grid(row=MILES_ROW, column=MILES_COL)
        # mile label
        Label(text="Miles", font=DEFAULT_FONT_CONFIG, padx=PADX_MILES).grid(row=MILES_LABEL_ROW, column=MILES_LABEL_COL)

        # result
        self.km = Label(text="0.0", font=DEFAULT_FONT_CONFIG)
        self.km.grid(row=RESULT_ROW, column=RESULT_COL)

        # km label
        Label(text="KM", font=DEFAULT_FONT_CONFIG).grid(row=KM_ROW, column=KM_COL)

        # calc btn
        Button(
            text=BTN_TEXT,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            bg=BTN_GREEN_BG,
            fg=BTN_WHITE_FG,
            borderwidth=BTN_BORDER_WIDTH,
            font=BTN_FONT,
            command=self.show_conversion_result,
        ).grid(row=BTN_ROW, column=BTN_COL, pady=PADY_BTN)

    def show_conversion_result(self):
        value = self.mile.get()
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
