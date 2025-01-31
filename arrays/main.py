from reverseArray import reverseArray

class Array():
    def __init__(self, arr: list):
        self.arr = arr

    def reverse(self) -> list:
        return reverseArray(self.arr)

