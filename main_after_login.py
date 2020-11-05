from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import mysql.connector
import re
import datetime
import time
from datetime import date
import time
import requests
import json
from configparser import  ConfigParser
import random
import smtplib
from tkinter import filedialog
import os



class main_display():
    def __init__(self,l_root):
        self.root=l_root
        self.l_width=int(self.root.winfo_screenwidth())
        self.l_height = int(self.root.winfo_screenheight())
        self.l_x = int(0)
        self.l_y = int(0)
        self.root.overrideredirect(1)
        self.root.title("Registration Window")
        self.root.geometry(f"{self.l_width}x{self.l_height}+{self.l_x}+{self.l_y}")
        self.main_frame_graphic()
        # self.main_graphic_counter()
        # self.main_graphic_dashboard(self)
        self.database_host = "localhost"
        self.database_user = "root"
        self.database_password="m81321a"
        self.database_name="register_rms"


    def main_frame_graphic(self):
        self.main_background_color = "#F1F4F9"
        self.main_background_upward_color = "#4150F5"
        self.box_background_color = "#E0E0E0"
        self.box_in_box_background_color = "#ffffff"
        self.box_text_color_big = "#1B2026"
        self.box_text_color_small = "#72706E"
        self.green = "#00C300"
        self.light_blue = "#1DECFB"
        self.orange = "#F49021"
        self.red = "#FB1D1D"
        self.purpal = "#B21DFB"
        self.yellow = "#FFFF41"
        self.pink = "#FF41BA"


#=========================================    main_frame_graphic_1 ====================================================
        self.main_frame_graphic_1 = Frame(self.root,bg=self.main_background_color)
        self.main_frame_graphic_1.place(relx=0,rely=0,relwidth=1,relheight=1)

#=========================================    main_frame_graphic_2 ====================================================
        self.main_frame_graphic_2 = Frame(self.root,bg=self.main_background_upward_color)
        self.main_frame_graphic_2.place(relx=0,rely=0,relwidth=1,relheight=0.35)

# =========================================    main_frame_graphic_3 ====================================================
        self.main_frame_graphic_3 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_3.place(relx=0.27, rely=0.31, relwidth=0.2, relheight=0.3)




        self.main_frame_graphic_3_image_1 = Image.open("33.png")
        self.main_frame_graphic_3_image_2 = self.main_frame_graphic_3_image_1.resize((300,250))
        self.main_frame_graphic_3_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_3_image_2)

        self.main_frame_graphic_3_1 = Label(self.main_frame_graphic_3, image=self.main_frame_graphic_3_image_3,bg=self.main_background_color)
        self.main_frame_graphic_3_1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.main_frame_graphic_31 = Frame(self.main_frame_graphic_3, bg=self.main_background_upward_color)
        self.main_frame_graphic_31.place(relx=0, rely=0, relwidth=1, relheight=0.13)


        self.main_frame_graphic_31_image_1 = Image.open("333.png")
        self.main_frame_graphic_31_image_2 = self.main_frame_graphic_31_image_1.resize((300, 40))
        self.main_frame_graphic_31_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_31_image_2)

        self.main_frame_graphic_31_1 = Label(self.main_frame_graphic_31, image=self.main_frame_graphic_31_image_3,bg=self.main_background_upward_color)
        self.main_frame_graphic_31_1.place(relx=0, rely=0, relwidth=1, relheight=1)






        self.main_frame_graphic_3_2 = Label(self.main_frame_graphic_3_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_3_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_3_2_image_1 = Image.open("1table.png")
        self.main_frame_graphic_3_2_image_2 = self.main_frame_graphic_3_2_image_1.resize((30, 30))
        self.main_frame_graphic_3_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_3_2_image_2)

        self.main_frame_graphic_3_2_1 = Label(self.main_frame_graphic_3_2, image=self.main_frame_graphic_3_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_3_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)


        self.main_frame_graphic_3_2_2 = Label(self.main_frame_graphic_3_2,text="100",bg=self.box_in_box_background_color, font=("Bungee Inline", 12), fg=self.box_text_color_big)
        self.main_frame_graphic_3_2_2.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)




        self.main_frame_graphic_3_3 = Label(self.main_frame_graphic_3_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_3_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_3_3_1 = Label(self.main_frame_graphic_3_3, text="Tables", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_3_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)

        self.main_frame_graphic_3_3_1_1 = Label(self.main_frame_graphic_3_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_3_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)

        self.main_frame_graphic_3_3_1_1 = Label(self.main_frame_graphic_3_3,bg=self.green)
        self.main_frame_graphic_3_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_3_4 = Label(self.main_frame_graphic_3_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_3_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_3_4_1 = Label(self.main_frame_graphic_3_4, text="Tables Acquired", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_3_4_1.place(relx=0, rely=0, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_3_4_1_1 = Label(self.main_frame_graphic_3_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_3_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.45)

        self.main_frame_graphic_3_4_2 = Label(self.main_frame_graphic_3_4, text="Tables Vacent", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_3_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_3_4_2_1 = Label(self.main_frame_graphic_3_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_3_4_2_1.place(relx=0.55, rely=0.5, relwidth=0.45, relheight=0.45)






# =========================================    main_frame_graphic_4 ====================================================
        self.main_frame_graphic_4 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_4.place(relx=0.52, rely=0.31, relwidth=0.2, relheight=0.3)

        self.main_frame_graphic_4_image_1 = Image.open("33.png")
        self.main_frame_graphic_4_image_2 = self.main_frame_graphic_4_image_1.resize((300,250))
        self.main_frame_graphic_4_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_4_image_2)

        self.main_frame_graphic_4_1 = Label(self.main_frame_graphic_4, image=self.main_frame_graphic_4_image_3,bg=self.main_background_color)
        self.main_frame_graphic_4_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_frame_graphic_41 = Frame(self.main_frame_graphic_4, bg=self.main_background_upward_color)
        self.main_frame_graphic_41.place(relx=0, rely=0, relwidth=1, relheight=0.13)


        self.main_frame_graphic_41_image_1 = Image.open("333.png")
        self.main_frame_graphic_41_image_2 = self.main_frame_graphic_41_image_1.resize((300, 40))
        self.main_frame_graphic_41_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_41_image_2)

        self.main_frame_graphic_41_1 = Label(self.main_frame_graphic_41, image=self.main_frame_graphic_41_image_3,bg=self.main_background_upward_color)
        self.main_frame_graphic_41_1.place(relx=0, rely=0, relwidth=1, relheight=1)




        self.main_frame_graphic_4_2 = Label(self.main_frame_graphic_4_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_4_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_4_2_image_1 = Image.open("1waiter.png")
        self.main_frame_graphic_4_2_image_2 = self.main_frame_graphic_4_2_image_1.resize((30, 30))
        self.main_frame_graphic_4_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_4_2_image_2)

        self.main_frame_graphic_4_2_1 = Label(self.main_frame_graphic_4_2, image=self.main_frame_graphic_4_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_4_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.main_frame_graphic_4_2_2 = Label(self.main_frame_graphic_4_2,text="100",bg=self.box_in_box_background_color, font=("Bungee Inline", 12), fg=self.box_text_color_big)
        self.main_frame_graphic_4_2_2.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



        self.main_frame_graphic_4_3 = Label(self.main_frame_graphic_4_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_4_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_4_3_1 = Label(self.main_frame_graphic_4_3, text="Waiters", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_4_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)

        self.main_frame_graphic_4_3_1_1 = Label(self.main_frame_graphic_4_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_4_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)

        self.main_frame_graphic_4_3_1_1 = Label(self.main_frame_graphic_4_3,bg=self.red)
        self.main_frame_graphic_4_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_4_4 = Label(self.main_frame_graphic_4_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_4_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_4_4_1 = Label(self.main_frame_graphic_4_4, text="Active Waiter", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_4_4_1.place(relx=0, rely=0, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_4_4_1_1 = Label(self.main_frame_graphic_4_4, text="0", bg=self.box_in_box_background_color,font=("Cascadia Mono", 10), fg=self.box_text_color_small, anchor=CENTER)
        self.main_frame_graphic_4_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.45)

        self.main_frame_graphic_4_4_2 = Label(self.main_frame_graphic_4_4, text="Free Waiter", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_4_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_4_4_2_1 = Label(self.main_frame_graphic_4_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_4_4_2_1.place(relx=0.55, rely=0.5, relwidth=0.45, relheight=0.45)










# =========================================    main_frame_graphic_5 ====================================================
        self.main_frame_graphic_5 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_5.place(relx=0.76, rely=0.31, relwidth=0.2, relheight=0.3)

        self.main_frame_graphic_5_image_1 = Image.open("33.png")
        self.main_frame_graphic_5_image_2 = self.main_frame_graphic_5_image_1.resize((300,250))
        self.main_frame_graphic_5_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_5_image_2)

        self.main_frame_graphic_5_1 = Label(self.main_frame_graphic_5, image=self.main_frame_graphic_5_image_3,bg=self.main_background_color)
        self.main_frame_graphic_5_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_frame_graphic_51 = Frame(self.main_frame_graphic_5, bg=self.main_background_upward_color)
        self.main_frame_graphic_51.place(relx=0, rely=0, relwidth=1, relheight=0.13)


        self.main_frame_graphic_51_image_1 = Image.open("333.png")
        self.main_frame_graphic_51_image_2 = self.main_frame_graphic_51_image_1.resize((300, 40))
        self.main_frame_graphic_51_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_51_image_2)

        self.main_frame_graphic_51_1 = Label(self.main_frame_graphic_51, image=self.main_frame_graphic_51_image_3,bg=self.main_background_upward_color)
        self.main_frame_graphic_51_1.place(relx=0, rely=0, relwidth=1, relheight=1)



        self.main_frame_graphic_5_2 = Label(self.main_frame_graphic_5_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_5_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_5_2_image_1 = Image.open("1chef.png")
        self.main_frame_graphic_5_2_image_2 = self.main_frame_graphic_5_2_image_1.resize((30, 30))
        self.main_frame_graphic_5_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_5_2_image_2)

        self.main_frame_graphic_5_2_1 = Label(self.main_frame_graphic_5_2, image=self.main_frame_graphic_5_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_5_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.main_frame_graphic_5_2_2 = Label(self.main_frame_graphic_5_2,text="100",bg=self.box_in_box_background_color, font=("Bungee Inline", 12), fg=self.box_text_color_big)
        self.main_frame_graphic_5_2_2.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



        self.main_frame_graphic_5_3 = Label(self.main_frame_graphic_5_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_5_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_5_3_1 = Label(self.main_frame_graphic_5_3, text="Kitchen", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_5_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)

        self.main_frame_graphic_5_3_1_1 = Label(self.main_frame_graphic_5_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_5_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)

        self.main_frame_graphic_5_3_1_1 = Label(self.main_frame_graphic_5_3,bg=self.light_blue)
        self.main_frame_graphic_5_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_5_4 = Label(self.main_frame_graphic_5_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_5_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_5_4_1 = Label(self.main_frame_graphic_5_4, text="Active Order", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_5_4_1.place(relx=0, rely=0, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_5_4_1_1 = Label(self.main_frame_graphic_5_4, text="0", bg=self.box_in_box_background_color,font=("Cascadia Mono", 10), fg=self.box_text_color_small, anchor=CENTER)
        self.main_frame_graphic_5_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.45)


        self.main_frame_graphic_5_4_2 = Label(self.main_frame_graphic_5_4, text="Cancelled Order", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_5_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_5_4_2_1 = Label(self.main_frame_graphic_5_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_5_4_2_1.place(relx=0.55, rely=0.5, relwidth=0.45, relheight=0.45)




# =========================================    main_frame_graphic_6 ====================================================
        self.main_frame_graphic_6 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_6.place(relx=0.27, rely=0.665, relwidth=0.2, relheight=0.3)

        self.main_frame_graphic_6_image_1 = Image.open("33.png")
        self.main_frame_graphic_6_image_2 = self.main_frame_graphic_6_image_1.resize((300,250))
        self.main_frame_graphic_6_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_6_image_2)

        self.main_frame_graphic_6_1 = Label(self.main_frame_graphic_6, image=self.main_frame_graphic_6_image_3,bg=self.main_background_color)
        self.main_frame_graphic_6_1.place(relx=0, rely=0, relwidth=1, relheight=1)



        self.main_frame_graphic_6_2 = Label(self.main_frame_graphic_6_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_6_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_6_2_image_1 = Image.open("2customer.png")
        self.main_frame_graphic_6_2_image_2 = self.main_frame_graphic_6_2_image_1.resize((30, 30))
        self.main_frame_graphic_6_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_6_2_image_2)

        self.main_frame_graphic_6_2_1 = Label(self.main_frame_graphic_6_2, image=self.main_frame_graphic_6_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_6_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)


        self.main_frame_graphic_6_2_2 = Label(self.main_frame_graphic_6_2,text="100",bg=self.box_in_box_background_color, font=("Bungee Inline", 12), fg=self.box_text_color_big)
        self.main_frame_graphic_6_2_2.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)




        self.main_frame_graphic_6_3 = Label(self.main_frame_graphic_6_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_6_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_6_3_1 = Label(self.main_frame_graphic_6_3, text="Customers", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_6_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)

        self.main_frame_graphic_6_3_1_1 = Label(self.main_frame_graphic_6_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_6_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)

        self.main_frame_graphic_6_3_1_1 = Label(self.main_frame_graphic_6_3,bg=self.purpal)
        self.main_frame_graphic_6_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_6_4 = Label(self.main_frame_graphic_6_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_6_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_6_4_1 = Label(self.main_frame_graphic_6_4, text="Active Customers", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_6_4_1.place(relx=0, rely=0, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_6_4_1_1 = Label(self.main_frame_graphic_6_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_6_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.45)

        self.main_frame_graphic_6_4_2 = Label(self.main_frame_graphic_6_4, text="Done Customers", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_6_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_6_4_2_1 = Label(self.main_frame_graphic_6_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_6_4_2_1.place(relx=0.55, rely=0.5, relwidth=0.45, relheight=0.45)






# =========================================    main_frame_graphic_7 ====================================================
        self.main_frame_graphic_7 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_7.place(relx=0.52, rely=0.665, relwidth=0.2, relheight=0.3)
        self.main_frame_graphic_7_image_1 = Image.open("33.png")
        self.main_frame_graphic_7_image_2 = self.main_frame_graphic_7_image_1.resize((300,250))
        self.main_frame_graphic_7_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_7_image_2)

        self.main_frame_graphic_7_1 = Label(self.main_frame_graphic_7, image=self.main_frame_graphic_7_image_3,bg=self.main_background_color)
        self.main_frame_graphic_7_1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_frame_graphic_7_1.bind('<Button-1>',self.call_nex_page_1)



        self.main_frame_graphic_7_2 = Label(self.main_frame_graphic_7_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_7_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)
        self.main_frame_graphic_7_2.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_2_image_1 = Image.open("1counter.png")
        self.main_frame_graphic_7_2_image_2 = self.main_frame_graphic_7_2_image_1.resize((30, 30))
        self.main_frame_graphic_7_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_7_2_image_2)
        # self.main_frame_graphic_7_2_image_3.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_2_1 = Label(self.main_frame_graphic_7_2, image=self.main_frame_graphic_7_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_7_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        self.main_frame_graphic_7_2_1.bind('<Button-1>', self.call_nex_page_1)

        self.main_frame_graphic_7_2_2 = Label(self.main_frame_graphic_7_2,text="100",bg=self.box_in_box_background_color, font=("Bungee Inline", 12), fg=self.box_text_color_big)
        self.main_frame_graphic_7_2_2.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
        self.main_frame_graphic_7_2_2.bind('<Button-1>', self.call_nex_page_1)


        self.main_frame_graphic_7_3 = Label(self.main_frame_graphic_7_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_7_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)
        self.main_frame_graphic_7_3.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_3_1 = Label(self.main_frame_graphic_7_3, text="Counter", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_7_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)
        self.main_frame_graphic_7_3_1.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_3_1_1 = Label(self.main_frame_graphic_7_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_7_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)
        self.main_frame_graphic_7_3_1_1.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_3_1_1 = Label(self.main_frame_graphic_7_3,bg=self.yellow)
        self.main_frame_graphic_7_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_7_4 = Label(self.main_frame_graphic_7_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_7_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)
        self.main_frame_graphic_7_4.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_4_1 = Label(self.main_frame_graphic_7_4, text="By Cash", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_7_4_1.place(relx=0, rely=0, relwidth=0.5, relheight=0.45)
        self.main_frame_graphic_7_4_1.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_4_1_1 = Label(self.main_frame_graphic_7_4, text="0", bg=self.box_in_box_background_color,font=("Cascadia Mono", 10), fg=self.box_text_color_small, anchor=CENTER)
        self.main_frame_graphic_7_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.45)
        self.main_frame_graphic_7_4_1_1.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_4_2 = Label(self.main_frame_graphic_7_4, text="By Card", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_7_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)
        self.main_frame_graphic_7_4_2.bind('<Button-1>', self.call_nex_page_1)
        self.main_frame_graphic_7_4_2_1 = Label(self.main_frame_graphic_7_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_7_4_2_1.place(relx=0.55, rely=0.5, relwidth=0.45, relheight=0.45)
        self.main_frame_graphic_7_4_2_1.bind('<Button-1>', self.call_nex_page_1)




# =========================================    main_frame_graphic_8 ====================================================
        self.main_frame_graphic_8 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_8.place(relx=0.77, rely=0.665, relwidth=0.2, relheight=0.3)
        self.main_frame_graphic_8_image_1 = Image.open("33.png")
        self.main_frame_graphic_8_image_2 = self.main_frame_graphic_8_image_1.resize((300,250))
        self.main_frame_graphic_8_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_8_image_2)

        self.main_frame_graphic_8_1 = Label(self.main_frame_graphic_8, image=self.main_frame_graphic_8_image_3,bg=self.main_background_color)
        self.main_frame_graphic_8_1.place(relx=0, rely=0, relwidth=1, relheight=1)



        self.main_frame_graphic_8_2 = Label(self.main_frame_graphic_8_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_8_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_8_2_image_1 = Image.open("2report.png")
        self.main_frame_graphic_8_2_image_2 = self.main_frame_graphic_8_2_image_1.resize((30, 30))
        self.main_frame_graphic_8_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_8_2_image_2)

        self.main_frame_graphic_8_2_1 = Label(self.main_frame_graphic_8_2, image=self.main_frame_graphic_8_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_8_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.main_frame_graphic_8_2_2 = Label(self.main_frame_graphic_8_2,text="100",bg=self.box_in_box_background_color, font=("Bungee Inline", 12), fg=self.box_text_color_big)
        self.main_frame_graphic_8_2_2.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



        self.main_frame_graphic_8_3 = Label(self.main_frame_graphic_8_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_8_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_8_3_1 = Label(self.main_frame_graphic_8_3, text="Reports", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_8_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)

        self.main_frame_graphic_8_3_1_1 = Label(self.main_frame_graphic_8_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_8_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)

        self.main_frame_graphic_8_3_1_1 = Label(self.main_frame_graphic_8_3,bg=self.pink)
        self.main_frame_graphic_8_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_8_4 = Label(self.main_frame_graphic_8_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_8_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_8_4_1 = Label(self.main_frame_graphic_8_4, text="Report Compeleted", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_8_4_1.place(relx=0, rely=0, relwidth=0.515, relheight=0.45)

        self.main_frame_graphic_8_4_1_1 = Label(self.main_frame_graphic_8_4, text="0", bg=self.box_in_box_background_color,font=("Cascadia Mono", 10), fg=self.box_text_color_small, anchor=CENTER)
        self.main_frame_graphic_8_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.45)


        self.main_frame_graphic_8_4_2 = Label(self.main_frame_graphic_8_4, text="Report Pending", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_8_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)

        self.main_frame_graphic_8_4_2_1 = Label(self.main_frame_graphic_8_4, text="0", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=CENTER)
        self.main_frame_graphic_8_4_2_1.place(relx=0.55, rely=0.5, relwidth=0.45, relheight=0.45)







# =========================================    main_frame_graphic_9 ====================================================
        self.main_frame_graphic_9 = Frame(self.root, bg=self.box_background_color,cursor="hand2")
        self.main_frame_graphic_9.place(relx=0.01, rely=0.4, relwidth=0.2, relheight=0.3)
        self.main_frame_graphic_9.bind('<Button-1>',self.main_graphic_dashboard)

        self.main_frame_graphic_9_image_1 = Image.open("33.png")
        self.main_frame_graphic_9_image_2 = self.main_frame_graphic_9_image_1.resize((300, 250))
        self.main_frame_graphic_9_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_9_image_2)

        self.main_frame_graphic_9_1 = Label(self.main_frame_graphic_9, image=self.main_frame_graphic_9_image_3,bg=self.main_background_color)
        self.main_frame_graphic_9_1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_frame_graphic_9_1.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_2 = Label(self.main_frame_graphic_9_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_9_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        self.main_frame_graphic_9_2_image_1 = Image.open("1dashboard.png")
        self.main_frame_graphic_9_2_image_2 = self.main_frame_graphic_9_2_image_1.resize((50, 50))
        self.main_frame_graphic_9_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_9_2_image_2)

        self.main_frame_graphic_9_2_1 = Label(self.main_frame_graphic_9_2, image=self.main_frame_graphic_9_2_image_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_9_2_1.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        self.main_frame_graphic_9_2_1.bind('<Button-1>', self.main_graphic_dashboard)


        self.main_frame_graphic_9_3 = Label(self.main_frame_graphic_9_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_9_3.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)
        self.main_frame_graphic_9_3.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_3_1 = Label(self.main_frame_graphic_9_3, text="Dashboard", bg=self.box_in_box_background_color,font=("Cascadia Mono",20),fg=self.box_text_color_big,anchor=W)
        self.main_frame_graphic_9_3_1.place(relx=0, rely=0, relwidth=1, relheight=0.8)
        self.main_frame_graphic_9_3_1.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_3_1_1 = Label(self.main_frame_graphic_9_3,bg=self.box_in_box_background_color)
        self.main_frame_graphic_9_3_1_1.place(relx=0, rely=0.83, relwidth=1, relheight=0.1)
        self.main_frame_graphic_9_3_1_1.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_3_1_1 = Label(self.main_frame_graphic_9_3,bg=self.orange)
        self.main_frame_graphic_9_3_1_1.place(relx=0, rely=0.83, relwidth=0.1, relheight=0.1)



        self.main_frame_graphic_9_4 = Label(self.main_frame_graphic_9_1, bg=self.box_in_box_background_color)
        self.main_frame_graphic_9_4.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)
        self.main_frame_graphic_9_4.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_4_1 = Label(self.main_frame_graphic_9_4, text="View Data", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_9_4_1.place(relx=0, rely=0, relwidth=0.515, relheight=0.45)
        self.main_frame_graphic_9_4_1.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_4_1_1_image_1 = Image.open("2dashboard.png")
        self.main_frame_graphic_9_4_1_1_image_2 = self.main_frame_graphic_9_4_1_1_image_1.resize((50, 50))
        self.main_frame_graphic_9_4_1_1_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_9_4_1_1_image_2)

        self.main_frame_graphic_9_4_1_1 = Label(self.main_frame_graphic_9_4, image=self.main_frame_graphic_9_4_1_1_image_3, bg=self.box_in_box_background_color, anchor=CENTER)
        self.main_frame_graphic_9_4_1_1.place(relx=0.55, rely=0, relwidth=0.45, relheight=0.9)
        self.main_frame_graphic_9_4_1_1.bind('<Button-1>', self.main_graphic_dashboard)

        self.main_frame_graphic_9_4_2 = Label(self.main_frame_graphic_9_4, text="Analysis Data", bg=self.box_in_box_background_color, font=("Cascadia Mono", 10), fg=self.box_text_color_small,anchor=W)
        self.main_frame_graphic_9_4_2.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.45)
        self.main_frame_graphic_9_4_2.bind('<Button-1>', self.main_graphic_dashboard)




# =========================================    main_frame_graphic_10 ====================================================
        self.main_frame_graphic_10 = Frame(self.root, bg=self.main_background_upward_color)
        self.main_frame_graphic_10.place(relx=0.2, rely=0.12, relwidth=0.4, relheight=0.1)


        self.main_frame_graphic_10_1 = Label(self.main_frame_graphic_10,text="Restaurant Management System", bg=self.main_background_upward_color,font=("Mistral", 32,"bold"),fg=self.box_in_box_background_color,anchor=W)
        self.main_frame_graphic_10_1.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.main_frame_graphic_10_2_image_1 = Image.open("rrr.png")
        self.main_frame_graphic_10_2_image_2 = self.main_frame_graphic_10_2_image_1.resize((50, 50))
        self.main_frame_graphic_10_2_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_10_2_image_2)


        self.main_frame_graphic_10_2 = Label(self.main_frame_graphic_10, bg=self.main_background_upward_color,image=self.main_frame_graphic_10_2_image_3,anchor=E)
        self.main_frame_graphic_10_2.place(relx=0, rely=0, relwidth=0.2, relheight=1)





# =========================================    main_frame_graphic_11 ====================================================
        self.main_frame_graphic_11 = Frame(self.root, bg=self.main_background_upward_color,cursor="hand2")
        self.main_frame_graphic_11.place(relx=0.85, rely=0.03, relwidth=0.12, relheight=0.06)

        self.main_frame_graphic_11_1_image_1 = Image.open("man_12.png")
        self.main_frame_graphic_11_1_image_2 = self.main_frame_graphic_11_1_image_1.resize((60, 60))
        self.main_frame_graphic_11_1_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_11_1_image_2)


        self.main_frame_graphic_11_1 = Label(self.main_frame_graphic_11, bg=self.main_background_upward_color,image=self.main_frame_graphic_11_1_image_3,anchor=E)
        self.main_frame_graphic_11_1.place(relx=0, rely=0, relwidth=0.325, relheight=1)

        self.main_frame_graphic_11_2 = Label(self.main_frame_graphic_11,text="Log out", bg=self.main_background_upward_color,font=("Comic Sans MS", 20),fg=self.box_in_box_background_color,anchor=W)
        self.main_frame_graphic_11_2.place(relx=0.325, rely=0, relwidth=0.675, relheight=1)
        self.main_frame_graphic_11_2.bind('<Button-1>',self.logouttt)





# =========================================    main_frame_graphic_12 ====================================================
        self.main_frame_graphic_12 = Frame(self.root, bg=self.main_background_upward_color,cursor="hand2")
        self.main_frame_graphic_12.place(relx=0.01, rely=0.01, relwidth=0.025, relheight=0.07)


        self.main_frame_graphic_12_1_image_1 = Image.open("op_1.png")
        self.main_frame_graphic_12_1_image_2 = self.main_frame_graphic_12_1_image_1.resize((25, 25))
        self.main_frame_graphic_12_1_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_12_1_image_2)


        self.main_frame_graphic_12_1 = Label(self.main_frame_graphic_12, bg=self.main_background_upward_color,image=self.main_frame_graphic_12_1_image_3,anchor=CENTER)
        self.main_frame_graphic_12_1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.main_frame_graphic_12.bind('<Button-1>',self.chage_display_screen)
        self.main_frame_graphic_12_1.bind('<Button-1>', self.chage_display_screen)

    def change_1(self):
        self.main_frame_graphic_12 = Frame(self.root, bg=self.main_background_upward_color,cursor="hand2")
        self.main_frame_graphic_12.place(relx=0.01, rely=0.01, relwidth=0.025, relheight=0.07)


        self.main_frame_graphic_12_1_image_1 = Image.open("op_1.png")
        self.main_frame_graphic_12_1_image_2 = self.main_frame_graphic_12_1_image_1.resize((25, 25))
        self.main_frame_graphic_12_1_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_12_1_image_2)


        self.main_frame_graphic_12_1 = Label(self.main_frame_graphic_12, bg=self.main_background_upward_color,image=self.main_frame_graphic_12_1_image_3,anchor=CENTER)
        self.main_frame_graphic_12_1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.main_frame_graphic_12.bind('<Button-1>',self.chage_display_screen)
        self.main_frame_graphic_12_1.bind('<Button-1>', self.chage_display_screen)


    def chage_display_screen(self,e):

        self.main_frame_graphic_12_2 = Frame(self.root, bg=self.main_background_color,cursor="hand2")
        self.main_frame_graphic_12_2.place(relx=0.04, rely=0.035, relwidth=0.12, relheight=0.07)

        self.main_frame_graphic_12_3_image_1 = Image.open("33.png")
        self.main_frame_graphic_12_3_image_2 = self.main_frame_graphic_12_3_image_1.resize((180, 55))
        self.main_frame_graphic_12_3_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_12_3_image_2)


        self.main_frame_graphic_12_3 = Label(self.main_frame_graphic_12_2, bg=self.main_background_upward_color,image=self.main_frame_graphic_12_3_image_3,anchor=CENTER)
        self.main_frame_graphic_12_3.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_frame_graphic_12_4 = Label(self.main_frame_graphic_12_3, bg=self.box_in_box_background_color)
        self.main_frame_graphic_12_4.place(relx=0.04, rely=0.03, relwidth=0.4, relheight=0.94)

        self.main_frame_graphic_12_5_image_1 = Image.open("AII.png")
        self.main_frame_graphic_12_5_image_2 = self.main_frame_graphic_12_5_image_1.resize((85, 52))
        self.main_frame_graphic_12_5_image_3 = ImageTk.PhotoImage(self.main_frame_graphic_12_5_image_2)


        self.main_frame_graphic_12_5 = Label(self.main_frame_graphic_12_4, bg=self.box_in_box_background_color,image=self.main_frame_graphic_12_5_image_3,anchor=CENTER)
        self.main_frame_graphic_12_5.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.main_frame_graphic_12_6 = Label(self.main_frame_graphic_12_3,text="Change Display", font=("Cascadia Mono", 8),bg=self.box_in_box_background_color, anchor=W)
        self.main_frame_graphic_12_6.place(relx=0.45, rely=0.2, relwidth=0.5, relheight=0.6)

        self.main_frame_graphic_12_2.bind('<Button-1>',self.AI_with_me)
        self.main_frame_graphic_12_3.bind('<Button-1>', self.AI_with_me)
        self.main_frame_graphic_12_4.bind('<Button-1>', self.AI_with_me)
        self.main_frame_graphic_12_5.bind('<Button-1>', self.AI_with_me)
        self.main_frame_graphic_12_6.bind('<Button-1>', self.AI_with_me)


        self.main_frame_graphic_12.bind('<Button-1>', self.chage_display_screen_destroy)
        self.main_frame_graphic_12_1.bind('<Button-1>', self.chage_display_screen_destroy)

    def chage_display_screen_destroy(self,e):
        self.main_frame_graphic_12_2.destroy()
        self.change_1()

    def AI_with_me(self,e):
        messagebox.askyesnocancel("Change screen","Are you sure you want to go with AI?")

    def call_nex_page_1(self,e):
        self.root.destroy()
        os.system('main_billing_syatem.py')











#======================================================================================== main graphic counter ==================================================================================



    def main_graphic_counter(self):
        self.main_background_color = "#F1F4F9"
        self.main_background_upward_color = "#4150F5"
        self.box_background_color = "#E0E0E0"
        self.box_in_box_background_color = "#ffffff"
        self.box_text_color_big = "#1B2026"
        self.box_text_color_small = "#72706E"

# =========================================    main_counter_graphic_1 ====================================================
        self.main_counter_graphic_1 = Frame(self.root, bg=self.main_background_color)
        self.main_counter_graphic_1.place(relx=0, rely=0, relwidth=1, relheight=1)

# =========================================    main_counter_graphic_2 ====================================================
        self.main_counter_graphic_2 = Frame(self.main_counter_graphic_1, bg=self.main_background_upward_color)
        self.main_counter_graphic_2.place(relx=0, rely=0, relwidth=1, relheight=0.15)


# =========================================    main_counter_graphic_3 ====================================================
        self.main_counter_graphic_3 = Frame(self.main_counter_graphic_1, bg=self.box_in_box_background_color,bd=1,relief="solid")
        self.main_counter_graphic_3.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)


# =========================================    main_counter_graphic_3_1 ====================================================
        self.main_counter_graphic_3_1 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
        self.main_counter_graphic_3_1.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        self.main_counter_graphic_3_1_1 = Frame(self.main_counter_graphic_3_1, bg=self.box_in_box_background_color,bd=1,relief="solid")
        self.main_counter_graphic_3_1_1.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        self.main_counter_graphic_3_1_1_Enter_search = Entry(self.main_counter_graphic_3_1_1, bg=self.box_in_box_background_color,bd=1,relief="solid")
        self.main_counter_graphic_3_1_1_Enter_search.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_counter_graphic_3_1_1_Enter_search.insert(0,"search")


        self.main_counter_graphic_3_1_2 = Frame(self.main_counter_graphic_3_1, bg=self.box_in_box_background_color)
        self.main_counter_graphic_3_1_2.place(relx=0, rely=0.08, relwidth=1, relheight=0.92)



        #  # =========================================    main_counter_graphic_3_2 ====================================================
#         self.main_counter_graphic_3_2 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
#         self.main_counter_graphic_3_2.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.5)
#
# # =========================================    main_counter_graphic_3_3 ====================================================
#         self.main_counter_graphic_3_3 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
#         self.main_counter_graphic_3_3.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.5)
#
# # =========================================    main_counter_graphic_3_4 ====================================================
#         self.main_counter_graphic_3_4 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
#         self.main_counter_graphic_3_4.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.5)
#
# # =========================================    main_counter_graphic_3_4 ====================================================
#         self.main_counter_graphic_3_5 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
#         self.main_counter_graphic_3_5.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.5)
#
# # =========================================    main_counter_graphic_3_5 ====================================================
#         self.main_counter_graphic_3_6 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
#         self.main_counter_graphic_3_6.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5)
#
# # =========================================    main_counter_graphic_3_6 ====================================================
#         self.main_counter_graphic_3_7 = Frame(self.main_counter_graphic_3, bg=self.box_in_box_background_color,bd=1,relief="solid")
#         self.main_counter_graphic_3_7.place(relx=0.75, rely=0.5, relwidth=0.25, relheight=0.5)
#











    def main_graphic_dashboard(self,e):
        self.main_background_color = "#F1F4F9"
        self.main_background_upward_color = "#ffffff"
        self.box_background_color = "#E0E0E0"
        self.box_in_box_background_color = "#ffffff"
        self.box_text_color_big = "#1B2026"
        self.box_text_color_small = "#72706E"
        self.box_on_click = '#4150F5'
        self.before_click = "#7a7a7a"
        self.after_click = "#000000"
        self.shadow = "#EFEFEF"

# =========================================    main_background ====================================================
        self.main_background = Frame(self.root, bg=self.main_background_color)
        self.main_background.place(relx=0, rely=0, relwidth=1, relheight=1)

# =========================================    main_left ====================================================
        self.main_left_back = Frame(self.root, bg=self.shadow)
        self.main_left_back.place(relx=0, rely=0, relwidth=0.13, relheight=1)

        self.main_left = Frame(self.main_left_back, bg=self.main_background_upward_color)
        self.main_left.place(relx=0, rely=0, relwidth=0.994, relheight=1)


# =========================================    main_left_icon ====================================================
        self.main_left_icon_back = Frame(self.main_left, bg=self.shadow)
        self.main_left_icon_back.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        self.main_left_icon = Frame(self.main_left_icon_back, bg=self.main_background_upward_color)
        self.main_left_icon.place(relx=0, rely=0, relwidth=1, relheight=0.99)

        self.main_left_icon_image_1 = Image.open("mainicon.png")
        self.main_left_icon_image_2 = self.main_left_icon_image_1.resize((70,70))
        self.main_left_icon_image_3 = ImageTk.PhotoImage(self.main_left_icon_image_2)

        self.img1=Image.open("z1.png")
        self.img11=self.img1.resize((110, 75))
        self.img2=Image.open("z2.png")
        self.img22=self.img2.resize((110, 75))
        self.img3=Image.open("z3.png")
        self.img33=self.img3.resize((110, 75))
        self.img4=Image.open("z4.png")
        self.img44=self.img4.resize((110, 75))
        self.img1=ImageTk.PhotoImage(self.img11)
        self.img2=ImageTk.PhotoImage(self.img22)
        self.img3=ImageTk.PhotoImage(self.img33)
        self.img4=ImageTk.PhotoImage(self.img44)


        self.main_left_icon_image = Label(self.main_left_icon,image=self.img1, bg=self.main_background_upward_color, cursor="hand2")
        self.main_left_icon_image.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.animate()
        self.main_left_icon_image.bind('<Button-1>',self.home)


        # =========================================    main_left_dashboard ====================================================
        self.main_left_dashboard = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_dashboard.place(relx=0, rely=0.09, relwidth=1, relheight=0.09)

        self.main_left_dashboard_1 = Label(self.main_left_dashboard, bg=self.main_background_upward_color)
        self.main_left_dashboard_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_dashboard_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_dashboard_image_w_2 = self.main_left_dashboard_image_w_1.resize((47,40))
        self.main_left_dashboard_image_w_3 = ImageTk.PhotoImage(self.main_left_dashboard_image_w_2)

        self.main_left_dashboard_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_dashboard_image_2 = self.main_left_dashboard_image_1.resize((47,40))
        self.main_left_dashboard_image_3 = ImageTk.PhotoImage(self.main_left_dashboard_image_2)


        self.main_left_dashboard_image_frame = Label(self.main_left_dashboard_1,image=self.main_left_dashboard_image_3, bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_dashboard_image_w_1_1 = Image.open("3dashboard.png")
        self.main_left_dashboard_image_w_2_1 = self.main_left_dashboard_image_w_1_1.resize((25,25))
        self.main_left_dashboard_image_w_3_1 = ImageTk.PhotoImage(self.main_left_dashboard_image_w_2_1)

        self.main_left_dashboard_image_1_2 = Image.open("3dashboard_w.png")
        self.main_left_dashboard_image_2_2 = self.main_left_dashboard_image_1_2.resize((25,25))
        self.main_left_dashboard_image_3_2 = ImageTk.PhotoImage(self.main_left_dashboard_image_2_2)


        self.main_left_dashboard_image_frame_1 = Label(self.main_left_dashboard_image_frame, image=self.main_left_dashboard_image_3_2, bg=self.box_on_click)
        self.main_left_dashboard_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_dashboard_label = Label(self.main_left_dashboard_1,text="Dashboard",bg=self.main_background_upward_color,fg=self.after_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_dashboard_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_dashboard_1.bind('<Button-1>', self.main_left_dashboard_1_fun)
        self.main_left_dashboard_image_frame.bind('<Button-1>', self.main_left_dashboard_1_fun)
        self.main_left_dashboard_image_frame_1.bind('<Button-1>', self.main_left_dashboard_1_fun)
        self.main_left_dashboard_label.bind('<Button-1>', self.main_left_dashboard_1_fun)





# =========================================    main_left_employee ====================================================
        self.main_left_employee = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_employee.place(relx=0, rely=0.18, relwidth=1, relheight=0.09)

        self.main_left_employee_1 = Label(self.main_left_employee, bg=self.main_background_upward_color)
        self.main_left_employee_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_employee_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_employee_image_w_2 = self.main_left_employee_image_w_1.resize((47,40))
        self.main_left_employee_image_w_3 = ImageTk.PhotoImage(self.main_left_employee_image_w_2)

        self.main_left_employee_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_employee_image_2 = self.main_left_employee_image_1.resize((47,40))
        self.main_left_employee_image_3 = ImageTk.PhotoImage(self.main_left_employee_image_2)

        self.main_left_employee_image_frame = Label(self.main_left_employee_1,image=self.main_left_employee_image_w_3, bg=self.main_background_upward_color)
        self.main_left_employee_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_employee_image_w_1_1 = Image.open("em_1.png")
        self.main_left_employee_image_w_2_1 = self.main_left_employee_image_w_1_1.resize((25,25))
        self.main_left_employee_image_w_3_1 = ImageTk.PhotoImage(self.main_left_employee_image_w_2_1)

        self.main_left_employee_image_1_2 = Image.open("em_1_w.png")
        self.main_left_employee_image_2_2 = self.main_left_employee_image_1_2.resize((25,25))
        self.main_left_employee_image_3_2 = ImageTk.PhotoImage(self.main_left_employee_image_2_2)


        self.main_left_employee_image_frame_1 = Label(self.main_left_employee_image_frame, image=self.main_left_employee_image_w_3_1, bg=self.main_background_color)
        self.main_left_employee_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_employee_label = Label(self.main_left_employee_1,text="Employee",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_employee_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_employee_1.bind('<Button-1>', self.main_left_employee_1_fun)
        self.main_left_employee_image_frame.bind('<Button-1>', self.main_left_employee_1_fun)
        self.main_left_employee_image_frame_1.bind('<Button-1>', self.main_left_employee_1_fun)
        self.main_left_employee_label.bind('<Button-1>', self.main_left_employee_1_fun)

















# =========================================    main_left_item ====================================================
        self.main_left_item = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_item.place(relx=0, rely=0.27, relwidth=1, relheight=0.09)

        self.main_left_item_1 = Label(self.main_left_item, bg=self.main_background_upward_color)
        self.main_left_item_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_item_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_item_image_w_2 = self.main_left_item_image_w_1.resize((47,40))
        self.main_left_item_image_w_3 = ImageTk.PhotoImage(self.main_left_item_image_w_2)

        self.main_left_item_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_item_image_2 = self.main_left_item_image_1.resize((47,40))
        self.main_left_item_image_3 = ImageTk.PhotoImage(self.main_left_item_image_2)

        self.main_left_item_image_frame = Label(self.main_left_item_1,image=self.main_left_item_image_w_3, bg=self.main_background_upward_color)
        self.main_left_item_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_item_image_w_1_1 = Image.open("it_1.png")
        self.main_left_item_image_w_2_1 = self.main_left_item_image_w_1_1.resize((25,25))
        self.main_left_item_image_w_3_1 = ImageTk.PhotoImage(self.main_left_item_image_w_2_1)

        self.main_left_item_image_1_2 = Image.open("it_1_w.png")
        self.main_left_item_image_2_2 = self.main_left_item_image_1_2.resize((25,25))
        self.main_left_item_image_3_2 = ImageTk.PhotoImage(self.main_left_item_image_2_2)


        self.main_left_item_image_frame_1 = Label(self.main_left_item_image_frame, image=self.main_left_item_image_w_3_1, bg=self.main_background_color)
        self.main_left_item_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_item_label = Label(self.main_left_item_1,text="Items",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_item_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_item_1.bind('<Button-1>', self.main_left_item_1_fun)
        self.main_left_item_image_frame.bind('<Button-1>', self.main_left_item_1_fun)
        self.main_left_item_image_frame_1.bind('<Button-1>', self.main_left_item_1_fun)
        self.main_left_item_label.bind('<Button-1>', self.main_left_item_1_fun)


# =========================================    main_left_table ====================================================
        self.main_left_table = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_table.place(relx=0, rely=0.36, relwidth=1, relheight=0.09)

        self.main_left_table_1 = Label(self.main_left_table, bg=self.main_background_upward_color)
        self.main_left_table_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_table_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_table_image_w_2 = self.main_left_table_image_w_1.resize((47,40))
        self.main_left_table_image_w_3 = ImageTk.PhotoImage(self.main_left_table_image_w_2)

        self.main_left_table_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_table_image_2 = self.main_left_table_image_1.resize((47,40))
        self.main_left_table_image_3 = ImageTk.PhotoImage(self.main_left_table_image_2)

        self.main_left_table_image_frame = Label(self.main_left_table_1,image=self.main_left_table_image_w_3, bg=self.main_background_upward_color)
        self.main_left_table_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_table_image_w_1_1 = Image.open("ta_1.png")
        self.main_left_table_image_w_2_1 = self.main_left_table_image_w_1_1.resize((25,25))
        self.main_left_table_image_w_3_1 = ImageTk.PhotoImage(self.main_left_table_image_w_2_1)

        self.main_left_table_image_1_2 = Image.open("ta_1_w.png")
        self.main_left_table_image_2_2 = self.main_left_table_image_1_2.resize((25,25))
        self.main_left_table_image_3_2 = ImageTk.PhotoImage(self.main_left_table_image_2_2)


        self.main_left_table_image_frame_1 = Label(self.main_left_table_image_frame, image=self.main_left_table_image_w_3_1, bg=self.main_background_color)
        self.main_left_table_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_table_label = Label(self.main_left_table_1,text="Tables",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_table_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_table_1.bind('<Button-1>', self.main_left_table_1_fun)
        self.main_left_table_image_frame.bind('<Button-1>', self.main_left_table_1_fun)
        self.main_left_table_image_frame_1.bind('<Button-1>', self.main_left_table_1_fun)
        self.main_left_table_label.bind('<Button-1>', self.main_left_table_1_fun)


# =========================================    main_left_materials ====================================================
        self.main_left_materials = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_materials.place(relx=0, rely=0.45, relwidth=1, relheight=0.09)

        self.main_left_materials_1 = Label(self.main_left_materials, bg=self.main_background_upward_color)
        self.main_left_materials_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_materials_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_materials_image_w_2 = self.main_left_materials_image_w_1.resize((47,40))
        self.main_left_materials_image_w_3 = ImageTk.PhotoImage(self.main_left_materials_image_w_2)

        self.main_left_materials_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_materials_image_2 = self.main_left_materials_image_1.resize((47,40))
        self.main_left_materials_image_3 = ImageTk.PhotoImage(self.main_left_materials_image_2)

        self.main_left_materials_image_frame = Label(self.main_left_materials_1,image=self.main_left_materials_image_w_3, bg=self.main_background_upward_color)
        self.main_left_materials_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_materials_image_w_1_1 = Image.open("met_1.png")
        self.main_left_materials_image_w_2_1 = self.main_left_materials_image_w_1_1.resize((25,25))
        self.main_left_materials_image_w_3_1 = ImageTk.PhotoImage(self.main_left_materials_image_w_2_1)

        self.main_left_materials_image_1_2 = Image.open("met_1_w.png")
        self.main_left_materials_image_2_2 = self.main_left_materials_image_1_2.resize((25,25))
        self.main_left_materials_image_3_2 = ImageTk.PhotoImage(self.main_left_materials_image_2_2)


        self.main_left_materials_image_frame_1 = Label(self.main_left_materials_image_frame, image=self.main_left_materials_image_w_3_1, bg=self.main_background_color)
        self.main_left_materials_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_materials_label = Label(self.main_left_materials_1,text="Material",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_materials_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_materials_1.bind('<Button-1>', self.main_left_materials_1_fun)
        self.main_left_materials_image_frame.bind('<Button-1>', self.main_left_materials_1_fun)
        self.main_left_materials_image_frame_1.bind('<Button-1>', self.main_left_materials_1_fun)
        self.main_left_materials_label.bind('<Button-1>', self.main_left_materials_1_fun)


# =========================================    main_left_sales ====================================================
        self.main_left_sales = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_sales.place(relx=0, rely=0.54, relwidth=1, relheight=0.09)

        self.main_left_sales_1 = Label(self.main_left_sales, bg=self.main_background_upward_color)
        self.main_left_sales_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_sales_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_sales_image_w_2 = self.main_left_sales_image_w_1.resize((47,40))
        self.main_left_sales_image_w_3 = ImageTk.PhotoImage(self.main_left_sales_image_w_2)

        self.main_left_sales_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_sales_image_2 = self.main_left_sales_image_1.resize((47,40))
        self.main_left_sales_image_3 = ImageTk.PhotoImage(self.main_left_sales_image_2)

        self.main_left_sales_image_frame = Label(self.main_left_sales_1,image=self.main_left_sales_image_w_3, bg=self.main_background_upward_color)
        self.main_left_sales_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_sales_image_w_1_1 = Image.open("sal_1.png")
        self.main_left_sales_image_w_2_1 = self.main_left_sales_image_w_1_1.resize((25,25))
        self.main_left_sales_image_w_3_1 = ImageTk.PhotoImage(self.main_left_sales_image_w_2_1)

        self.main_left_sales_image_1_2 = Image.open("sal_1_w.png")
        self.main_left_sales_image_2_2 = self.main_left_sales_image_1_2.resize((25,25))
        self.main_left_sales_image_3_2 = ImageTk.PhotoImage(self.main_left_sales_image_2_2)


        self.main_left_sales_image_frame_1 = Label(self.main_left_sales_image_frame, image=self.main_left_sales_image_w_3_1, bg=self.main_background_color)
        self.main_left_sales_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_sales_label = Label(self.main_left_sales_1,text="Sale",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_sales_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_sales_1.bind('<Button-1>', self.main_left_sales_1_fun)
        self.main_left_sales_image_frame.bind('<Button-1>', self.main_left_sales_1_fun)
        self.main_left_sales_image_frame_1.bind('<Button-1>', self.main_left_sales_1_fun)
        self.main_left_sales_label.bind('<Button-1>', self.main_left_sales_1_fun)



# =========================================    main_left_recipes ====================================================
        self.main_left_recipes = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_recipes.place(relx=0, rely=0.63, relwidth=1, relheight=0.09)

        self.main_left_recipes_1 = Label(self.main_left_recipes, bg=self.main_background_upward_color)
        self.main_left_recipes_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_recipes_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_recipes_image_w_2 = self.main_left_recipes_image_w_1.resize((47,40))
        self.main_left_recipes_image_w_3 = ImageTk.PhotoImage(self.main_left_recipes_image_w_2)

        self.main_left_recipes_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_recipes_image_2 = self.main_left_recipes_image_1.resize((47,40))
        self.main_left_recipes_image_3 = ImageTk.PhotoImage(self.main_left_recipes_image_2)

        self.main_left_recipes_image_frame = Label(self.main_left_recipes_1,image=self.main_left_recipes_image_w_3, bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_recipes_image_w_1_1 = Image.open("rec_1.png")
        self.main_left_recipes_image_w_2_1 = self.main_left_recipes_image_w_1_1.resize((25,25))
        self.main_left_recipes_image_w_3_1 = ImageTk.PhotoImage(self.main_left_recipes_image_w_2_1)

        self.main_left_recipes_image_1_2 = Image.open("rec_1_w.png")
        self.main_left_recipes_image_2_2 = self.main_left_recipes_image_1_2.resize((25,25))
        self.main_left_recipes_image_3_2 = ImageTk.PhotoImage(self.main_left_recipes_image_2_2)


        self.main_left_recipes_image_frame_1 = Label(self.main_left_recipes_image_frame, image=self.main_left_recipes_image_w_3_1, bg=self.main_background_color)
        self.main_left_recipes_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_recipes_label = Label(self.main_left_recipes_1,text="Recipe",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_recipes_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_recipes_1.bind('<Button-1>', self.main_left_recipes_1_fun)
        self.main_left_recipes_image_frame.bind('<Button-1>', self.main_left_recipes_1_fun)
        self.main_left_recipes_image_frame_1.bind('<Button-1>', self.main_left_recipes_1_fun)
        self.main_left_recipes_label.bind('<Button-1>', self.main_left_recipes_1_fun)


# =========================================    main_left_restaurant_info ====================================================
        self.main_left_restaurant_info = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_restaurant_info.place(relx=0, rely=0.72, relwidth=1, relheight=0.09)

        self.main_left_restaurant_info_1 = Label(self.main_left_restaurant_info, bg=self.main_background_upward_color)
        self.main_left_restaurant_info_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_restaurant_info_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_restaurant_info_image_w_2 = self.main_left_restaurant_info_image_w_1.resize((47,40))
        self.main_left_restaurant_info_image_w_3 = ImageTk.PhotoImage(self.main_left_restaurant_info_image_w_2)

        self.main_left_restaurant_info_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_restaurant_info_image_2 = self.main_left_restaurant_info_image_1.resize((47,40))
        self.main_left_restaurant_info_image_3 = ImageTk.PhotoImage(self.main_left_restaurant_info_image_2)

        self.main_left_restaurant_info_image_frame = Label(self.main_left_restaurant_info_1,image=self.main_left_restaurant_info_image_w_3, bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_restaurant_info_image_w_1_1 = Image.open("res_1.png")
        self.main_left_restaurant_info_image_w_2_1 = self.main_left_restaurant_info_image_w_1_1.resize((25,25))
        self.main_left_restaurant_info_image_w_3_1 = ImageTk.PhotoImage(self.main_left_restaurant_info_image_w_2_1)

        self.main_left_restaurant_info_image_1_2 = Image.open("res_1_w.png")
        self.main_left_restaurant_info_image_2_2 = self.main_left_restaurant_info_image_1_2.resize((25,25))
        self.main_left_restaurant_info_image_3_2 = ImageTk.PhotoImage(self.main_left_restaurant_info_image_2_2)


        self.main_left_restaurant_info_image_frame_1 = Label(self.main_left_restaurant_info_image_frame, image=self.main_left_restaurant_info_image_w_3_1, bg=self.main_background_color)
        self.main_left_restaurant_info_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_restaurant_info_label = Label(self.main_left_restaurant_info_1,text="Restaurant info",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_restaurant_info_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_restaurant_info_1.bind('<Button-1>', self.main_left_restaurant_info_1_fun)
        self.main_left_restaurant_info_image_frame.bind('<Button-1>', self.main_left_restaurant_info_1_fun)
        self.main_left_restaurant_info_image_frame_1.bind('<Button-1>', self.main_left_restaurant_info_1_fun)
        self.main_left_restaurant_info_label.bind('<Button-1>', self.main_left_restaurant_info_1_fun)




# =========================================    main_left_setting ====================================================
        self.main_left_setting = Frame(self.main_left, bg=self.main_background_upward_color,cursor="hand2")
        self.main_left_setting.place(relx=0, rely=0.81, relwidth=1, relheight=0.09)


        self.main_left_setting_1 = Label(self.main_left_setting, bg=self.main_background_upward_color)
        self.main_left_setting_1.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.main_left_setting_image_w_1 = Image.open("3dashboard_b.png")
        self.main_left_setting_image_w_2 = self.main_left_setting_image_w_1.resize((47,40))
        self.main_left_setting_image_w_3 = ImageTk.PhotoImage(self.main_left_setting_image_w_2)

        self.main_left_setting_image_1 = Image.open("3dashboard_w_b.png")
        self.main_left_setting_image_2 = self.main_left_setting_image_1.resize((47,40))
        self.main_left_setting_image_3 = ImageTk.PhotoImage(self.main_left_setting_image_2)

        self.main_left_setting_image_frame = Label(self.main_left_setting_1,image=self.main_left_setting_image_w_3, bg=self.main_background_upward_color)
        self.main_left_setting_image_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.6)


        self.main_left_setting_image_w_1_1 = Image.open("sett_1.png")
        self.main_left_setting_image_w_2_1 = self.main_left_setting_image_w_1_1.resize((25,25))
        self.main_left_setting_image_w_3_1 = ImageTk.PhotoImage(self.main_left_setting_image_w_2_1)

        self.main_left_setting_image_1_2 = Image.open("sett_1_w.png")
        self.main_left_setting_image_2_2 = self.main_left_setting_image_1_2.resize((25,25))
        self.main_left_setting_image_3_2 = ImageTk.PhotoImage(self.main_left_setting_image_2_2)


        self.main_left_setting_image_frame_1 = Label(self.main_left_setting_image_frame, image=self.main_left_setting_image_w_3_1, bg=self.main_background_color)
        self.main_left_setting_image_frame_1.place(relx=0.07, rely=0.07, relwidth=0.86, relheight=0.86)

        self.main_left_setting_label = Label(self.main_left_setting_1,text="Settings",bg=self.main_background_upward_color,fg=self.before_click,font=("Comic Sans MS",10,'bold'),anchor=W)
        self.main_left_setting_label.place(relx=0.4, rely=0.33, relwidth=0.6, relheight=0.4)

        self.main_left_setting_1.bind('<Button-1>', self.main_left_setting_1_fun)
        self.main_left_setting_image_frame.bind('<Button-1>', self.main_left_setting_1_fun)
        self.main_left_setting_image_frame_1.bind('<Button-1>', self.main_left_setting_1_fun)
        self.main_left_setting_label.bind('<Button-1>', self.main_left_setting_1_fun)





# =========================================    main_top ====================================================
        self.main_top_full = Frame(self.root, bg=self.main_background_color)
        self.main_top_full.place(relx=0.13, rely=0, relwidth=0.87, relheight=1)

        self.main_top_back = Frame(self.main_top_full, bg=self.shadow)
        self.main_top_back.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        self.main_top = Frame(self.main_top_back, bg=self.main_background_upward_color)
        self.main_top.place(relx=0, rely=0, relwidth=1, relheight=0.99)

# =========================================    main_top_navigation_bar ====================================================
        self.main_top_navigation_bar = Frame(self.main_top, bg=self.main_background_upward_color,cursor="hand2")
        self.main_top_navigation_bar.place(relx=0, rely=0.2, relwidth=0.04, relheight=0.6)

        self.main_left_navigation_bar_1 = Label(self.main_top_navigation_bar, bg=self.main_background_upward_color)
        self.main_left_navigation_bar_1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.main_left_navigation_bar_image_w_1 = Image.open("mu_1.png")
        self.main_left_navigation_bar_image_w_2 = self.main_left_navigation_bar_image_w_1.resize((32, 25))
        self.main_left_navigation_bar_image_w_3 = ImageTk.PhotoImage(self.main_left_navigation_bar_image_w_2)

        self.main_left_navigation_bar_image_1 = Image.open("mu_1_w.png")
        self.main_left_navigation_bar_image_2 = self.main_left_navigation_bar_image_1.resize((33, 28))
        self.main_left_navigation_bar_image_3 = ImageTk.PhotoImage(self.main_left_navigation_bar_image_2)

        self.main_left_navigation_bar_image_frame = Label(self.main_left_navigation_bar_1, image=self.main_left_navigation_bar_image_w_3,bg=self.main_background_upward_color)
        self.main_left_navigation_bar_image_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.main_left_navigation_bar_1.bind('<Enter>', self.main_left_navigation_bar_1_fun_hover_on)
        self.main_left_navigation_bar_image_frame.bind('<Enter>', self.main_left_navigation_bar_1_fun_hover_on)

        self.main_left_navigation_bar_1.bind('<Leave>', self.main_left_navigation_bar_1_fun_hover_off)
        self.main_left_navigation_bar_image_frame.bind('<Leave>', self.main_left_navigation_bar_1_fun_hover_off)
        self.top=0
        self.main_left_navigation_bar_1.bind('<Button-1>', self.main_left_navigation_bar_1_fun)
        self.main_left_navigation_bar_image_frame.bind('<Button-1>', self.main_left_navigation_bar_1_fun)

# =========================================    main_top_temp ====================================================
        self.main_top_temp = Frame(self.main_top, bg=self.main_background_upward_color, cursor="hand2")
        self.main_top_temp.place(relx=0.2, rely=0.1, relwidth=0.15, relheight=0.8)

# =========================================    main_top_logout ====================================================
        self.main_top_logout = Frame(self.main_top, bg=self.main_background_upward_color, cursor="hand2")
        self.main_top_logout.place(relx=0.89, rely=0.2, relwidth=0.1, relheight=0.6)

        self.main_top_logout_image_1 = Image.open("man_1.png")
        self.main_top_logout_image_2 = self.main_top_logout_image_1.resize((50,50))
        self.main_top_logout_image_3 = ImageTk.PhotoImage(self.main_top_logout_image_2)

        self.main_top_logout_image = Button(self.main_top_logout,text="   Log out",font=("Comic Sans MS", 10),image=self.main_top_logout_image_3,compound=LEFT, bg=self.main_background_upward_color,activebackground=self.box_on_click,activeforeground=self.box_in_box_background_color, cursor="hand2",anchor=W,borderwidth=0)
        self.main_top_logout_image.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_top_logout_image.bind('<Button-1>',self.logouttt)
        self.main_Employee_record_main()

    def home(self,e):
        self.root.destroy()
        os.system('main_after_login.py')



    def animate(self):
        self.img = self.img1
        self.img1 = self.img2
        self.img2 = self.img3
        self.img3 = self.img4
        self.img4 = self.img
        self.main_left_icon_image.config(image=self.img)
        self.main_left_icon_image.after(5000, self.animate)

    def  main_Employee_record_main(self):
#======================================  main_Employee_record ========================================================

        self.main_Employee_record = Frame(self.main_top_full, bg=self.main_background_color)
        self.main_Employee_record.place(relx=0, rely=0.09, relwidth=1, relheight=0.9)

#==================  Upward_part_of_Employee_record ===================

        self.upward_part_of_employee_record = Frame(self.main_Employee_record, bg=self.main_background_color)
        self.upward_part_of_employee_record.place(relx=0, rely=0, relwidth=1, relheight=0.2)
#=======Total========
        self.upward_part_of_employee_record_total = Frame(self.upward_part_of_employee_record, bg=self.main_background_color)
        self.upward_part_of_employee_record_total.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        self.upward_part_of_employee_record_total_1 = Frame(self.upward_part_of_employee_record_total, bg=self.main_background_color)
        self.upward_part_of_employee_record_total_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)

        self.upward_part_of_employee_record_total_image_1_1 = Image.open("33.png")
        self.upward_part_of_employee_record_total_image_2_1 = self.upward_part_of_employee_record_total_image_1_1.resize((278,98))
        self.upward_part_of_employee_record_total_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_total_image_2_1)

        self.upward_part_of_employee_record_total_image_1_2 = Image.open("33_on.png")
        self.upward_part_of_employee_record_total_image_2_2 = self.upward_part_of_employee_record_total_image_1_2.resize((278,98))
        self.upward_part_of_employee_record_total_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_total_image_2_2)


        self.upward_part_of_employee_record_total_image = Label(self.upward_part_of_employee_record_total_1,image=self.upward_part_of_employee_record_total_image_3_2, bg=self.main_background_color)
        self.upward_part_of_employee_record_total_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.upward_part_of_employee_record_total_inside_image = Frame(self.upward_part_of_employee_record_total_image, bg=self.box_on_click)
        self.upward_part_of_employee_record_total_inside_image.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.88)

        self.upward_part_of_employee_record_total_inside_image_image_1_1 = Image.open("to_em_1.png")
        self.upward_part_of_employee_record_total_inside_image_image_2_1 = self.upward_part_of_employee_record_total_inside_image_image_1_1.resize((50,50))
        self.upward_part_of_employee_record_total_inside_image_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_total_inside_image_image_2_1)

        self.upward_part_of_employee_record_total_inside_image_image_1_2 = Image.open("to_em_1_w.png")
        self.upward_part_of_employee_record_total_inside_image_image_2_2 = self.upward_part_of_employee_record_total_inside_image_image_1_2.resize((40,40))
        self.upward_part_of_employee_record_total_inside_image_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_total_inside_image_image_2_2)


        self.upward_part_of_employee_record_total_inside_image_image = Label(self.upward_part_of_employee_record_total_inside_image,image=self.upward_part_of_employee_record_total_inside_image_image_3_2, bg=self.box_on_click)
        self.upward_part_of_employee_record_total_inside_image_image.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
        self.cur = self.con.cursor()
        self.cur.execute("SELECT First_name FROM employee_data")
        self.number_tt = self.cur.fetchall()
        self.print_total = len(self.number_tt)



        self.upward_part_of_employee_record_total_inside_image_number = Label(self.upward_part_of_employee_record_total_inside_image,text=f"{self.print_total}",font=("Cascadia Mono",20),bg=self.box_on_click, fg=self.main_background_upward_color,anchor=SE)
        self.upward_part_of_employee_record_total_inside_image_number.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.8)


        self.con.commit()
        self.con.close()
        self.cur.close()

        self.upward_part_of_employee_record_total_inside_image_theo = Label(self.upward_part_of_employee_record_total_inside_image,font=("Cascadia Mono",7),text="Total Number of Employees",bg=self.box_on_click, fg=self.main_background_upward_color,anchor=E)
        self.upward_part_of_employee_record_total_inside_image_theo.place(relx=0.3, rely=0.8, relwidth=0.7, relheight=0.2)

        self.upward_part_of_employee_record_total_image.bind('<Button-1>',self.number_of_employee)
        self.upward_part_of_employee_record_total_inside_image.bind('<Button-1>', self.number_of_employee)
        self.upward_part_of_employee_record_total_inside_image_image.bind('<Button-1>', self.number_of_employee)
        self.upward_part_of_employee_record_total_inside_image_number.bind('<Button-1>', self.number_of_employee)
        self.upward_part_of_employee_record_total_inside_image_theo.bind('<Button-1>', self.number_of_employee)


# =======add========
        self.upward_part_of_employee_record_add = Frame(self.upward_part_of_employee_record, bg=self.main_background_color)
        self.upward_part_of_employee_record_add.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)


        self.upward_part_of_employee_record_add_1 = Frame(self.upward_part_of_employee_record_add, bg=self.main_background_color)
        self.upward_part_of_employee_record_add_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)


        self.upward_part_of_employee_record_add_image_1_1 = Image.open("33.png")
        self.upward_part_of_employee_record_add_image_2_1 = self.upward_part_of_employee_record_add_image_1_1.resize((278,98))
        self.upward_part_of_employee_record_add_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_add_image_2_1)

        self.upward_part_of_employee_record_add_image_1_2 = Image.open("33_on.png")
        self.upward_part_of_employee_record_add_image_2_2 = self.upward_part_of_employee_record_add_image_1_2.resize((278,98))
        self.upward_part_of_employee_record_add_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_add_image_2_2)


        self.upward_part_of_employee_record_add_image = Label(self.upward_part_of_employee_record_add_1,image=self.upward_part_of_employee_record_add_image_3_1, bg=self.main_background_color)
        self.upward_part_of_employee_record_add_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.upward_part_of_employee_record_add_inside_image = Frame(self.upward_part_of_employee_record_add_image, bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_add_inside_image.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.88)

        self.upward_part_of_employee_record_add_inside_image_image_1_1 = Image.open("to_add_1.png")
        self.upward_part_of_employee_record_add_inside_image_image_2_1 = self.upward_part_of_employee_record_add_inside_image_image_1_1.resize((50,50))
        self.upward_part_of_employee_record_add_inside_image_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_add_inside_image_image_2_1)

        self.upward_part_of_employee_record_add_inside_image_image_1_2 = Image.open("to_add_1_w.png")
        self.upward_part_of_employee_record_add_inside_image_image_2_2 = self.upward_part_of_employee_record_add_inside_image_image_1_2.resize((40,40))
        self.upward_part_of_employee_record_add_inside_image_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_add_inside_image_image_2_2)


        self.upward_part_of_employee_record_add_inside_image_image = Label(self.upward_part_of_employee_record_add_inside_image,image=self.upward_part_of_employee_record_add_inside_image_image_3_1, bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_add_inside_image_image.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        #
        self.upward_part_of_employee_record_add_inside_image_number = Label(self.upward_part_of_employee_record_add_inside_image,text="Add New Employee",font=("Cascadia Mono",13),fg=self.box_on_click, bg=self.main_background_upward_color,anchor=CENTER)
        self.upward_part_of_employee_record_add_inside_image_number.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        #
        # self.upward_part_of_employee_record_add_inside_image_theo = Label(self.upward_part_of_employee_record_add_inside_image,font=("Cascadia Mono",7),text="Total Number of Employees",fg=self.box_on_click, bg=self.main_background_upward_color,anchor=E, bd=1, relief="solid")
        # self.upward_part_of_employee_record_add_inside_image_theo.place(relx=0.3, rely=0.8, relwidth=0.7, relheight=0.2)

        self.upward_part_of_employee_record_add_image.bind('<Button-1>',self.add_to_of_employee)
        self.upward_part_of_employee_record_add_inside_image.bind('<Button-1>', self.add_to_of_employee)
        self.upward_part_of_employee_record_add_inside_image_image.bind('<Button-1>', self.add_to_of_employee)
        self.upward_part_of_employee_record_add_inside_image_number.bind('<Button-1>', self.add_to_of_employee)




# =======remove========================================================
        self.upward_part_of_employee_record_remove = Frame(self.upward_part_of_employee_record, bg=self.main_background_color)
        self.upward_part_of_employee_record_remove.place(relx=0.5, rely=0, relwidth=0.25, relheight=1)


        self.upward_part_of_employee_record_remove_1 = Frame(self.upward_part_of_employee_record_remove, bg=self.main_background_color)
        self.upward_part_of_employee_record_remove_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)

        self.upward_part_of_employee_record_remove_image_1_1 = Image.open("33.png")
        self.upward_part_of_employee_record_remove_image_2_1 = self.upward_part_of_employee_record_remove_image_1_1.resize((278,98))
        self.upward_part_of_employee_record_remove_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_remove_image_2_1)

        self.upward_part_of_employee_record_remove_image_1_2 = Image.open("33_on.png")
        self.upward_part_of_employee_record_remove_image_2_2 = self.upward_part_of_employee_record_remove_image_1_2.resize((278,98))
        self.upward_part_of_employee_record_remove_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_remove_image_2_2)

        self.upward_part_of_employee_record_remove_image = Label(self.upward_part_of_employee_record_remove_1,image=self.upward_part_of_employee_record_remove_image_3_1, bg=self.main_background_color)
        self.upward_part_of_employee_record_remove_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.upward_part_of_employee_record_remove_inside_image = Frame(self.upward_part_of_employee_record_remove_image, bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_remove_inside_image.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.88)

        self.upward_part_of_employee_record_remove_inside_image_image_1_1 = Image.open("to_remove_1.png")
        self.upward_part_of_employee_record_remove_inside_image_image_2_1 = self.upward_part_of_employee_record_remove_inside_image_image_1_1.resize((50,50))
        self.upward_part_of_employee_record_remove_inside_image_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_remove_inside_image_image_2_1)

        self.upward_part_of_employee_record_remove_inside_image_image_1_2 = Image.open("to_remove_1_w.png")
        self.upward_part_of_employee_record_remove_inside_image_image_2_2 = self.upward_part_of_employee_record_remove_inside_image_image_1_2.resize((40,40))
        self.upward_part_of_employee_record_remove_inside_image_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_remove_inside_image_image_2_2)


        self.upward_part_of_employee_record_remove_inside_image_image = Label(self.upward_part_of_employee_record_remove_inside_image,image=self.upward_part_of_employee_record_remove_inside_image_image_3_1, bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_remove_inside_image_image.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        #
        self.upward_part_of_employee_record_remove_inside_image_number = Label(self.upward_part_of_employee_record_remove_inside_image,text="Remove Employee",font=("Cascadia Mono",13),fg=self.box_on_click, bg=self.main_background_upward_color,anchor=CENTER)
        self.upward_part_of_employee_record_remove_inside_image_number.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        #
        # self.upward_part_of_employee_record_remove_inside_image_theo = Label(self.upward_part_of_employee_record_remove_inside_image,font=("Cascadia Mono",7),text="Total Number of Employees",fg=self.box_on_click, bg=self.main_background_upward_color,anchor=E, bd=1, relief="solid")
        # self.upward_part_of_employee_record_remove_inside_image_theo.place(relx=0.3, rely=0.8, relwidth=0.7, relheight=0.2)

        self.upward_part_of_employee_record_remove_image.bind('<Button-1>',self.remove_to_of_employee)
        self.upward_part_of_employee_record_remove_inside_image.bind('<Button-1>', self.remove_to_of_employee)
        self.upward_part_of_employee_record_remove_inside_image_image.bind('<Button-1>', self.remove_to_of_employee)
        self.upward_part_of_employee_record_remove_inside_image_number.bind('<Button-1>', self.remove_to_of_employee)




# =======Edit========
        self.upward_part_of_employee_record_edit = Frame(self.upward_part_of_employee_record, bg=self.main_background_color)
        self.upward_part_of_employee_record_edit.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)



        self.upward_part_of_employee_record_edit_1 = Frame(self.upward_part_of_employee_record_edit, bg=self.main_background_color)
        self.upward_part_of_employee_record_edit_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)

        self.upward_part_of_employee_record_edit_image_1_1 = Image.open("33.png")
        self.upward_part_of_employee_record_edit_image_2_1 = self.upward_part_of_employee_record_edit_image_1_1.resize((278,98))
        self.upward_part_of_employee_record_edit_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_edit_image_2_1)

        self.upward_part_of_employee_record_edit_image_1_2 = Image.open("33_on.png")
        self.upward_part_of_employee_record_edit_image_2_2 = self.upward_part_of_employee_record_edit_image_1_2.resize((278,98))
        self.upward_part_of_employee_record_edit_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_edit_image_2_2)

        self.upward_part_of_employee_record_edit_image = Label(self.upward_part_of_employee_record_edit_1,image=self.upward_part_of_employee_record_edit_image_3_1, bg=self.main_background_color)
        self.upward_part_of_employee_record_edit_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.upward_part_of_employee_record_edit_inside_image = Frame(self.upward_part_of_employee_record_edit_image, bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_edit_inside_image.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.88)

        self.upward_part_of_employee_record_edit_inside_image_image_1_1 = Image.open("to_edit_1.png")
        self.upward_part_of_employee_record_edit_inside_image_image_2_1 = self.upward_part_of_employee_record_edit_inside_image_image_1_1.resize((50,50))
        self.upward_part_of_employee_record_edit_inside_image_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_employee_record_edit_inside_image_image_2_1)

        self.upward_part_of_employee_record_edit_inside_image_image_1_2 = Image.open("to_edit_1_w.png")
        self.upward_part_of_employee_record_edit_inside_image_image_2_2 = self.upward_part_of_employee_record_edit_inside_image_image_1_2.resize((40,40))
        self.upward_part_of_employee_record_edit_inside_image_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_employee_record_edit_inside_image_image_2_2)


        self.upward_part_of_employee_record_edit_inside_image_image = Label(self.upward_part_of_employee_record_edit_inside_image,image=self.upward_part_of_employee_record_edit_inside_image_image_3_1, bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_edit_inside_image_image.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.upward_part_of_employee_record_edit_inside_image_number = Label(self.upward_part_of_employee_record_edit_inside_image,text="Edit Employee Record",font=("Cascadia Mono",11),fg=self.box_on_click, bg=self.main_background_upward_color,anchor=CENTER)
        self.upward_part_of_employee_record_edit_inside_image_number.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        # self.upward_part_of_employee_record_edit_inside_image_theo = Label(self.upward_part_of_employee_record_edit_inside_image,font=("Cascadia Mono",7),text="Total Number of Employees",fg=self.box_on_click, bg=self.main_background_upward_color,anchor=E, bd=1, relief="solid")
        # self.upward_part_of_employee_record_edit_inside_image_theo.place(relx=0.3, rely=0.8, relwidth=0.7, relheight=0.2)

        self.upward_part_of_employee_record_edit_image.bind('<Button-1>',self.edit_to_of_employee)
        self.upward_part_of_employee_record_edit_inside_image.bind('<Button-1>', self.edit_to_of_employee)
        self.upward_part_of_employee_record_edit_inside_image_image.bind('<Button-1>', self.edit_to_of_employee)
        self.upward_part_of_employee_record_edit_inside_image_number.bind('<Button-1>', self.edit_to_of_employee)


        # self.OTP_varifaction()
        # self.create_new_account()
        self.employee_user()
        # self.employee_user_remove()


    def employee_user_remove(self):
            # ================== add_lower_part ======================
            self.lower_part_of_employee_record_employee_user_button_f = Frame(self.main_Employee_record,
                                                                     bg=self.main_background_color)
            self.lower_part_of_employee_record_employee_user_button_f.place(relx=0, rely=0.25, relwidth=1, relheight=0.06)

            self.lower_part_of_employee_record_employee_user_button = Button(self.lower_part_of_employee_record_employee_user_button_f,text="Remove selected Employee", bg=self.box_on_click,fg="#ffffff", relief=FLAT)
            self.lower_part_of_employee_record_employee_user_button.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.9)
            self.lower_part_of_employee_record_employee_user_button.bind('<Button-1>',self.remove_selected)

            self.lower_part_of_employee_record_employee_user = Frame(self.main_Employee_record,
                                                                     bg=self.main_background_upward_color)
            self.lower_part_of_employee_record_employee_user.place(relx=0, rely=0.31, relwidth=1, relheight=0.69)

            # treeview scrollbar
            self.tree_scrollbar = Scrollbar(self.lower_part_of_employee_record_employee_user)
            self.tree_scrollbar.pack(side=RIGHT, fill=Y)
            # Add some style
            self.tree_style = ttk.Style()

            # Pick a theme
            self.tree_style.theme_use("default")

            # Configure our treeview colors
            self.tree_style.configure("Treeview",
                                      background="#ffffff",
                                      foreground=self.box_on_click,
                                      rowheight=30,
                                      fieldbackground="#000000",
                                      font=("Cascadia Mono", 11)
                                      )
            self.tree_style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
            self.tree_style.configure("Treeview.Heading", foreground=self.main_background_upward_color,
                                      background=self.box_on_click, font=("Cascadia Mono", 11), rowheight=30)

            self.tree_style.configure("Treeview.Column", foreground=self.box_on_click, background="#ffffff",
                                      font=("Cascadia Mono", 11))

            self.tree_style.configure("Treeview.insert", foreground=self.box_on_click, background="#ffffff",
                                      font=("Cascadia Mono", 11))

            # Change selected color
            self.tree_style.map('Treeview', background=[('selected', 'blue')])

            # create tree view
            self.my_tree_view = ttk.Treeview(self.lower_part_of_employee_record_employee_user,
                                             yscrollcommand=self.tree_scrollbar.set)

            # Define our columns
            self.my_tree_view['column'] = ('Name', 'Position', 'Joining Date')

            self.im_checked_1 = Image.open("checkbox_1.png")
            self.im_checked_2 = self.im_checked_1.resize((30,30))
            self.im_checked = ImageTk.PhotoImage(self.im_checked_2)

            self.im_unchecked_1 = Image.open("unchecked_1.png")
            self.im_unchecked_2 = self.im_unchecked_1.resize((30,30))
            self.im_unchecked = ImageTk.PhotoImage(self.im_unchecked_2)

            self.my_tree_view.tag_configure('checked', image=self.im_checked)
            self.my_tree_view.tag_configure('unchecked', image=self.im_unchecked)


            # formate our columns
            self.my_tree_view.column('#0', anchor=W, width=0)
            self.my_tree_view.column('Name', anchor=W, width=120)
            self.my_tree_view.column('Position', anchor=W, width=80)
            self.my_tree_view.column('Joining Date', anchor=W, width=120)

            # create Heading
            self.my_tree_view.heading('#0', text="Select", anchor=W)
            self.my_tree_view.heading('#1', text="Name", anchor=CENTER)
            self.my_tree_view.heading('#2', text="Position", anchor=CENTER)
            self.my_tree_view.heading('#3', text="Joining Date", anchor=CENTER)

            # Add data
            # create striped row tags
            self.my_tree_view.tag_configure('oddrow', background="#E8EAFB")
            self.my_tree_view.tag_configure('evenrow', background=self.main_background_upward_color)

            try:
                self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
                self.cur = self.con.cursor()
                self.cur.execute("SELECT First_name FROM employee_data")
                self.tree_first_name = self.cur.fetchall()
                self.cur.execute("SELECT Last_name FROM employee_data")
                self.tree_last_name = self.cur.fetchall()
                self.cur.execute("SELECT Position FROM employee_data")
                self.tree_position = self.cur.fetchall()
                self.cur.execute("SELECT date_of_joining FROM employee_data")
                self.tree_date_of_joining = self.cur.fetchall()

                self.con.commit()
                self.con.close()
                self.cur.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due 1 to: {str(es)}", parent=self.root)
                print(str(es))

            self.count_strip = 0
            for i in range(self.cur.rowcount):
                if self.count_strip % 2 == 0:
                    self.my_tree_view.insert('', index='end', iid=i,
                                             values=(self.tree_first_name[i][0] + self.tree_last_name[i][0],
                                                     self.tree_position[i][0], self.tree_date_of_joining[i][0]),
                                             tags=('evenrow','unchecked'))
                else:
                    self.my_tree_view.insert('', index='end', iid=i,
                                             values=(self.tree_first_name[i][0] + self.tree_last_name[i][0],
                                                     self.tree_position[i][0], self.tree_date_of_joining[i][0]),
                                             tags=('oddrow','unchecked'))
                self.count_strip += 1

            # pack to the screen
            self.my_tree_view.place(relx=0, rely=0, relwidth=0.99, relheight=1)
            self.my_tree_view.bind('<Button-1>', self.togglecheck)

    def togglecheck(self,e):
        self.rowid = self.my_tree_view.identify_row(e.y)
        self.tag = self.my_tree_view.item(self.rowid,"tags")[0]
        self.tags = list(self.my_tree_view.item(self.rowid,"tags"))
        self.tags.remove(self.tag)
        self.my_tree_view.item(self.rowid, tags="tags")
        if self.tag == "checked":
            self.my_tree_view.item(self.rowid, tags="unchecked")
        else:
            self.my_tree_view.item(self.rowid, tags="checked")

    def remove_selected(self,e):
        # self.tree_first_name = self.cur.fetchall()
        try:

            if self.tag == "unchecked":
                self.selected_x = self.my_tree_view.selection()[0]
                print(self.tree_first_name[int(self.selected_x)][0])

                self.ask_to_remove = messagebox.askyesnocancel("Verify","Are you sure you want to remove employee data?")
                if self.ask_to_remove:
                    self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
                    self.cur = self.con.cursor()
                    self.cur.execute("SELECT username FROM employee_data WHERE First_name=%s",
                                     (f"{self.tree_first_name[int(self.selected_x)][0]}"))
                    self.us = self.cur.fetchone()
                    self.cur.execute("DELETE FROM employee_data WHERE username=%s ", (f"{self.us[0]}"))
                    self.selected_x = self.my_tree_view.selection()[0]
                    self.my_tree_view.delete(self.selected_x)

            else:
                messagebox.showinfo("Information","Nothing is selected!")


            self.con.commit()
            self.con.close()
            self.cur.close()




        except Exception as es:
            messagebox.showerror("Error", f"Error due 1 to: {str(es)}", parent=self.root)

        # self.my_tree_view.delete(self.selected_x)









    def employee_user(self):
# ================== add_lower_part ======================
        self.lower_part_of_employee_record_employee_user = Frame(self.main_Employee_record, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_employee_user.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

#treeview scrollbar
        self.tree_scrollbar = Scrollbar(self.lower_part_of_employee_record_employee_user)
        self.tree_scrollbar.pack(side=RIGHT,fill=Y)
#Add some style
        self.tree_style = ttk.Style()

#Pick a theme
        self.tree_style.theme_use("default")

#Configure our treeview colors
        self.tree_style.configure("Treeview",
                                  background="#ffffff",
                                  foreground=self.box_on_click,
                                  rowheight=30,
                                  fieldbackground="#d3d3d3",
                                  font=("Cascadia Mono",11)
                                  )
        self.tree_style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.tree_style.configure("Treeview.Heading",foreground=self.main_background_upward_color,background=self.box_on_click,font=("Cascadia Mono",11),rowheight=30)


        self.tree_style.configure("Treeview.Column", foreground=self.box_on_click, background="#ffffff",
                          font=("Cascadia Mono", 11))


        self.tree_style.configure("Treeview.insert", foreground=self.box_on_click, background="#ffffff",
                          font=("Cascadia Mono", 11))


#Change selected color
        self.tree_style.map('Treeview', background=[('selected','blue')])

#create tree view
        self.my_tree_view = ttk.Treeview(self.lower_part_of_employee_record_employee_user, yscrollcommand=self.tree_scrollbar.set, selectmode="none")

#Define our columns
        self.my_tree_view['column'] = ('Name', 'Position', 'Joining Date')

#formate our columns
        self.my_tree_view.column('#0', width=0, stretch=NO)
        self.my_tree_view.column('Name', anchor=W, width=120)
        self.my_tree_view.column('Position', anchor=W, width=80)
        self.my_tree_view.column('Joining Date', anchor=W, width=120)

#create Heading
        self.my_tree_view.heading('#0', text="Label", anchor=W)
        self.my_tree_view.heading('Name', text="Name", anchor=CENTER)
        self.my_tree_view.heading('Position', text="Position", anchor=CENTER)
        self.my_tree_view.heading('Joining Date', text="Joining Date", anchor=CENTER)

#Add data
    #create striped row tags
        self.my_tree_view.tag_configure('oddrow', background="#E8EAFB")
        self.my_tree_view.tag_configure('evenrow', background=self.main_background_upward_color)



        try:
            self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
            self.cur = self.con.cursor()
            self.cur.execute("SELECT First_name FROM employee_data")
            self.tree_first_name = self.cur.fetchall()
            self.cur.execute("SELECT Last_name FROM employee_data")
            self.tree_last_name = self.cur.fetchall()
            self.cur.execute("SELECT Position FROM employee_data")
            self.tree_position = self.cur.fetchall()
            self.cur.execute("SELECT date_of_joining FROM employee_data")
            self.tree_date_of_joining = self.cur.fetchall()


            self.con.commit()
            self.con.close()
            self.cur.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due 1 to: {str(es)}", parent=self.root)
            print(str(es))


        self.count_strip = 0
        for i in range(self.cur.rowcount):
            if self.count_strip%2 == 0:
                self.my_tree_view.insert(parent='', index='end', iid=i, text='parent',
                                 values=(self.tree_first_name[i][0]+self.tree_last_name[i][0],self.tree_position[i][0],self.tree_date_of_joining[i][0]), tags=('evenrow'))
            else:
                self.my_tree_view.insert(parent='', index='end', iid=i, text='parent',
                                 values=(self.tree_first_name[i][0]+self.tree_last_name[i][0],self.tree_position[i][0],self.tree_date_of_joining[i][0]), tags=('oddrow'))
            self.count_strip +=1

#pack to the screen
        self.my_tree_view.place(relx=0, rely=0, relwidth=0.99, relheight=1)







    def create_new_account(self):
        # ================== add_lower_part ======================
        self.lower_part_of_employee_record_add = Frame(self.main_Employee_record, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

        self.lower_part_of_employee_record_add_top_frame = Frame(self.lower_part_of_employee_record_add,
                                                                 bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.lower_part_of_employee_record_add_top_label = Label(self.lower_part_of_employee_record_add_top_frame,
                                                                 text="Create New Record", font=("Cascadia Mono", 13),
                                                                 bg=self.box_on_click,
                                                                 fg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_top_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame = Frame(self.lower_part_of_employee_record_add,
                                                                    bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        # ===== first name  and  last name
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1 = Frame(
            self.lower_part_of_employee_record_add_bottom_frame, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1.place(relx=0, rely=0.02, relwidth=1,
                                                                               relheight=0.1)
        # === first name
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_first_name_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname.place(relx=0, rely=0, relwidth=0.5,
                                                                                         relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname, text="First name",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_label.place(relx=0, rely=0,
                                                                                               relwidth=0.3,
                                                                                               relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname,
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.place(relx=0.31, rely=0.05,
                                                                                               relwidth=0.68,
                                                                                               relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.insert(0,"Enter First name")
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.bind('<Button-1>', self.on_click_first_name)

        # === last name
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_first_name_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname.place(relx=0.5, rely=0, relwidth=0.5,
                                                                                        relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname, text="Last name",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_label.place(relx=0, rely=0,
                                                                                              relwidth=0.3, relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname, font=("Cascadia Code Light", 10),
            bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.place(relx=0.31, rely=0.05,
                                                                                              relwidth=0.68,
                                                                                              relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.insert(0,"Enter Last name")
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.bind('<Button-1>', self.on_click_last_name)

        # ===== username  and  email
        self.lower_part_of_employee_record_add_bottom_frame_username_1 = Frame(
            self.lower_part_of_employee_record_add_bottom_frame, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_username_1.place(relx=0, rely=0.14, relwidth=1,
                                                                             relheight=0.1)
        # === username
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_username_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username.place(relx=0, rely=0, relwidth=0.5,
                                                                                      relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_username_1_username, text="Username",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_label.place(relx=0, rely=0,
                                                                                            relwidth=0.3, relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_username_1_username, font=("Cascadia Code Light", 10),
            bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.place(relx=0.31, rely=0.05,
                                                                                            relwidth=0.68,
                                                                                            relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.insert(0,"Enter Username")
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.bind('<Button-1>', self.on_click_username_name)


        # === email
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_username_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email.place(relx=0.5, rely=0, relwidth=0.5,
                                                                                   relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_username_1_email, text="Email Address",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_label.place(relx=0, rely=0, relwidth=0.3,
                                                                                         relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_username_1_email, font=("Cascadia Code Light", 10),
            bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.place(relx=0.31, rely=0.05,
                                                                                         relwidth=0.68, relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.insert(0, "Enter Email Address")
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.bind('<Button-1>', self.on_click_email_name)


        # ===== password  and  confirm password

        self.lower_part_of_employee_record_add_bottom_frame_password_1 = Frame(
            self.lower_part_of_employee_record_add_bottom_frame, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_password_1.place(relx=0, rely=0.26, relwidth=1,
                                                                             relheight=0.1)
        # === password
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_password_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password.place(relx=0, rely=0, relwidth=0.5,
                                                                                      relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_password_1_password, text="Password",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_label.place(relx=0, rely=0,
                                                                                            relwidth=0.3, relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_password_1_password, font=("Cascadia Code Light", 10),
            bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.place(relx=0.31, rely=0.05,
                                                                                            relwidth=0.68,
                                                                                            relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.insert(0, "Create Password")
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.bind('<Button-1>', self.on_click_password_name)


        # === confirm password
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_password_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword.place(relx=0.5, rely=0,
                                                                                             relwidth=0.5, relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword, text="Confirm Password",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_label.place(relx=0, rely=0,
                                                                                                   relwidth=0.3,
                                                                                                   relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword,
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.place(relx=0.31, rely=0.05,
                                                                                                   relwidth=0.68,
                                                                                                   relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.insert(0, "Repeat Password")
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.bind('<Button-1>',self.on_click_confirmpassword_name)

        # ===== Position  ========
        self.lower_part_of_employee_record_add_bottom_frame_position_1 = Frame(
            self.lower_part_of_employee_record_add_bottom_frame, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_position_1.place(relx=0, rely=0.38, relwidth=1,
                                                                             relheight=0.1)

        # === choose_position
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_position_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position.place(relx=0, rely=0, relwidth=1,
                                                                                             relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position, text="Position",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_label.place(relx=0, rely=0,
                                                                                                   relwidth=0.15,
                                                                                                   relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry = Entry(
            self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position,
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.place(relx=0.155,
                                                                                                   rely=0.05,
                                                                                                   relwidth=0.84,
                                                                                                   relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.insert(0, "What's the Position of your employee?")
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.bind('<Button-1>',self.on_click_position_name)


        # ===== DOB  and  joining_date

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1 = Frame(
            self.lower_part_of_employee_record_add_bottom_frame, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)
        # === DOB
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB, text="Date Of Birth",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_label.place(relx=0, rely=0, relwidth=0.3,
                                                                                  relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1 = ttk.Combobox(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB, font=("Cascadia Code Light", 12), justify=CENTER)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1['values'] = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21'
        , '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1.place(relx=0.31, rely=0.05,
                                                                                    relwidth=0.2266, relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1.set(value="DD")

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2 = ttk.Combobox(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB, font=("Cascadia Code Light", 10), justify=CENTER)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2['values'] = (
        ' January', ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September',
        ' October', ' November', ' December')
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2.place(relx=0.5366, rely=0.05,
                                                                                    relwidth=0.2266, relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2.set(value="MM")

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3 = ttk.Combobox(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB, font=("Cascadia Code Light", 10), justify=CENTER)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3['values'] = (
        '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961',
        '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973',
        '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985',
        '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
        '1998', '1999', '2000', '2001', '2002', '2003')
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3.place(relx=0.7632, rely=0.05,
                                                                                    relwidth=0.2266, relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3.set(value="YYYY")

        # === joining_date
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date = Frame(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date.place(relx=0.5, rely=0, relwidth=0.5,
                                                                                     relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_label = Label(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date, text="Joining Date",
            font=("Cascadia Code Light", 10), bg=self.main_background_upward_color, anchor=W)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_label.place(relx=0, rely=0, relwidth=0.3,
                                                                                           relheight=1)

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1 = ttk.Combobox(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date, font=("Cascadia Code Light", 10), justify=CENTER)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1['values'] = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21'
        , '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1.place(relx=0.31, rely=0.05,
                                                                                             relwidth=0.2266,
                                                                                             relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1.set(value="DD")

        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2 = ttk.Combobox(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date, font=("Cascadia Code Light", 10), justify=CENTER)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2['values'] = (
        ' January', ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September',
        ' October', ' November', ' December')
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2.place(relx=0.5366, rely=0.05,
                                                                                             relwidth=0.2266,
                                                                                             relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2.set(value="MM")


        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3 = ttk.Combobox(
            self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date, font=("Cascadia Code Light", 10), justify=CENTER)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3['values'] = (
        '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961',
        '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973',
        '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985',
        '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
        '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3.place(relx=0.7632, rely=0.05,
                                                                                             relwidth=0.2266,
                                                                                             relheight=0.9)
        self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3.set(value="YYYY")
        print(self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3.get())

        # ================== Continue
        self.lower_part_of_employee_record_add_bottom_frame_Continue_1 = Frame(
            self.lower_part_of_employee_record_add_bottom_frame, bg=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_Continue_1.place(relx=0, rely=0.85, relwidth=1,
                                                                             relheight=0.1)

        self.lower_part_of_employee_record_add_bottom_frame_Continue_1_button = Button(
            self.lower_part_of_employee_record_add_bottom_frame_Continue_1, text="Continue",
            font=("Cascadia Code Light", 12), borderwidth=0, bg=self.box_on_click, activebackground=self.box_on_click,
            fg=self.main_background_upward_color, activeforeground=self.main_background_upward_color)
        self.lower_part_of_employee_record_add_bottom_frame_Continue_1_button.place(relx=0.8, rely=0, relwidth=0.15,relheight=1)
        self.lower_part_of_employee_record_add_bottom_frame_Continue_1_button.bind('<Button-1>',self.continue_to_otp)

#=============================================================================================================================================================================================
    # ========================================= Placeholder =================================================================================================================================

    def on_click_first_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.delete(0,END)

    def on_click_last_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.delete(0,END)

    def on_click_username_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.delete(0,END)

    def on_click_email_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.delete(0,END)

    def on_click_password_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.delete(0,END)

    def on_click_confirmpassword_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.delete(0,END)

    def on_click_position_name(self,e):
        self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.delete(0,END)

    def continue_to_otp(self,e):
        if self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.get() == "Enter First name" or self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.get() == "Enter Last name" or self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.get() == "Enter Username" or self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.get() == "Enter Email Address" or self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get() == "Create Password" or self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.get() == "Repeat Password" or self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.get() == "What's the Position of your employee?" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1.get() == "DD" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2.get() == "MM" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3.get() == "YYYY" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1.get() == "DD" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2.get() == "MM" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3.get() == "" or self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3.get() == "YYYY":
            messagebox.showerror("Validation","Please Fill All detail")

        elif self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get() != "" and self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get() != "Create Password" and self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.get() != "" and self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.get() != "Repeat Password":
            if self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get() != self.lower_part_of_employee_record_add_bottom_frame_password_1_confirmpassword_Entry.get():
                messagebox.showerror("Validation", "Password and ConfirmPassword doesn't match!")
            else:
                if len(self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get()) < 7:
                    messagebox.showerror("Validation", "Password is to short")


        self.regex_employee = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.email_employee = self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.get()
        self.test_domain_employee = self.email_employee.split('@')[1]
        self.reg_email_employee = ""
        print(self.test_domain_employee)
        if re.search(self.regex_employee, self.email_employee):
            if self.test_domain_employee == "gmail.com":
                self.reg_email_employee = self.email_employee
                try:
                    self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
                    self.cur = self.con.cursor()
                    self.cur.execute("SELECT * FROM employee_data where email=%s", (self.email_employee))
                    self.row = self.cur.fetchone()
                    self.cur.execute("SELECT * FROM employee_data where username=%s", (self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.get()))
                    self.row_1 = self.cur.fetchone()

                    if self.row == None:
                        if self.row_1 == None:
                            self.OTP_varifaction()
                            self.password = "mhlffknvjujzcwtk"
                            self.server = smtplib.SMTP('smtp.gmail.com', 587)
                            self.server.starttls()
                            self.server.login('prity123gain@gmail.com', self.password)
                            self.otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
                            self.msg = 'Hello , your otp is ' + str(self.otp)
                            self.server.sendmail('prity123gain@gmail.com', self.reg_email_employee, self.msg)
                            self.server.quit()
                        else:
                            messagebox.showinfo("Validation", "Username all ready exist.")
                    else:
                        messagebox.showinfo("Validation","Your all ready exist.")

                    self.con.commit()
                    self.con.close()
                    self.cur.close()


                except Exception as es:
                     messagebox.showerror("Error",f"Error due 1 to: {str(es)}",parent= self.root)
                     print(str(es))


            else:
                messagebox.showerror("Validation", "Email Id is not valid!")
        else:
            messagebox.showerror("Validation", "Email Id is not valid!")





























    # =============================================================================================================================================================================================

    def OTP_varifaction(self):
        # ================== add_lower_part ======================
        self.lower_part_of_OTP_varifaction = Frame(self.main_Employee_record,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

        self.lower_part_of_OTP_varifaction_frame = Frame(self.lower_part_of_OTP_varifaction,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.lower_part_of_OTP_varifaction_label = Label(self.lower_part_of_OTP_varifaction_frame,text="Email varification", font=("Cascadia Mono", 13),bg=self.box_on_click,fg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_label.place(relx=0, rely=0, relwidth=1, relheight=1)



#==============================================================================================================================
        self.lower_part_of_OTP_varifaction_frame_in = Frame(self.lower_part_of_OTP_varifaction,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_in.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.9)


        self.lower_part_of_OTP_varifaction_frame_title = Frame(self.lower_part_of_OTP_varifaction_frame_in,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_title.place(relx=0, rely=0.01, relwidth=1, relheight=0.1)

        self.lower_part_of_OTP_varifaction_title_1 = Label(self.lower_part_of_OTP_varifaction_frame_title,text="OTP", font=("Cascadia Mono", 13),fg=self.box_on_click,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_title_1.place(relx=0, rely=0, relwidth=1, relheight=1)

#=======================================================================
        self.lower_part_of_OTP_varifaction_frame_theo = Frame(self.lower_part_of_OTP_varifaction_frame_in,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_theo.place(relx=0, rely=0.12, relwidth=1, relheight=0.2)

        self.lower_part_of_OTP_varifaction_theo_1 = Label(self.lower_part_of_OTP_varifaction_frame_theo,text="A one-time password (OTP), also known as one-time PIN or dynamic password, is a password that is\n valid for only one login session or transaction, on a computer system or other digital device\n On the downside, OTPs are difficult for human beings to memorize.\n Therefore, they require additional technology to work.", font=("Cascadia Mono", 11),fg=self.box_text_color_big,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_theo_1.place(relx=0, rely=0, relwidth=1, relheight=1)

# =======================================================================
        self.lower_part_of_OTP_varifaction_frame_take = Frame(self.lower_part_of_OTP_varifaction_frame_in,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_take.place(relx=0, rely=0.36, relwidth=1, relheight=0.12)

        self.lower_part_of_OTP_varifaction_frame_take_label = Label(self.lower_part_of_OTP_varifaction_frame_take,text="Verify Code :",bg=self.main_background_upward_color,fg=self.box_text_color_big, font=("Cascadia Mono", 11),anchor=E)
        self.lower_part_of_OTP_varifaction_frame_take_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.lower_part_of_OTP_varifaction_frame_take_entry_frame = Label(self.lower_part_of_OTP_varifaction_frame_take,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_take_entry_frame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        self.lower_part_of_OTP_varifaction_frame_take_entry = Entry(self.lower_part_of_OTP_varifaction_frame_take_entry_frame,bg=self.main_background_upward_color,fg=self.box_text_color_big, font=("Cascadia Mono", 11))
        self.lower_part_of_OTP_varifaction_frame_take_entry.place(relx=0.025, rely=0.1, relwidth=0.54, relheight=0.8)

# =======================================================================
        self.lower_part_of_OTP_varifaction_frame_buttton_fr = Frame(self.lower_part_of_OTP_varifaction_frame_in,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_buttton_fr.place(relx=0, rely=0.5, relwidth=1, relheight=0.12)

        self.lower_part_of_OTP_varifaction_frame_buttton = Button(self.lower_part_of_OTP_varifaction_frame_buttton_fr,fg=self.main_background_upward_color,text="Verify",bg=self.box_on_click, font=("Cascadia Mono", 11))
        self.lower_part_of_OTP_varifaction_frame_buttton.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.8)

# =======================================================================
        self.lower_part_of_OTP_varifaction_frame_resend_fr = Frame(self.lower_part_of_OTP_varifaction_frame_in,bg=self.main_background_upward_color)
        self.lower_part_of_OTP_varifaction_frame_resend_fr.place(relx=0, rely=0.63, relwidth=1, relheight=0.04)

        self.lower_part_of_OTP_varifaction_frame_resend_Label = Label(self.lower_part_of_OTP_varifaction_frame_resend_fr,text="Resend OTP",bg=self.main_background_upward_color,fg=self.box_on_click,font=("Cascadia Mono", 11))
        self.lower_part_of_OTP_varifaction_frame_resend_Label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lower_part_of_OTP_varifaction_frame_buttton.bind('<Button-1>',self.varifaction_otp)

    def varifaction_otp(self,e):
        self.of_DOB = (self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_3.get()+"-"+self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_2.get()+"-"+self.lower_part_of_employee_record_add_bottom_frame_DOB_1_DOB_combo_1.get())
        self.of_joining_date = (str(self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_3.get()) + "-" + str(self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_2.get()) + "-" + str(self.lower_part_of_employee_record_add_bottom_frame_DOB_1_joining_date_combo_1.get()))
        self.gett = self.lower_part_of_OTP_varifaction_frame_take_entry.get()
        if self.gett == self.otp:
            try:
                self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
                self.cur = self.con.cursor()
                self.cur.execute("INSERT INTO employee_data(First_name,Last_name,username,email,password,Position,DOB,date_of_joining) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                 (
                                 self.lower_part_of_employee_record_add_bottom_frame_first_name_1_firstname_Entry.get(),
                                 self.lower_part_of_employee_record_add_bottom_frame_first_name_1_lastname_Entry.get(),
                                 self.lower_part_of_employee_record_add_bottom_frame_username_1_username_Entry.get(),
                                 self.lower_part_of_employee_record_add_bottom_frame_username_1_email_Entry.get(),
                                 self.lower_part_of_employee_record_add_bottom_frame_password_1_password_Entry.get(),
                                 self.lower_part_of_employee_record_add_bottom_frame_position_1_choose_position_Entry.get(),
                                 self.of_DOB,
                                 self.of_joining_date
                                 )
                                 )
                self.con.commit()
                self.con.close()
                self.employee_user()
                self.number_of_employee(self)
                messagebox.showinfo("Validation","Registration Successfull")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

        else:
            messagebox.showinfo("Validation","Registration Failed")


    def number_of_employee(self,e):
        self.employee_user()
        self.upward_part_of_employee_record_total_image['image'] = (self.upward_part_of_employee_record_total_image_3_2)
        self.upward_part_of_employee_record_total_inside_image_image['image'] = (self.upward_part_of_employee_record_total_inside_image_image_3_2)
        self.upward_part_of_employee_record_total_inside_image_image.configure(bg=self.box_on_click)
        self.upward_part_of_employee_record_total_inside_image_number.configure(bg=self.box_on_click,fg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_theo.configure(bg=self.box_on_click,fg=self.main_background_upward_color)

        self.upward_part_of_employee_record_add_image['image'] = (self.upward_part_of_employee_record_add_image_3_1)
        self.upward_part_of_employee_record_add_inside_image_image['image'] = (self.upward_part_of_employee_record_add_inside_image_image_3_1)
        self.upward_part_of_employee_record_add_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_add_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_remove_image['image'] = (self.upward_part_of_employee_record_remove_image_3_1)
        self.upward_part_of_employee_record_remove_inside_image_image['image'] = (self.upward_part_of_employee_record_remove_inside_image_image_3_1)
        self.upward_part_of_employee_record_remove_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_remove_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_edit_image['image'] = (self.upward_part_of_employee_record_edit_image_3_1)
        self.upward_part_of_employee_record_edit_inside_image_image['image'] = (self.upward_part_of_employee_record_edit_inside_image_image_3_1)
        self.upward_part_of_employee_record_edit_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_edit_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)



    def add_to_of_employee(self,e):
        self.create_new_account()
        self.upward_part_of_employee_record_add_image['image'] = (self.upward_part_of_employee_record_add_image_3_2)
        self.upward_part_of_employee_record_add_inside_image_image['image'] = (self.upward_part_of_employee_record_add_inside_image_image_3_2)
        self.upward_part_of_employee_record_add_inside_image_image.configure(bg=self.box_on_click)
        self.upward_part_of_employee_record_add_inside_image_number.configure(bg=self.box_on_click,fg=self.main_background_upward_color)

        self.upward_part_of_employee_record_total_image['image'] = (self.upward_part_of_employee_record_total_image_3_1)
        self.upward_part_of_employee_record_total_inside_image_image['image'] = (self.upward_part_of_employee_record_total_inside_image_image_3_1)
        self.upward_part_of_employee_record_total_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_theo.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_remove_image['image'] = (self.upward_part_of_employee_record_remove_image_3_1)
        self.upward_part_of_employee_record_remove_inside_image_image['image'] = (self.upward_part_of_employee_record_remove_inside_image_image_3_1)
        self.upward_part_of_employee_record_remove_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_remove_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_edit_image['image'] = (self.upward_part_of_employee_record_edit_image_3_1)
        self.upward_part_of_employee_record_edit_inside_image_image['image'] = (self.upward_part_of_employee_record_edit_inside_image_image_3_1)
        self.upward_part_of_employee_record_edit_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_edit_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)



    def remove_to_of_employee(self,e):
        self.employee_user_remove()
        self.upward_part_of_employee_record_remove_image['image'] = (self.upward_part_of_employee_record_remove_image_3_2)
        self.upward_part_of_employee_record_remove_inside_image_image['image'] = (self.upward_part_of_employee_record_remove_inside_image_image_3_2)
        self.upward_part_of_employee_record_remove_inside_image_image.configure(bg=self.box_on_click)
        self.upward_part_of_employee_record_remove_inside_image_number.configure(bg=self.box_on_click,fg=self.main_background_upward_color)

        self.upward_part_of_employee_record_total_image['image'] = (self.upward_part_of_employee_record_total_image_3_1)
        self.upward_part_of_employee_record_total_inside_image_image['image'] = (self.upward_part_of_employee_record_total_inside_image_image_3_1)
        self.upward_part_of_employee_record_total_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_theo.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_add_image['image'] = (self.upward_part_of_employee_record_add_image_3_1)
        self.upward_part_of_employee_record_add_inside_image_image['image'] = (self.upward_part_of_employee_record_add_inside_image_image_3_1)
        self.upward_part_of_employee_record_add_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_add_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_edit_image['image'] = (self.upward_part_of_employee_record_edit_image_3_1)
        self.upward_part_of_employee_record_edit_inside_image_image['image'] = (self.upward_part_of_employee_record_edit_inside_image_image_3_1)
        self.upward_part_of_employee_record_edit_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_edit_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)


    def edit_to_of_employee(self,e):
        self.upward_part_of_employee_record_edit_image['image'] = (self.upward_part_of_employee_record_edit_image_3_2)
        self.upward_part_of_employee_record_edit_inside_image_image['image'] = (self.upward_part_of_employee_record_edit_inside_image_image_3_2)
        self.upward_part_of_employee_record_edit_inside_image_image.configure(bg=self.box_on_click)
        self.upward_part_of_employee_record_edit_inside_image_number.configure(bg=self.box_on_click,fg=self.main_background_upward_color)

        self.upward_part_of_employee_record_total_image['image'] = (self.upward_part_of_employee_record_total_image_3_1)
        self.upward_part_of_employee_record_total_inside_image_image['image'] = (self.upward_part_of_employee_record_total_inside_image_image_3_1)
        self.upward_part_of_employee_record_total_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_total_inside_image_theo.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_add_image['image'] = (self.upward_part_of_employee_record_add_image_3_1)
        self.upward_part_of_employee_record_add_inside_image_image['image'] = (self.upward_part_of_employee_record_add_inside_image_image_3_1)
        self.upward_part_of_employee_record_add_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_add_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)

        self.upward_part_of_employee_record_remove_image['image'] = (self.upward_part_of_employee_record_remove_image_3_1)
        self.upward_part_of_employee_record_remove_inside_image_image['image'] = (self.upward_part_of_employee_record_remove_inside_image_image_3_1)
        self.upward_part_of_employee_record_remove_inside_image_image.configure(bg=self.main_background_upward_color)
        self.upward_part_of_employee_record_remove_inside_image_number.configure(fg=self.box_on_click,bg=self.main_background_upward_color)









#=================================================  main_item_main ===============================================================================================================
    def main_item_main(self):
        # ======================================  main_item_record ========================================================

        self.main_item_record = Frame(self.main_top_full, bg=self.main_background_color)
        self.main_item_record.place(relx=0, rely=0.09, relwidth=1, relheight=0.9)

        # ==================  Upward_part_of_item_record ===================

        self.upward_part_of_item_record = Frame(self.main_item_record, bg=self.main_background_color)
        self.upward_part_of_item_record.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        self.upward_part_of_item_record_background_image_f = Frame(self.upward_part_of_item_record, bg=self.main_background_color)
        self.upward_part_of_item_record_background_image_f.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.upward_part_of_item_record_background_image_1 = Image.open("large33_on.png")
        self.upward_part_of_item_record_background_image_2 = self.upward_part_of_item_record_background_image_1.resize((1336,150))
        self.upward_part_of_item_record_background_image_3 = ImageTk.PhotoImage(self.upward_part_of_item_record_background_image_2)

        self.upward_part_of_item_record_background_image = Label(self.upward_part_of_item_record_background_image_f,image=self.upward_part_of_item_record_background_image_3, bg=self.main_background_color)
        self.upward_part_of_item_record_background_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.upward_part_of_item_record_background_label_f_1 = Frame(self.upward_part_of_item_record_background_image, bg=self.box_on_click)
        self.upward_part_of_item_record_background_label_f_1.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.4)

        self.upward_part_of_item_record_background_label_1 = Label(self.upward_part_of_item_record_background_label_f_1, text="Item Overview" ,fg=self.main_background_upward_color,font=("Forte", 21), bg=self.box_on_click)
        self.upward_part_of_item_record_background_label_1.place(relx=0, rely=0, relwidth=0.4, relheight=1)

        self.upward_part_of_item_record_background_label_2 = Label(self.upward_part_of_item_record_background_label_f_1, text="Do Anything With Items" ,fg=self.main_background_upward_color,font=("MV Boli", 10), bg=self.box_on_click,anchor=SW)
        self.upward_part_of_item_record_background_label_2.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.9)

        self.upward_part_of_item_record_button_image_f_1 = Frame(self.upward_part_of_item_record_background_image, bg=self.box_on_click)
        self.upward_part_of_item_record_button_image_f_1.place(relx=0.01, rely=0.42, relwidth=0.8, relheight=0.4)
        #=========================  mmmmmmmmmmmmmmm===========================================================================================================
        self.upward_part_of_item_record_button_image_f = Frame(self.upward_part_of_item_record_background_image, bg=self.box_on_click)
        self.upward_part_of_item_record_button_image_f.place(relx=0.01, rely=0.42, relwidth=0.8, relheight=0.5)
        # =========================  1111111111111111111111
        self.upward_part_of_item_record_button_image_f_1 = Frame(self.upward_part_of_item_record_button_image_f,
                                                                 bg=self.box_on_click)
        self.upward_part_of_item_record_button_image_f_1.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        self.upward_part_of_item_record_button_image_1_1 = Image.open("33.png")
        self.upward_part_of_item_record_button_image_2_1 = self.upward_part_of_item_record_button_image_1_1.resize((160,50))
        self.upward_part_of_item_record_button_image_3_1 = ImageTk.PhotoImage(self.upward_part_of_item_record_button_image_2_1)

        self.upward_part_of_item_record_button_image_1 = Label(self.upward_part_of_item_record_button_image_f_1,image=self.upward_part_of_item_record_button_image_3_1, bg=self.box_on_click,cursor="hand2")
        self.upward_part_of_item_record_button_image_1.place(relx=0.19, rely=0, relwidth=0.62, relheight=1)

        self.upward_part_of_item_record_button_label_1 = Label(self.upward_part_of_item_record_button_image_1,text="View Items",font=("Kristen ITC",11), bg=self.main_background_upward_color,fg=self.box_on_click)
        self.upward_part_of_item_record_button_label_1.place(relx=0.05, rely=0.14, relwidth=0.9, relheight=0.72)
        self.upward_part_of_item_record_button_label_1.bind('<Button-1>',self.lower_part_of_item_record_fun_view)


        # =========================  222222222222222222
        self.upward_part_of_item_record_button_image_f_2 = Frame(self.upward_part_of_item_record_button_image_f,
                                                                 bg=self.box_on_click)
        self.upward_part_of_item_record_button_image_f_2.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)


        self.upward_part_of_item_record_button_image_1_2 = Image.open("33.png")
        self.upward_part_of_item_record_button_image_2_2 = self.upward_part_of_item_record_button_image_1_2.resize((160,50))
        self.upward_part_of_item_record_button_image_3_2 = ImageTk.PhotoImage(self.upward_part_of_item_record_button_image_2_2)


        self.upward_part_of_item_record_button_image_2 = Label(self.upward_part_of_item_record_button_image_f_2,image=self.upward_part_of_item_record_button_image_3_2, bg=self.box_on_click,cursor="hand2")
        self.upward_part_of_item_record_button_image_2.place(relx=0.19, rely=0, relwidth=0.62, relheight=1)

        self.upward_part_of_item_record_button_label_2 = Label(self.upward_part_of_item_record_button_image_2,text="Add Items",font=("Kristen ITC",11), bg=self.main_background_upward_color,fg=self.box_on_click)
        self.upward_part_of_item_record_button_label_2.place(relx=0.05, rely=0.14, relwidth=0.9, relheight=0.72)
        self.upward_part_of_item_record_button_label_2.bind('<Button-1>',self.lower_part_of_item_record_fun)


        # =========================  33333333333333333333
        self.upward_part_of_item_record_button_image_f_3 = Frame(self.upward_part_of_item_record_button_image_f,
                                                                 bg=self.box_on_click)
        self.upward_part_of_item_record_button_image_f_3.place(relx=0.5, rely=0, relwidth=0.25, relheight=1)


        self.upward_part_of_item_record_button_image_1_3 = Image.open("33.png")
        self.upward_part_of_item_record_button_image_2_3 = self.upward_part_of_item_record_button_image_1_3.resize((160,50))
        self.upward_part_of_item_record_button_image_3_3 = ImageTk.PhotoImage(self.upward_part_of_item_record_button_image_2_3)


        self.upward_part_of_item_record_button_image_3 = Label(self.upward_part_of_item_record_button_image_f_3,image=self.upward_part_of_item_record_button_image_3_3, bg=self.box_on_click,cursor="hand2")
        self.upward_part_of_item_record_button_image_3.place(relx=0.19, rely=0, relwidth=0.62, relheight=1)

        self.upward_part_of_item_record_button_label_3 = Label(self.upward_part_of_item_record_button_image_3,text="Remove Items",font=("Kristen ITC",11), bg=self.main_background_upward_color,fg=self.box_on_click)
        self.upward_part_of_item_record_button_label_3.place(relx=0.05, rely=0.14, relwidth=0.9, relheight=0.72)





        # =========================  444444444444444444444
        self.upward_part_of_item_record_button_image_f_4 = Frame(self.upward_part_of_item_record_button_image_f,
                                                                 bg=self.box_on_click)
        self.upward_part_of_item_record_button_image_f_4.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)


        self.upward_part_of_item_record_button_image_1_4 = Image.open("33.png")
        self.upward_part_of_item_record_button_image_2_4 = self.upward_part_of_item_record_button_image_1_4.resize((160,50))
        self.upward_part_of_item_record_button_image_3_4 = ImageTk.PhotoImage(self.upward_part_of_item_record_button_image_2_4)


        self.upward_part_of_item_record_button_image_4 = Label(self.upward_part_of_item_record_button_image_f_4,image=self.upward_part_of_item_record_button_image_3_4, bg=self.box_on_click,cursor="hand2")
        self.upward_part_of_item_record_button_image_4.place(relx=0.19, rely=0, relwidth=0.62, relheight=1)

        self.upward_part_of_item_record_button_label_4 = Label(self.upward_part_of_item_record_button_image_4,text="Edit Items",font=("Kristen ITC",11), bg=self.main_background_upward_color,fg=self.box_on_click)
        self.upward_part_of_item_record_button_label_4.place(relx=0.05, rely=0.14, relwidth=0.9, relheight=0.72)
        self.lower_part_of_item_record_fun_view(self)



    def lower_part_of_item_record_fun_view(self,e):
        # ==================  lower_part_of_item_record =====================================================================================================
        self.lower_part_of_item_record_view = Frame(self.main_item_record, bg=self.main_background_color)
        self.lower_part_of_item_record_view.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)


        self.lower_part_of_item_record_background_image_f_view = Frame(self.lower_part_of_item_record_view, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.lower_part_of_item_record_background_image_f_view_s = Frame(self.lower_part_of_item_record_view, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_s.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

        # =======================================================
        # treeview scrollbar

        self.tree_scrollbar = Scrollbar(self.lower_part_of_item_record_background_image_f_view_s)
        self.tree_scrollbar.pack(side=RIGHT, fill=Y)

        self.tree_style = ttk.Style()

        # Pick a theme
        self.tree_style.theme_use("default")


        # Configure our treeview colors
        self.tree_style.configure("Treeview",
                                  background="#ffffff",
                                  foreground=self.box_on_click,
                                  rowheight=50,
                                  fieldbackground="#000000",
                                  font=("Cascadia Mono", 11)
                                  )
        self.tree_style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.tree_style.configure("Treeview.Heading", foreground=self.main_background_upward_color,
                                  background=self.box_on_click, font=("Cascadia Mono", 11), rowheight=50)

        self.tree_style.configure("Treeview.Column", foreground=self.box_on_click, background="#ffffff",
                                  font=("Cascadia Mono", 11))

        self.tree_style.configure("Treeview.insert", foreground=self.box_on_click, background="#ffffff",
                                  font=("Cascadia Mono", 11))

        # Change selected color
        self.tree_style.map('Treeview', background=[('selected', 'blue')])

        self.item_tree_view = ttk.Treeview(self.lower_part_of_item_record_background_image_f_view,yscrollcommand=self.tree_scrollbar.set,selectmode="none")


        #Define our columns
        self.item_tree_view['columns'] = ("Number_of_Item","item_name","item_price")

        #Formate our columns
        self.item_tree_view.column("#0",width=0, stretch=NO)
        self.item_tree_view.column("Number_of_Item", anchor=W, width=20)
        self.item_tree_view.column("item_name", anchor=W, width=120)
        self.item_tree_view.column("item_price", anchor=W, width=120)

        #create headings
        self.item_tree_view.heading("#0", text="", anchor=W)
        self.item_tree_view.heading("Number_of_Item", text="Number of Item", anchor=W)
        self.item_tree_view.heading("item_name", text="Item Name", anchor=CENTER)
        self.item_tree_view.heading("item_price", text="Item Price", anchor=W)

        self.item_tree_view.tag_configure('oddrow', background="#E8EAFB")
        self.item_tree_view.tag_configure('evenrow', background=self.main_background_upward_color)

        try:
            self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM item_data")
            self.item_data = self.cur.fetchall()
            self.cur.execute("SELECT item_name FROM item_data")
            self.tree_item_name = self.cur.fetchall()
            self.cur.execute("SELECT item_price FROM item_data")
            self.tree_item_price = self.cur.fetchall()
            self.cur.execute("SELECT item_id FROM item_data")
            self.tree_id = self.cur.fetchall()


            self.count = 0
            for record in  range(len(self.tree_item_name)):

                # add data
                if self.count%2 == 0:
                    self.item_tree_view.insert(parent='', index='end', iid=self.count, values=(self.tree_id[record][0], self.tree_item_name[record][0], self.tree_item_price[record]),tags='evenrow')
                    self.item_tree_view.place(relx=0, rely=0, relwidth=1, relheight=1)
                    self.tree_scrollbar.config(command=self.item_tree_view.yview)
                else:
                    self.item_tree_view.insert(parent='', index='end', iid=self.count, values=(
                    self.tree_id[record][0], self.tree_item_name[record][0], self.tree_item_price[record]), tags='oddrow')
                    self.item_tree_view.place(relx=0, rely=0, relwidth=1, relheight=1)
                    self.tree_scrollbar.config(command=self.item_tree_view.yview)

                self.count +=1

            #pack tree view

            self.con.commit()
            self.con.close()
            self.cur.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due 1 to: {str(es)}", parent=self.root)
            print(str(es))
















    def lower_part_of_item_record_fun(self,e):
        # ==================  lower_part_of_item_record =====================================================================================================

        self.lower_part_of_item_record = Frame(self.main_item_record, bg=self.main_background_color)
        self.lower_part_of_item_record.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

        self.lower_part_of_item_record_background_image_f = Frame(self.lower_part_of_item_record, bg=self.main_background_color)
        self.lower_part_of_item_record_background_image_f.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lower_part_of_item_record_background_image_1 = Image.open("large33_w.png")
        self.lower_part_of_item_record_background_image_2 = self.lower_part_of_item_record_background_image_1.resize((1280,530))
        self.lower_part_of_item_record_background_image_3 = ImageTk.PhotoImage(self.lower_part_of_item_record_background_image_2)

        self.lower_part_of_item_record_background_image = Label(self.lower_part_of_item_record_background_image_f,image=self.lower_part_of_item_record_background_image_3, bg=self.main_background_color)
        self.lower_part_of_item_record_background_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lower_part_of_item_record_background_image_f_view_item_1 = Frame(self.lower_part_of_item_record_background_image, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.lower_part_of_item_record_background_image_f_view_item_2 = Frame(self.lower_part_of_item_record_background_image_f_view_item_1, bg=self.box_on_click)
        self.lower_part_of_item_record_background_image_f_view_item_2.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.3)

        self.lower_part_of_item_record_background_image_f_view_item_3 = Frame(self.lower_part_of_item_record_background_image_f_view_item_2, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_3.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)


        self.lower_part_of_item_record_background_image_f_view_item_4 = Label(self.lower_part_of_item_record_background_image_f_view_item_3,fg=self.box_on_click, text="ADD Image", bg=self.main_background_upward_color,cursor="hand2")
        self.lower_part_of_item_record_background_image_f_view_item_4.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)
        self.lower_part_of_item_record_background_image_f_view_item_4.bind('<Button-1>',self.open_image)

        self.lower_part_of_item_record_background_image_f_view_item_5 = Frame(self.lower_part_of_item_record_background_image_f_view_item_1, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_5.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.1)

        self.lower_part_of_item_record_background_image_f_view_item_5_label = Label(self.lower_part_of_item_record_background_image_f_view_item_5,text="Item Name",font=("Cascadia Code SemiBold",10), bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_5_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        self.lower_part_of_item_record_background_image_f_view_item_5_entry = Entry(self.lower_part_of_item_record_background_image_f_view_item_5,font=("Cascadia Code SemiBold",10), bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_5_entry.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.9)


        self.lower_part_of_item_record_background_image_f_view_item_6 = Frame(self.lower_part_of_item_record_background_image_f_view_item_1, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_6.place(relx=0.05, rely=0.55, relwidth=0.5, relheight=0.1)

        self.lower_part_of_item_record_background_image_f_view_item_6_label = Label(self.lower_part_of_item_record_background_image_f_view_item_6,text="Item Price", bg=self.main_background_upward_color,font=("Cascadia Code SemiBold",10))
        self.lower_part_of_item_record_background_image_f_view_item_6_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        self.lower_part_of_item_record_background_image_f_view_item_6_entry = Entry(self.lower_part_of_item_record_background_image_f_view_item_6,font=("Cascadia Code SemiBold",10), bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_6_entry.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.9)


        self.lower_part_of_item_record_background_image_f_view_item_7 = Frame(self.lower_part_of_item_record_background_image_f_view_item_1, bg=self.main_background_upward_color)
        self.lower_part_of_item_record_background_image_f_view_item_7.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.1)

        self.lower_part_of_item_record_background_image_f_view_item_7_button = Button(self.lower_part_of_item_record_background_image_f_view_item_7,text="Save Item",font=("Cascadia Code SemiBold",10),cursor="hand2", fg=self.main_background_upward_color,bg=self.box_on_click)
        self.lower_part_of_item_record_background_image_f_view_item_7_button.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        self.lower_part_of_item_record_background_image_f_view_item_7_button.bind('<Button-1>',self.save_item)





    def open_image(self,e):
        self.root.filename = filedialog.askopenfilename(initialdir="C:/Users/ASUS/PycharmProjects/untitled2/Resturant management system",title="select file",filetype=(("png files",".png"),("All file","*.*")))

        self.im_1 = Image.open(self.root.filename)
        self.im_2 = self.im_1.resize((70,70))
        self.im_3 = ImageTk.PhotoImage(self.im_2)

        self.lower_part_of_item_record_background_image_f_view_item_4_image = Label(self.lower_part_of_item_record_background_image_f_view_item_3,image=self.im_3,fg=self.box_on_click, text="ADD Image", bg=self.main_background_upward_color,cursor="hand2")
        self.lower_part_of_item_record_background_image_f_view_item_4_image.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)

    def save_item(self,e):
        try:
            self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
            self.cur = self.con.cursor()
            self.cur.execute("INSERT INTO item_data(item_name,item_price,item_image) values(%s,%s,%s)",(self.lower_part_of_item_record_background_image_f_view_item_5_entry.get(),self.lower_part_of_item_record_background_image_f_view_item_6_entry.get(),f"{self.root.filename}"))
            messagebox.showinfo("Information", "Item Saved Successfully")

            self.con.commit()
            self.cur.close()
            self.con.close()
            self.lower_part_of_item_record_fun_view(self)
        except Exception as es:
            messagebox.showerror("Error", f"photo Error due to: {str(es)}", parent=self.root)
            print(str(es))


    #==================================================================================================================================================================================
# ==================================================================================================================================================================================

    def logouttt(self,e):
        ask_him = messagebox.askyesno("Log out","Are you sure you want to Log out ?")
        if ask_him:
            self.root.destroy()
            os.system("python main_rms_login.py")
        else:
            print("no")

    def main_left_navigation_bar_1_fun(self,e):
        self.p=0

        if self.top == 0:
            m = 0.13
            n=0

            for x in range(200):

                m=m-0.00065
                n = n - 0.00065
                self.main_left_back.place(relx=-0.13)
                self.main_left_back.update()
                self.main_top_full.place(relx=0, relwidth=1)
                self.main_top_full.update()
                self.upward_part_of_employee_record_total_inside_image.place(relx=0.11,relwidth=0.78)
                self.upward_part_of_employee_record_add_inside_image.place(relx=0.11,relwidth=0.78)
                self.upward_part_of_employee_record_remove_inside_image.place(relx=0.11,relwidth=0.78)
                self.upward_part_of_employee_record_edit_inside_image.place(relx=0.11,relwidth=0.78)
            if self.main_left_navigation_bar_1.bind('<Button-1>', self.main_left_navigation_bar_1_fun) or self.main_left_navigation_bar_image_frame.bind('<Button-1>', self.main_left_navigation_bar_1_fun) :
               self.top=1
        elif self.top == 1:
            self.main_left_back.place(relx=0)
            self.main_top_full.place(relx=0.13, relwidth=0.87)
            self.upward_part_of_employee_record_total_inside_image.place(relx=0.05, relwidth=0.9)
            self.upward_part_of_employee_record_add_inside_image.place(relx=0.05, relwidth=0.9)
            self.upward_part_of_employee_record_remove_inside_image.place(relx=0.05, relwidth=0.9)
            self.upward_part_of_employee_record_edit_inside_image.place(relx=0.05, relwidth=0.9)
            if self.main_left_navigation_bar_1.bind('<Button-1>', self.main_left_navigation_bar_1_fun) or self.main_left_navigation_bar_image_frame.bind('<Button-1>', self.main_left_navigation_bar_1_fun) :
               self.top=0




    def main_left_navigation_bar_1_fun_hover_on(self,e):
        self.main_left_navigation_bar_image_frame['image'] = (self.main_left_navigation_bar_image_3)


    def main_left_navigation_bar_1_fun_hover_off(self,e):
        self.main_left_navigation_bar_image_frame['image'] = (self.main_left_navigation_bar_image_w_3)









    def main_left_dashboard_1_fun(self,e):
        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_3_2)
        self.main_left_dashboard_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_dashboard_label.configure(fg=self.after_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)





    def main_left_employee_1_fun(self, e):
        self.main_Employee_record_main()
        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_3_2)
        self.main_left_employee_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_employee_label.configure(fg=self.after_click)

        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)


    def main_left_item_1_fun(self, e):
        self.main_item_main()
        # self.main_Employee_record_main()
        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_3_2)
        self.main_left_item_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_item_label.configure(fg=self.after_click)


        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)

    def main_left_table_1_fun(self, e):
        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_3_2)
        self.main_left_table_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_table_label.configure(fg=self.after_click)


        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)


        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)


    def main_left_materials_1_fun(self, e):
        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_3_2)
        self.main_left_materials_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_materials_label.configure(fg=self.after_click)


        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)



    def main_left_sales_1_fun(self, e):
        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_3_2)
        self.main_left_sales_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_sales_label.configure(fg=self.after_click)


        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)




    def main_left_recipes_1_fun(self, e):
        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_3_2)
        self.main_left_recipes_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_recipes_label.configure(fg=self.after_click)


        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)


        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)


        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)





    def main_left_restaurant_info_1_fun(self, e):
        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_3_2)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_restaurant_info_label.configure(fg=self.after_click)

        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)

        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)

        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_w_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_w_3_1)
        self.main_left_setting_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_setting_label.configure(fg=self.before_click)




    def main_left_setting_1_fun(self, e):
        self.main_left_setting_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_setting_image_frame['image'] = (self.main_left_setting_image_3)
        self.main_left_setting_image_frame_1['image'] = (self.main_left_setting_image_3_2)
        self.main_left_setting_image_frame_1.configure(bg=self.box_on_click)
        self.main_left_setting_label.configure(fg=self.after_click)

        self.main_left_dashboard_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_dashboard_image_frame['image'] = (self.main_left_dashboard_image_w_3)
        self.main_left_dashboard_image_frame_1['image'] = (self.main_left_dashboard_image_w_3_1)
        self.main_left_dashboard_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_dashboard_label.configure(fg=self.before_click)

        self.main_left_employee_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_employee_image_frame['image'] = (self.main_left_employee_image_w_3)
        self.main_left_employee_image_frame_1['image'] = (self.main_left_employee_image_w_3_1)
        self.main_left_employee_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_employee_label.configure(fg=self.before_click)

        self.main_left_item_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_item_image_frame['image'] = (self.main_left_item_image_w_3)
        self.main_left_item_image_frame_1['image'] = (self.main_left_item_image_w_3_1)
        self.main_left_item_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_item_label.configure(fg=self.before_click)

        self.main_left_table_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_table_image_frame['image'] = (self.main_left_table_image_w_3)
        self.main_left_table_image_frame_1['image'] = (self.main_left_table_image_w_3_1)
        self.main_left_table_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_table_label.configure(fg=self.before_click)

        self.main_left_materials_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_materials_image_frame['image'] = (self.main_left_materials_image_w_3)
        self.main_left_materials_image_frame_1['image'] = (self.main_left_materials_image_w_3_1)
        self.main_left_materials_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_materials_label.configure(fg=self.before_click)


        self.main_left_sales_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_sales_image_frame['image'] = (self.main_left_sales_image_w_3)
        self.main_left_sales_image_frame_1['image'] = (self.main_left_sales_image_w_3_1)
        self.main_left_sales_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_sales_label.configure(fg=self.before_click)

        self.main_left_recipes_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_recipes_image_frame['image'] = (self.main_left_recipes_image_w_3)
        self.main_left_recipes_image_frame_1['image'] = (self.main_left_recipes_image_w_3_1)
        self.main_left_recipes_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_recipes_label.configure(fg=self.before_click)

        self.main_left_restaurant_info_image_frame.configure(bg=self.main_background_upward_color)
        self.main_left_restaurant_info_image_frame['image'] = (self.main_left_restaurant_info_image_w_3)
        self.main_left_restaurant_info_image_frame_1['image'] = (self.main_left_restaurant_info_image_w_3_1)
        self.main_left_restaurant_info_image_frame_1.configure(bg=self.main_background_color)
        self.main_left_restaurant_info_label.configure(fg=self.before_click)














































main_root=Tk()
l_obj1=main_display(main_root)
mainloop()