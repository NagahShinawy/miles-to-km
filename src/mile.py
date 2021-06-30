"""
created by Nagaj at 30/06/2021
"""


class Mile:
    def __init__(self, value):
        self.value = value

    def to_km(self):
        return self.value * 1.60934

    def is_valid(self):
        try:
            self.value = float(self.value)
            return True
        except ValueError:
            return False
