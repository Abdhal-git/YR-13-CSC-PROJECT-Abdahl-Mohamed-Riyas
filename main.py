

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

            # Store frames in a dictionary#
            self.frames = {}

            # Create all pages #
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
            pil_img = Image.open("images/head_logo.jpg")
            pil_img_resized = pil_img.resize((100, 100))
            self.logo_img = ImageTk.PhotoImage(pil_img_resized)

            pil_pomo = Image.open("images/stop_logo.jpg")
            pil_pomo_resized = pil_pomo.resize((45, 45))
            self.pomo_img = ImageTk.PhotoImage(pil_pomo_resized)


            pil_stop = Image.open("images/sett_logo.jpg")
            pil_stop_resized = pil_stop.resize((45, 45))
            self.stop_img = ImageTk.PhotoImage(pil_stop_resized)


            pil_set = Image.open("images/pomo_logo.jpg")
            pil_set_resized = pil_set.resize((45, 45))
            self.set_img = ImageTk.PhotoImage(pil_set_resized)


            title = tk.Label(frame, text="FOCUS TRACKER ", image=self.logo_img,
                             compound="right", font=("Impact", 70), bg="black", fg="white")
            title.place(relx=0.5, y=20, anchor="n")

            # BUTTONS#
            button_frame = tk.Frame(frame, bg="black")
            button_frame.pack(expand=True)

            tk.Button(button_frame, text="  POMODORO ", image=self.pomo_img, compound="right",font=("Impact", 40), bg="black", fg="white",
                      command=lambda: self.show_frame("open_POM")).pack(fill="x", pady=10)
            tk.Button(button_frame, text="  STOPWATCH", image=self.stop_img, compound="right",font=("Impact", 40), bg="black", fg="white",
                      command=lambda: self.show_frame("open_STO")).pack(fill="x", pady=10)
            tk.Button(button_frame, text="  SETTINGS ", image=self.set_img, compound="right",font=("Impact", 40), bg="black", fg="white",
                      command=lambda: self.show_frame("open_SET")).pack(fill="x", pady=10)
            return frame

        # POMODORO #
    def open_POM(self):
            frame = tk.Frame(self.root, bg="black")
            top_bar = tk.Frame(frame, bg="black")
            top_bar.pack( fill="x",pady=25)
            tk.Button(top_bar, text="  BACK  ", font=("Impact", 25), bg="black", fg="white",activebackground="red",activeforeground="white",command=lambda: self.show_frame("open_HME")).pack(side="right", padx=20,fill="x")
            tk.Label(top_bar, text="   POMODORO TIMER", font=("Impact", 50), bg="black", fg="white").pack(side="left", padx=10,fill="x")



            Pomodoro_container = tk.Frame(frame, bg="black")
            Pomodoro_container.pack(fill="both", expand=True, padx=20)

            # LEFT INNER FRAME
            left_frame = tk.Frame(Pomodoro_container, bg="black")
            left_frame.pack(side="left", fill="both", expand=True, padx=10,)

            tk.Label(left_frame, text="Pomodoro Timer", font=("Impact", 30), bg="black", fg="#ff4444").pack(pady=30)
            tk.Label(left_frame, text="[ 25:00 ]", font=("Impact", 60), bg="black", fg="white").pack(pady=10)

            #Target Button to open the deep sub-screen
            tk.Button(left_frame, text="FULL VIEW", font=("Arial", 14, "bold"), bg="red", fg="white",command=lambda: self.show_frame("open_POM_DET")).pack(pady=10)


            # CENTRE INNER FRAME
            center_frame = tk.Frame(Pomodoro_container, bg="black")
            center_frame.pack(side="left", fill="both", expand=True, padx=10)

            tk.Label(center_frame, text="Short Break", font=("Impact",30), bg="black", fg="#ff4444").pack(pady=30)
            tk.Label(center_frame, text="[ 05:00 ]", font=("Impact", 60), bg="black", fg="white").pack(pady=10)

            # Target Button to open the deep sub-screen
            tk.Button(center_frame, text="FULL VIEW", font=("Arial", 14, "bold"), bg="red", fg="white",command=lambda: self.show_frame("open_SB_DET")).pack(pady=10)


            # RIGHT INNER FRAME
            right_frame = tk.Frame(Pomodoro_container, bg="black")
            right_frame.pack(side="left", fill="both", expand=True, padx=10)

            tk.Label(right_frame, text="Long Break ", font=("Impact",30), bg="black", fg="#ff4444").pack(pady=30)
            tk.Label(right_frame, text="[ 10:00 ]", font=("Impact", 60), bg="black", fg="white").pack(pady=10)

            # Target Button to open the deep sub-screen
            tk.Button(right_frame, text="FULL VIEW", font=("Arial", 14, "bold"), bg="red", fg="white",command=lambda: self.show_frame("open_LB_DET")).pack(pady=10)

            return frame



    def open_POM_DET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="POMODORO DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)
            tk.Label(frame, text="Needs to workout the things like timer and adjust settings here ",font=("Arial", 20), bg="black", fg="white").pack(pady=100)

            # Back button returns explicitly to Pomodoro main view instead of Main Menu
            tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",activebackground="red",activeforeground="white",command=lambda: self.show_frame("open_POM")).pack(pady=20)

            return frame

    def open_SB_DET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="SHORT BREAK DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)
            tk.Label(frame, text="Needs to workout the things like timer and adjust settings here",font=("Arial", 20), bg="black", fg="white").pack(pady=100)

            # Back button returns explicitly to Pomodoro main view instead of Main Menu
            tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",activebackground="red",activeforeground="white",command=lambda: self.show_frame("open_POM")).pack(pady=20)

            return frame

    def open_LB_DET(self):
            frame = tk.Frame(self.root, bg="black")
            tk.Label(frame, text="LONG BREAK DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)
            tk.Label(frame, text="Needs to workout the things like timer and adjust settings here",font=("Arial", 20), bg="black", fg="white").pack(pady=100)

            # Back button returns explicitly to Pomodoro main view instead of Main Menu
            tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",activebackground="red",activeforeground="white",command=lambda: self.show_frame("open_POM")).pack(pady=20)

            return frame








        # STOPWATCH#
    def open_STO(self):

        # Initialize stopwatch instance variables if they don't exist
        if not hasattr(self, "running"):
            self.running = False
            self.counter = 0

        frame = tk.Frame(self.root, bg="black")
        top_bar = tk.Frame(frame, bg="black")
        top_bar.pack(fill="x", pady=25)

        tk.Button(top_bar, text="BACK", font=("Impact", 25), bg="black", fg="white",
                  activebackground="red", activeforeground="white",
                  command=lambda: [self.stop_stopwatch(), self.show_frame("open_HME")]).pack(side="right", padx=20,
                                                                                             fill="x")

        tk.Label(top_bar, text="   STOPWATCH", font=("Impact", 50), bg="black", fg="white").pack(side="left", padx=10,
                                                                                                 fill="x")

       #step1 neeed to create a label
        self.stopwatch_label = tk.Label(frame, text="00 : 00 : 00 ", font=("Impact", 120), bg="black", fg="red")
        self.stopwatch_label.pack(pady=80)

       #step2 need to create buttons (start , stop, reset) ive created using images
        #make sure the command for is included
        stopwatch_container = tk.Frame(frame, bg="black")
        stopwatch_container.pack(fill="both", expand=True, padx=20)

        # Load images
        pil_pau = Image.open("images/pause.jpg")
        pil_pau_resized = pil_pau.resize((100, 100))
        self.pau_img = ImageTk.PhotoImage(pil_pau_resized)

        pil_stp = Image.open("images/resume.jpg")
        pil_stp_resized = pil_stp.resize((100, 100))
        self.stp_img = ImageTk.PhotoImage(pil_stp_resized)

        pil_res = Image.open("images/reset.jpg")
        pil_res_resized = pil_res.resize((100, 100))
        self.res_img = ImageTk.PhotoImage(pil_res_resized)

        # LEFT INNER FRAME (Pause)
        left_frame = tk.Frame(stopwatch_container, bg="black")
        left_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Button(left_frame, image=self.pau_img, bg="black", activebackground="black",
                  command=self.pause_stopwatch).pack(pady=20)

        # CENTRE INNER FRAME (Start / Resume)
        center_frame = tk.Frame(stopwatch_container, bg="black")
        center_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Button(center_frame, image=self.stp_img, bg="black", activebackground="black",
                  command=self.start_stopwatch).pack(pady=20)

        # RIGHT INNER FRAME (Reset)
        right_frame = tk.Frame(stopwatch_container, bg="black")
        right_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Button(right_frame, image=self.res_img, bg="black", activebackground="black",
                  command=self.reset_stopwatch).pack(pady=20)

        # If it was already running when returning to the frame, resume UI updates
        if self.running:
            self.update_stopwatch_label()

        return frame

    # --- Stopwatch Logic Methods ---

    def update_stopwatch_label(self):

        if self.running:
        #m= minutes, s= seconds , h= hours
        #60 means the limit if the for example seconds reach the 60 it in m it will be if m reach 60 the hour will be 1
            m, s = divmod(self.counter, 60)
            h, m = divmod(m, 60)
            display = f"{h:02d} : {m:02d} : {s:02d}"

            # Safely update label if the frame hasn't been destroyed by using the  hasattr
            #setting how fast the timer needs to run like in milliseconds
            #counter needs to be get increased by 1
            if hasattr(self, 'stopwatch_label') and self.stopwatch_label.winfo_exists():
                self.stopwatch_label.config(text=display)
                self.stopwatch_label.after(100, self.update_stopwatch_label)
                self.counter +=1

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_stopwatch_label()

    def pause_stopwatch(self):
        self.running = False

    def stop_stopwatch(self):
        # Stops calculation completely (used when leaving the page)
        self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.counter = 0
        if hasattr(self, 'stopwatch_label') and self.stopwatch_label.winfo_exists():
            self.stopwatch_label.config(text="00 : 00 : 00")



















        # SETTINGS#
    def open_SET(self):
        frame = tk.Frame(self.root, bg="black")
        top_bar = tk.Frame(frame, bg="black")
        top_bar.pack(fill="x", pady=25)
        tk.Button(top_bar, text="BACK", font=("Impact", 25), bg="black", fg="white",activebackground="red",activeforeground="white",command=lambda: self.show_frame("open_HME")).pack(side="right", padx=20, fill="x")
        tk.Label(top_bar, text="   SETTINGS", font=("Impact", 50), bg="black", fg="white").pack(side="left", padx=10, fill="x")
        return frame

# Run app
root = tk.Tk()
app = Application(root)
root.mainloop()

