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



        # --- Pomodoro --- Timer Logic State Variables ---
        self.pomo_running = False  # Tracks if the countdown is active (True) or paused (False)
        self.pomo_counter = 0  # Stores the remaining time in total seconds
        self.current_timer_mode = None  # Tracks which screen is active: "POM", "SB", or "LB"

        # --- Customizable Durations (in minutes) ---
        self.pom_minutes = 25
        self.sb_minutes = 5
        self.lb_minutes = 10

        # Store frames in a dictionary #
        self.frames = {}

        # Create all pages #
        for I in (self.open_HME, self.open_POM, self.open_POM_DET, self.open_SB_DET, self.open_LB_DET, self.open_STO,
                  self.open_SET):
            frame = I()
            self.frames[I.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show home first#
        self.show_frame("open_HME")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()





    #HOME PAGE
    def open_HME(self):
        frame = tk.Frame(self.root, bg="black")

        # Images
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



        # Heading for the Home page
        title = tk.Label(frame, text="FOCUS TRACKER ", image=self.logo_img,
                         compound="right", font=("Impact", 70), bg="black", fg="white", )
        title.place(relx=0.5, y=20, anchor="n")

        # Navigation Buttons
        button_frame = tk.Frame(frame, bg="black")
        button_frame.pack(expand=True)

        tk.Button(button_frame, text="  POMODORO ", image=self.pomo_img, compound="right", font=("Impact", 40),
                  bg="black", fg="white",
                  command=lambda: self.show_frame("open_POM")).pack(fill="x", pady=10)
        tk.Button(button_frame, text="  STOPWATCH", image=self.stop_img, compound="right", font=("Impact", 40),
                  bg="black", fg="white",
                  command=lambda: self.show_frame("open_STO")).pack(fill="x", pady=10)
        tk.Button(button_frame, text="  SETTINGS ", image=self.set_img, compound="right", font=("Impact", 40),
                  bg="black", fg="white",
                  command=lambda: self.show_frame("open_SET")).pack(fill="x", pady=10)
        return frame

    #POMODORO
    def open_POM(self):
        frame = tk.Frame(self.root, bg="black")



        # Navigation_POMODORO
        top_bar = tk.Frame(frame, bg="black")
        top_bar.pack(fill="x", pady=25)
        tk.Button(top_bar, text="  BACK  ", font=("Impact", 25), bg="black", fg="white", activebackground="red",
                  activeforeground="white", command=lambda: self.show_frame("open_HME")).pack(side="right", padx=20,
                                                                                              fill="x")
        tk.Label(top_bar, text="   POMODORO TIMER", font=("Impact", 50), bg="black", fg="white").pack(side="left",
                                                                                                      padx=10, fill="x")


        Pomodoro_container = tk.Frame(frame, bg="black")
        Pomodoro_container.pack(fill="both", expand=True, padx=20)



        #Side_left_Pomodoro_Timer
        left_frame = tk.Frame(Pomodoro_container, bg="black")
        left_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Label(left_frame, text="Pomodoro", font=("Impact", 30), bg="black", fg="#ff4444").pack(pady=30)
        tk.Label(left_frame, text=f"[ {self.pom_minutes}:00 ]", font=("Impact", 60), bg="black", fg="white").pack(pady=10)
        tk.Button(left_frame, text="FULL VIEW", font=("Arial", 14, "bold"), bg="red", fg="white",
                  command=lambda: self.setup_and_open_timer("POM", self.pom_minutes * 60, "open_POM_DET")).pack(pady=10)

        # Side_center_Short_Break
        center_frame = tk.Frame(Pomodoro_container, bg="black")
        center_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Label(center_frame, text="Short Break", font=("Impact", 30), bg="black", fg="#ff4444").pack(pady=30)
        tk.Label(center_frame, text=f"[ {self.sb_minutes:02d}:00 ]", font=("Impact", 60), bg="black", fg="white").pack(pady=10)
        tk.Button(center_frame, text="FULL VIEW", font=("Arial", 14, "bold"), bg="red", fg="white",
                  command=lambda: self.setup_and_open_timer("SB", self.sb_minutes * 60, "open_SB_DET")).pack(pady=10)

        #Side_right_Short_Break
        right_frame = tk.Frame(Pomodoro_container, bg="black")
        right_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Label(right_frame, text="Long Break ", font=("Impact", 30), bg="black", fg="#ff4444").pack(pady=30)
        tk.Label(right_frame, text=f"[ {self.lb_minutes:02d}:00 ]", font=("Impact", 60), bg="black", fg="white").pack(pady=10)
        tk.Button(right_frame, text="FULL VIEW", font=("Arial", 14, "bold"), bg="red", fg="white",
                  command=lambda: self.setup_and_open_timer("LB", self.lb_minutes * 60, "open_LB_DET")).pack(pady=10)

        return frame

    # --- POMODORO DETAILED VIEWS ---
    def open_POM_DET(self):
        frame = tk.Frame(self.root, bg="black")
        tk.Label(frame, text="POMODORO DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)

        self.pom_label = tk.Label(frame, text="25 : 00", font=("Impact", 100), bg="black", fg="white")
        self.pom_label.pack(pady=20)

        self.create_timer_controls(frame)

        tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",
                  activebackground="red", activeforeground="white", command=self.leave_pomo_view).pack(pady=40)
        return frame

    def open_SB_DET(self):
        frame = tk.Frame(self.root, bg="black")
        tk.Label(frame, text="SHORT BREAK DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)

        self.sb_label = tk.Label(frame, text="05 : 00", font=("Impact", 100), bg="black", fg="white")
        self.sb_label.pack(pady=20)

        self.create_timer_controls(frame)

        tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",
                  activebackground="red", activeforeground="white", command=self.leave_pomo_view).pack(pady=40)
        return frame

    def open_LB_DET(self):
        frame = tk.Frame(self.root, bg="black")
        tk.Label(frame, text="LONG BREAK DETAILED VIEW", font=("Impact", 40), bg="black", fg="red").pack(pady=20)

        self.lb_label = tk.Label(frame, text="10 : 00", font=("Impact", 100), bg="black", fg="white")
        self.lb_label.pack(pady=20)

        self.create_timer_controls(frame)

        tk.Button(frame, text="← Back to Pomodoro", font=("Impact", 20), bg="#333333", fg="white",
                  activebackground="red", activeforeground="white", command=self.leave_pomo_view).pack(pady=40)
        return frame

    #STOPWATCH
    def open_STO(self):
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

        self.stopwatch_label = tk.Label(frame, text="00 : 00 : 00 ", font=("Impact", 120), bg="black", fg="red")
        self.stopwatch_label.pack(pady=80)

        stopwatch_container = tk.Frame(frame, bg="black")
        stopwatch_container.pack(fill="both", expand=True, padx=20)

        # Button Image Asset Bindings
        pil_pau = Image.open("images/pause.jpg")
        pil_pau_resized = pil_pau.resize((100, 100))
        self.pau_img = ImageTk.PhotoImage(pil_pau_resized)

        pil_stp = Image.open("images/resume.jpg")
        pil_stp_resized = pil_stp.resize((100, 100))
        self.stp_img = ImageTk.PhotoImage(pil_stp_resized)

        pil_res = Image.open("images/reset.jpg")
        pil_res_resized = pil_res.resize((100, 100))
        self.res_img = ImageTk.PhotoImage(pil_res_resized)

        # images
        left_frame = tk.Frame(stopwatch_container, bg="black")
        left_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Button(left_frame, image=self.pau_img, bg="black", activebackground="black",
                  command=self.start_stopwatch).pack(pady=20)

        center_frame = tk.Frame(stopwatch_container, bg="black")
        center_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Button(center_frame, image=self.stp_img, bg="black", activebackground="black",
                  command=self.pause_stopwatch).pack(pady=20)

        right_frame = tk.Frame(stopwatch_container, bg="black")
        right_frame.pack(side="left", fill="both", expand=True, padx=10)
        tk.Button(right_frame, image=self.res_img, bg="black", activebackground="black",
                  command=self.reset_stopwatch).pack(pady=20)

        if self.running:
            self.update_stopwatch_label()

        return frame

    #SETTINGS
    def open_SET(self):


        frame = tk.Frame(self.root, bg="black")
        top_bar = tk.Frame(frame, bg="black")
        top_bar.pack(fill="x", pady=25)
        tk.Button(top_bar, text="SAVE & BACK", font=("Impact", 25), bg="black", fg="white", activebackground="red",
                  activeforeground="white", command= self.save_settings).pack(side="right", padx=20)

        tk.Label(top_bar, text="   SETTINGS", font=("Impact", 50), bg="black", fg="white").pack(side="left", padx=10)



        settings_container = tk.Frame(frame, bg="black")
        settings_container.pack(pady=40)


        #1 pomodoro slider
        tk.Label(settings_container, text="Pomodoro Work Time (Minutes)", font=("Arial", 14, "bold"),bg="black", fg="white").pack(pady=5)
        self.pom_slider = tk.Scale(settings_container, from_=1, to=60, orient="horizontal", length=400,bg="black",fg="white", highlightthickness=0, troughcolor="#333333", activebackground="red")
        self.pom_slider.set(self.pom_minutes)  # Set slider to current value
        self.pom_slider.pack(pady=10)

        #2 Short break slider
        tk.Label(settings_container, text="Short Break Work Time (Minutes)", font=("Arial", 14, "bold"), bg="black",fg="white").pack(pady=5)
        self.sb_slider = tk.Scale(settings_container, from_=1, to=30, orient="horizontal", length=400, bg="black",fg="white", highlightthickness=0, troughcolor="#333333", activebackground="red")
        self.sb_slider.set(self.sb_minutes)  # Set slider to current value
        self.sb_slider.pack(pady=10)

        #3 Long break slider

        # 3. Long Break Slider
        tk.Label(settings_container, text="Long Break Time (Minutes)", font=("Arial", 14, "bold"), bg="black",fg="white").pack(pady=5)
        self.lb_slider = tk.Scale(settings_container, from_=1, to=45, orient="horizontal", length=400, bg="black",fg="white", highlightthickness=0, troughcolor="#333333", activebackground="red")
        self.lb_slider.set(self.lb_minutes)
        self.lb_slider.pack(pady=10)


        return frame






    # Functions and Logics for the stopwatch and pomodoro timer


    # --- STOPWATCH ---
    def update_stopwatch_label(self):

        if self.running:
            m, s = divmod(self.counter, 60)
            h, m = divmod(m, 60)
            display = f"{h:02d} : {m:02d} : {s:02d}"

            if hasattr(self, 'stopwatch_label') and self.stopwatch_label.winfo_exists():
                self.stopwatch_label.config(text=display)
                self.root.after(1000, self.update_stopwatch_label)
                self.counter += 1

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_stopwatch_label()

    def pause_stopwatch(self):
        self.running = False

    def stop_stopwatch(self):
        self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.counter = 0
        if hasattr(self, 'stopwatch_label') and self.stopwatch_label.winfo_exists():
            self.stopwatch_label.config(text="00 : 00 : 00")



    # --- POMODORO TEXT DISPLAY COUPLER ---
    def update_pomo_display_text(self):

        m, s = divmod(self.pomo_counter, 60)
        display = f"{m:02d} : {s:02d}"

        if self.current_timer_mode == "POM" and hasattr(self, 'pom_label'):
            self.pom_label.config(text=display)
        elif self.current_timer_mode == "SB" and hasattr(self, 'sb_label'):
            self.sb_label.config(text=display)
        elif self.current_timer_mode == "LB" and hasattr(self, 'lb_label'):
            self.lb_label.config(text=display)

    # --- POMODORO DATA BRIDGE CONFIGURATION ---
    def setup_and_open_timer(self, mode, duration_seconds, frame_name):

        self.pomo_running = False
        self.current_timer_mode = mode
        self.pomo_counter = duration_seconds
        self.update_pomo_display_text()
        self.show_frame(frame_name)

    # --- buttons for the timer and breaks  ---
    def create_timer_controls(self, frame):
        cntrl_frame = tk.Frame(frame, bg="black")
        cntrl_frame.pack(pady=10)

        tk.Button(cntrl_frame, text="START", font=("Arial", 16, "bold"), bg="red", fg="white", width=10,
                  command=self.start_pomo).pack(side="left", padx=10)
        tk.Button(cntrl_frame, text="PAUSE", font=("Arial", 16, "bold"), bg="red", fg="white", width=10,
                  command=self.pause_pomo).pack(side="left", padx=10)
        tk.Button(cntrl_frame, text="RESET", font=("Arial", 16, "bold"), bg="red", fg="white", width=10,
                  command=self.reset_pomo).pack(side="left", padx=10)

    # --- back to pomodoro button to leave from the pom,sb and lb ---
    def leave_pomo_view(self):
        self.pomo_running = False
        self.show_frame("open_POM")

    # --- CORE COUNTDOWN LOOP ENGINE ENGINE ---
    def update_pomo_loop(self):
        if self.pomo_running:
            if self.pomo_counter > 0:
                self.pomo_counter -= 1
                self.update_pomo_display_text()
                self.root.after(10, self.update_pomo_loop)
            else:
                self.pomo_running = False
                self.leave_pomo_view()

    # this function is for starting the timer and breaks , for the start button that  put
    def start_pomo(self):
        if not self.pomo_running:
            self.pomo_running = True
            self.update_pomo_loop()

    # this function is for stopping  the timer and breaks , for the pause button that  put
    def pause_pomo(self):
        self.pomo_running = False

    # this function is for restarting the timer and breaks , for the restart button that  put
    def reset_pomo(self):
        self.pomo_running = False
        if self.current_timer_mode == "POM":
            self.pomo_counter = self.pom_minutes * 60
        elif self.current_timer_mode == "SB":
            self.pomo_counter = self.sb_minutes * 60
        elif self.current_timer_mode == "LB":
            self.pomo_counter = self.lb_minutes * 60

        self.update_pomo_display_text()

    # --- SETTINGS ---

    def save_settings(self):
        # 1. Pull the new values from the UI sliders
        self.pom_minutes = self.pom_slider.get()
        self.sb_minutes = self.sb_slider.get()
        self.lb_minutes = self.lb_slider.get()

        # 2. Re-initialize the POM frame so it displays the brand new adjusted times
        p_frame = self.open_POM()
        self.frames["open_POM"] = p_frame
        p_frame.grid(row=0, column=0, sticky="nsew")

        # 3. Send the user back to the home screen safely
        self.show_frame("open_HME")











#final code to run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()