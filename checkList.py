import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("560x420")
        self.title("Check List")
        self.config(background="#ffffff")
        
        # window icon and resizing
        icon = tk.PhotoImage(file="checkMark.png")
        self.iconphoto(True, icon)
        # self.resizable(False, False)
        self.minsize(560, 420)

        # commands for widgets
        def addTaskBtnClicked():
            text1 = self.dateEntry.get()
            text2 = self.taskEntry.get()
            self.taskListbox.insert(tk.END, f"{text1} - {text2}")
            self.dateEntry.delete(0, tk.END)
            self.taskEntry.delete(0, tk.END)

        def removeItem(event):
            print(event.y)
            idx = self.taskListbox.curselection()
            if idx and event.y >= 22+((idx[0]-1)*16) and event.y <= 22+((idx[0])*16):
                self.taskListbox.delete(idx)


        # widgets
        self.taskLbl = tk.Label(self,text="Task:", bg="#ffffff")
        self.taskEntry = tk.Entry(self,width=70)
        self.dateLbl = tk.Label(self,text="Date(mm/dd/yy):", bg="#ffffff")
        self.dateEntry = tk.Entry(self,width=20)
        self.addTaskBtn = tk.Button(self,
                         text="Add Task",
                         command=addTaskBtnClicked)
        self.taskListbox = tk.Listbox(self,width=70)

        self.taskListbox.bind("<Button-1>", removeItem)

        # place widgets
        self.taskLbl.pack()
        self.taskEntry.pack()
        self.dateLbl.pack()
        self.dateEntry.pack()
        self.addTaskBtn.pack()
        self.taskListbox.pack()


if __name__ == "__main__":
    root = App()
    root.mainloop()