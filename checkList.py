import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("520x420")
        self.title("Check List")
        self.config(background="#ffffff")
        
        # window icon and resizing
        icon = tk.PhotoImage(file="checkMark.png")
        self.iconphoto(True, icon)
        # self.resizable(False, False)
        self.minsize(520, 420)

        # widgets
        self.taskLbl = tk.Label(self,text="Task:", bg="#ffffff")
        self.taskEntry = tk.Text(self,width=50,height=3)
        self.dateLbl = tk.Label(self,text="Date(mm/dd/yy):", bg="#ffffff")
        self.dateEntry = tk.Entry(self,width=20)
        self.addTaskBtn = tk.Button(self,
                         text="Add Task")

        # place widgets
        self.taskLbl.pack()
        self.taskEntry.pack()
        self.dateLbl.pack()
        self.dateEntry.pack()
        self.addTaskBtn.pack()

if __name__ == "__main__":
    root = App()
    root.mainloop()