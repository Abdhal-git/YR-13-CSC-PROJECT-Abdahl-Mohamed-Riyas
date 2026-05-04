import tkinter as tk
from PIL import Image, ImageTk


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Tracker")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0b3d91")
        self.root.resizable(False, False)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Store frames in a dictionary
        self.frames = {}

        #Create all pages
        for I in (self.open_HME, self.open_POM, self.open_STO, self.open_SET):
            frame = I()
            self.frames[I.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Show home first
        self.show_frame("open_HME")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # HOME PAGE
    def open_HME(self):
        frame = tk.Frame(self.root, bg="yellow")
        title = tk.Label(frame, text="Focus Tracker", font=("Impact", 60), bg="yellow")
        title.place(relx=0.5, y=20, anchor="n")

        #BUTTONS
        button_frame = tk.Frame(frame, bg="#ffffff")
        button_frame.place(x=50, y=150)

        tk.Button(button_frame, text="Pomodoro", font=("Impact", 30),command=lambda: self.show_frame("open_POM")).pack(pady=10)
        tk.Button(button_frame, text="Stopwatch", font=("Impact", 30),command=lambda: self.show_frame("open_STO")).pack(pady=10)
        tk.Button(button_frame, text="Settings", font=("Impact", 30),command=lambda: self.show_frame("open_SET")).pack(pady=10)
        return frame

    #POMODORO
    def open_POM(self):
        frame = tk.Frame(self.root, bg="blue")
        tk.Label(frame, text="Pomodoro", font=("Impact", 40), bg="blue").pack(pady=20)
        tk.Button(frame, text="Back", font=("Impact", 20),command=lambda: self.show_frame("open_HME")).pack()
        return frame

    #STOPWATCH
    def open_STO(self):
        frame = tk.Frame(self.root, bg="green")
        tk.Label(frame, text="Stopwatch", font=("Impact", 40), bg="green").pack(pady=20)
        tk.Button(frame, text="Back", font=("Impact", 20),command=lambda: self.show_frame("open_HME")).pack()
        return frame

    #SETTINGS
    def open_SET(self):
        frame = tk.Frame(self.root, bg="red")
        tk.Label(frame, text="Settings", font=("Impact", 40), bg="red").pack(pady=20)
        tk.Button(frame, text="Back", font=("Impact", 20),command=lambda: self.show_frame("open_HME")).pack()
        return frame





# Run app
root = tk.Tk()
app = Application(root)
root.mainloop()