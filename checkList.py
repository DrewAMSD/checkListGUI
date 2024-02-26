from tkinter import *

def main():
    window = Tk() # create new tkinter window
    window.geometry("720x620")
    window.title("Check List")

    # window icon
    icon = PhotoImage(file="checkMark.png")
    window.iconphoto(True, icon)
    window.config(background="#ffffff")

    window.mainloop() # display window, activate event listeners

if __name__ == "__main__":
    main()