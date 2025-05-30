import tkinter as tk
from package.interface import SistemaInterface

if __name__ == "__main__":
    root = tk.Tk()
    sistema = SistemaInterface(root)
    root.mainloop()