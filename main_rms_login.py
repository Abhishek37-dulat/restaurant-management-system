from tkinter import *
import PIL
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
import subprocess
import os



class Register:
    def __init__(self,l_root):
        self.root_l=l_root
        self.l_width=int(self.root_l.winfo_screenwidth()/1.5)
        self.l_height = int(self.root_l.winfo_screenheight()/2)
        self.l_x = int(self.root_l.winfo_screenwidth() / 6)
        self.l_y = int(self.root_l.winfo_screenheight() / 5)
        self.root_l.overrideredirect(1)
        self.root_l.title("Registration Window")
        self.root_l.geometry(f"{self.l_width}x{self.l_height}+{self.l_x}+{self.l_y}")
        self.frame1_main("#1B2026","#ffffff")
        # self.frame2_main("#1B2026",1,"#908F8C","#ffffff","bold","normal")
        # self.login_form("#1B2026","#ffffff")
        # self.create_new_account("#1B2026","#ffffff")
        path = "main_after_login.py"
        self.path = path
        self.database_host = "localhost"
        self.database_user = "root"
        self.database_password="m81321a"
        self.database_name="register_rms"


    def frame1_main(self,Dark_theme_color,Text_color):
        self.Dark_theme_color = Dark_theme_color
        self.Text_color = Text_color
    #====================== Frame1 ========================

        self.frame1 = Frame(self.root_l,bg=self.Dark_theme_color)
        self.frame1.place(relx=0,rely=0,width=self.l_width,height=self.l_height)



        self.frame1_Login_image_open_1 = Image.open("log_rotate_1.png")
        self.frame1_Login_image_resize_1 = self.frame1_Login_image_open_1.resize((232,213))
        self.frame1_Login_image_apply_1 = ImageTk.PhotoImage(self.frame1_Login_image_resize_1)

        self.frame1_Login_image_open_2 = Image.open("log_rotate_1.png")
        self.frame1_Login_image_resize_2 = self.frame1_Login_image_open_2.resize((272,253))
        self.frame1_Login_image_apply_2 = ImageTk.PhotoImage(self.frame1_Login_image_resize_2)

        self.frame1_Login_image_1 = Label(self.frame1, image=self.frame1_Login_image_apply_1, bg=self.Dark_theme_color)
        self.frame1_Login_image_1.place(relx=0.15, rely=0.35)
        self.frame1_Login_image_Label_1 = Label(self.frame1_Login_image_1, text="Login",font=("Kristen ITC",23),fg=self.Text_color, bg=self.Dark_theme_color)
        self.frame1_Login_image_Label_1.place(relx=0.3, rely=0.38)

        self.frame1_Login_image_2 = Label(self.frame1, image=self.frame1_Login_image_apply_2, bg=self.Dark_theme_color,borderwidth=0)
        self.frame1_Login_image_2.place(relx=0.55, rely=0.3)
        self.frame1_Login_image_Label_2 = Label(self.frame1_Login_image_2, text="Register", font=("Kristen ITC", 19), fg=self.Text_color,bg=self.Dark_theme_color)
        self.frame1_Login_image_Label_2.place(relx=0.3, rely=0.4)


        self.frame1_Login_image_2.bind('<Button-1>', self.create_form_call)
        self.frame1_Login_image_2.bind('<Enter>',self.frame1_hover_reg_on1)
        self.frame1_Login_image_2.bind('<Leave>',self.frame1_hover_reg_off1)

        self.frame1_Login_image_1.bind('<Button-1>', self.login_form_call)
        self.frame1_Login_image_1.bind('<Enter>', self.frame1_hover_log_on1)
        self.frame1_Login_image_1.bind('<Leave>', self.frame1_hover_log_off1)





    # ====================== Frame2 ========================
        self.frame2 = Frame(self.frame1, bg=self.Dark_theme_color)
        self.frame2.place(relx=0, rely=0, width=int(self.l_width/12), height=int(self.l_height/6))

        self.frame2_Login_image_open_1_c = Image.open("logo.png")
        self.frame2_Login_image_resize_1_c = self.frame2_Login_image_open_1_c.resize((30, 30))
        self.frame2_Login_image_apply_1_c = ImageTk.PhotoImage(self.frame2_Login_image_resize_1_c)

        self.frame2_Login_image_open_2_c = Image.open("logo_gold.png")
        self.frame2_Login_image_resize_2_c = self.frame2_Login_image_open_2_c.resize((30, 30))
        self.frame2_Login_image_apply_2_c = ImageTk.PhotoImage(self.frame2_Login_image_resize_2_c)
        if self.Dark_theme_color == "#ffffff":
            self.frame2_Login_image_apply_1 = self.frame2_Login_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.frame2_Login_image_apply_1 = self.frame2_Login_image_apply_1_c
        else:
            print("Error in frame one theme")

        self.frame2_Login_image_Label_2 = Label(self.frame2, image=self.frame2_Login_image_apply_1, bg=self.Dark_theme_color)
        self.frame2_Login_image_Label_2.place(relx=0.1, rely=0.1)
        self.frame2_Login_image_Label_2.bind('<Button-1>',self.connect_to_frames)
        self.L_f1_t = "#ffffff"

    # ====================== Frame3 ========================
        self.frame3 = Frame(self.frame1, bg=self.Dark_theme_color)
        self.frame3.place(relx=0.2, rely=0, width=int(self.l_width / 2), height=int(self.l_height / 6))

        self.frame3_Login_image_Label_1 = Label(self.frame3, text="Restaurant Management System", font=("Mistral", 30,"bold"), fg=self.Text_color,bg=self.Dark_theme_color)
        self.frame3_Login_image_Label_1.place(relx=0.1, rely=0.1)

    # ====================== Frame4 ========================
        self.frame4 = Frame(self.frame1, bg=self.Dark_theme_color)
        self.frame4.place(relx=0.93, rely=0, width=int(self.l_width / 14), height=int(self.l_height / 8))

        self.frame4_Login_image_open_1_c = Image.open("close.png")
        self.frame4_Login_image_resize_1_c = self.frame4_Login_image_open_1_c.resize((30, 30))
        self.frame4_Login_image_apply_1_c = ImageTk.PhotoImage(self.frame4_Login_image_resize_1_c)

        self.frame4_Login_image_open_2_c = Image.open("close_blue.png")
        self.frame4_Login_image_resize_2_c = self.frame4_Login_image_open_2_c.resize((30, 30))
        self.frame4_Login_image_apply_2_c = ImageTk.PhotoImage(self.frame4_Login_image_resize_2_c)

        if self.Dark_theme_color == "#ffffff":
            self.frame4_Login_image_apply_1 = self.frame4_Login_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.frame4_Login_image_apply_1 = self.frame4_Login_image_apply_1_c
        else:
            print("Error in frame one theme")


        self.frame4_Login_image_Label_2 = Label(self.frame4, image=self.frame4_Login_image_apply_1, bg=self.Dark_theme_color)
        self.frame4_Login_image_Label_2.place(relx=0.1, rely=0.1)
        self.frame4_Login_image_Label_2.bind('<Button-1>',self.close_me)

    def frame1_hover_reg_on1(self, e):
        self.frame1_Login_image_Label_2_reg_on2 = self.frame1_Login_image_Label_2
        self.frame1_hover_on1_image_label =self.frame1_Login_image_2
        self.frame1_Login_image_open_2 = Image.open("log_rotate_1.png")
        self.frame1_Login_image_resize_2 = self.frame1_Login_image_open_2.resize((282, 263))
        self.frame1_Login_image_apply_2 = ImageTk.PhotoImage(self.frame1_Login_image_resize_2)

        self.frame1_hover_on1_image_label = Label(self.frame1, image=self.frame1_Login_image_apply_2, bg=self.Dark_theme_color,borderwidth=0)
        self.frame1_hover_on1_image_label.place(relx=0.55, rely=0.3)
        self.frame1_Login_image_Label_2_reg_on2 = Label(self.frame1_hover_on1_image_label, text="Register", font=("Kristen ITC", 21), fg=self.Text_color,bg=self.Dark_theme_color)
        self.frame1_Login_image_Label_2_reg_on2.place(relx=0.28, rely=0.4)
        self.frame1_hover_on1_image_label.bind('<Button-1>', self.create_form_call)
        self.frame1_Login_image_Label_2_reg_on2.bind('<Button-1>', self.create_form_call)
        self.frame1_hover_on1_image_label.bind('<Leave>', self.frame1_hover_reg_off1)
        self.frame1_Login_image_2.destroy()
        self.frame1_Login_image_Label_2.destroy()



    def frame1_hover_reg_off1(self,e):
        self.frame1_Login_image_Label_2_reg_off2 = self.frame1_Login_image_Label_2
        self.frame1_hover_off1_image_label = self.frame1_Login_image_2
        self.frame1_Login_image_open_2 = Image.open("log_rotate_1.png")
        self.frame1_Login_image_resize_2 = self.frame1_Login_image_open_2.resize((272, 253))
        self.frame1_Login_image_apply_2 = ImageTk.PhotoImage(self.frame1_Login_image_resize_2)
        self.frame1_hover_off1_image_label = Label(self.frame1, image=self.frame1_Login_image_apply_2, bg=self.Dark_theme_color, borderwidth=0)
        self.frame1_hover_off1_image_label.place(relx=0.55, rely=0.3)
        self.frame1_Login_image_Label_2_reg_off2 = Label(self.frame1_hover_off1_image_label, text="Register", font=("Kristen ITC", 19), fg=self.Text_color,bg=self.Dark_theme_color)
        self.frame1_Login_image_Label_2_reg_off2.place(relx=0.3, rely=0.4)
        self.frame1_hover_off1_image_label.bind('<Enter>',self.frame1_hover_reg_on1)
        self.frame1_Login_image_2.destroy()
        self.frame1_Login_image_Label_2.destroy()



    def frame1_hover_log_on1(self, e):

        self.frame1_Login_image_Label_1_log_on1 = self.frame1_Login_image_Label_1
        self.frame1_hover_log_on1_image_label =self.frame1_Login_image_1
        self.frame1_Login_image_open_1 = Image.open("log_rotate_1.png")
        self.frame1_Login_image_resize_1 = self.frame1_Login_image_open_1.resize((242, 223))
        self.frame1_Login_image_apply_1 = ImageTk.PhotoImage(self.frame1_Login_image_resize_1)

        self.frame1_hover_log_on1_image_label = Label(self.frame1, image=self.frame1_Login_image_apply_1, bg=self.Dark_theme_color )
        self.frame1_hover_log_on1_image_label.place(relx=0.15, rely=0.35)

        self.frame1_Login_image_Label_1_log_on1 = Label(self.frame1_hover_log_on1_image_label, text="Login",font=("Kristen ITC", 25), fg=self.Text_color, bg=self.Dark_theme_color)
        self.frame1_Login_image_Label_1_log_on1.place(relx=0.3, rely=0.38)
        self.frame1_Login_image_Label_1_log_on1.bind('<Button-1>', self.login_form_call)
        self.frame1_hover_log_on1_image_label.bind('<Button-1>', self.login_form_call)
        self.frame1_hover_log_on1_image_label.bind('<Leave>', self.frame1_hover_log_off1)
        self.frame1_Login_image_1.destroy()

    def frame1_hover_log_off1(self, e):
        self.frame1_Login_image_Label_1_log_off1 = self.frame1_Login_image_Label_1
        self.frame1_hover_log_off1_image_label = self.frame1_Login_image_1
        self.frame1_Login_image_open_1 = Image.open("log_rotate_1.png")
        self.frame1_Login_image_resize_1 = self.frame1_Login_image_open_1.resize((232, 213))
        self.frame1_Login_image_apply_1 = ImageTk.PhotoImage(self.frame1_Login_image_resize_1)

        self.frame1_hover_log_off1_image_label = Label(self.frame1, image=self.frame1_Login_image_apply_1, bg=self.Dark_theme_color, borderwidth=0)
        self.frame1_hover_log_off1_image_label.place(relx=0.15, rely=0.35)

        self.frame1_Login_image_Label_1_log_off1 = Label(self.frame1_hover_log_off1_image_label,text="Login", font=("Kristen ITC", 23), fg=self.Text_color,bg=self.Dark_theme_color)
        self.frame1_Login_image_Label_1_log_off1.place(relx=0.3, rely=0.38)
        self.frame1_hover_log_off1_image_label.bind('<Enter>', self.frame1_hover_log_on1)
        self.frame1_Login_image_1.destroy()

    def close_me(self,e):
        self.root_l.destroy()
    def connect_to_frames(self,e):
        if self.Dark_theme_color == "#ffffff":
           self.frame2_main("#F6F4F0",0,"#1B2026","#333B47","normal","bold","#ffffff")
        elif self.Dark_theme_color == "#1B2026":
            self.frame2_main("#1B2026", 1, "#908F8C", "#ffffff", "bold", "normal", "#ffffff")
        else:
            print("not")

    def connect_to_frames_1(self):
        if self.L_f1_t == self.light_text_color:
           self.frame1_main("#ffffff","#1B2026")
        elif self.D_f1_t == self.light_text_color:
            self.frame1_main("#1B2026","#ffffff")
        else:
            print("not")

    def connect_to_frames_1_by_login_form(self,e):
        if self.Dark_theme_color == "#ffffff":
           self.frame1_main("#ffffff","#1B2026")
        elif self.Dark_theme_color == "#1B2026":
            self.frame1_main("#1B2026","#ffffff")
        else:
            print("not")

    def login_form_call(self,e):
        if self.Dark_theme_color == "#1B2026":
           self.login_form("#1B2026","#ffffff")
        elif self.Dark_theme_color == "#ffffff":
           self.login_form("#ffffff","#1B2026")
        else:
            print("not possible!")


    def connect_to_create_new_account_frame3(self,e):
        if self.Dark_theme_color == "#ffffff":
           self.frame1_main("#ffffff","#1B2026")
        elif self.Dark_theme_color == "#1B2026":
            self.frame1_main("#1B2026","#ffffff")
        else:
            print("not")


    def create_form_call(self, e):
        if self.Dark_theme_color == "#1B2026":
           self.create_new_account("#1B2026","#ffffff")
        elif self.Dark_theme_color == "#ffffff":
           self.create_new_account("#ffffff","#1B2026")
        else:
            print("not possible!")









    def frame2_main(self,theme,mode_value,light_text_color,dark_text_color,text_bold,text_normal,theme_label_color):

          self.Dark_theme_color = theme
          self.mode_value  = mode_value
          self.light_text_color = light_text_color
          self.dark_text_color = dark_text_color
          self.text_bold = text_bold
          self.text_normal = text_normal
          self.theme_label_color = theme_label_color



          self.frame2_1 = Frame(self.root_l, bg=self.Dark_theme_color)

          self.frame2_1.place(relx=0, rely=0, width=self.l_width, height=self.l_height)

    # ====================== Frame2_2 ========================
          self.frame2_2 = Frame(self.frame2_1,bd=1, bg=self.Dark_theme_color)
          self.frame2_2.place(relx=0, rely=0, width=int(self.l_width / 12), height=int(self.l_height / 6))

          self.frame2_2_Login_image_open_1 = Image.open("logo_gold.png")
          self.frame2_2_Login_image_resize_1 = self.frame2_2_Login_image_open_1.resize((50, 50))
          self.frame2_2_Login_image_apply_1 = ImageTk.PhotoImage(self.frame2_2_Login_image_resize_1)

          self.frame2_2_Login_image_Label_1 = Label(self.frame2_2, image=self.frame2_2_Login_image_apply_1, bg=self.Dark_theme_color)
          self.frame2_2_Login_image_Label_1.place(relx=0.1, rely=0.1)

    # ====================== Frame2_3 ========================

          self.frame2_3 = Frame(self.frame2_1, bg=self.Dark_theme_color, relief="solid")
          self.frame2_3.place(relx=0.25, rely=0.25, width=int(self.l_width / 2), height=int(self.l_height / 5))

    # ====================== Frame2_3_1 ========================

          self.frame2_3_1 = Frame(self.frame2_3, bg=self.Dark_theme_color,  relief="solid")
          self.frame2_3_1.place(relx=0, rely=0.06, width=int(self.l_width / 6), height=int(self.l_height / 6))

          self.frame2_3_1_Login_image_Label_1 = Button(self.frame2_3_1,bd=0, font=("Maiandra GD", 12,self.text_normal), text="LIGHT", bg=self.Dark_theme_color,fg=self.light_text_color,command = lambda *dark_up: self.light_up_value(1) )
          self.frame2_3_1_Login_image_Label_1.place(relx=0.3, rely=0.31)

          self.build_offhover = self.frame2_3_1_Login_image_Label_1
          self.build_onhover = self.frame2_3_1_Login_image_Label_1

    # ====================== Frame2_3_2 ========================

          self.frame2_3_2 = Frame(self.frame2_3, bg=self.Dark_theme_color, relief="solid")
          self.frame2_3_2.place(relx=0.35, rely=0.06, width=int(self.l_width / 6.5), height=int(self.l_height / 6))

    # ====================== Frame2_3_3 ========================




          self.frame2_3_3 = Frame(self.frame2_3, bg=self.Dark_theme_color,  relief="solid")
          self.frame2_3_3.place(relx=0.675, rely=0.06, width=int(self.l_width / 6.5), height=int(self.l_height / 6))

          self.frame2_3_3_Login_image_Label_1 = Button(self.frame2_3_3, bd=0,  font=("Maiandra GD", 14,self.text_bold),text="DARK", bg=self.Dark_theme_color, fg=self.dark_text_color,command = lambda *dark_up: self.dark_up_value(1) )
          self.frame2_3_3_Login_image_Label_1.place(relx=0.3, rely=0.31)

          self.build_dark_offhover = self.frame2_3_3_Login_image_Label_1
          self.build_dark_onhover = self.frame2_3_3_Login_image_Label_1

          self.build_dark_offhover_orizanal = self.frame2_3_3_Login_image_Label_1





    # ====================== Frame2_4 ========================

          self.frame2_4_m = Frame(self.frame2_1, bg=self.Dark_theme_color, relief="solid")
          self.frame2_4_m.place(relx=0.04, rely=0.25, width=int(self.l_width / 6), height=int(self.l_height / 5))

    # ====================== Frame2_4_1 ========================

          self.frame2_4 = Frame(self.frame2_4_m, bg=self.Dark_theme_color, relief="solid")
          self.frame2_4.place(relx=0.0, rely=0.06, width=int(self.l_width / 6.5), height=int(self.l_height / 6))

          self.frame2_4_Login_image_Label_1 = Label(self.frame2_4, font=("Cascadia Code", 18, self.text_bold), text="THEMES",bg=self.Dark_theme_color, fg=self.theme_label_color)
          self.frame2_4_Login_image_Label_1.place(relx=0.2, rely=0.21)





    # ====================== Frame2_5 ========================

          self.frame2_5 = Frame(self.frame2_1, bg=self.Dark_theme_color, borderwidth=0,relief="flat")
          self.frame2_5.place(relx=0.7, rely=0.7, width=int(self.l_width / 7), height=int(self.l_height / 7))

          self.frame2_5_save_image_open = PhotoImage(file=r"s1.png")
          self.photoimage = self.frame2_5_save_image_open.subsample(3, 3)

          self.frame2_5_save_image_open_w = PhotoImage(file=r"s2.png")
          self.photoimage_w = self.frame2_5_save_image_open_w.subsample(3, 3)

          self.frame2_5_save_button = Button(self.frame2_5,text="Save Theme ",borderwidth=0,image=self.photoimage,bg="#ffffff",compound = RIGHT,width=150,height=50,font=("Cascadia Code", 10, self.text_bold),command=self.connect_to_frames_1)
          self.frame2_5_save_button.pack()








          self.self_mode(self.mode_value)
    def self_mode(self,e):
        self.condition_on_dark_and_light_mode=e
        print(self.condition_on_dark_and_light_mode)

        if self.condition_on_dark_and_light_mode == 0:
            self.light_theme()
        elif self.condition_on_dark_and_light_mode == 1:
            self.dark_theme()
        else:
            print("Error")
    # ----------------------- Light Theme -------------------------------
    def light_theme(self):
            self.frame2_5_save_button_L = self.frame2_5_save_button
            self.frame2_3_Login_image_open_1 = Image.open("switch_off.png")
            self.frame2_3_Login_image_resize_1 = self.frame2_3_Login_image_open_1.resize((55, 55))
            self.frame2_3_Login_image_apply_1 = ImageTk.PhotoImage(self.frame2_3_Login_image_resize_1)

            self.frame2_3_Login_image_Label_2 = Label(self.frame2_3_2, image=self.frame2_3_Login_image_apply_1,bg=self.Dark_theme_color)
            self.frame2_3_Login_image_Label_2.place(relx=0.3, rely=0.1)
            self.frame2_4_Login_image_Label_1 = Label(self.frame2_4, font=("Cascadia Code", 18, self.text_bold),text="THEMES", bg=self.Dark_theme_color, fg=self.light_text_color)
            self.frame2_4_Login_image_Label_1.place(relx=0.2, rely=0.21)
            self.frame2_5_save_button_L = Button(self.frame2_5, text="Save Theme ", image=self.photoimage_w, bg=self.light_text_color,fg=self.Dark_theme_color,
                                               compound=RIGHT, width=150, height=50,
                                               font=("Cascadia Code", 10, self.text_bold),
                                               command=self.connect_to_frames_1,borderwidth=0)
            self.frame2_5_save_button_L.pack()
            self.frame2_5_save_button.destroy()
            self.L_f1_t = self.light_text_color
            self.L_f1_t_L = self.Dark_theme_color


    def light_text_onhover(self, e):
            self.build_onhover = self.frame2_3_1_Login_image_Label_1
            self.build_onhover = Button(self.frame2_3_1,bd=0, font=("Maiandra GD", 16,self.text_bold),cursor="hand2", text="LIGHT", bg=self.Dark_theme_color,fg=self.light_text_color,command=lambda *light_up: self.light_up_value(1) )
            self.build_onhover.place(relx=0.3, rely=0.31)
            self.build_offhover.destroy()
            self.frame2_4_Login_image_Label_1 = Label(self.frame2_4, font=("Cascadia Code", 18, self.text_bold),
                                                      text="THEMES", bg=self.Dark_theme_color, fg=self.dark_text_color)
            self.frame2_4_Login_image_Label_1.place(relx=0.2, rely=0.21)




    def light_text_offhover(self,e):
            self.build_offhover = self.frame2_3_1_Login_image_Label_1
            self.build_offhover = Button(self.frame2_3_1,bd=0, font=("Maiandra GD", 12,self.text_normal),cursor="hand2", text="LIGHT", bg=self.Dark_theme_color,fg=self.dark_text_color,command=lambda *light_up: self.light_up_value(1))
            self.build_offhover.place(relx=0.3, rely=0.31)
            self.build_onhover.destroy()



    # ----------------------- Dark Theme -------------------------------
    def dark_theme(self):
            self.frame2_5_save_button_D = self.frame2_5_save_button
            self.frame2_3_Login_image_open_2 = Image.open("on_meanu_bar.png")
            self.frame2_3_Login_image_resize_2 = self.frame2_3_Login_image_open_2.resize((55, 55))
            self.frame2_3_Login_image_apply_2 = ImageTk.PhotoImage(self.frame2_3_Login_image_resize_2)

            self.frame2_3_Login_image_Label_2 = Label(self.frame2_3_2, image=self.frame2_3_Login_image_apply_2,  bg=self.Dark_theme_color)
            self.frame2_3_Login_image_Label_2.place(relx=0.3, rely=0.1)

            self.frame2_5_save_button_D = Button(self.frame2_5, text="Save Theme ",cursor="hand2", image=self.photoimage,bg="#ffffff", fg=self.Dark_theme_color,compound=RIGHT, width=150, height=50,font=("Cascadia Code", 10, self.text_bold),command=self.connect_to_frames_1, borderwidth=0)
            self.frame2_5_save_button_D.pack()
            self.frame2_5_save_button.destroy()
            self.D_f1_t = self.light_text_color
            self.D_f1_t_D = self.Dark_theme_color



    def dark_text_onhover(self, e):
            self.build_dark_onhover = self.frame2_3_3_Login_image_Label_1
            self.build_dark_onhover = Button(self.frame2_3_3, bd=0, font=("Maiandra GD", 16,self.text_bold),cursor="hand2", text="DARK", bg=self.Dark_theme_color,fg=self.dark_text_color,command=lambda *dark_up: self.dark_up_value(1))
            self.build_dark_onhover.place(relx=0.3, rely=0.31)
            self.build_dark_offhover.destroy()
            self.frame2_4_Login_image_Label_1 = Label(self.frame2_4, font=("Cascadia Code", 18, self.text_bold),text="THEMES", bg=self.Dark_theme_color, fg=self.dark_text_color)
            self.frame2_4_Login_image_Label_1.place(relx=0.2, rely=0.21)





    def dark_text_offhover(self,e):
            self.build_dark_offhover = self.frame2_3_3_Login_image_Label_1
            self.build_dark_offhover = Button(self.frame2_3_3, bd=0, font=("Maiandra GD", 12,self.text_normal),cursor="hand2", text="DARK",bg=self.Dark_theme_color,fg=self.light_text_color,command=lambda *dark_up: self.dark_up_value(1))
            self.build_dark_offhover.place(relx=0.3, rely=0.31)
            self.build_dark_onhover.destroy()
            self.frame2_4_Login_image_Label_1 = Label(self.frame2_4, font=("Cascadia Code", 18, self.text_bold),text="THEMES", bg=self.Dark_theme_color, fg=self.light_text_color)
            self.frame2_4_Login_image_Label_1.place(relx=0.2, rely=0.21)




    def dark_up_value(self, values):
                if values == 0:
                    self.light_text_onhover(1)
                    self.dark_text_offhover(1)
                    print("Dark mode off")
                    self.self_mode(0)
                    self.frame2_main("#F6F4F0", 0, "#1B2026","#333B47", "bold", "normal","#1B2026")



                elif values == 1:
                    self.light_text_offhover(0)
                    self.dark_text_onhover(1)
                    print("Dark mode on")
                    self.self_mode(1)
                    self.frame1_main(self.D_f1_t, self.D_f1_t_D)
                    self.frame2_main("#1B2026",1,"#908F8C","#ffffff","bold","normal","#ffffff")



                else:
                    print("hello")
    def light_up_value(self, value):
                if value == 0:
                    self.dark_text_onhover(1)
                    self.light_text_offhover(1)
                    print("light mode off")
                    self.self_mode(1)
                    self.frame2_main("#F6F4F0",0,"#1B2026","#ffffff","bold","normal","#1B2026")
                elif value == 1:
                    self.light_text_onhover(1)
                    self.dark_text_offhover(1)
                    print("light mode on")
                    self.self_mode(0)
                    self.frame1_main(self.L_f1_t,self.L_f1_t_L)
                    self.frame2_main("#F6F4F0",0,"#1B2026","#333B47","normal","bold","#ffffff")

                else:
                    print("hello")










#========================================     Login form    =============================================================================================




    def login_form(self,Dark_theme_color,login_form_text_color):
        self.Dark_theme_color = Dark_theme_color
        self.login_form_text_color = login_form_text_color


#=========================== login_background_frame 1 ==============================
        self.login_background_frame1 = Frame(self.root_l, bg=self.Dark_theme_color)
        self.login_background_frame1.place(relx=0, rely=0, width=self.l_width, height=self.l_height)

#=========================== login__frame 2 ==============================
        self.login_frame2 = Frame( self.login_background_frame1, bg=self.Dark_theme_color)
        self.login_frame2.place(relx=0.25, rely=0, width=self.l_width/2, height=self.l_height)


#=========================== login__frame 2_1 ==============================
        self.login_frame2_1 = Frame(self.login_frame2 , bg=self.Dark_theme_color)
        self.login_frame2_1.place(relx=0, rely=0.05, width=self.l_width/2.01, height=self.l_height/6)

# ============== login__frame 2_1_1 ===============
        self.login_frame2_1_1 = Frame(self.login_frame2_1, bg=self.Dark_theme_color)
        self.login_frame2_1_1.place(relx=0.2, rely=0, width=self.l_width / 10, height=self.l_height / 6.1)

        self.login_frame2_1_1_image_open = Image.open("login_as_user.png")
        self.login_frame2_1_1_image_resize = self.login_frame2_1_1_image_open.resize((50,50))
        self.login_frame2_1_1_image_appling = ImageTk.PhotoImage(self.login_frame2_1_1_image_resize)

        self.login_frame2_1_1_image_label = Label(self.login_frame2_1_1,image=self.login_frame2_1_1_image_appling,bg=self.Dark_theme_color)
        self.login_frame2_1_1_image_label.place(relx=0.35,rely=0.1)


# ============== login__frame 2_1_2 ===============
        self.login_frame2_1_2 = Frame(self.login_frame2_1, bg=self.Dark_theme_color)
        self.login_frame2_1_2.place(relx=0.4, rely=0, width=self.l_width / 4, height=self.l_height / 6.1)

        self.login_frame2_1_2_label = Label(self.login_frame2_1_2,text="LOGIN",bg=self.Dark_theme_color,fg=self.login_form_text_color,font=("Mistral", 38,"bold"))
        self.login_frame2_1_2_label.place(relx=0,rely=0)





#=========================== login__frame 2_2 ==============================
        self.login_frame2_2 = Frame(self.login_frame2 , bg=self.Dark_theme_color)
        self.login_frame2_2.place(relx=0, rely=0.22, width=self.l_width/2.01, height=self.l_height/6)

        self.login_frame2_2_1 = Frame(self.login_frame2_2, bg=self.Dark_theme_color)
        self.login_frame2_2_1.place(relx=0, rely=0, width=self.l_width / 6, height=self.l_height / 6.1)

        self.login_frame2_2_label = Label(self.login_frame2_2_1, text="Username", bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Eras Light ITC", 20))
        self.login_frame2_2_label.place(relx=0.1, rely=0.4)

        self.login_frame2_2_2 = Frame(self.login_frame2_2, bg=self.Dark_theme_color)
        self.login_frame2_2_2.place(relx=0.34, rely=0, width=self.l_width / 3.05, height=self.l_height / 6.1)

        self.login_frame2_2_2_entry = Entry(self.login_frame2_2_2,font=("Eras Medium ITC",15))
        self.login_frame2_2_2_entry.place(relx=0.1,rely=0.4,width=self.l_width/3.6,height=self.l_height /12)
        self.login_frame2_2_2_entry.insert(0, "Enter username")
        self.login_frame2_2_2_entry.bind('<Button-1>', self.placeholder_username)





#=========================== login__frame 2_3 ==============================
        self.login_frame2_3 = Frame(self.login_frame2 , bg=self.Dark_theme_color)
        self.login_frame2_3.place(relx=0, rely=0.39, width=self.l_width/2.01, height=self.l_height/6)

        self.login_frame2_3_1 = Frame(self.login_frame2_3, bg=self.Dark_theme_color)
        self.login_frame2_3_1.place(relx=0, rely=0, width=self.l_width / 6, height=self.l_height / 6.1)

        self.login_frame2_3_label = Label(self.login_frame2_3_1, text="Password", bg=self.Dark_theme_color,fg=self.login_form_text_color, font=("Eras Light ITC", 20))
        self.login_frame2_3_label.place(relx=0.1, rely=0.4)

        self.login_frame2_3_2 = Frame(self.login_frame2_3, bg=self.Dark_theme_color)
        self.login_frame2_3_2.place(relx=0.34, rely=0, width=self.l_width / 3.05, height=self.l_height / 6.1)

        self.login_frame2_3_2_entry = Entry(self.login_frame2_3_2, font=("Eras Medium ITC", 15))
        self.login_frame2_3_2_entry.place(relx=0.1, rely=0.4, width=self.l_width / 3.6, height=self.l_height / 12)
        self.login_frame2_3_2_entry.insert(0,"Enter password")
        self.login_frame2_3_2_entry.bind('<Button-1>',self.placeholder_password)









#=========================== login__frame 2_4 ==============================
        self.login_frame2_4 = Frame(self.login_frame2 , bg=self.Dark_theme_color)
        self.login_frame2_4.place(relx=0, rely=0.6, width=self.l_width/2.01, height=self.l_height/6)

        self.login_frame2_4_1 = Frame(self.login_frame2_4, bg=self.Dark_theme_color)
        self.login_frame2_4_1.place(relx=0.04, rely=0.1, width=self.l_width / 2.18, height=self.l_height / 8)

        self.login_frame2_4_1_continue = Button(self.login_frame2_4_1,text="Continue",font=("Eras Medium ITC", 15),borderwidth=0,bd=0,relief="flat")
        self.login_frame2_4_1_continue.place(relx=0,rely=0, width=self.l_width / 2, height=self.l_height / 7.5)
        self.login_frame2_4_1_continue.bind('<Button-1>',self.login_to_system)

        if self.Dark_theme_color == "#ffffff":
            self.login_frame2_4_1_continue.config(bg="#1B2026",fg="#ffffff",activebackground="#1B2026",activeforeground="#ffffff")
        elif self.Dark_theme_color == "#1B2026":
            self.login_frame2_4_1_continue.config(bg="#ffffff",fg="#1B2026",activebackground="#ffffff",activeforeground="#1B2026")
        else:
            print("Error in frame one theme")




#=========================== login__frame 2_5 ==============================
        self.login_frame2_5 = Frame(self.login_frame2 , bg=self.Dark_theme_color)
        self.login_frame2_5.place(relx=0, rely=0.8, width=self.l_width/2.01, height=self.l_height/6)

        self.login_frame2_5_1 = Frame(self.login_frame2_5, bg=self.Dark_theme_color)
        self.login_frame2_5_1.place(relx=0.2, rely=0, width=self.l_width / 3, height=self.l_height / 13)

        self.login_frame2_5_1_label = Label(self.login_frame2_5_1,text="Forgot password?",font=("Kristen ITC",10),bg=self.Dark_theme_color,fg="#FFC800")
        self.login_frame2_5_1_label.pack()

        self.login_frame2_5_1_label.bind('<Button-1>', self.create_form_call)
        self.login_frame2_5_1_label.bind('<Enter>', self.login_frame2_5_1_label_create_in_hover)
        self.login_frame2_5_1_label.bind('<Leave>', self.login_frame2_5_1_label_create_out_hover)

        self.login_frame2_5_2 = Frame(self.login_frame2_5, bg=self.Dark_theme_color)
        self.login_frame2_5_2.place(relx=0.2, rely=0.5, width=self.l_width / 3, height=self.l_height / 13)

        self.login_frame2_5_2_label = Label(self.login_frame2_5_2, text="Create New Account", font=("Kristen ITC", 10),bg=self.Dark_theme_color, fg="#FFC800")
        self.login_frame2_5_2_label.pack()
        self.login_frame2_5_2_label.bind('<Button-1>',self.create_form_call)
        self.login_frame2_5_2_label.bind('<Enter>', self.login_frame2_5_2_label_create_in_hover)
        self.login_frame2_5_2_label.bind('<Leave>', self.login_frame2_5_2_label_create_out_hover)


# =========================== login__frame 2_6 ==============================
        self.login_frame2_6 = Frame(self.login_background_frame1, bg=self.Dark_theme_color)
        self.login_frame2_6.place(relx=0, rely=0, width=self.l_width / 7, height=self.l_height / 6)

        self.frame2_6_Login_image_open_1_c = Image.open("left_side.png")
        self.frame2_6_Login_image_resize_1_c = self.frame2_6_Login_image_open_1_c.resize((30, 30))
        self.frame2_6_Login_image_apply_1_c = ImageTk.PhotoImage(self.frame2_6_Login_image_resize_1_c)

        self.frame2_6_Login_image_open_2_c = Image.open("left_side_blue.png")
        self.frame2_6_Login_image_resize_2_c = self.frame2_6_Login_image_open_2_c.resize((30, 30))
        self.frame2_6_Login_image_apply_2_c = ImageTk.PhotoImage(self.frame2_6_Login_image_resize_2_c)

        if self.Dark_theme_color == "#ffffff":
            self.frame2_6_Login_image_apply_1 = self.frame2_6_Login_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.frame2_6_Login_image_apply_1 = self.frame2_6_Login_image_apply_1_c
        else:
            print("Error in frame one theme")

        self.frame2_6_Login_image_Label_2 = Label(self.login_frame2_6, image=self.frame2_6_Login_image_apply_1,bg=self.Dark_theme_color)
        self.frame2_6_Login_image_Label_2.place(relx=0.1, rely=0.1)
        self.frame2_6_Login_image_Label_2.bind('<Button-1>', self.connect_to_frames_1_by_login_form)






# =========================== login__frame 2_7 ==============================
        self.login_frame2_7 = Frame(self.login_background_frame1, bg=self.Dark_theme_color)
        self.login_frame2_7.place(relx=0.855, rely=0, width=self.l_width / 7, height=self.l_height / 6)

        self.frame2_7_Login_image_open_1_c = Image.open("close.png")
        self.frame2_7_Login_image_resize_1_c = self.frame2_7_Login_image_open_1_c.resize((30, 30))
        self.frame2_7_Login_image_apply_1_c = ImageTk.PhotoImage(self.frame2_7_Login_image_resize_1_c)

        self.frame2_7_Login_image_open_2_c = Image.open("close_blue.png")
        self.frame2_7_Login_image_resize_2_c = self.frame2_7_Login_image_open_2_c.resize((30, 30))
        self.frame2_7_Login_image_apply_2_c = ImageTk.PhotoImage(self.frame2_7_Login_image_resize_2_c)

        if self.Dark_theme_color == "#ffffff":
            self.frame2_7_Login_image_apply_1 = self.frame2_7_Login_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.frame2_7_Login_image_apply_1 = self.frame2_7_Login_image_apply_1_c
        else:
            print("Error in frame one theme")

        self.frame2_7_Login_image_Label_2 = Label(self.login_frame2_7, image=self.frame2_7_Login_image_apply_1,bg=self.Dark_theme_color)
        self.frame2_7_Login_image_Label_2.place(relx=0.5, rely=0.1)
        self.frame2_7_Login_image_Label_2.bind('<Button-1>', self.close_me)








    def placeholder_username(self, e):
        self.login_frame2_2_2_entry.delete(0, END)

    def placeholder_password(self,e):
        self.login_frame2_3_2_entry.delete(0, END)
        self.login_frame2_3_2_entry.config(show="*")

    def login_frame2_5_2_label_create_in_hover(self,e):
        self.login_frame2_5_2_label.config(font=("Kristen ITC", 12))

    def login_frame2_5_2_label_create_out_hover(self,e):
        self.login_frame2_5_2_label.config(font=("Kristen ITC", 10))

    def login_frame2_5_1_label_create_in_hover(self,e):
        self.login_frame2_5_1_label.config(font=("Kristen ITC", 12))

    def login_frame2_5_1_label_create_out_hover(self,e):
        self.login_frame2_5_1_label.config(font=("Kristen ITC", 10))



    def login_to_system(self,e):
        try:
            self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
            self.cur = self.con.cursor()

            self.login_username = self.cur.execute("SELECT owner_username FROM owner_register WHERE owner_username=%s",self.login_frame2_2_2_entry.get())
            self.login_username_fetch = self.cur.fetchone()
            self.login_password = self.cur.execute("SELECT owner_password FROM owner_register WHERE owner_username=%s and owner_password=%s",(self.login_frame2_2_2_entry.get(),self.login_frame2_3_2_entry.get()))
            self.login_password_fetch = self.cur.fetchone()

            if self.login_username_fetch == None and self.login_password_fetch == None:
                messagebox.showerror("Validation","Username or Password are Invalid")

            else:
                if self.login_username_fetch[0] == self.login_frame2_2_2_entry.get() and self.login_password_fetch[0] == self.login_frame2_3_2_entry.get():
                   self.call_nex_page()
                   self.con.commit()
                   self.con.close()
                   self.cur.close()
                   messagebox.showinfo("Success", "login Successful", parent=self.root_l)

                else:
                    print(self.login_username_fetch[0])
                    print(self.login_password_fetch[0])

                    messagebox.showinfo("ERROR", "Sorry , your username or password is not correct!", parent=self.root_l)





        except Exception as es:
            messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root_l)

    def call_nex_page(self):
        self.root_l.destroy()
        os.system('python main_after_login.py')







#========================================     create new account form    =============================================================================================




    def create_new_account(self,Dark_theme_color,login_form_text_color):
        self.Dark_theme_color = Dark_theme_color
        self.login_form_text_color = login_form_text_color


#=========================== create_background_frame 1 ==============================
        self.create_new_account_background_frame1 = Frame(self.root_l, bg=self.Dark_theme_color)
        self.create_new_account_background_frame1.place(relx=0, rely=0, width=self.l_width, height=self.l_height*2)

#=========================== create__frame 2 ==============================
        self.create_new_account_frame2 = Frame( self.create_new_account_background_frame1, bg=self.Dark_theme_color)
        self.create_new_account_frame2.place(relx=0.08, rely=0, width=self.l_width/1.2, height=self.l_height)


#=========================== create__frame 2_1 ==============================
        self.create_new_account_frame2_1 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_1.place(relx=0.001, rely=0, width=self.l_width/1.207, height=self.l_height/7)
#=========== create__frame 2_1_1 ===========
        self.create_new_account_frame2_1_1 = Frame(self.create_new_account_frame2_1, bg=self.Dark_theme_color)
        self.create_new_account_frame2_1_1.place(relx=0.2, rely=0, width=self.l_width /10,height=self.l_height / 7.2)

        self.create_new_account_frame2_1_1_image_open = Image.open("create_new_account.png")
        self.create_new_account_frame2_1_1_image_resize = self.create_new_account_frame2_1_1_image_open.resize((40,40))
        self.create_new_account_frame2_1_2_image_apply_1_c = ImageTk.PhotoImage(self.create_new_account_frame2_1_1_image_resize)

        self.create_new_account_frame2_1_2_image_open = Image.open("create_new_account_blue.png")
        self.create_new_account_frame2_1_2_image_resize = self.create_new_account_frame2_1_2_image_open.resize((40, 40))
        self.create_new_account_frame2_1_2_image_apply_2_c = ImageTk.PhotoImage(self.create_new_account_frame2_1_2_image_resize)


        if self.Dark_theme_color == "#ffffff":
            self.create_new_account_frame2_1_2_image_apply_1 = self.create_new_account_frame2_1_2_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.create_new_account_frame2_1_2_image_apply_1 = self.create_new_account_frame2_1_2_image_apply_1_c
        else:
            print("Error in frame one theme")



        self.create_new_account_frame2_1_1_image_label = Label(self.create_new_account_frame2_1_1,image=self.create_new_account_frame2_1_2_image_apply_1,bg=self.Dark_theme_color)
        self.create_new_account_frame2_1_1_image_label.place(relx=0.55, rely=0.2)


# =========== create__frame 2_1_2 ===========
        self.create_new_account_frame2_1_2 = Frame(self.create_new_account_frame2_1, bg=self.Dark_theme_color)
        self.create_new_account_frame2_1_2.place(relx=0.32, rely=0, width=self.l_width/2.43,height=self.l_height/7.2)

        self.create_new_account_frame2_1_2_label = Label(self.create_new_account_frame2_1_2,text="Create New Account",bg=self.Dark_theme_color,fg=self.login_form_text_color,font=("Mistral", 38,"bold"))
        self.create_new_account_frame2_1_2_label.place(relx=0,rely=0)





# =========================== create__frame 2_2 ==============================
        self.create_new_account_frame2_2 = Frame(self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_2.place(relx=0.001, rely=0.21, width=self.l_width / 1.207,
                                               height=self.l_height / 10)
# =========== create__frame 2_3_1 ===========
        self.create_new_account_frame2_2_1 = Frame(self.create_new_account_frame2_2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_2_1.place(relx=0, rely=0, width=self.l_width / 7.8, height=self.l_height / 10.5)

        self.create_new_account_frame2_2_1_label = Label(self.create_new_account_frame2_2_1, text="Restaurant Name",
                                                         bg=self.Dark_theme_color, fg=self.login_form_text_color,
                                                         font=("Kalam", 12))
        self.create_new_account_frame2_2_1_label.place(relx=0, rely=0)

# =========== create__frame 2_3_2 ===========
        self.create_new_account_frame2_2_2 = Frame(self.create_new_account_frame2_2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_2_2.place(relx=0.157, rely=0, width=self.l_width / 1.437,
                                                 height=self.l_height / 10.5)

        self.create_new_account_frame2_2_2_entry = Entry(self.create_new_account_frame2_2_2)
        self.create_new_account_frame2_2_2_entry.place(relx=0, rely=0, width=self.l_width / 1.445,
                                                       height=self.l_height / 13.5)
        self.create_new_account_frame2_2_2_entry.insert(0, "Enter Restaurant Name")

        self.create_new_account_frame2_2_2_entry.bind('<Button-1>', self.placeholder_creater_restaurant_name)




#=========================== create__frame 2_3 ==============================
        self.create_new_account_frame2_3 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_3.place(relx=0.001, rely=0.315, width=self.l_width/1.207, height=self.l_height/10)


# =========== create__frame 2_3_1 ===========
        self.create_new_account_frame2_3_1 = Frame(self.create_new_account_frame2_3, bg=self.Dark_theme_color)
        self.create_new_account_frame2_3_1.place(relx=0, rely=0, width=self.l_width / 7.8, height=self.l_height / 10.5)

        self.create_new_account_frame2_3_1_label = Label(self.create_new_account_frame2_3_1, text="First Name",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_3_1_label.place(relx=0, rely=0)


# =========== create__frame 2_3_2 ===========
        self.create_new_account_frame2_3_2 = Frame(self.create_new_account_frame2_3, bg=self.Dark_theme_color)
        self.create_new_account_frame2_3_2.place(relx=0.157, rely=0, width=self.l_width / 3.5, height=self.l_height / 10.5)

        self.create_new_account_frame2_3_2_entry = Entry(self.create_new_account_frame2_3_2)
        self.create_new_account_frame2_3_2_entry.place(relx=0,rely=0,width=self.l_width / 3.7, height=self.l_height / 13.5)
        self.create_new_account_frame2_3_2_entry.insert(0,"Enter First Name")

        self.create_new_account_frame2_3_2_entry.bind('<Button-1>',self.placeholder_creater_first_name)



# =========== create__frame 2_3_3 ===========
        self.create_new_account_frame2_3_3 = Frame(self.create_new_account_frame2_3, bg=self.Dark_theme_color)
        self.create_new_account_frame2_3_3.place(relx=0.51, rely=0, width=self.l_width / 7.8, height=self.l_height / 10.5)

        self.create_new_account_frame2_3_3_label = Label(self.create_new_account_frame2_3_3, text="Last Name",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_3_3_label.place(relx=0, rely=0)


# =========== create__frame 2_3_4 ===========
        self.create_new_account_frame2_3_4 = Frame(self.create_new_account_frame2_3, bg=self.Dark_theme_color)
        self.create_new_account_frame2_3_4.place(relx=0.668, rely=0, width=self.l_width / 3.65,height=self.l_height / 10.5)

        self.create_new_account_frame2_3_4_entry = Entry(self.create_new_account_frame2_3_4)
        self.create_new_account_frame2_3_4_entry.place(relx=0, rely=0, width=self.l_width / 3.7,height=self.l_height / 13.5)
        self.create_new_account_frame2_3_4_entry.insert(0,"Enter Last Name")

        self.create_new_account_frame2_3_4_entry.bind('<Button-1>',self.placeholder_creater_last_name)















#=========================== create__frame 2_4 ==============================
#         self.create_new_account_frame2_4 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
#         self.create_new_account_frame2_4.place(relx=0.001, rely=0.42, width=self.l_width/1.207, height=self.l_height/10)
#
# # =========== create__frame 2_4_1 ===========
#         self.create_new_account_frame2_4_1 = Frame(self.create_new_account_frame2_4, bg=self.Dark_theme_color)
#         self.create_new_account_frame2_4_1.place(relx=0, rely=0, width=self.l_width / 7.8, height=self.l_height / 10.5)
#
#         self.create_new_account_frame2_4_1_label = Label(self.create_new_account_frame2_4_1, text="Restaurant Loc",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
#         self.create_new_account_frame2_4_1_label.place(relx=0, rely=0)
#
#         # =========== create__frame 2_4_2 ===========
#         self.create_new_account_frame2_4_2 = Frame(self.create_new_account_frame2_4, bg=self.Dark_theme_color)
#         self.create_new_account_frame2_4_2.place(relx=0.157, rely=0, width=self.l_width / 1.437,height=self.l_height / 10.5)
#
#         self.create_new_account_frame2_4_2_entry = Entry(self.create_new_account_frame2_4_2)
#         self.create_new_account_frame2_4_2_entry.place(relx=0, rely=0, width=self.l_width / 1.445,height=self.l_height / 13.5)
#         self.create_new_account_frame2_4_2_entry.insert(0,"Enter Restaurant Address/Location")
#         self.create_new_account_frame2_4_2_entry.bind('<Button-1>',self.placeholder_creater_restaurant_location)







#=========================== create__frame 2_5 ==============================
        self.create_new_account_frame2_5 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_5.place(relx=0.001, rely=0.42, width=self.l_width/1.207, height=self.l_height/10)
# =========== create__frame 2_5_1 ===========
        self.create_new_account_frame2_5_1 = Frame(self.create_new_account_frame2_5, bg=self.Dark_theme_color)
        self.create_new_account_frame2_5_1.place(relx=0, rely=0, width=self.l_width /7.8, height=self.l_height / 10.5)

        self.create_new_account_frame2_5_1_label = Label(self.create_new_account_frame2_5_1, text="Email id",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_5_1_label.place(relx=0, rely=0)



# =========== create__frame 2_5_2 ===========
        self.create_new_account_frame2_5_2 = Frame(self.create_new_account_frame2_5, bg=self.Dark_theme_color)
        self.create_new_account_frame2_5_2.place(relx=0.157, rely=0, width=self.l_width / 3.5,height=self.l_height / 10.5)

        self.create_new_account_frame2_5_2_entry = Entry(self.create_new_account_frame2_5_2)
        self.create_new_account_frame2_5_2_entry.place(relx=0, rely=0, width=self.l_width / 3.7,height=self.l_height / 13.5)
        self.create_new_account_frame2_5_2_entry.insert(0,"Enter Email Id")

        self.create_new_account_frame2_5_2_entry.bind('<Button-1>',self.placeholder_creater_email_id)

# =========== create__frame 2_5_3 ===========
        self.create_new_account_frame2_5_3 = Frame(self.create_new_account_frame2_5, bg=self.Dark_theme_color)
        self.create_new_account_frame2_5_3.place(relx=0.51, rely=0, width=self.l_width / 7.8,height=self.l_height / 10.5)

        self.create_new_account_frame2_5_3_label = Label(self.create_new_account_frame2_5_3, text="Phone no.",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_5_3_label.place(relx=0, rely=0)



# =========== create__frame 2_5_4 ===========
        self.create_new_account_frame2_5_4 = Frame(self.create_new_account_frame2_5, bg=self.Dark_theme_color)
        self.create_new_account_frame2_5_4.place(relx=0.668, rely=0, width=self.l_width / 3.65,height=self.l_height / 10.5)

        self.create_new_account_frame2_5_4_entry = Entry(self.create_new_account_frame2_5_4)
        self.create_new_account_frame2_5_4_entry.place(relx=0, rely=0, width=self.l_width / 3.7,height=self.l_height / 13.5)
        self.create_new_account_frame2_5_4_entry.insert(0,"Enter Phone Number")

        self.create_new_account_frame2_5_4_entry.bind('<Button-1>',self.placeholder_creater_phone_no)






#=========================== create__frame 2_6 ==============================
        self.create_new_account_frame2_6 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_6.place(relx=0.001, rely=0.525, width=self.l_width/1.207, height=self.l_height/10)
# =========== create__frame 2_6_1 ===========
        self.create_new_account_frame2_6_1 = Frame(self.create_new_account_frame2_6, bg=self.Dark_theme_color)
        self.create_new_account_frame2_6_1.place(relx=0, rely=0, width=self.l_width /7.8, height=self.l_height / 10.5)

        self.create_new_account_frame2_6_1_label = Label(self.create_new_account_frame2_6_1, text="Password",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_6_1_label.place(relx=0, rely=0)


# =========== create__frame 2_6_2 ===========
        self.create_new_account_frame2_6_2 = Frame(self.create_new_account_frame2_6, bg=self.Dark_theme_color)
        self.create_new_account_frame2_6_2.place(relx=0.157, rely=0, width=self.l_width / 3.5,height=self.l_height / 10.5)

        self.create_new_account_frame2_6_2_entry = Entry(self.create_new_account_frame2_6_2)
        self.create_new_account_frame2_6_2_entry.place(relx=0, rely=0, width=self.l_width / 3.7,height=self.l_height / 13.5)
        self.create_new_account_frame2_6_2_entry.insert(0,"Create Password")

        self.create_new_account_frame2_6_2_entry.bind('<Button-1>',self.placeholder_creater_create_password)

# =========== create__frame 2_6_3 ===========
        self.create_new_account_frame2_6_3 = Frame(self.create_new_account_frame2_6, bg=self.Dark_theme_color)
        self.create_new_account_frame2_6_3.place(relx=0.51, rely=0, width=self.l_width / 7.8,height=self.l_height / 10.5)

        self.create_new_account_frame2_6_3_label = Label(self.create_new_account_frame2_6_3, text="Confirm Password",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_6_3_label.place(relx=0, rely=0)



# =========== create__frame 2_6_4 ===========
        self.create_new_account_frame2_6_4 = Frame(self.create_new_account_frame2_6, bg=self.Dark_theme_color)
        self.create_new_account_frame2_6_4.place(relx=0.668, rely=0, width=self.l_width / 3.65,height=self.l_height / 10.5)

        self.create_new_account_frame2_6_4_entry = Entry(self.create_new_account_frame2_6_4)
        self.create_new_account_frame2_6_4_entry.place(relx=0, rely=0, width=self.l_width / 3.7,height=self.l_height / 13.5)
        self.create_new_account_frame2_6_4_entry.insert(0,"Confirm Password")

        self.create_new_account_frame2_6_4_entry.bind('<Button-1>', self.placeholder_creater_confirm_password)





#=========================== create__frame 2_7 ==============================
        self.create_new_account_frame2_7 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_7.place(relx=0.001, rely=0.63, width=self.l_width/2.45, height=self.l_height/2.8)
# =========== create__frame 2_7_1 ===========
        self.create_new_account_frame2_7_1 = Frame(self.create_new_account_frame2_7, bg=self.Dark_theme_color)
        self.create_new_account_frame2_7_1.place(relx=0, rely=0, width=self.l_width /7.8, height=self.l_height / 10.5)

        self.create_new_account_frame2_7_1_label = Label(self.create_new_account_frame2_7_1, text="Date of birth",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_7_1_label.place(relx=0, rely=0)




# =========== create__frame 2_7_2 ===========
        self.create_new_account_frame2_7_2 = Frame(self.create_new_account_frame2_7, bg=self.Dark_theme_color)
        self.create_new_account_frame2_7_2.place(relx=0.32, rely=0, width=self.l_width / 3.6,height=self.l_height/3)


        self.create_new_account_frame2_7_2_entry = Entry(self.create_new_account_frame2_7_2)
        self.create_new_account_frame2_7_2_entry.place(relx=0, rely=0, width=self.l_width / 3.71,height=self.l_height/13.5)
        self.create_new_account_frame2_7_2_entry.insert(0,"DD / MM / YYYY")

        self.create_new_account_frame2_7_2_entry.bind('<Button-1>',self.calendar_1)





#=========================== create__frame 2_8 ==============================
        self.create_new_account_frame2_8 = Frame( self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_8.place(relx=0.5, rely=0.84, width=self.l_width/2.43, height=self.l_height/10)
# =========== create__frame 2_8_1 ===========
        self.create_new_account_frame2_8_1 = Frame(self.create_new_account_frame2_8, bg=self.Dark_theme_color)
        self.create_new_account_frame2_8_1.place(relx=0, rely=0, width=self.l_width / 2.45, height=self.l_height / 10.5)

        self.create_new_account_frame2_8_1_button = Button(self.create_new_account_frame2_8_1,text="Next",bg=self.login_form_text_color,fg=self.Dark_theme_color,font=("Kalam", 12))
        self.create_new_account_frame2_8_1_button.place(relx=0.622,rely=0.1,width=self.l_width/6.5, height=self.l_height /13 )

        self.create_new_account_frame2_8_1_button.bind('<Button-1>', self.calendar_4)





# =========================== create__frame 2_9 ==============================
        self.create_new_account_frame2_9 = Frame(self.create_new_account_frame2, bg=self.Dark_theme_color)
        self.create_new_account_frame2_9.place(relx=0.5, rely=0.63, width=self.l_width / 2.43,height=self.l_height / 10)

# =========== create__frame 2_9_1 ===========

        self.create_new_account_frame2_9_1 = Frame(self.create_new_account_frame2_9, bg=self.Dark_theme_color)
        self.create_new_account_frame2_9_1.place(relx=0, rely=0, width=self.l_width / 7.8,height=self.l_height / 10.5)

        self.create_new_account_frame2_9_1_label = Label(self.create_new_account_frame2_9_1, text="Username",bg=self.Dark_theme_color, fg=self.login_form_text_color,font=("Kalam", 12))
        self.create_new_account_frame2_9_1_label.place(relx=0, rely=0)

# =========== create__frame 2_9_2 ===========
        self.create_new_account_frame2_9_2 = Frame(self.create_new_account_frame2_9, bg=self.Dark_theme_color)
        self.create_new_account_frame2_9_2.place(relx=0.33, rely=0, width=self.l_width / 3.65, height=self.l_height / 10.5)

        self.create_new_account_frame2_9_2_entry = Entry(self.create_new_account_frame2_9_2)
        self.create_new_account_frame2_9_2_entry.place(relx=0, rely=0, width=self.l_width / 3.7,height=self.l_height / 13.5)
        self.create_new_account_frame2_9_2_entry.insert(0, "Enter unique username")
        self.create_new_account_frame2_9_2_entry.bind('<Button-1>',self.placeholder_username_call_me)












#=========================== create__frame3 ==============================
        self.create_new_account_frame3 = Frame(self.create_new_account_background_frame1, bg=self.Dark_theme_color)
        self.create_new_account_frame3.place(relx=0, rely=0, width=self.l_width/12.5, height=self.l_height/9.5)

        self.create_new_account_frame3_image_open_1_c = Image.open("left_side.png")
        self.create_new_account_frame3_image_resize_1_c = self.create_new_account_frame3_image_open_1_c.resize((30, 30))
        self.create_new_account_frame3_image_apply_1_c = ImageTk.PhotoImage(self.create_new_account_frame3_image_resize_1_c)

        self.create_new_account_frame3_image_open_2_c = Image.open("left_side_blue.png")
        self.create_new_account_frame3_image_resize_2_c = self.create_new_account_frame3_image_open_2_c.resize((30, 30))
        self.create_new_account_frame3_image_apply_2_c = ImageTk.PhotoImage(self.create_new_account_frame3_image_resize_2_c)

        if self.Dark_theme_color == "#ffffff":
            self.create_new_account_frame3_image_apply_1 = self.create_new_account_frame3_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.create_new_account_frame3_image_apply_1 = self.create_new_account_frame3_image_apply_1_c
        else:
            print("Error in frame one theme")

        self.create_new_account_frame3_image_Label_2 = Label(self.create_new_account_frame3, image=self.create_new_account_frame3_image_apply_1,bg=self.Dark_theme_color)
        self.create_new_account_frame3_image_Label_2.place(relx=0.1, rely=0.1)
        self.create_new_account_frame3_image_Label_2.bind('<Button-1>', self.connect_to_create_new_account_frame3)






#=========================== create__frame4 ==============================
        self.create_new_account_frame4 = Frame(self.create_new_account_background_frame1, bg=self.Dark_theme_color )
        self.create_new_account_frame4.place(relx=0.92, rely=0, width=self.l_width/12.5, height=self.l_height/9.5)


        self.create_new_account_frame4_image_open_1_c = Image.open("close.png")
        self.create_new_account_frame4_image_resize_1_c = self.create_new_account_frame4_image_open_1_c.resize((30, 30))
        self.create_new_account_frame4_image_apply_1_c = ImageTk.PhotoImage(self.create_new_account_frame4_image_resize_1_c)

        self.create_new_account_frame4_image_open_2_c = Image.open("close_blue.png")
        self.create_new_account_frame4_image_resize_2_c = self.create_new_account_frame4_image_open_2_c.resize((30, 30))
        self.create_new_account_frame4_image_apply_2_c = ImageTk.PhotoImage(self.create_new_account_frame4_image_resize_2_c)

        if self.Dark_theme_color == "#ffffff":
            self.create_new_account_frame4_image_apply_1 = self.create_new_account_frame4_image_apply_2_c
        elif self.Dark_theme_color == "#1B2026":
            self.create_new_account_frame4_image_apply_1 = self.create_new_account_frame4_image_apply_1_c
        else:
            print("Error in frame one theme")

        self.create_new_account_frame4_image_Label_2 = Label(self.create_new_account_frame4, image=self.create_new_account_frame4_image_apply_1,bg=self.Dark_theme_color)
        self.create_new_account_frame4_image_Label_2.place(relx=0.46, rely=0.1)
        self.create_new_account_frame4_image_Label_2.bind('<Button-1>', self.close_me)




    def placeholder_creater_first_name(self,e):
        if self.create_new_account_frame2_3_2_entry.get() == "Enter First Name":
            self.create_new_account_frame2_3_2_entry.delete(0, END)
        else:
            print("sorry")

    def placeholder_creater_last_name(self, e):
        if self.create_new_account_frame2_3_4_entry.get() == "Enter Last Name":
            self.create_new_account_frame2_3_4_entry.delete(0, END)
        else:
            print("sorry")

    def placeholder_creater_restaurant_name(self,e):
        if self.create_new_account_frame2_2_2_entry.get() == "Enter Restaurant Name":
            self.create_new_account_frame2_2_2_entry.delete(0, END)
        else:
            print("sorry")

    def placeholder_creater_email_id(self, e):
        if self.create_new_account_frame2_5_2_entry.get() == "Enter Email Id":
            self.create_new_account_frame2_5_2_entry.delete(0, END)
        else:
            print("sorry")


    def placeholder_creater_phone_no(self, e):
        if self.create_new_account_frame2_5_4_entry.get() == "Enter Phone Number":
            self.create_new_account_frame2_5_4_entry.delete(0, END)
        else:
            print("sorry")

    def placeholder_creater_create_password(self, e):
        if self.create_new_account_frame2_6_2_entry.get() == "Create Password":
            self.create_new_account_frame2_6_2_entry.delete(0, END)
        else:
            print("sorry")

    def placeholder_creater_confirm_password(self,e):
        if self.create_new_account_frame2_6_4_entry.get() == "Confirm Password":
            self.create_new_account_frame2_6_4_entry.delete(0, END)
        else:
            print("sorry")
    def placeholder_username_call_me(self,e):
        if self.create_new_account_frame2_9_2_entry.get() == "Enter unique username":
            self.create_new_account_frame2_9_2_entry.delete(0, END)
        else:
            print("sorry")

    def calendar_1(self,e):
        self.create_new_account_frame2_7_2_entry.delete(0,END)
        self.calendar_2(e)

    def calendar_2(self,e):
        self.create_new_account_frame2_7_2_calendar_frame = Frame(self.create_new_account_frame2_7, bg=self.Dark_theme_color)
        self.create_new_account_frame2_7_2_calendar_frame.place(relx=0.32, rely=0, width=self.l_width / 3.7,height=self.l_height / 3)
        self.create_new_account_frame2_7_2_calendar = Calendar(self.create_new_account_frame2_7_2_calendar_frame)
        self.create_new_account_frame2_7_2_calendar.place(relx=0, rely=0, width=self.l_width/3.7,height=self.l_height/3)
        self.calendar_3()
    def calendar_3(self):
        self.create_new_account_frame2_8_1_button.bind('<Button-1>',self.calendar_4)

    def calendar_4(self,e):
        if self.create_new_account_frame2_7_2_entry.get()  == "DD / MM / YYYY" or  self.create_new_account_frame2_6_2_entry.get() == "" or self.create_new_account_frame2_6_2_entry.get() == "Create Password" or self.create_new_account_frame2_6_4_entry.get() == "" or self.create_new_account_frame2_6_4_entry.get() == "Confirm Password" or self.create_new_account_frame2_5_2_entry.get() == "" or self.create_new_account_frame2_5_2_entry.get() == "Enter Email Id" or self.create_new_account_frame2_5_4_entry.get() == "" or self.create_new_account_frame2_5_4_entry.get() == "Enter Phone Number" or self.create_new_account_frame2_3_2_entry.get() == "" or self.create_new_account_frame2_3_2_entry.get() == "Enter First Name" or self.create_new_account_frame2_3_4_entry.get() == "" or self.create_new_account_frame2_3_4_entry.get() == "Enter Last Name" or self.create_new_account_frame2_2_2_entry.get() == "" or self.create_new_account_frame2_2_2_entry.get() == "Enter Restaurant Name" or self.create_new_account_frame2_9_2_entry.get()  == "Enter unique username" or self.create_new_account_frame2_9_2_entry.get()  == "":
            messagebox.showerror("All detail", "Please Fill All detail!")

        elif self.create_new_account_frame2_7_2_entry.get() != "DD / MM / YYYY" or self.create_new_account_frame2_6_2_entry.get() != "" or self.create_new_account_frame2_6_2_entry.get() != "Create Password" or self.create_new_account_frame2_6_4_entry.get() != "" or self.create_new_account_frame2_6_4_entry.get() != "Confirm Password" or self.create_new_account_frame2_5_2_entry.get() != "" or self.create_new_account_frame2_5_2_entry.get() != "Enter Email Id" or self.create_new_account_frame2_5_4_entry.get() != "" or self.create_new_account_frame2_5_4_entry.get() != "Enter Phone Number" or self.create_new_account_frame2_3_2_entry.get() != "" or self.create_new_account_frame2_3_2_entry.get() != "Enter First Name" or self.create_new_account_frame2_3_4_entry.get() != "" or self.create_new_account_frame2_3_4_entry.get() != "Enter Last Name" or self.create_new_account_frame2_2_2_entry.get() != "" or self.create_new_account_frame2_2_2_entry.get() != "Enter Restaurant Name" or self.create_new_account_frame2_9_2_entry.get()  != "Enter unique username" or self.create_new_account_frame2_9_2_entry.get()  != "":

            try:
                self.con = pymysql.connect(host=self.database_host, user=self.database_user, password=self.database_password, database=self.database_name)
                self.cur = self.con.cursor()



                if len(self.create_new_account_frame2_6_2_entry.get()) > 7:
                    if self.create_new_account_frame2_6_2_entry.get() != self.create_new_account_frame2_6_4_entry.get():
                        messagebox.showerror("Password", "Password and Confirm Password are not same!")
                elif len(self.create_new_account_frame2_6_2_entry.get()) < 7:
                    messagebox.showerror("Password", "Please create Password more then 10 Character!")
                elif len(
                        self.create_new_account_frame2_6_2_entry.get()) >= 7 and self.create_new_account_frame2_6_2_entry.get() == self.create_new_account_frame2_6_4_entry.get():
                    print("good to go")

                self.lenth_of_phone_no = self.create_new_account_frame2_5_4_entry.get()
                if str.isdigit(self.lenth_of_phone_no) is True:
                    if len(self.create_new_account_frame2_5_4_entry.get()) != 10:
                        messagebox.showerror("Phone number", "Your Phone Number is not valid!")
                elif str.isdigit(self.lenth_of_phone_no) is True:
                    if len(self.create_new_account_frame2_5_4_entry.get()) == 10:
                        print("Phone number is correct")
                elif str.isdigit(self.lenth_of_phone_no) is False:
                    messagebox.showerror("Phone number", "Your Phone Number is not valid!")

                if self.create_new_account_frame2_7_2_entry.get() == "":
                    self.DOB =  self.create_new_account_frame2_7_2_calendar.get_date()
                    self.fmt = "%m/%d/%y"
                    self.date_me = datetime.datetime.strptime(self.DOB, self.fmt).date()
                    print(self.date_me)
                    self.create_new_account_frame2_7_2_entry.insert(0,self.date_me)
                    self.calendar_5()







                self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                self.email = self.create_new_account_frame2_5_2_entry.get()
                self.test_domain = self.email.split('@')[1]
                self.reg_email = ""
                print(self.test_domain)
                if re.search(self.regex, self.email):
                    if self.test_domain == "gmail.com":
                        self.reg_email = self.email
                        print(self.reg_email)
                    else:
                        messagebox.showerror("Validation", "Email Id is not valid!")
                else:
                    messagebox.showerror("Validation", "Email Id is not valid!")

                self.username_data_f = self.create_new_account_frame2_7_2_entry.get()


                self.cur.execute("SELECT * FROM owner_register WHERE owner_Email_id=%s", self.reg_email)
                self.row = self.cur.fetchone()
                self.cur.execute("SELECT * FROM owner_register WHERE owner_username=%s", self.username_data_f)
                self.row_1 = self.cur.fetchone()
                if self.row != None or self.row_1 != None:
                    messagebox.showerror("Error", "User already exist", parent=self.root_l)

                else:
                    self.cur.execute(
                        "INSERT INTO owner_register(owner_username, Restaurant_name, owner_First_name, owner_Last_name, owner_Email_id, owner_Phone_number, owner_Password, owner_DOB) values(%s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.create_new_account_frame2_9_2_entry.get(),
                            self.create_new_account_frame2_2_2_entry.get(),
                            self.create_new_account_frame2_3_2_entry.get(),
                            self.create_new_account_frame2_3_4_entry.get(),
                            self.create_new_account_frame2_5_2_entry.get(),
                            self.create_new_account_frame2_5_4_entry.get(),
                            self.create_new_account_frame2_6_2_entry.get(),
                            self.create_new_account_frame2_7_2_entry.get()
                        )

                    )
                    self.con.commit()
                    self.con.close()
                    self.cur.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root_l)




            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root_l)









    def calendar_5(self):
        self.create_new_account_frame2_7_2_calendar_frame.destroy()





































l_root=Tk()
l_obj1=Register(l_root)
mainloop()