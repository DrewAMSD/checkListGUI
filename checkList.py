import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("720x620")
        self.title("Check List")
        self.config(background="#ffffff")
        
        # window icon and resizing
        icon = tk.PhotoImage(file="checkMark.png")
        self.iconphoto(True, icon)
        # self.resizable(False, False)
        self.minsize(420, 260)

        # widgets

if __name__ == "__main__":
    root = App()
    root.mainloop()