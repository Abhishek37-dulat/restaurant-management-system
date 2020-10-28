from tkinter import *
from PIL import Image, ImageTk
import math
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.title("BILLING SYSTEM")
        self.root.iconbitmap('billing_1.ico')
        self.l_width = int(self.root.winfo_screenwidth())
        self.l_height = int(self.root.winfo_screenheight())
        self.l_x = int(0)
        self.l_y = int(0)
        self.root.geometry(f"{self.l_width}x{self.l_height}+{self.l_x}+{self.l_y}")
        self.root.overrideredirect(1)
        self.billing_software()

    def billing_software(self):
        self.main_backgound_color = "#F1F4F9"
        self.green = "#4150f5"
        self.white = "#ffffff"
        self.black = "#1B2026"
        self.line_1_color = "#D8521D"
        self.line_2_color = "#C9D81D"
        self.line_3_color = "#D81D70"
        self.line_4_color = "#02E131"
        self.line_5_color = "#00DEFF"
        self.Bath_Soap = IntVar()
        self.Face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.hair_gell = IntVar()
        self.body_loshan = IntVar()
        self.face_cream1 = IntVar()
        self.face_cream2 = IntVar()
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.coffee = IntVar()
        self.milk = IntVar()
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooi = IntVar()
        self.thumbs_up = IntVar()
        self.red_bull = IntVar()
        self.sprite = IntVar()
        self.pepsi = IntVar()
        self.fanta = IntVar()
        self.Ct = StringVar()
        self.Gt = StringVar()
        self.Dt = StringVar()
        self.Ctax = StringVar()
        self.Gtax = StringVar()
        self.Dtax = StringVar()
        self.name = StringVar()
        self.number = StringVar()
        self.bill = StringVar()


    #=========main_frame==============
        self.billing_software_main_frame = Frame(self.root, bg=self.main_backgound_color)
        self.billing_software_main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)


    # =========main_frame_heading==============
        self.billing_software_main_heading_frame = Frame(self.billing_software_main_frame, bg=self.main_backgound_color)
        self.billing_software_main_heading_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    #===================== main_background_image==================
        self.billing_software_main_heading_image_1 = Image.open("billing_top_1.png")
        self.billing_software_main_heading_image_2 = self.billing_software_main_heading_image_1.resize((self.l_width,120))
        self.billing_software_main_heading_image_3 = ImageTk.PhotoImage(self.billing_software_main_heading_image_2)

        self.billing_software_main_heading_image = Label(self.billing_software_main_heading_frame,bg=self.main_backgound_color,image=self.billing_software_main_heading_image_3)
        self.billing_software_main_heading_image.place(relx=0, rely=0, relwidth=1, relheight=1)
    #============== main_title =================
        self.billing_software_main_heading_image_frame_for_label = Frame(self.billing_software_main_heading_image,bg=self.green)
        self.billing_software_main_heading_image_frame_for_label.place(relx=0.2, rely=0.1, relwidth=0.3, relheight=0.7)

        self.billing_software_main_heading_image_Label_for_label = Label(self.billing_software_main_heading_image_frame_for_label, text="Billing System", fg=self.main_backgound_color,bg=self.green, font=("Kristen ITC",25))
        self.billing_software_main_heading_image_Label_for_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    #================== main_close ====================
        self.billing_software_main_heading_image_frame_for_close = Frame(self.billing_software_main_heading_image,bg=self.green)
        self.billing_software_main_heading_image_frame_for_close.place(relx=0.94, rely=0.1, relwidth=0.05, relheight=0.7)

        self.billing_software_main_heading_image_1_close = Image.open("close.png")
        self.billing_software_main_heading_image_2_close = self.billing_software_main_heading_image_1_close.resize((35,35))
        self.billing_software_main_heading_image_3_close = ImageTk.PhotoImage(self.billing_software_main_heading_image_2_close)

        self.billing_software_main_heading_image_label_close = Label(self.billing_software_main_heading_image_frame_for_close,bg=self.green,image=self.billing_software_main_heading_image_3_close,cursor="hand2")
        self.billing_software_main_heading_image_label_close.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        self.billing_software_main_heading_image_label_close.bind('<Button-1>', self.close_root)

    #==================================================== Customer_Details =====================================================================================
        self.billing_software_main_Customer_Details_frame = Frame(self.billing_software_main_frame, bg=self.main_backgound_color)
        self.billing_software_main_Customer_Details_frame.place(relx=0, rely=0.11, relwidth=1, relheight=0.15)
    #===================== main_Customer_Details_background_image==================
        self.billing_software_main_Customer_Details_image_1 = Image.open("billing_midd.png")
        self.billing_software_main_Customer_Details_image_2 = self.billing_software_main_Customer_Details_image_1.resize((self.l_width-10,120))
        self.billing_software_main_Customer_Details_image_3 = ImageTk.PhotoImage(self.billing_software_main_Customer_Details_image_2)

        self.billing_software_main_Customer_Details_image = Label(self.billing_software_main_Customer_Details_frame,bg=self.main_backgound_color,image=self.billing_software_main_Customer_Details_image_3)
        self.billing_software_main_Customer_Details_image.place(relx=0, rely=0, relwidth=1, relheight=1)
    #================== Customer_Details_title
        self.billing_software_main_Customer_Details_title_frame = Frame(self.billing_software_main_Customer_Details_image, bg=self.white)
        self.billing_software_main_Customer_Details_title_frame.place(relx=0.02, rely=0.07, relwidth=0.96, relheight=0.25)

        self.billing_software_main_Customer_Details_title_label = Label(self.billing_software_main_Customer_Details_title_frame,text="Customer Detail",fg=self.green,font=("Comic Sans MS",9,"bold"),anchor=W, bg=self.white)
        self.billing_software_main_Customer_Details_title_label.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.billing_software_main_Customer_Details_title_frame_line = Frame(self.billing_software_main_Customer_Details_image, bg=self.line_1_color)
        self.billing_software_main_Customer_Details_title_frame_line.place(relx=0.02, rely=0.32, relwidth=0.1, relheight=0.1)


    #=================  Customer_Details_title_sub
        self.billing_software_main_Customer_Details_title_frame_sub = Frame(self.billing_software_main_Customer_Details_image, bg=self.white)
        self.billing_software_main_Customer_Details_title_frame_sub.place(relx=0.02, rely=0.34, relwidth=0.96, relheight=0.58)
    #================================= customer_name

        self.billing_software_main_Customer_Details_title_frame_sub_customer_name = Frame(self.billing_software_main_Customer_Details_title_frame_sub, bg=self.white)
        self.billing_software_main_Customer_Details_title_frame_sub_customer_name.place(relx=0, rely=0, relwidth=0.27, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_name_label = Label(self.billing_software_main_Customer_Details_title_frame_sub_customer_name,text="Customer Name",fg=self.black,font=("Cascadia Code",11),anchor=W, bg=self.white)
        self.billing_software_main_Customer_Details_title_sub_customer_name_label.place(relx=0, rely=0, relwidth=0.4, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_name_entry = Entry(self.billing_software_main_Customer_Details_title_frame_sub_customer_name,textvariable=self.name, bg=self.white,fg=self.green,font=("Cascadia Code",11))
        self.billing_software_main_Customer_Details_title_sub_customer_name_entry.place(relx=0.4, rely=0.15, relwidth=0.6, relheight=0.7)

    #=============================== customer number
        self.billing_software_main_Customer_Details_title_frame_sub_customer_number = Frame(self.billing_software_main_Customer_Details_title_frame_sub, bg=self.white)
        self.billing_software_main_Customer_Details_title_frame_sub_customer_number.place(relx=0.27, rely=0, relwidth=0.27, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_number_label = Label(self.billing_software_main_Customer_Details_title_frame_sub_customer_number,text="Customer Number",fg=self.black,font=("Cascadia Code",11),anchor=CENTER, bg=self.white)
        self.billing_software_main_Customer_Details_title_sub_customer_number_label.place(relx=0, rely=0, relwidth=0.4, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_number_entry = Entry(self.billing_software_main_Customer_Details_title_frame_sub_customer_number,textvariable=self.number, bg=self.white,fg=self.green,font=("Cascadia Code",11))
        self.billing_software_main_Customer_Details_title_sub_customer_number_entry.place(relx=0.4, rely=0.15, relwidth=0.6, relheight=0.7)

    #============================= customer bill_number

        self.billing_software_main_Customer_Details_title_frame_sub_customer_bill_number = Frame(self.billing_software_main_Customer_Details_title_frame_sub, bg=self.white)
        self.billing_software_main_Customer_Details_title_frame_sub_customer_bill_number.place(relx=0.54, rely=0, relwidth=0.27, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_bill_number_label = Label(self.billing_software_main_Customer_Details_title_frame_sub_customer_bill_number,textvariable=self.bill,text="Bill Number",fg=self.black,font=("Cascadia Code",11),anchor=CENTER, bg=self.white)
        self.billing_software_main_Customer_Details_title_sub_customer_bill_number_label.place(relx=0, rely=0, relwidth=0.4, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_bill_number_entry = Entry(self.billing_software_main_Customer_Details_title_frame_sub_customer_bill_number, bg=self.white,fg=self.green,font=("Cascadia Code",11))
        self.billing_software_main_Customer_Details_title_sub_customer_bill_number_entry.place(relx=0.4, rely=0.15, relwidth=0.6, relheight=0.7)

    #============================ customer_search

        self.billing_software_main_Customer_Details_title_frame_sub_customer_search_button = Frame(self.billing_software_main_Customer_Details_title_frame_sub, bg=self.white)
        self.billing_software_main_Customer_Details_title_frame_sub_customer_search_button.place(relx=0.81, rely=0, relwidth=0.19, relheight=1)

        self.billing_software_main_Customer_Details_title_sub_customer_search_button_label = Button(self.billing_software_main_Customer_Details_title_frame_sub_customer_search_button,text="Search",bg=self.green,font=("Cascadia Code",11),anchor=CENTER, fg=self.white,cursor="hand2")
        self.billing_software_main_Customer_Details_title_sub_customer_search_button_label.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

    #====================================================================================================================================
    #======================================================================================= Middle_part =======================================
        self.billing_software_main_Middle_part_Details_frame = Frame(self.billing_software_main_frame, bg=self.main_backgound_color)
        self.billing_software_main_Middle_part_Details_frame.place(relx=0, rely=0.26, relwidth=1,relheight=0.6)

        #==================================================== Middle_part_Cosmetics =====================================================================================
        self.billing_software_main_Middle_part_Cosmetics_Details_frame = Frame(self.billing_software_main_Middle_part_Details_frame, bg=self.main_backgound_color)
        self.billing_software_main_Middle_part_Cosmetics_Details_frame.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        # ===================== main_Cosmetics_Details_background_image==================
        self.billing_software_main_Cosmetics_Details_image_1 = Image.open("vertical_box.png")
        self.billing_software_main_Cosmetics_Details_image_2 = self.billing_software_main_Cosmetics_Details_image_1.resize((380, 515))
        self.billing_software_main_Cosmetics_Details_image_3 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2)

        self.billing_software_main_Cosmetics_Details_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_frame,bg=self.main_backgound_color,image=self.billing_software_main_Cosmetics_Details_image_3)
        self.billing_software_main_Cosmetics_Details_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ================== Middle_part_Cosmetics_Details_title
        self.billing_software_main_Middle_part_Cosmetics_Details_title_frame = Frame(self.billing_software_main_Cosmetics_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_title_frame.place(relx=0.08, rely=0.01, relwidth=0.8,relheight=0.08)

        self.billing_software_main_Middle_part_Cosmetics_Details_title_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_title_frame, text="Cosmetics", fg=self.green,font=("Comic Sans MS", 11, "bold"), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_title_label.place(relx=0, rely=0, relwidth=1, relheight=0.9)

        self.billing_software_main_Middle_part_Cosmetics_Details_title_frame_line = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_title_frame, bg=self.line_2_color)
        self.billing_software_main_Middle_part_Cosmetics_Details_title_frame_line.place(relx=0, rely=0.9, relwidth=0.4,relheight=0.05)


        # ================== Middle_part_Cosmetics_Details_list
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame = Frame(self.billing_software_main_Cosmetics_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame.place(relx=0.03, rely=0.1, relwidth=0.93,relheight=0.85)

        #================== item 1
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1.place(relx=0, rely=0, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_1 = Image.open("bi_1.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_1 = self.billing_software_main_Cosmetics_Details_image_1_item_1.resize((40, 40))
        self.billing_software_main_Cosmetics_Details_image_3_item_1 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_1)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_2,text="Bath Soap",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_2, textvariable=self.Bath_Soap, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)




    #=========== item 2

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2.place(relx=0, rely=0.12, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_2 = Image.open("bi_2.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_2 = self.billing_software_main_Cosmetics_Details_image_1_item_2.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_2 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_2)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_2, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_2,text="Face Cream",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_2, bg=self.white, textvariable=self.Face_cream)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)





    #======================== item 3


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3.place(relx=0, rely=0.24, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_3 = Image.open("bi_3.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_3 = self.billing_software_main_Cosmetics_Details_image_1_item_3.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_3 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_3)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_3, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_2,text="Face wash",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_2, bg=self.white, textvariable=self.face_wash)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)

        # ======================== item 4

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4.place(relx=0, rely=0.36, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_4 = Image.open("bi_4.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_4 = self.billing_software_main_Cosmetics_Details_image_1_item_4.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_4 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_4)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_4, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_2,text="Hair Spray",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_2, textvariable=self.hair_spray)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)

        # ======================== item 5

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5.place(relx=0, rely=0.48, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_5 = Image.open("bi_5.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_5 = self.billing_software_main_Cosmetics_Details_image_1_item_5.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_5 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_5)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_5, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_2,text="Hair Gell",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_2, bg=self.white, textvariable=self.hair_gell)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)



        # ======================== item 6

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6.place(relx=0, rely=0.60, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_6 = Image.open("bi_6.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_6 = self.billing_software_main_Cosmetics_Details_image_1_item_6.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_6 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_6)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_6, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_2,text="Body Loshan",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_2, bg=self.white, textvariable=self.body_loshan)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)



        # ======================== item 7

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7.place(relx=0, rely=0.72, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_7 = Image.open("pizza_1.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_7 = self.billing_software_main_Cosmetics_Details_image_1_item_7.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_7 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_7)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_7, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_2,text="Face Cream1",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_2, bg=self.white, textvariable=self.face_cream1)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)





        # ======================== item 8

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8.place(relx=0, rely=0.84, relwidth=1,relheight=0.12)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1.place(relx=0, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_1 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_1.place(relx=0, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Cosmetics_Details_image_1_item_8 = Image.open("pizza_1.png")
        self.billing_software_main_Cosmetics_Details_image_2_item_8 = self.billing_software_main_Cosmetics_Details_image_1_item_8.resize((30, 30))
        self.billing_software_main_Cosmetics_Details_image_3_item_8 = ImageTk.PhotoImage(self.billing_software_main_Cosmetics_Details_image_2_item_8)


        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_1_image = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_1,image=self.billing_software_main_Cosmetics_Details_image_3_item_8, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_1_image.place(relx=0, rely=0, relwidth=1,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_2.place(relx=0.4, rely=0, relwidth=0.6,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_2_label = Label(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_2,text="Face Cream2",font=("Cascadia Code SemiBold",9),anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_1_2_label.place(relx=0, rely=0, relwidth=1,relheight=1)



        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_2 = Frame(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8, bg=self.white)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_2.place(relx=0.6, rely=0, relwidth=0.4,relheight=1)

        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_2_entry = Entry(self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_2, bg=self.white, textvariable=self.face_cream2)
        self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_2_entry.place(relx=0.05, rely=0.1, relwidth=0.9,relheight=0.8)












        #==================================================== Middle_part_Grocery =============================================================================================
        #=======================================================================================================================================================================
        self.billing_software_main_Middle_part_Grocery_Details_frame = Frame(self.billing_software_main_Middle_part_Details_frame, bg=self.main_backgound_color)
        self.billing_software_main_Middle_part_Grocery_Details_frame.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)

        # ===================== main_Grocery_Details_background_image==================
        self.billing_software_main_Grocery_Details_image_1 = Image.open("vertical_box.png")
        self.billing_software_main_Grocery_Details_image_2 = self.billing_software_main_Grocery_Details_image_1.resize((380, 515))
        self.billing_software_main_Grocery_Details_image_3 = ImageTk.PhotoImage(self.billing_software_main_Grocery_Details_image_2)

        self.billing_software_main_Grocery_Details_image = Label(self.billing_software_main_Middle_part_Grocery_Details_frame,bg=self.main_backgound_color,image=self.billing_software_main_Cosmetics_Details_image_3)
        self.billing_software_main_Grocery_Details_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ================== Middle_part_Cosmetics_Details_title
        self.billing_software_main_Middle_part_Grocery_Details_title_frame = Frame(
            self.billing_software_main_Grocery_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_title_frame.place(relx=0.08, rely=0.01, relwidth=0.8,
                                                                                   relheight=0.08)

        self.billing_software_main_Middle_part_Grocery_Details_title_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_title_frame, text="Cold Drinks", fg=self.green,
            font=("Comic Sans MS", 11, "bold"), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_title_label.place(relx=0, rely=0, relwidth=1,
                                                                                   relheight=0.9)

        self.billing_software_main_Middle_part_Grocery_Details_title_frame_line = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_title_frame, bg=self.line_3_color)
        self.billing_software_main_Middle_part_Grocery_Details_title_frame_line.place(relx=0, rely=0.9, relwidth=0.4,
                                                                                        relheight=0.05)

        # ================== Middle_part_Cosmetics_Details_list
        self.billing_software_main_Middle_part_Grocery_Details_list_frame = Frame(
            self.billing_software_main_Grocery_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame.place(relx=0.03, rely=0.1, relwidth=0.93,
                                                                                  relheight=0.85)

        # ================== item 1
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1.place(relx=0, rely=0, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_1 = Image.open("sss_1.png")
        self.billing_software_main_Grocery_Details_image_2_item_1 = self.billing_software_main_Grocery_Details_image_1_item_1.resize(
            (40, 40))
        self.billing_software_main_Grocery_Details_image_3_item_1 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_2, text="Rice",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_2, bg=self.white, textvariable=self.rice)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # =========== item 2

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2.place(relx=0, rely=0.12, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_2 = Image.open("sss_2.png")
        self.billing_software_main_Grocery_Details_image_2_item_2 = self.billing_software_main_Grocery_Details_image_1_item_2.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_2 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_2)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_2, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_2, text="Food Oil",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_2, bg=self.white, textvariable=self.food_oil)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 3

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3.place(relx=0, rely=0.24, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_3 = Image.open("sss_3.png")
        self.billing_software_main_Grocery_Details_image_2_item_3 = self.billing_software_main_Grocery_Details_image_1_item_3.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_3 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_3)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_3, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_2, text="Daal",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_2, bg=self.white, textvariable=self.daal)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 4

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4.place(relx=0, rely=0.36, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_4 = Image.open("sss_4.png")
        self.billing_software_main_Grocery_Details_image_2_item_4 = self.billing_software_main_Grocery_Details_image_1_item_4.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_4 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_4)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_4, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_2, text="Wheat",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_2, textvariable=self.wheat)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 5

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5.place(relx=0, rely=0.48, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_5 = Image.open("sss_5.png")
        self.billing_software_main_Grocery_Details_image_2_item_5 = self.billing_software_main_Grocery_Details_image_1_item_5.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_5 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_5)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_5, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_2, text="Sugar",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_2, bg=self.white, textvariable=self.sugar)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 6

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6.place(relx=0, rely=0.60, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_6 = Image.open("sss_6.png")
        self.billing_software_main_Grocery_Details_image_2_item_6 = self.billing_software_main_Grocery_Details_image_1_item_6.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_6 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_6)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_6, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_2, text="Tea",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_2, bg=self.white, textvariable=self.tea)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 7

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7.place(relx=0, rely=0.72, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_7 = Image.open("sss_7.png")
        self.billing_software_main_Grocery_Details_image_2_item_7 = self.billing_software_main_Grocery_Details_image_1_item_7.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_7 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_7)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_7, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_2, text="Coffee",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_2, bg=self.white, textvariable=self.coffee)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 8

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8.place(relx=0, rely=0.84, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_1 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_Grocery_Details_image_1_item_8 = Image.open("sss_8.png")
        self.billing_software_main_Grocery_Details_image_2_item_8 = self.billing_software_main_Grocery_Details_image_1_item_8.resize(
            (30, 30))
        self.billing_software_main_Grocery_Details_image_3_item_8 = ImageTk.PhotoImage(
            self.billing_software_main_Grocery_Details_image_2_item_8)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_1_image = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_1,
            image=self.billing_software_main_Grocery_Details_image_3_item_8, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_2_label = Label(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_2, text="Milk",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_2 = Frame(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8, bg=self.white)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_2_entry = Entry(
            self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_2, bg=self.white, textvariable=self.milk)
        self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        #==================================================== Middle_part_cold_drink =====================================================================================
        #===============================================================================================================================================================
        self.billing_software_main_Middle_part_cold_drink_Details_frame = Frame(self.billing_software_main_Middle_part_Details_frame, bg=self.main_backgound_color)
        self.billing_software_main_Middle_part_cold_drink_Details_frame.place(relx=0.5, rely=0, relwidth=0.25, relheight=1)

        # ===================== main_Grocery_Details_background_image==================
        self.billing_software_main_cold_drink_Details_image_1 = Image.open("vertical_box.png")
        self.billing_software_main_cold_drink_Details_image_2 = self.billing_software_main_cold_drink_Details_image_1.resize((380, 515))
        self.billing_software_main_cold_drink_Details_image_3 = ImageTk.PhotoImage(self.billing_software_main_cold_drink_Details_image_2)

        self.billing_software_main_cold_drink_Details_image = Label(self.billing_software_main_Middle_part_cold_drink_Details_frame,bg=self.main_backgound_color,image=self.billing_software_main_Cosmetics_Details_image_3)
        self.billing_software_main_cold_drink_Details_image.place(relx=0, rely=0, relwidth=1, relheight=1)


        # ================== Middle_part_cold_drink_Details_title
        self.billing_software_main_Middle_part_cold_drink_Details_title_frame = Frame(
            self.billing_software_main_cold_drink_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_title_frame.place(relx=0.08, rely=0.01, relwidth=0.8,
                                                                                   relheight=0.08)

        self.billing_software_main_Middle_part_cold_drink_Details_title_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_title_frame, text="Cold Drinks", fg=self.green,
            font=("Comic Sans MS", 11, "bold"), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_title_label.place(relx=0, rely=0, relwidth=1,
                                                                                   relheight=0.9)

        self.billing_software_main_Middle_part_cold_drink_Details_title_frame_line = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_title_frame, bg=self.line_4_color)
        self.billing_software_main_Middle_part_cold_drink_Details_title_frame_line.place(relx=0, rely=0.9, relwidth=0.4,
                                                                                        relheight=0.05)

        # ================== Middle_part_Cosmetics_Details_list
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame = Frame(
            self.billing_software_main_cold_drink_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame.place(relx=0.03, rely=0.1, relwidth=0.93,
                                                                                  relheight=0.85)

        # ================== item 1
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1.place(relx=0, rely=0, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_1 = Image.open("iii_1.png")
        self.billing_software_main_cold_drink_Details_image_2_item_1 = self.billing_software_main_cold_drink_Details_image_1_item_1.resize(
            (40, 40))
        self.billing_software_main_cold_drink_Details_image_3_item_1 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_2, text="Maza",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_2, bg=self.white, textvariable=self.maza)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # =========== item 2

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2.place(relx=0, rely=0.12, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_2 = Image.open("iii_2.png")
        self.billing_software_main_cold_drink_Details_image_2_item_2 = self.billing_software_main_cold_drink_Details_image_1_item_2.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_2 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_2)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_2, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_2, text="Cock",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_2, bg=self.white, textvariable=self.cock)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 3

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3.place(relx=0, rely=0.24, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_3 = Image.open("iii_3.png")
        self.billing_software_main_cold_drink_Details_image_2_item_3 = self.billing_software_main_cold_drink_Details_image_1_item_3.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_3 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_3)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_3, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_2, text="Frooti",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_2, bg=self.white, textvariable=self.frooi)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 4

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4.place(relx=0, rely=0.36, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_4 = Image.open("iii_4.png")
        self.billing_software_main_cold_drink_Details_image_2_item_4 = self.billing_software_main_cold_drink_Details_image_1_item_4.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_4 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_4)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_4, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_2, text="Thumbs Up",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_2, textvariable=self.thumbs_up)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 5

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5.place(relx=0, rely=0.48, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_5 = Image.open("iii_5.png")
        self.billing_software_main_cold_drink_Details_image_2_item_5 = self.billing_software_main_cold_drink_Details_image_1_item_5.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_5 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_5)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_5, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_2, text="Red Bull",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_2, bg=self.white, textvariable=self.red_bull)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 6

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6.place(relx=0, rely=0.60, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_6 = Image.open("iii_6.png")
        self.billing_software_main_cold_drink_Details_image_2_item_6 = self.billing_software_main_cold_drink_Details_image_1_item_6.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_6 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_6)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_6, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_2, text="Sprite",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_2, bg=self.white, textvariable=self.sprite)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 7

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7.place(relx=0, rely=0.72, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_7 = Image.open("iii_7.png")
        self.billing_software_main_cold_drink_Details_image_2_item_7 = self.billing_software_main_cold_drink_Details_image_1_item_7.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_7 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_7)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_7, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_2, text="Pepsi",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_2, bg=self.white, textvariable=self.pepsi)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)

        # ======================== item 8

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8.place(relx=0, rely=0.84, relwidth=1,
                                                                                         relheight=0.12)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1.place(relx=0, rely=0, relwidth=0.6,
                                                                                           relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_1 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_1.place(relx=0, rely=0,
                                                                                             relwidth=0.4, relheight=1)

        self.billing_software_main_cold_drink_Details_image_1_item_8 = Image.open("iii_8.png")
        self.billing_software_main_cold_drink_Details_image_2_item_8 = self.billing_software_main_cold_drink_Details_image_1_item_8.resize(
            (30, 30))
        self.billing_software_main_cold_drink_Details_image_3_item_8 = ImageTk.PhotoImage(
            self.billing_software_main_cold_drink_Details_image_2_item_8)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_1_image = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_1,
            image=self.billing_software_main_cold_drink_Details_image_3_item_8, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_1_image.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_2.place(relx=0.4, rely=0,
                                                                                             relwidth=0.6, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_2_label = Label(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_2, text="Fanta",
            font=("Cascadia Code SemiBold", 9), anchor=W, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_1_2_label.place(relx=0, rely=0,
                                                                                                   relwidth=1,
                                                                                                   relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_2 = Frame(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8, bg=self.white)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_2.place(relx=0.6, rely=0,
                                                                                           relwidth=0.4, relheight=1)

        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_2_entry = Entry(
            self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_2, bg=self.white, textvariable=self.fanta)
        self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_2_entry.place(relx=0.05, rely=0.1,
                                                                                                 relwidth=0.9,
                                                                                                 relheight=0.8)






























        #==================================================== Middle_part_bill_area =====================================================================================
        self.billing_software_main_Middle_part_bill_area_Details_frame = Frame(self.billing_software_main_Middle_part_Details_frame, bg=self.main_backgound_color)
        self.billing_software_main_Middle_part_bill_area_Details_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

        # ===================== main_Grocery_Details_background_image==================
        self.billing_software_main_bill_area_Details_image_1 = Image.open("vertical_box.png")
        self.billing_software_main_bill_area_Details_image_2 = self.billing_software_main_bill_area_Details_image_1.resize((380, 515))
        self.billing_software_main_bill_area_Details_image_3 = ImageTk.PhotoImage(self.billing_software_main_bill_area_Details_image_2)

        self.billing_software_main_bill_area_Details_image = Label(self.billing_software_main_Middle_part_bill_area_Details_frame,bg=self.main_backgound_color,image=self.billing_software_main_Cosmetics_Details_image_3)
        self.billing_software_main_bill_area_Details_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.billing_software_main_Middle_part_bill_area_Details_frame_f1 = Frame(self.billing_software_main_bill_area_Details_image, bg=self.white)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)


        self.billing_software_main_Middle_part_bill_area_Details_frame_f2 = Frame(self.billing_software_main_Middle_part_bill_area_Details_frame_f1, bg=self.white)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f2.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.billing_software_main_Middle_part_bill_area_Details_frame_f2_1 = Label(self.billing_software_main_Middle_part_bill_area_Details_frame_f2,text="Bill Area",font=("Cascadia Code SemiBold", 13),fg=self.white, bg=self.green)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f2_1.place(relx=0, rely=0, relwidth=1, relheight=1)



        self.billing_software_main_Middle_part_bill_area_Details_frame_f3 = Frame(self.billing_software_main_Middle_part_bill_area_Details_frame_f1, bg=self.white)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f3.place(relx=0, rely=0.125, relwidth=1, relheight=0.85)

        self.billing_software_main_Middle_part_bill_area_Details_frame_f3_1 = Label(self.billing_software_main_Middle_part_bill_area_Details_frame_f3,text="########## Welcome to Billing System ##########",bg=self.white, fg=self.black)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f3_1.place(relx=0, rely=0, relwidth=1, relheight=0.05)

        self.billing_software_main_Middle_part_bill_area_Details_frame_f3_2 = Label(self.billing_software_main_Middle_part_bill_area_Details_frame_f3,text="Name: ",anchor=W,bg=self.white, fg=self.black)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f3_2.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)

        self.billing_software_main_Middle_part_bill_area_Details_frame_f3_3 = Label(self.billing_software_main_Middle_part_bill_area_Details_frame_f3,text="Number: ",anchor=W,bg=self.white, fg=self.black)
        self.billing_software_main_Middle_part_bill_area_Details_frame_f3_3.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)

















    #====================================================================================================================================
    #======================================================================================= Buttom_part =======================================
        self.billing_software_main_Buttom_part_Details_frame = Frame(self.billing_software_main_frame, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_Details_frame.place(relx=0, rely=0.86, relwidth=1,relheight=0.14)

        #==================================================== _Buttom_part_1 =====================================================================================
        self.billing_software_main_Buttom_part_1_frame = Frame(self.billing_software_main_Buttom_part_Details_frame, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_1_frame.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_1_frame_1 = Frame(self.billing_software_main_Buttom_part_1_frame, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_1_frame_1.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        self.billing_software_main_Buttom_part_1_frame_1_image_1 = Image.open("33.png")
        self.billing_software_main_Buttom_part_1_frame_1_image_2 = self.billing_software_main_Buttom_part_1_frame_1_image_1.resize((425,110))
        self.billing_software_main_Buttom_part_1_frame_1_image_3 = ImageTk.PhotoImage(self.billing_software_main_Buttom_part_1_frame_1_image_2)

        self.billing_software_main_Buttom_part_1_frame_1_image = Label(self.billing_software_main_Buttom_part_1_frame_1,image=self.billing_software_main_Buttom_part_1_frame_1_image_3, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_1_frame_1_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.billing_software_main_Buttom_part_1_frame_2 = Frame(self.billing_software_main_Buttom_part_1_frame_1_image, bg=self.white)
        self.billing_software_main_Buttom_part_1_frame_2.place(relx=0.05, rely=0.075, relwidth=0.9, relheight=0.85)

        #================
        self.billing_software_main_Buttom_part_1_frame_2_1 = Frame(self.billing_software_main_Buttom_part_1_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_1_frame_2_1.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        self.billing_software_main_Buttom_part_1_frame_2_1_label = Label(self.billing_software_main_Buttom_part_1_frame_2_1,text="Bill Menu",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_1_frame_2_1_label.place(relx=0, rely=0, relwidth=1, relheight=0.9)

        self.billing_software_main_Buttom_part_1_frame_2_1_label_li = Frame(self.billing_software_main_Buttom_part_1_frame_2_1,bg=self.line_5_color)
        self.billing_software_main_Buttom_part_1_frame_2_1_label_li.place(relx=0, rely=0.9, relwidth=0.4, relheight=0.1)



        #==================

        self.billing_software_main_Buttom_part_1_frame_2_2 = Frame(self.billing_software_main_Buttom_part_1_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_1_frame_2_2.place(relx=0, rely=0.15, relwidth=1, relheight=0.283)

        self.billing_software_main_Buttom_part_1_frame_2_2_label = Label(self.billing_software_main_Buttom_part_1_frame_2_2,text="Total Cosmetic Price",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_1_frame_2_2_label.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_1_frame_2_2_entry = Entry(self.billing_software_main_Buttom_part_1_frame_2_2,fg=self.green,font=("Comic Sans MS", 9, "bold"),textvariable=self.Ct)
        self.billing_software_main_Buttom_part_1_frame_2_2_entry.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)


        #==================

        self.billing_software_main_Buttom_part_1_frame_2_3 = Frame(self.billing_software_main_Buttom_part_1_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_1_frame_2_3.place(relx=0, rely=0.41, relwidth=1, relheight=0.283)

        self.billing_software_main_Buttom_part_1_frame_2_3_label = Label(self.billing_software_main_Buttom_part_1_frame_2_3,text="Total Grocery Price",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_1_frame_2_3_label.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_1_frame_2_3_entry = Entry(self.billing_software_main_Buttom_part_1_frame_2_3,fg=self.green,font=("Comic Sans MS", 9, "bold"),textvariable=self.Gt)
        self.billing_software_main_Buttom_part_1_frame_2_3_entry.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)


        #==================



        self.billing_software_main_Buttom_part_1_frame_2_4 = Frame(self.billing_software_main_Buttom_part_1_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_1_frame_2_4.place(relx=0, rely=0.7, relwidth=1, relheight=0.283)

        self.billing_software_main_Buttom_part_1_frame_2_4_label = Label(self.billing_software_main_Buttom_part_1_frame_2_4,text="Total Cold Drink Price",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_1_frame_2_4_label.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_1_frame_2_4_entry = Entry(self.billing_software_main_Buttom_part_1_frame_2_4,fg=self.green,font=("Comic Sans MS", 9, "bold"),textvariable=self.Dt)
        self.billing_software_main_Buttom_part_1_frame_2_4_entry.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)


        #================== ============================================== ===========================



        self.billing_software_main_Buttom_part_2_frame_1 = Frame(self.billing_software_main_Buttom_part_1_frame, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_2_frame_1.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        self.billing_software_main_Buttom_part_2_frame_1_image_1 = Image.open("33.png")
        self.billing_software_main_Buttom_part_2_frame_1_image_2 = self.billing_software_main_Buttom_part_2_frame_1_image_1.resize((425,110))
        self.billing_software_main_Buttom_part_2_frame_1_image_3 = ImageTk.PhotoImage(self.billing_software_main_Buttom_part_2_frame_1_image_2)

        self.billing_software_main_Buttom_part_2_frame_1_image = Label(self.billing_software_main_Buttom_part_2_frame_1,image=self.billing_software_main_Buttom_part_2_frame_1_image_3, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_2_frame_1_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.billing_software_main_Buttom_part_2_frame_2 = Frame(self.billing_software_main_Buttom_part_2_frame_1_image, bg=self.white)
        self.billing_software_main_Buttom_part_2_frame_2.place(relx=0.05, rely=0.075, relwidth=0.9, relheight=0.85)






        #================
        self.billing_software_main_Buttom_part_2_frame_2_1 = Frame(self.billing_software_main_Buttom_part_2_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_2_frame_2_1.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        self.billing_software_main_Buttom_part_2_frame_2_1_label = Label(self.billing_software_main_Buttom_part_2_frame_2_1,text="Bill Menu",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_2_frame_2_1_label.place(relx=0, rely=0, relwidth=1, relheight=0.9)

        self.billing_software_main_Buttom_part_2_frame_2_1_label_li = Frame(self.billing_software_main_Buttom_part_2_frame_2_1,bg=self.line_5_color)
        self.billing_software_main_Buttom_part_2_frame_2_1_label_li.place(relx=0, rely=0.9, relwidth=0.4, relheight=0.1)



        #==================

        self.billing_software_main_Buttom_part_2_frame_2_2 = Frame(self.billing_software_main_Buttom_part_2_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_2_frame_2_2.place(relx=0, rely=0.15, relwidth=1, relheight=0.283)

        self.billing_software_main_Buttom_part_2_frame_2_2_label = Label(self.billing_software_main_Buttom_part_2_frame_2_2,text="Cosmetic Tax",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_2_frame_2_2_label.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_2_frame_2_2_entry = Entry(self.billing_software_main_Buttom_part_2_frame_2_2,fg=self.green,font=("Comic Sans MS", 9, "bold"),textvariable=self.Ctax)
        self.billing_software_main_Buttom_part_2_frame_2_2_entry.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)


        #==================

        self.billing_software_main_Buttom_part_2_frame_2_3 = Frame(self.billing_software_main_Buttom_part_2_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_2_frame_2_3.place(relx=0, rely=0.41, relwidth=1, relheight=0.283)

        self.billing_software_main_Buttom_part_2_frame_2_3_label = Label(self.billing_software_main_Buttom_part_2_frame_2_3,text="Grocery Tax",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_2_frame_2_3_label.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_2_frame_2_3_entry = Entry(self.billing_software_main_Buttom_part_2_frame_2_3,fg=self.green,font=("Comic Sans MS", 9, "bold"),textvariable=self.Gtax)
        self.billing_software_main_Buttom_part_2_frame_2_3_entry.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)


        #==================



        self.billing_software_main_Buttom_part_2_frame_2_4 = Frame(self.billing_software_main_Buttom_part_2_frame_2, bg=self.white)
        self.billing_software_main_Buttom_part_2_frame_2_4.place(relx=0, rely=0.7, relwidth=1, relheight=0.283)

        self.billing_software_main_Buttom_part_2_frame_2_4_label = Label(self.billing_software_main_Buttom_part_2_frame_2_4,text="Cold Drink Tax",fg=self.green,anchor=W,font=("Comic Sans MS", 9, "bold"))
        self.billing_software_main_Buttom_part_2_frame_2_4_label.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.billing_software_main_Buttom_part_2_frame_2_4_entry = Entry(self.billing_software_main_Buttom_part_2_frame_2_4,fg=self.green,font=("Comic Sans MS", 9, "bold"),textvariable=self.Dtax)
        self.billing_software_main_Buttom_part_2_frame_2_4_entry.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)







        #==================================================== _Buttom_part_2 =====================================================================================
        self.billing_software_main_Buttom_part_2_frame = Frame(self.billing_software_main_Buttom_part_Details_frame, bg=self.main_backgound_color)
        self.billing_software_main_Buttom_part_2_frame.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)

        self.billing_software_main_Buttom_part_2_frame_button_total = Button(self.billing_software_main_Buttom_part_2_frame,text="Total", bg="#FFC500", command=self.total_me, cursor="hand2")
        self.billing_software_main_Buttom_part_2_frame_button_total.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.35)


        self.billing_software_main_Buttom_part_2_frame_button_genrate_bill = Button(self.billing_software_main_Buttom_part_2_frame,text="Genrate Bill", bg="#00FF52",command=self.billsss,  cursor="hand2")
        self.billing_software_main_Buttom_part_2_frame_button_genrate_bill.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.35)


        self.billing_software_main_Buttom_part_2_frame_button_clear = Button(self.billing_software_main_Buttom_part_2_frame,text="Clear", bg="#FF0000", command=self.clear_all, cursor="hand2")
        self.billing_software_main_Buttom_part_2_frame_button_clear.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.35)





    def billsss(self):
        if self.name.get() == "" or self.number.get() == "":
            messagebox.showinfo("Information", "Please Fill Name or Phone Number!")
        else:

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3 = Frame(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f1, bg=self.white, )
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3.place(relx=0, rely=0.125, relwidth=1,
                                                                                    relheight=0.85)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_1 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="########## Welcome to Billing System ##########", bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_1.place(relx=0, rely=0, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_2 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3, text="Name: " + self.name.get(),
                anchor=W, bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_2.place(relx=0, rely=0.05, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_3 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3, text="Number: " + self.number.get(),
                anchor=W, bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_3.place(relx=0, rely=0.1, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_4 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="##############################################", bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_4.place(relx=0, rely=0.15, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_5 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="Cosmetics :   \t" + (str(self.costmetic_price)), anchor=W, bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_5.place(relx=0, rely=0.2, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_6 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="Grocery :  \t" + (str(self.grocery_price)), anchor=W, bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_6.place(relx=0, rely=0.25, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_7 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="Cold Drink :  \t" + (str(self.cold_drink_price)), anchor=W, bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_7.place(relx=0, rely=0.3, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_8 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="##############################################", bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_8.place(relx=0, rely=0.35, relwidth=1,
                                                                                      relheight=0.05)

            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_9 = Label(
                self.billing_software_main_Middle_part_bill_area_Details_frame_f3,
                text="Total :  \t" + (str(self.cold_drink_price + self.costmetic_price + self.grocery_price)),
                bg=self.white, fg=self.black)
            self.billing_software_main_Middle_part_bill_area_Details_frame_f3_9.place(relx=0, rely=0.4, relwidth=1,
                                                                                      relheight=0.05)

    def total_me(self):
        self.c1=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_1_2_entry.get()
        self.c2=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_2_2_entry.get()
        self.c3=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_3_2_entry.get()
        self.c4=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_4_2_entry.get()
        self.c5=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_5_2_entry.get()
        self.c6=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_6_2_entry.get()
        self.c7=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_7_2_entry.get()
        self.c8=self.billing_software_main_Middle_part_Cosmetics_Details_list_frame_item_8_2_entry.get()
        self.g1=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_1_2_entry.get()
        self.g2=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_2_2_entry.get()
        self.g3=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_3_2_entry.get()
        self.g4=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_4_2_entry.get()
        self.g5=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_5_2_entry.get()
        self.g6=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_6_2_entry.get()
        self.g7=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_7_2_entry.get()
        self.g8=self.billing_software_main_Middle_part_Grocery_Details_list_frame_item_8_2_entry.get()
        self.d1=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_1_2_entry.get()
        self.d2=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_2_2_entry.get()
        self.d3=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_3_2_entry.get()
        self.d4=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_4_2_entry.get()
        self.d5=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_5_2_entry.get()
        self.d6=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_6_2_entry.get()
        self.d7=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_7_2_entry.get()
        self.d8=self.billing_software_main_Middle_part_cold_drink_Details_list_frame_item_8_2_entry.get()

        self.costmetic_price=float(
            (self.Bath_Soap.get()*10)+
            (self.Face_cream.get()*10)+
            (self.face_wash.get()*10)+
            (self.hair_spray.get()*10)+
            (self.hair_gell.get()*10)+
            (self.body_loshan.get()*10)+
            (self.face_cream1.get()*10)+
            (self.face_cream2.get()*10)

         )

        self.grocery_price = float(
            (self.rice.get()*10)+
            (self.food_oil.get()*10)+
            (self.daal.get()*10)+
            (self.wheat.get()*10)+
            (self.sugar.get()*10)+
            (self.tea.get()*10)+
            (self.coffee.get()*10)+
            (self.milk.get()*10)
        )

        self.cold_drink_price = float(
            (self.maza.get()*10)+
            (self.cock.get()*10)+
            (self.frooi.get()*10)+
            (self.thumbs_up.get()*10)+
            (self.red_bull.get()*10)+
            (self.sprite.get()*10)+
            (self.pepsi.get()*10)+
            (self.fanta.get()*10)
        )

        self.Ct.set("Rs. "+str(self.costmetic_price))
        self.Ctax.set("Rs. "+str(round((self.costmetic_price)*0.05,2)))


        self.Gt.set("Rs. " + str(self.costmetic_price))
        self.Gtax.set("Rs. " + str(round((self.costmetic_price) * 0.05, 2)))

        self.Dt.set("Rs. " + str(self.cold_drink_price))
        self.Dtax.set("Rs. " + str(round((self.cold_drink_price) * 0.05, 2)))

    def clear_all(self):
        self.billing_software()



















    def close_root(self,e):
        self.root.quit()




root=Tk()
obj = Bill_App(root)
root.mainloop()