import tkinter as tk
from PIL import Image, ImageTk


class Application :
    def __init__(self,root):
        self.root = root
        self.root.title("Focus Tracker")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0b3d91")
        self.root.resizable(False, False)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #home page
        self.Home_page = tk.Frame(root, width=800, height=500, bg="#ffffff")
        self.Home_page.grid(row=0, column=0, sticky="nsew")

        # Background image
        self.home_bg_image = Image.open("images/Bg1.png")  # Make sure this image is 900x600
        self.home_bg_image = self.home_bg_image.resize((1100, 700))
        self.bg_photo = ImageTk.PhotoImage(self.home_bg_image)
        self.bg_label = tk.Label(self.Home_page, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # focus tracker
        self.title_label = tk.Label(
        self.Home_page,text="Focus Tracker",font=("Impact", 60),fg="black",bg=self.Home_page["bg"],  # match parent background
   )
        self.title_label.place(relx=0.5,y=20, anchor="n")

        #nav buttons
        button_frame = tk.Frame(self.Home_page)
        button_frame.place(x=50, y=150)

        tk.Button(button_frame, text="Pomodoro",font=("Impact", 40),command=self.open_pomo).pack(pady=5)
        tk.Button(button_frame, text="Stopwatch",font=("Impact", 40)).pack(pady=5)
        tk.Button(button_frame, text="Settings",font=("Impact", 40)).pack(pady=5)


        #####

        #Pomodoro page
        self.Pomo_page = tk.Frame(root,bg="blue")
        self.Pomo_page.grid(row=0, column=0, sticky="nsew")
        tk.Button(self.Pomo_page, text="Stopwatch", font=("Impact", 40)).pack(pady=5)

    def show_frame(self, frame):
        frame.tkraise()
    def open_pomo(self):
        self.show_frame(self.Pomo_page)




root = tk.Tk()
app = Application(root)
root.mainloop()