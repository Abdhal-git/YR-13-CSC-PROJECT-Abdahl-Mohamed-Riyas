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

    # POMODORO #
    def open_POM(self):
        frame = tk.Frame(self.root, bg="black")
        frame.grid_columnconfigure(0, weight=1)


        tk.Label(frame,text="POMODORO",font=("Impact", 70),bg="black",fg="white").grid(row=0, column=0, pady=20)
        tk.Label(frame, text="helloo",
                 font=("Impact", 70), bg="black", fg="white").grid(row=3, column=0, pady=20)

        # BUTTON FRAME
        button_frame = tk.Frame(frame, bg="black")
        button_frame.grid(row=1, column=0)

        # CONTENT FRAME
        content_frame = tk.Frame(frame, bg="black")
        content_frame.grid(row=2, column=0)

        # SHORT BREAK FRAME
        short_frame = tk.Frame(content_frame,bg="blue",width=1100,height=700)
        short_frame.grid_propagate(False)
        tk.Label(short_frame,text="SHORT BREAK",font=("Impact", 40),bg="blue",fg="white").place(relx=0.5, rely=0.5, anchor="center")

        # LONG BREAK FRAME
        long_frame = tk.Frame(content_frame,bg="green",width=1100,height=700)
        long_frame.grid_propagate(False)
        tk.Label(long_frame,text="LONG BREAK",font=("Impact", 40),bg="green",fg="white").place(relx=0.5, rely=0.5, anchor="center")

        # FUNCTIONS
        def show_short():
            button_frame.grid_forget()
            long_frame.grid_forget()
            short_frame.grid(row=0, column=0, sticky="nsew")

        def show_long():
            button_frame.grid_forget()
            short_frame.grid_forget()
            long_frame.grid(row=0, column=0, sticky="nsew")

        def go_back():
            short_frame.grid_forget()
            long_frame.grid_forget()
            button_frame.grid(row=1, column=0)

        # BACK BUTTONS
        tk.Button(short_frame,text="BACK",font=("Impact", 20),bg="black",fg="white",command=go_back).place(x=20, y=20)
        tk.Button(long_frame,text="BACK",font=("Impact", 20),bg="black",fg="white",command=go_back).place(x=20, y=20)

        # MAIN BUTTONS
        tk.Button(button_frame,text="LONG BREAK",font=("Impact", 40),bg="black",fg="white",command=show_long).grid(row=0, column=1, padx=10)
        tk.Button(button_frame,text="SHORT BREAK",font=("Impact", 40),bg="black",fg="white",command=show_short).grid(row=0, column=2, padx=10)

        return frame



    #STOPWATCH#
    def open_STO(self):
        frame = tk.Frame(self.root, bg="black")
        tk.Label(frame, text="Stopwatch", font=("Impact", 40),bg="black",fg="white").pack(pady=20)

        tk.Button(frame, text="Back", font=("Impact", 20),bg="black",fg="white",command=lambda: self.show_frame("open_HME")).pack()
        return frame

    #SETTINGS#
    def open_SET(self):
        frame = tk.Frame(self.root, bg="black")
        tk.Label(frame, text="Settings", font=("Impact", 40),bg="black",fg="white").pack(pady=20)
        tk.Button(frame, text="Back", font=("Impact", 20),bg="black",fg="white",command=lambda: self.show_frame("open_HME")).pack()
        return frame





# Run app
root = tk.Tk()
app = Application(root)
root.mainloop()