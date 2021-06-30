"""
created by Nagaj at 30/06/2021
"""
from ui import WindowWidget

LOGO = "./static/km-to-miles.ico"


def main():
    window = WindowWidget()
    window.config(title="Miles To Kilo", width=500, height=300, image=LOGO)
    window.center()
    window.run()


if __name__ == "__main__":
    main()
