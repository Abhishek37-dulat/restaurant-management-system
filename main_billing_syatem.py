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
import os
import random


class main_billing_system:
    def __init__(self,b_root):
        self.root=b_root
        self.l_width=int(self.root.winfo_screenwidth())
        self.l_height = int(self.root.winfo_screenheight())
        self.l_x = int(0)
        self.l_y = int(0)
        self.root.overrideredirect(1)
        self.root.title("Registration Window")
        self.root.geometry(f"{self.l_width}x{self.l_height}+{self.l_x}+{self.l_y}")
        self.start_billing_system()


    def start_billing_system(self):
        #===================== Color ==========================================================================
        self.main_billing_background_color = "#F1F4F9"
        self.back_up = "#4150F5"
        self.back_down = "#E0E0E0"
        self.frame_color_white = "#ffffff"
        self.text_color_white = "#ffffff"
        self.text_color_dack = "#1B2026"
        self.frame_right_top = "#F4F5F7"
        self.text_right_top = "#737070"
        self.frame_green = "#139451"
        self.frame_red = "#FF0000"
        self.frame_yellow = "#FFF000"
        self.frame_pur = "#9D00FF"



        self.c_name = StringVar()
        self.c_number = StringVar()


        #===================== main_start_frame ===============================================================
        self.main_start_frame = Frame(self.root,bg=self.main_billing_background_color)
        self.main_start_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        #===================== main_start_frame_upward ===============================================================
        self.main_start_frame_upward_back = Frame(self.main_start_frame,bg=self.back_down)
        self.main_start_frame_upward_back.place(relx=0,rely=0,relwidth=1,relheight=0.08)

        self.main_start_frame_upward_front = Frame(self.main_start_frame_upward_back,bg=self.back_up)
        self.main_start_frame_upward_front.place(relx=0,rely=0,relwidth=1,relheight=0.99)

        # ===================== main_start_frame_upward_front_logo ===============================================================
        self.main_logo_image_1 = Image.open("dayna_logo.png")
        self.main_logo_image_2 = self.main_logo_image_1.resize((70,70))
        self.main_logo_image_3 = ImageTk.PhotoImage(self.main_logo_image_2)

        self.main_start_frame_upward_front_logo = Label(self.main_start_frame_upward_front, image=self.main_logo_image_3 ,bg=self.back_up)
        self.main_start_frame_upward_front_logo.place(relx=0,rely=0,relwidth=0.06,relheight=1)


        # ===================== main_start_frame_upward_front_Label ===============================================================
        self.main_start_frame_upward_front_Label = Label(self.main_start_frame_upward_front, text="Billing System",font=("Kristen ITC",21),fg=self.text_color_white,bg=self.back_up,anchor=W)
        self.main_start_frame_upward_front_Label.place(relx=0.06,rely=0,relwidth=0.15,relheight=1)

        # ===================== main_start_frame_upward_front_logout ===============================================================
        self.main_logout_image_1 = Image.open("sh_1.png")
        self.main_logout_image_2 = self.main_logout_image_1.resize((30,30))
        self.main_logout_image_3 = ImageTk.PhotoImage(self.main_logout_image_2)

        self.main_start_frame_upward_front_logout = Label(self.main_start_frame_upward_front, image=self.main_logout_image_3 ,bg=self.back_up,cursor="hand2")
        self.main_start_frame_upward_front_logout.place(relx=0.97,rely=0.2,relwidth=0.02,relheight=0.6)
        self.main_start_frame_upward_front_logout.bind('<Button-1>', self.logout_me)

        self.left_start_billing_system()
        self.right_start_billing_system()
        self.right_end_start_billing_system_top()


    def logout_me(self,e):
        self.root.destroy()
        os.system('python main_after_login.py')





    def left_start_billing_system(self):
        #===================== left_main_start_frame ===============================================================
        self.left_main_start_frame = Frame(self.main_start_frame,bg=self.main_billing_background_color)
        self.left_main_start_frame.place(relx=0,rely=0.08,relwidth=0.6,relheight=0.92)
        self.left_main_start_frame_downward_fun()
        self.left_main_start_frame_upward_fun()

    def left_main_start_frame_upward_fun(self):
        # ===================== left_main_start_frame_upward ===============================================================
        self.left_main_start_frame_upward_background = Frame(self.left_main_start_frame, bg=self.back_down)
        self.left_main_start_frame_upward_background.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.left_main_start_frame_upward = Frame(self.left_main_start_frame_upward_background, bg=self.back_up)
        self.left_main_start_frame_upward.place(relx=0, rely=0, relwidth=1, relheight=0.99)

        self.left_main_start_frame_upward_label = Label(self.left_main_start_frame_upward,text="Food Items",font=("Comic Sans MS",15),fg=self.text_color_white, bg=self.back_up)
        self.left_main_start_frame_upward_label.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.8)

        self.left_main_start_frame_upward_label_name = Label(self.left_main_start_frame_upward,text="Customer Name ",font=("Comic Sans MS",15),fg=self.text_color_white, bg=self.back_up)
        self.left_main_start_frame_upward_label_name.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.8)

        self.left_main_start_frame_upward_label_name_entry = Entry(self.left_main_start_frame_upward,font=("Comic Sans MS",15),textvariable=self.c_name,bg=self.text_color_white, fg=self.back_up)
        self.left_main_start_frame_upward_label_name_entry.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.6)

        self.left_main_start_frame_upward_label_ph = Label(self.left_main_start_frame_upward,text="Customer Number ",font=("Comic Sans MS",15),fg=self.text_color_white, bg=self.back_up)
        self.left_main_start_frame_upward_label_ph.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.8)

        self.left_main_start_frame_upward_label_ph_entry = Entry(self.left_main_start_frame_upward,font=("Comic Sans MS",15),textvariable=self.c_number,bg=self.text_color_white, fg=self.back_up)
        self.left_main_start_frame_upward_label_ph_entry.place(relx=0.8, rely=0.2, relwidth=0.19, relheight=0.6)



    def left_main_start_frame_downward_fun(self):
        # ===================== left_main_start_frame_downward ===============================================================
        self.left_main_start_frame_downward = Frame(self.left_main_start_frame, bg=self.main_billing_background_color)
        self.left_main_start_frame_downward.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        # ===================== left_main_start_frame_downward_scrollbar ===============================================================
        # self.left_main_start_frame_downward_scrollbar = Scrollbar(self.left_main_start_frame_downward)
        # self.left_main_start_frame_downward_scrollbar.pack(side=RIGHT, fill=Y)
        #


        # ===================== left_main_start_frame_downward_left ===============================================================
        self.left_main_start_frame_downward_left = Frame(self.left_main_start_frame_downward,bg=self.main_billing_background_color)
        # self.left_main_start_frame_downward_left.place(relx=0.01, rely=0, relwidth=0.97, relheight=1)

        # wrapper1 = LabelFrame(self.left_main_start_frame_downward_left)

        self.mycanvas = Canvas(self.left_main_start_frame_downward_left,bg=self.main_billing_background_color)
        self.mycanvas.pack(side=LEFT, fill="both", expand="yes")

        self.yscrollbar = ttk.Scrollbar(self.left_main_start_frame_downward_left, orient="vertical", command=self.mycanvas.yview)
        self.yscrollbar.pack(side=RIGHT, fill="y")
        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)

        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))
        #
        self.myframe = Frame(self.mycanvas,bg=self.main_billing_background_color)
        self.mycanvas.create_window((0, 0), window=self.myframe, anchor="nw")
        self.mycanvas.bind('<MouseWheel>', self.on_mousewheel)
        self.left_main_start_frame_downward_left.place(relx=0, rely=0, relwidth=1, relheight=1)
        # for i in range(50):
        #     Button(self.myframe, text="myButton" + str(i)).pack()

        self.left_main_start_frame_downward_item_image_fun()

    def on_mousewheel(self,event):
        self.mycanvas.yview_scroll(int(-1 * (event.delta / 50)), "units")


    def left_main_start_frame_downward_item_image_fun(self):
        try:
            self.con = pymysql.connect(host="localhost", user="root", password="m81321a", database="register_rms")
            self.cur = self.con.cursor()

            self.cur.execute("SELECT item_name FROM item_data")
            self.all_name = list(self.cur.fetchall())
            self.cur.execute("SELECT item_image FROM item_data")
            self.all_image = list(self.cur.fetchall())
            self.cur.execute("SELECT item_price FROM item_data")
            self.all_price = list(self.cur.fetchall())
            self.cur.execute("SELECT item_id FROM item_data")
            self.all_id = list(self.cur.fetchall())


        except Exception as es:
            messagebox.showerror("ERROR", f"ERROR due to: {str(es)}",parent=self.root)



        self.length_is_image = len(self.all_image)

        # ===================== left_main_start_frame_downward_item_image ===============================================================
        self.item_image_1 = Image.open("33.png")
        self.item_image_2 = self.item_image_1.resize((170,135))
        self.item_image_3 = ImageTk.PhotoImage(self.item_image_2)

        self.item_image_1_2 = Image.open("add_1.png")
        self.item_image_2_2 = self.item_image_1_2.resize((50,50))
        self.item_image_3_2 = ImageTk.PhotoImage(self.item_image_2_2)

        self.item_image_1_3 = Image.open("billing_image_1.png")
        self.item_image_2_3 = self.item_image_1_3.resize((170,135))
        self.item_image_3_3 = ImageTk.PhotoImage(self.item_image_2_3)

        self.l = [self.item_image_3]
        for i in range(self.length_is_image-1):
            self.l.append(self.item_image_3)

        self.add_bill = []
        self.add_bill_button = []
        for i in range(self.length_is_image):
            self.add_bill.append(self.item_image_3_2)


        self.image_ls = []

        for i in range(self.length_is_image):
            self.left_main_start_frame_downward_item_image_input_1_label_image_1 = Image.open(self.all_image[i][0])
            self.left_main_start_frame_downward_item_image_input_1_label_image_2 = self.left_main_start_frame_downward_item_image_input_1_label_image_1.resize((50, 50))
            self.left_main_start_frame_downward_item_image_input_1_label_image_3 = ImageTk.PhotoImage(self.left_main_start_frame_downward_item_image_input_1_label_image_2)
            self.image_ls.append(self.left_main_start_frame_downward_item_image_input_1_label_image_3)


        self.length_is_id = len(self.all_id)
        self.id_ls = []

        for i in range(self.length_is_id):
            self.id_ls.append(i)


        k=1
        m=len(self.all_name)


        # for i in range(len(self.all_name)):
        #     print(self.all_name[i][0])
        # if len(self.all_name) > 2 :
        #     k=2
        self.rr = 0
        self.cc = 0
        self.image_count = 0
        for j in range(k):
            for i in range(int(m)):
                if self.image_count == 5:
                    j+=1
                    self.rr = 5

                if self.image_count == 10:
                    j+=1
                    self.rr = 10

                if self.image_count == 15:
                    j+=1
                    self.rr = 15

                if self.image_count == 20:
                    j+=1
                    self.rr = 20

                if self.image_count == 25:
                    j=0
                    self.rr = 20

                if self.image_count == 30:
                    j+=1
                    self.rr = 25


                self.left_main_start_frame_downward_item_image = Label(self.myframe, image=self.l[i],bg=self.main_billing_background_color,cursor="hand2")
                self.left_main_start_frame_downward_item_image.grid(row=i-self.rr, column=j-self.cc,padx=1,pady=2)

                self.left_main_start_frame_downward_item_image_input_1_frame = Frame(self.left_main_start_frame_downward_item_image, bg=self.frame_color_white,cursor="hand2")
                self.left_main_start_frame_downward_item_image_input_1_frame.place(relx=0.07, rely=0.05,relwidth=0.86, relheight=0.9)


                self.left_main_start_frame_downward_item_image_input_1_label_image = Label(self.left_main_start_frame_downward_item_image_input_1_frame,image=self.image_ls[i], bg=self.frame_color_white,cursor="hand2")
                self.left_main_start_frame_downward_item_image_input_1_label_image.place(relx=0, rely=0,relwidth=0.5,relheight=0.5)

                self.add_bill_button.append(Button(self.left_main_start_frame_downward_item_image_input_1_frame,image=self.add_bill[i], bg=self.frame_color_white,cursor="hand2", borderwidth=0))
                self.add_bill_button[i].place(relx=0.5, rely=0,relwidth=0.5,relheight=0.5)



                self.left_main_start_frame_downward_item_image_input_1_label_name = Label(self.left_main_start_frame_downward_item_image_input_1_frame,font=("Cascadia Mono",9),fg=self.text_color_dack, text=self.all_name[i][0],bg=self.frame_color_white,anchor=W,cursor="hand2")
                self.left_main_start_frame_downward_item_image_input_1_label_name.place(relx=0, rely=0.5,relwidth=1, relheight=0.25)

                self.left_main_start_frame_downward_item_image_input_1_label_price = Label(self.left_main_start_frame_downward_item_image_input_1_frame,font=("Cascadia Mono",11),fg=self.text_color_dack, text="Rs "+f"{self.all_price[i][0]}", bg=self.frame_color_white,anchor=W,cursor="hand2")
                self.left_main_start_frame_downward_item_image_input_1_label_price.place(relx=0, rely=0.75,relwidth=1, relheight=0.25)
                self.image_count+=1

        self.bill_item()


    def bill_item(self):
        self.total = 0
        self.total_all = self.total
        self.b0 = 0
        self.b1 = 0
        self.b2 = 0
        self.b3 = 0
        self.b4 = 0
        self.b5 = 0
        self.b6 = 0
        self.b7 = 0
        self.b8 = 0
        self.b9 = 0
        self.b10 = 0
        self.b11 = 0
        self.b12 = 0
        self.b13 = 0
        self.b14 = 0
        self.b15 = 0
        self.b16 = 0
        self.b17 = 0
        self.b18 = 0
        self.b19 = 0
        self.b20 = 0
        self.b21 = 0
        self.b22 = 0
        self.b23 = 0
        self.b24 = 0



        self.add_bill_button[0].bind('<Button-1>', self.l1)
        self.add_bill_button[1].bind('<Button-1>', self.l2)
        self.add_bill_button[2].bind('<Button-1>', self.l3)
        self.add_bill_button[3].bind('<Button-1>', self.l4)
        self.add_bill_button[4].bind('<Button-1>', self.l5)
        self.add_bill_button[5].bind('<Button-1>', self.l6)
        self.add_bill_button[6].bind('<Button-1>', self.l7)
        self.add_bill_button[7].bind('<Button-1>', self.l8)
        self.add_bill_button[8].bind('<Button-1>', self.l9)
        self.add_bill_button[9].bind('<Button-1>', self.l10)
        self.add_bill_button[10].bind('<Button-1>', self.l11)
        self.add_bill_button[11].bind('<Button-1>', self.l12)
        self.add_bill_button[12].bind('<Button-1>', self.l13)
        self.add_bill_button[13].bind('<Button-1>', self.l14)
        self.add_bill_button[14].bind('<Button-1>', self.l15)
        self.add_bill_button[15].bind('<Button-1>', self.l16)
        self.add_bill_button[16].bind('<Button-1>', self.l17)
        self.add_bill_button[17].bind('<Button-1>', self.l18)
        self.add_bill_button[18].bind('<Button-1>', self.l19)
        self.add_bill_button[19].bind('<Button-1>', self.l20)
        self.add_bill_button[20].bind('<Button-1>', self.l21)
        self.add_bill_button[21].bind('<Button-1>', self.l22)
        self.add_bill_button[22].bind('<Button-1>', self.l23)
        self.add_bill_button[23].bind('<Button-1>', self.l24)
        self.add_bill_button[24].bind('<Button-1>', self.l25)

    def l1(self,e):
           print(self.all_name[0][0])
           print(self.all_price[0][0])
           self.total_all = self.all_price[0][0]
           self.b0 = self.total_all
           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[0][0]}"+"\t\t\t"+f"Rs  {self.all_price[0][0]}"+"\t\t\t1"+"\n")

    def l2(self,e):
           print(self.all_name[1][0])
           print(self.all_price[1][0])
           self.total_all = self.all_price[1][0]
           self.b1 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[1][0]}"+"\t\t\t"+f"Rs  {self.all_price[1][0]}"+"\t\t\t1"+"\n")

    def l3(self,e):
           print(self.all_name[2][0])
           print(self.all_price[2][0])
           self.total_all = self.all_price[2][0]
           self.b2 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[2][0]}"+"\t\t\t"+f"Rs  {self.all_price[2][0]}"+"\t\t\t1"+"\n")

    def l4(self,e):
           print(self.all_name[3][0])
           print(self.all_price[3][0])
           self.total_all = self.all_price[3][0]
           self.b3 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[3][0]}"+"\t\t\t"+f"Rs  {self.all_price[3][0]}"+"\t\t\t1"+"\n")

    def l5(self,e):
           print(self.all_name[4][0])
           print(self.all_price[4][0])
           self.total_all = self.all_price[4][0]
           self.b4 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[4][0]}"+"\t\t\t"+f"Rs  {self.all_price[4][0]}"+"\t\t\t1"+"\n")

    def l6(self,e):
           print(self.all_name[5][0])
           print(self.all_price[5][0])
           self.total_all = self.all_price[5][0]
           self.b5 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[5][0]}"+"\t\t\t"+f"Rs  {self.all_price[5][0]}"+"\t\t\t1"+"\n")

    def l7(self,e):
           print(self.all_name[6][0])
           print(self.all_price[6][0])
           self.total_all = self.all_price[6][0]
           self.b6 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[6][0]}"+"\t\t\t"+f"Rs  {self.all_price[6][0]}"+"\t\t\t1"+"\n")

    def l8(self,e):
           print(self.all_name[7][0])
           print(self.all_price[7][0])
           self.total_all = self.all_price[7][0]
           self.b7 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[7][0]}"+"\t\t\t"+f"Rs  {self.all_price[7][0]}"+"\t\t\t1"+"\n")

    def l9(self,e):
           print(self.all_name[8][0])
           print(self.all_price[8][0])
           self.total_all = self.all_price[8][0]
           self.b8 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[8][0]}"+"\t\t\t"+f"Rs  {self.all_price[8][0]}"+"\t\t\t1"+"\n")

    def l10(self,e):
           print(self.all_name[9][0])
           print(self.all_price[9][0])
           self.total_all = self.all_price[9][0]
           self.b9 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[9][0]}"+"\t\t\t"+f"Rs  {self.all_price[9][0]}"+"\t\t\t1"+"\n")

    def l11(self,e):
           print(self.all_name[10][0])
           print(self.all_price[10][0])
           self.total_all = self.all_price[10][0]
           self.b10 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[10][0]}"+"\t\t\t"+f"Rs  {self.all_price[10][0]}"+"\t\t\t1"+"\n")

    def l12(self,e):
           print(self.all_name[11][0])
           print(self.all_price[11][0])
           self.total_all = self.all_price[11][0]
           self.b11 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[11][0]}"+"\t\t\t"+f"Rs  {self.all_price[11][0]}"+"\t\t\t1"+"\n")

    def l13(self,e):
           print(self.all_name[12][0])
           print(self.all_price[12][0])
           self.total_all = self.all_price[12][0]
           self.b12 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[12][0]}"+"\t\t\t"+f"Rs  {self.all_price[12][0]}"+"\t\t\t1"+"\n")

    def l14(self,e):
           print(self.all_name[13][0])
           print(self.all_price[13][0])
           self.total_all = self.all_price[13][0]
           self.b13 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[13][0]}"+"\t\t\t"+f"Rs  {self.all_price[13][0]}"+"\t\t\t1"+"\n")

    def l15(self,e):
           print(self.all_name[14][0])
           print(self.all_price[14][0])
           self.total_all = self.all_price[14][0]
           self.b14 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[14][0]}"+"\t\t\t"+f"Rs  {self.all_price[14][0]}"+"\t\t\t1"+"\n")


    def l16(self,e):
           print(self.all_name[15][0])
           print(self.all_price[15][0])
           self.total_all = self.all_price[15][0]
           self.b15 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[15][0]}"+"\t\t\t"+f"Rs  {self.all_price[15][0]}"+"\t\t\t1"+"\n")

    def l17(self,e):
           print(self.all_name[16][0])
           print(self.all_price[16][0])
           self.total_all = self.all_price[16][0]
           self.b16 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[16][0]}"+"\t\t\t"+f"Rs  {self.all_price[16][0]}"+"\t\t\t1"+"\n")

    def l18(self,e):
           print(self.all_name[17][0])
           print(self.all_price[17][0])
           self.total_all = self.all_price[17][0]
           self.b17 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[17][0]}"+"\t\t\t"+f"Rs  {self.all_price[17][0]}"+"\t\t\t1"+"\n")

    def l19(self,e):
           print(self.all_name[18][0])
           print(self.all_price[18][0])
           self.total_all = self.all_price[18][0]
           self.b18 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[18][0]}"+"\t\t\t"+f"Rs  {self.all_price[18][0]}"+"\t\t\t1"+"\n")

    def l20(self,e):
           print(self.all_name[19][0])
           print(self.all_price[19][0])
           self.total_all = self.all_price[19][0]
           self.b19 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[19][0]}"+"\t\t\t"+f"Rs  {self.all_price[19][0]}"+"\t\t\t1"+"\n")

    def l21(self,e):
           print(self.all_name[20][0])
           print(self.all_price[20][0])
           self.total_all = self.all_price[20][0]
           self.b20 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[20][0]}"+"\t\t\t"+f"Rs  {self.all_price[20][0]}"+"\t\t\t1"+"\n")

    def l22(self,e):
           print(self.all_name[21][0])
           print(self.all_price[21][0])
           self.total_all = self.all_price[21][0]
           self.b21 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[21][0]}"+"\t\t\t"+f"Rs  {self.all_price[21][0]}"+"\t\t\t1"+"\n")

    def l23(self,e):
           print(self.all_name[22][0])
           print(self.all_price[22][0])
           self.total_all = self.all_price[22][0]
           self.b22 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[22][0]}"+"\t\t\t"+f"Rs  {self.all_price[22][0]}"+"\t\t\t1"+"\n")

    def l24(self,e):
           print(self.all_name[23][0])
           print(self.all_price[23][0])
           self.total_all = self.all_price[23][0]
           self.b23 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[23][0]}"+"\t\t\t"+f"Rs  {self.all_price[23][0]}"+"\t\t\t1"+"\n")


    def l25(self,e):
           print(self.all_name[24][0])
           print(self.all_price[24][0])
           self.total_all = self.all_price[24][0]
           self.b24 = self.total_all

           self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\t"+f"{self.all_name[24][0]}"+"\t\t\t"+f"Rs  {self.all_price[24][0]}"+"\t\t\t1"+"\n")



    def right_start_billing_system(self):
        #===================== right_main_start_frame ===============================================================
        self.right_main_start_frame = Frame(self.main_start_frame,bg=self.main_billing_background_color)
        self.right_main_start_frame.place(relx=0.601,rely=0.08,relwidth=0.399,relheight=0.92)
        self.right_start_billing_system_top()
        self.right_mid_start_billing_system_top()

    def right_start_billing_system_top(self):
        #===================== right_main_start_frame_top ===============================================================
        self.right_main_start_frame_top = Frame(self.right_main_start_frame,bg=self.back_up)
        self.right_main_start_frame_top.place(relx=0,rely=0,relwidth=1,relheight=0.1)

        #===================== right_main_start_frame_top_part1 ==============================================================
        self.right_main_start_frame_top_part1_frame = Frame(self.right_main_start_frame_top,bg=self.back_up)
        self.right_main_start_frame_top_part1_frame.place(relx=0,rely=0,relwidth=0.5,relheight=1)

        self.right_main_start_frame_top_part1_image_1 = Image.open("table.png")
        self.right_main_start_frame_top_part1_image_2 = self.right_main_start_frame_top_part1_image_1.resize((30,30))
        self.right_main_start_frame_top_part1_image_3 = ImageTk.PhotoImage(self.right_main_start_frame_top_part1_image_2)

        self.right_main_start_frame_top_part1_image = Label(self.right_main_start_frame_top_part1_frame, image=self.right_main_start_frame_top_part1_image_3, bg=self.back_up,font=("Comic Sans MS",10),fg=self.text_right_top)
        self.right_main_start_frame_top_part1_image.place(relx=0, rely=0, relwidth=1, relheight=0.7)

        self.right_main_start_frame_top_part1_Label = Label(self.right_main_start_frame_top_part1_frame,text="Table",bg=self.back_up,font=("Comic Sans MS",12),fg=self.text_color_white)
        self.right_main_start_frame_top_part1_Label.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)



        #===================== right_main_start_frame_top_part2 ===============================================================
        self.right_main_start_frame_top_part2_frame = Frame(self.right_main_start_frame_top,bg=self.back_up)
        self.right_main_start_frame_top_part2_frame.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)

        self.right_main_start_frame_top_part2_image_1 = Image.open("cat.png")
        self.right_main_start_frame_top_part2_image_2 = self.right_main_start_frame_top_part2_image_1.resize((30,30))
        self.right_main_start_frame_top_part2_image_3 = ImageTk.PhotoImage(self.right_main_start_frame_top_part2_image_2)

        self.right_main_start_frame_top_part2_image = Label(self.right_main_start_frame_top_part2_frame, image=self.right_main_start_frame_top_part2_image_3, bg=self.back_up,font=("Comic Sans MS",10),fg=self.text_right_top)
        self.right_main_start_frame_top_part2_image.place(relx=0, rely=0, relwidth=1, relheight=0.7)

        self.right_main_start_frame_top_part2_Label = Label(self.right_main_start_frame_top_part2_frame,text="order", bg=self.back_up,font=("Comic Sans MS",12),fg=self.text_color_white)
        self.right_main_start_frame_top_part2_Label.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)


    def right_mid_start_billing_system_top(self):
        #===================== right_main_start_frame_top ===============================================================
        self.right_mid_main_start_frame_top = Frame(self.right_main_start_frame,bg=self.frame_color_white)
        self.right_mid_main_start_frame_top.place(relx=0,rely=0.1,relwidth=1,relheight=0.78)


        # ===================== right_main_start_frame_top_text_frame_scroll ===============================================================
        self.right_mid_main_start_frame_top_text_frame_scroll = Frame(self.right_mid_main_start_frame_top, bg=self.frame_color_white)
        self.right_mid_main_start_frame_top_text_frame_scroll.pack(side=RIGHT,fill=Y)

        #===================== right_main_start_frame_top_text_frame ===============================================================
        self.right_mid_main_start_frame_top_text_frame = Text(self.right_mid_main_start_frame_top,yscrollcommand=self.right_mid_main_start_frame_top_text_frame_scroll,bg=self.frame_color_white)
        self.right_mid_main_start_frame_top_text_frame.place(relx=0,rely=0,relwidth=0.98,relheight=1)

        self.bill_number = ''.join([str(random.randint(0, 9)) for i in range(4)])
        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t#########################################################\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END, f"\t\tBill Number:\t\t\t{self.bill_number}\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END, f"\t\tCustomer Name:\t\t\t\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END, f"\t\tCustomer Number:\t\t\t\n")

        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t###############################################################\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t\tItem Name\t\t\tItem Price\t\t\tQtn.\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t###############################################################\n")






    def right_end_start_billing_system_top(self):
        #===================== right_main_start_frame_top ===============================================================
        self.right_end_main_start_frame_top = Frame(self.right_main_start_frame,bg=self.main_billing_background_color)
        self.right_end_main_start_frame_top.place(relx=0,rely=0.78,relwidth=1,relheight=0.25)

        self.right_end_main_start_frame_top_entry_la = Label(self.right_end_main_start_frame_top,text="Total",bg=self.main_billing_background_color,font=("Comic Sans MS",12),fg=self.text_color_dack,borderwidth=0,cursor="hand2")
        self.right_end_main_start_frame_top_entry_la.place(relx=0.05, rely=0.1, relwidth=0.2, relheight=0.25)


        self.right_end_main_start_frame_top_entry = Entry(self.right_end_main_start_frame_top,text=self.total,bg=self.frame_color_white,font=("Comic Sans MS",12),fg=self.text_color_dack,borderwidth=0,cursor="hand2",relief="groove")
        self.right_end_main_start_frame_top_entry.place(relx=0.25, rely=0.1, relwidth=0.3, relheight=0.25)


        self.right_end_main_start_frame_top_button_0 = Button(self.right_end_main_start_frame_top,text="Print",bg=self.frame_pur,activebackground=self.frame_pur,font=("Comic Sans MS",12),fg=self.text_color_white,borderwidth=0,cursor="hand2")
        self.right_end_main_start_frame_top_button_0.place(relx=0.667, rely=0.1, relwidth=0.3, relheight=0.25)
        self.right_end_main_start_frame_top_button_0.bind('<Button-1>',self.new_file)


        self.right_end_main_start_frame_top_button_1 = Button(self.right_end_main_start_frame_top,text="Total",bg=self.frame_yellow,activebackground=self.frame_yellow,font=("Comic Sans MS",12),fg=self.text_color_white,borderwidth=0,cursor="hand2")
        self.right_end_main_start_frame_top_button_1.place(relx=0.01, rely=0.5, relwidth=0.3, relheight=0.25)
        self.right_end_main_start_frame_top_button_1.bind('<Button-1>',self.tt)
        self.right_end_main_start_frame_top_entry.insert(0,"Rs  0.00")

        self.right_end_main_start_frame_top_button_2 = Button(self.right_end_main_start_frame_top,text="Genrate",bg=self.frame_green,activebackground=self.frame_green,font=("Comic Sans MS",12),fg=self.text_color_white,borderwidth=0,cursor="hand2")
        self.right_end_main_start_frame_top_button_2.place(relx=0.341, rely=0.5, relwidth=0.3, relheight=0.25)
        self.right_end_main_start_frame_top_button_2.bind('<Button-1>', self.gg)

        self.right_end_main_start_frame_top_button_3 = Button(self.right_end_main_start_frame_top,text="New",bg=self.frame_red,activebackground=self.frame_red,font=("Comic Sans MS",12),fg=self.text_color_white,borderwidth=0,cursor="hand2")
        self.right_end_main_start_frame_top_button_3.place(relx=0.667, rely=0.5, relwidth=0.3, relheight=0.25)
        self.right_end_main_start_frame_top_button_3.bind('<Button-1>',self.clear_button)

    def tt(self,e):
        self.t_all = self.b0+self.b1 + self.b2+self.b3 + self.b4+self.b5 + self.b6+self.b7 + self.b8+self.b9 + self.b10+self.b11 + self.b12+self.b13 + self.b14+self.b15 + self.b16+self.b17 + self.b18+self.b19 + self.b20+self.b21 + self.b22+self.b23 + self.b24
        self.right_end_main_start_frame_top_entry.delete(0,END)
        self.right_end_main_start_frame_top_entry.insert(0, "Rs  "+f"{self.t_all}")

    def gg(self,e):
        if len(self.left_main_start_frame_upward_label_ph_entry.get()) != 10 or self.left_main_start_frame_upward_label_ph_entry.get() == "" or self.left_main_start_frame_upward_label_name_entry.get() == "":
            messagebox.showerror("Customer detail","Please fill Customer detail carefully!")
        else:
            self.right_mid_main_start_frame_top_text_frame.delete(1.0,7.0)
            self.right_mid_main_start_frame_top_text_frame.insert(1.0,"\t#########################################################\n")
            self.right_mid_main_start_frame_top_text_frame.insert(2.0, f"\t\tBill Number:\t\t\t{self.bill_number}\n")
            self.right_mid_main_start_frame_top_text_frame.insert(3.0, f"\t\tCustomer Name:\t\t\t{self.left_main_start_frame_upward_label_name_entry.get()}\n")
            self.right_mid_main_start_frame_top_text_frame.insert(4.0, f"\t\tCustomer Number:\t\t\t{self.left_main_start_frame_upward_label_ph_entry.get()}\n")

            self.right_mid_main_start_frame_top_text_frame.insert(5.0,"\t###############################################################\n")
            self.right_mid_main_start_frame_top_text_frame.insert(6.0, "\t\tItem Name\t\t\tItem Price\t\t\tQtn.\n")
            self.right_mid_main_start_frame_top_text_frame.insert(7.0,"\t###############################################################\n")

            self.right_mid_main_start_frame_top_text_frame.insert(END,"\t###############################################################\n")
            self.right_mid_main_start_frame_top_text_frame.insert(END, "\t\tTotal\t\t\t" + f"Rs  {self.t_all}" + "\n")
            self.right_mid_main_start_frame_top_text_frame.insert(END,"\t###############################################################\n")


    def clear_button(self,e):
        self.right_mid_main_start_frame_top_text_frame.delete(1.0,END)
        self.left_main_start_frame_upward_label_name_entry.delete(0,END)
        self.left_main_start_frame_upward_label_ph_entry.delete(0,END)
        self.bill_number = ''.join([str(random.randint(0, 9)) for i in range(4)])
        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t#########################################################\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END, f"\t\tBill Number:\t\t\t{self.bill_number}\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END, f"\t\tCustomer Name:\t\t\t{self.left_main_start_frame_upward_label_name_entry.get()}\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END, f"\t\tCustomer Number:\t\t\t{self.left_main_start_frame_upward_label_ph_entry.get()}\n")

        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t##############################################################\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t\tItem Name\t\t\tItem Price\t\t\tQtn.\n")
        self.right_mid_main_start_frame_top_text_frame.insert(END,"\t###############################################################\n")
        self.right_end_main_start_frame_top_entry.delete(0,END)
        self.right_end_main_start_frame_top_entry.insert(0,"Rs  0.00")

    def new_file(self,e):
        self.file = open(f'bill_file\{self.bill_number}.txt', 'a')
        self.file.write(f"{self.right_mid_main_start_frame_top_text_frame.get(1.0,END)}")
        self.file.close()


b_root = Tk()
objective = main_billing_system(b_root)
mainloop()