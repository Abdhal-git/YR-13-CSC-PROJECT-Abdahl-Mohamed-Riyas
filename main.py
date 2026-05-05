import tkinter as tk



class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Tracker")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0b3d91")
        self.root.resizable(False, False)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Store frames in a dictionary#
        self.frames = {}

        #Create all pages#
        for I in (self.open_HME, self.open_POM, self.open_STO, self.open_SET):
            frame = I()
            self.frames[I.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Show home first#
        self.show_frame("open_HME")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # HOME PAGE#
    def open_HME(self):
        frame = tk.Frame(self.root, bg="black")
        title = tk.Label(frame, text="FOCUS TRACKER", font=("Impact", 70), bg="black",fg="white")
        title.place(relx=0.5, y=20, anchor="n")

        #BUTTONS#
        button_frame = tk.Frame(frame, bg="black")
        button_frame.pack(expand=True)

        tk.Button(button_frame, text="  POMODORO ", font=("Impact", 40),bg="black",fg="white",command=lambda: self.show_frame("open_POM")).pack(fill="x",pady=10)
        tk.Button(button_frame, text="  STOPWATCH", font=("Impact", 40),bg="black",fg="white",command=lambda: self.show_frame("open_STO")).pack(fill="x",pady=10)
        tk.Button(button_frame, text="  SETTINGS ", font=("Impact", 40),bg="black",fg="white",command=lambda: self.show_frame("open_SET")).pack(fill="x",pady=10)
        return frame

    #POMODORO#
    def open_POM(self):
        frame = tk.Frame(self.root, bg="blue")
        frame.grid_columnconfigure(0, weight=1)

        tk.Label(frame, text="POMODORO", font=("Impact", 70), bg="blue") \
            .grid(row=0, column=0, pady=20)

        #BUTTONS#
        button_frame = tk.Frame(frame, bg="blue")
        button_frame.grid(row=1, column=0)

        tk.Button(button_frame, text="LONG BREAK", font=("Impact", 40),command=lambda: self.show_frame("open_HME")).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="SHORT BREAK", font=("Impact",40),command=lambda: self.show_frame("open_HME")).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="BACK", font=("Impact", 40),command=lambda: self.show_frame("open_HME")).grid(row=0, column=2, padx=10)

        return frame

    #STOPWATCH#
    def open_STO(self):
        frame = tk.Frame(self.root, bg="green")
        tk.Label(frame, text="Stopwatch", font=("Impact", 40), bg="green").pack(pady=20)

        tk.Button(frame, text="Back", font=("Impact", 20),command=lambda: self.show_frame("open_HME")).pack()
        return frame

    #SETTINGS#
    def open_SET(self):
        frame = tk.Frame(self.root, bg="red")
        tk.Label(frame, text="Settings", font=("Impact", 40), bg="red").pack(pady=20)
        tk.Button(frame, text="Back", font=("Impact", 20),command=lambda: self.show_frame("open_HME")).pack()
        return frame





# Run app
root = tk.Tk()
app = Application(root)
root.mainloop()