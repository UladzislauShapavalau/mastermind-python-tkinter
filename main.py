from tkinter import Tk
from game import *

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    ox = root.winfo_screenwidth() / 2
    oy = root.winfo_screenheight() / 2
    root.geometry(f'+{int(ox - 400)}+{int(oy - 345)}')
    n = AlgorithmGame(root)
    n.drawField()
    root.mainloop()