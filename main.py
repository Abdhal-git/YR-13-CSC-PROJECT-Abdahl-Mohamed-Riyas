

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

            # Store frames in a dictionary#
            self.frames = {}

            # Create all pages (Added open_POM_DET to the layout loop)#
            for I in (self.open_HME, self.open_POM, self.open_POM_DET,self.open_SB_DET,self.open_LB_DET, self.open_STO, self.open_SET):
                frame = I()
                self.frames[I.__name__] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            # Show home first#
            self.show_frame("open_HME")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

        # HOME PAGE#
    def open_HME(self):
            frame = tk.Frame(self.root, bg="black")
            title = tk.Label(frame, text="FOCUS TRACKER", font=("Impact", 70), bg="black", fg="white")
            title.place(relx=0.5, y=20, anchor="n")

            # BUTTONS#
            button_frame = tk.Frame(frame, bg="black")
            button_frame.pack(expand=True)

            tk.Button(button_frame, text="  POMODORO ", font=("Impact", 40), bg="black", fg="white",
                      command=lambda: self.show_frame("open_POM")).pack(fill="x", pady=10)
            tk.Button(button_frame, text="  STOPWATCH", font=("Impact", 40), bg="black", fg="white",
                      command=lambda: self.show_frame("open_STO")).pack(fill="x", pady=10)
            tk.Button(button_frame, text="  SETTINGS ", font=("Impact", 40), bg="black", fg="white",
                      command=lambda: self.show_frame("open_SET")).pack(fill="x", pady=10)
            return frame

        # POMODORO #
    def open_POM(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="POMODORO TIMER", font=("Impact", 40), bg="black", fg="white").pack(pady=15)

            Pomodoro_container = tk.Frame(frame, bg="black")
            Pomodoro_container.pack(fill="both", expand=True, padx=20, pady=10)

            # LEFT INNER FRAME
            left_frame = tk.Frame(Pomodoro_container, bg="#1a1a1a", highlightbackground="#333333", highlightthickness=2)
            left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

            tk.Label(left_frame, text="Pomodoro Timer Display", font=("Impact", 24), bg="#1a1a1a", fg="#ff4444").pack(pady=30)
            tk.Label(left_frame, text="[ 25:00 ]", font=("Impact", 60), bg="#1a1a1a", fg="white").pack(pady=10)

            #Target Button to open the deep sub-screen
            tk.Button(left_frame, text="View Details", font=("Arial", 14, "bold"), bg="red", fg="white",command=lambda: self.show_frame("open_POM_DET")).pack(pady=10)


            # CENTRE INNER FRAME
            center_frame = tk.Frame(Pomodoro_container, bg="#1a1a1a", highlightbackground="#333333",highlightthickness=2)
            center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

            tk.Label(center_frame, text="Short Break Display", font=("Impact", 24), bg="#1a1a1a", fg="#ff4444").pack(pady=30)
            tk.Label(center_frame, text="[ 05:00 ]", font=("Impact", 60), bg="#1a1a1a", fg="white").pack(pady=10)

            # Target Button to open the deep sub-screen
            tk.Button(center_frame, text="View Details", font=("Arial", 14, "bold"), bg="red", fg="white",command=lambda: self.show_frame("open_SB_DET")).pack(pady=10)


            # RIGHT INNER FRAME
            right_frame = tk.Frame(Pomodoro_container, bg="#1a1a1a", highlightbackground="#333333",highlightthickness=2)
            right_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

            tk.Label(right_frame, text="Long Break Display", font=("Impact", 24), bg="#1a1a1a", fg="#ff4444").pack(pady=30)
            tk.Label(right_frame, text="[ 10:00 ]", font=("Impact", 60), bg="#1a1a1a", fg="white").pack(pady=10)

            # Target Button to open the deep sub-screen
            tk.Button(right_frame, text="View Details", font=("Arial", 14, "bold"), bg="red", fg="white",command=lambda: self.show_frame("open_LB_DET")).pack(pady=10)

            return frame



    def open_POM_DET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="POMODORO DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)
            tk.Label(frame, text="This is the specific inner screen you requested.",font=("Arial", 20), bg="black", fg="white").pack(pady=100)

            # Back button returns explicitly to Pomodoro main view instead of Main Menu
            tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",command=lambda: self.show_frame("open_POM")).pack(pady=20)

            return frame

    def open_SB_DET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="SHORT BREAK DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)
            tk.Label(frame, text="This is the specific inner screen you requested.",font=("Arial", 20), bg="black", fg="white").pack(pady=100)

            # Back button returns explicitly to Pomodoro main view instead of Main Menu
            tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",command=lambda: self.show_frame("open_POM")).pack(pady=20)

            return frame

    def open_LB_DET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="LONG BREAK DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)
            tk.Label(frame, text="This is the specific inner screen you requested.",font=("Arial", 20), bg="black", fg="white").pack(pady=100)

            # Back button returns explicitly to Pomodoro main view instead of Main Menu
            tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",command=lambda: self.show_frame("open_POM")).pack(pady=20)

            return frame




        # STOPWATCH#
    def open_STO(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="Stopwatch", font=("Impact", 40), bg="black", fg="white").pack(pady=20)
            (tk.Label(frame, text="You are here in stopwatch timer page ", font=("Impact", 40), bg="black", fg="white")
             .pack(pady=200))
            tk.Button(frame, text="Back", font=("Impact", 20), bg="black", fg="white",
                      command=lambda: self.show_frame("open_HME")).pack()
            return frame

        # SETTINGS#
    def open_SET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="Settings", font=("Impact", 40), bg="black", fg="white").pack(pady=20)
            (tk.Label(frame, text="You are here in settings page ", font=("Impact", 40), bg="black", fg="white")
             .pack(pady=200))
            tk.Button(frame, text="Back", font=("Impact", 20), bg="black", fg="white",
                      command=lambda: self.show_frame("open_HME")).pack()
            return frame

# Run app
root = tk.Tk()
app = Application(root)
root.mainloop()

