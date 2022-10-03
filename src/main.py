# Equipo 6
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
theme= {
    "red":"#E63946",
    "lg_blue":"#A8DADC",
    "dg_blue":"#1D3557",
    "blue":"#457B9D",
    "white":"#F1FAEE",
    "green":"#5CE639",
    "black":"#000000"
}
PATH = os.path.dirname(os.path.realpath(__file__))

coins = [0,0,0,0]
class product:
    def __init__ (self,name,img, price,code, quantity):
        self.name = name
        self.img = img
        self.price = price
        self.quantity = quantity
    
    def setPrice(self, newprice):
        self.price = newprice
    
    def getPrice(self):
        price = self.price
        return price 
    
    def addquantity(self, newquantity):
        self.quantity = self.quantity + newquantity
    
    def getQuantity(self):
        quantity = self.quantity
        return quantity
    
    def pop_prudct(self):
        self.quantity = self.quantity - 1

#========= Products-Object-Declaration==================
product0= product("agua-simple","Botella_01",15,"1A",2)
product1= product("agua-naranja","Botella_02",20,"1B",2)
product2= product("agua-limon","Botella_03",20,"1C",2)
product3= product("agua-uva","Botella_04",20,"1D",2)
product4= product("chocolate","Chocolate_01",12,"2A",5)
product5= product("Chocolate-fresa","Chocolate_02",12,"2B",5)
product6= product("Papas-chile","Papitas_03",18,"2C",5)
product7= product("Papas-Sal","Papitas_01",15,"2D",5)
product8= product("Cocacola","Lata_01",24,"3A",5)
product9= product("Sprite","Lata_04",24,"3B",5)
product10= product("Papas-Queso","Papitas_02",18,"3C",5)
product11= product("Papas-Picantes","Papitas_04",22,"3D",5)

class Change_Coins:
    
    def __init__(self, coins10, coins5, coins2, coins1):
        self.existing_coins =  [coins10,coins5,coins2,coins1]

    def exchange(self, price, cash):
        change = cash - price
        if(change<=100):
            dif10= 0 
            dif5 = 0
            dif2 = 0
            coins_exchange=[0,0,0,0]
            if (change/10) >= 1:
                coins_exchange[0] = int(change/10)
            dif10 = change % 10
            if (dif10/5) >= 1:
                coins_exchange[1] = int(dif10/5)
            dif5= dif10 % 5
            if  (dif5/2) >= 1: 
                coins_exchange[2] = int(dif5/2)
            dif2= dif5 % 2
            if  (dif2/1) >= 1:
                coins_exchange[3] = int(dif2/1)
            return coins_exchange
    
        else:
            return coins_exchange
    

    def logic_coins(self, coins):
        logic_coins = [0,0,0,0]
        if (self.existing_coins[0] >= coins[0]):
            logic_coins[0] = coins[0]
        else:
            missing_10 = coins[0] - self.existing_coins[0]
            extra_5 = missing_10 * 2
            coins [1] = coins [1] + extra_5
        
        if (self.existing_coins[0] >= coins[1]):
            logic_coins[1] = coins[1]
        else:
            missing_5 = coins[1] - self.existing_coins[1]
            extra_2 = missing_5 * 2
            extra_1 = missing_5
            coins [2] = coins [2] + extra_2
            coins [3] = coins [3] + extra_1
        
        if (self.existing_coins[0] >= coins[2]):
            logic_coins[2] = coins[2]
        else:
            missing_2 = coins[2] - self.existing_coins[2]
            extra_1 = missing_2 * 2 
            coins [3] = coins [3] + extra_1
    
        if (self.existing_coins[0] >= coins[3]):
            logic_coins[3] = coins[3]
        else:
            return [3444,3444,3444,3444]    
        return logic_coins
    
    def pop_coins(self, given_change):
        
        self.existing_coins[0] = self.existing_coins[0] - given_change[0]
        self.existing_coins[1] = self.existing_coins[1] - given_change[1]
        self.existing_coins[2] = self.existing_coins[2] - given_change[2]
        self.existing_coins[3] = self.existing_coins[3] - given_change[3] 

    def add_coins(self, string_add):
        
        self.existing_coins[0] = self.existing_coins[0] + string_add[0]
        self.existing_coins[1] = self.existing_coins[1] + string_add[1]
        self.existing_coins[2] = self.existing_coins[2] + string_add[2]
        self.existing_coins[3] = self.existing_coins[3] + string_add[3]
         
change_coins =  Change_Coins(20, 20, 20, 20)     

class App(customtkinter.CTk):

    WIDTH = 1920
    HEIGHT = 1080

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry("1920x1080")
        self.resizable(False,False)
        self.attributes('-alpha',0.7)
        # ============ create base frames ============

        # configure grid layout (2x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=1200,height=1030, corner_radius=0, fg_color=theme["lg_blue"])
        self.frame_left.grid(row=1, column=0, sticky="nw")
        
        self.frame_right = customtkinter.CTkFrame(master=self, width=720,height=1030, corner_radius=0, fg_color=theme["white"])
        self.frame_right.grid(row=1, column=1, sticky="nwse")
        
        self.frame_top = customtkinter.CTkFrame(master=self, width=1920,height=50, corner_radius=0, fg_color=theme["red"])
        self.frame_top.grid(row=0, column=0, columnspan=2, sticky="nw")

        #============= create right frame =============
        
        #Configure layout (6x2)
        self.frame_right.grid_columnconfigure(1, weight=1, uniform= True)
        self.frame_right.grid_rowconfigure(5, weight=1, uniform= True)
        self.label_price= customtkinter.CTkLabel(text="Codigo",master= self.frame_right)
        self.label_money= customtkinter.CTkLabel(text="Precio",master= self.frame_right)
        self.label_price.grid(row = 0, column=0, padx=20, sticky="w")
        self.label_money.grid(row = 1, column=0, padx=20, sticky="w")
        self.entry_price = customtkinter.CTkEntry(master= self.frame_right,fg_color=theme["lg_blue"], width=270, height=70, corner_radius=30, border_width=0)
        self.entry_money = customtkinter.CTkEntry(master= self.frame_right, fg_color=theme["lg_blue"], width=270, height=70, corner_radius=30, border_width=0)
        self.entry_price.grid(row = 0, column=1, pady=10, padx=20, sticky="ne") 
        self.entry_money.grid(row = 1, column=1, pady=10, padx=20, sticky="ne")
        self.Cancel_button = customtkinter.CTkButton(master= self.frame_right, fg_color=theme["red"], width=200, height=50, corner_radius=50, border_width=0, text="Cancelar", command= lambda:self.cancelar())
        self.Cancel_button.grid(row=2, column=0, pady=5, padx=20, sticky="nw")
        self.Confirm_button = customtkinter.CTkButton(master= self.frame_right, fg_color=theme["green"], width=200, height=50, corner_radius=50, border_width=0, text="Confirmar", command=lambda:self.confirm())
        self.Confirm_button.grid(row=2, column=1, pady=5,padx=20, sticky="ne")
        
        #=========== Create pad frame ===============
        self.pad_frame = customtkinter.CTkFrame(master=self.frame_right, width=550, height=500, fg_color=theme["lg_blue"])
        self.pad_frame.grid(row=3, column=0, columnspan=2, sticky="nwse", pady=10, padx=10)
        #======= Create grid layout for pad =========
        self.pad_frame.grid_rowconfigure(3,weight=1)
        self.pad_frame.grid_columnconfigure(4, weight=1)
        self.label_code_A= customtkinter.CTkLabel(master= self.pad_frame, text="A", width=60, height=60)
        self.label_code_A.grid(row= 0, column= 1, pady=5, padx=5, sticky="nwe")
        self.label_code_B= customtkinter.CTkLabel(master= self.pad_frame, text="B",width=60, height=60)
        self.label_code_B.grid(row= 0, column= 2, pady=5, padx=5, sticky="nwe")
        self.label_code_C= customtkinter.CTkLabel(master= self.pad_frame, text="C",width=60, height=60)
        self.label_code_C.grid(row= 0, column= 3, pady=5, padx=5, sticky="nwe")
        self.label_code_D= customtkinter.CTkLabel(master= self.pad_frame, text="D",width=60, height=60)
        self.label_code_D.grid(row= 0, column= 4, pady=5, padx=5, sticky="nwe")
        
        self.label_code_1= customtkinter.CTkLabel(master= self.pad_frame, text="1",width=60, height=60)
        self.label_code_1.grid(row= 1, column= 0, pady=5, padx=5, sticky="nwe")
        self.label_code_2= customtkinter.CTkLabel(master= self.pad_frame, text="2",width=60, height=60)
        self.label_code_2.grid(row= 2, column= 0, pady=5, padx=5, sticky="nwe")
        self.label_code_3= customtkinter.CTkLabel(master= self.pad_frame, text="3",width=60, height=60)
        self.label_code_3.grid(row= 3, column= 0, pady=5, padx=5, sticky="nwe")

        
        self.code_button0=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1A",text_color=theme["white"], command=lambda:self.button_code("1A"), text_font=("Arial",16))
        self.code_button0.grid(row= 1, column= 1, pady=5, padx=5, sticky="nwes")
        self.code_button1=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1B",text_color=theme["white"], command=lambda:self.button_code("1B"),text_font=("Arial",16))
        self.code_button1.grid(row= 1, column= 2, pady=5, padx=5, sticky="nwes")
        self.code_button2=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1C",text_color=theme["white"], command=lambda:self.button_code("1C"),text_font=("Arial",16))
        self.code_button2.grid(row= 1, column= 3, pady=5, padx=5, sticky="nwes")
        self.code_button3=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1D",text_color=theme["white"], command=lambda:self.button_code("1D"),text_font=("Arial",16))
        self.code_button3.grid(row= 1, column= 4, pady=5, padx=5, sticky="nwes")
        self.code_button4=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2A",text_color=theme["white"], command=lambda:self.button_code("2A"),text_font=("Arial",16))
        self.code_button4.grid(row= 2, column= 1, pady=5, padx=5, sticky="nwes")
        self.code_button5=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2B",text_color=theme["white"], command=lambda:self.button_code("2B"),text_font=("Arial",16))
        self.code_button5.grid(row= 2, column= 2, pady=5, padx=5, sticky="nwes")
        self.code_button6=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2C",text_color=theme["white"], command=lambda:self.button_code("2C"),text_font=("Arial",16))
        self.code_button6.grid(row= 2, column= 3, pady=5, padx=5, sticky="nwes")
        self.code_button7=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2D",text_color=theme["white"], command=lambda:self.button_code("2D"),text_font=("Arial",16))
        self.code_button7.grid(row= 2, column= 4, pady=5, padx=5, sticky="nwes")
        self.code_button8=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3A",text_color=theme["white"], command=lambda:self.button_code("3A"),text_font=("Arial",16))
        self.code_button8.grid(row= 3, column= 1, pady=5, padx=5, sticky="nwes")
        self.code_button9=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3B",text_color=theme["white"], command=lambda:self.button_code("3B"),text_font=("Arial",16))
        self.code_button9.grid(row= 3, column= 2, pady=5, padx=5, sticky="nwes")
        self.code_button10=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3C",text_color=theme["white"], command=lambda:self.button_code("3C"),text_font=("Arial",16))
        self.code_button10.grid(row= 3, column= 3, pady=5, padx=5, sticky="nwes")
        self.code_button11=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3D", text_color=theme["white"], command=lambda:self.button_code("3D"),text_font=("Arial",16))
        self.code_button11.grid(row= 3, column= 4, pady=5, padx=5, sticky="nwes")
        
        #=========== Create buttons for add money ==========
        self.add_10_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$10", text_color=theme["white"], command=lambda:self.button_money(10), state=tkinter.DISABLED,text_font=("Arial",20))
        self.add_10_button.grid(row=4, column=0, pady=40, padx= 40, sticky="nw")
        self.add_5_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$5", text_color=theme["white"], command=lambda:self.button_money(5), state=tkinter.DISABLED,text_font=("Arial",20))
        self.add_5_button.grid(row=5, column=0, pady=40, padx= 40, sticky="nw")
        self.add_2_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$2", text_color=theme["white"], command=lambda:self.button_money(2), state=tkinter.DISABLED,text_font=("Arial",20))
        self.add_2_button.grid(row=4, column=1, pady=40, padx= 40, sticky="ne")
        self.add_1_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$1", text_color=theme["white"],command=lambda:self.button_money(1), state=tkinter.DISABLED,text_font=("Arial",20))
        self.add_1_button.grid(row=5, column=1, pady=40, padx= 40, sticky="ne")
        
        #========= Put background image for the frame =======
        image_back_machine= Image.open(PATH +"/img/Vending-machine.png").resize((1200,1030))
        self.back_img= ImageTk.PhotoImage(image_back_machine)
        self.label_image_back= tkinter.Label(master=self.frame_left, image=self.back_img,borderwidth=0)
        self.label_image_back.place(x=0, y=0)
        product_image0= Image.open(PATH +"/img/products/"+product0.img+".png").resize((115,115))
        self.image_producto0 = ImageTk.PhotoImage(product_image0)
        self.label_img_pr0 = tkinter.Label(master=self.frame_left, image=self.image_producto0, borderwidth=0)
        product_image1= Image.open(PATH +"/img/products/"+product1.img+".png").resize((115,115))
        self.image_producto1 = ImageTk.PhotoImage(product_image1)
        self.label_img_pr1 = tkinter.Label(master=self.frame_left, image=self.image_producto1, borderwidth=0)
        product_image2= Image.open(PATH +"/img/products/"+product2.img+".png").resize((115,115))
        self.image_producto2 = ImageTk.PhotoImage(product_image2)
        self.label_img_pr2 = tkinter.Label(master=self.frame_left, image=self.image_producto2, borderwidth=0)
        product_image3= Image.open(PATH +"/img/products/"+product3.img+".png").resize((115,115))
        self.image_producto3 = ImageTk.PhotoImage(product_image3)
        self.label_img_pr3 = tkinter.Label(master=self.frame_left, image=self.image_producto3, borderwidth=0)
        product_image4= Image.open(PATH +"/img/products/"+product4.img+".png").resize((115,115))
        self.image_producto4 = ImageTk.PhotoImage(product_image4)
        self.label_img_pr4 = tkinter.Label(master=self.frame_left, image=self.image_producto4, borderwidth=0)
        product_image5= Image.open(PATH +"/img/products/"+product5.img+".png").resize((115,115))
        self.image_producto5 = ImageTk.PhotoImage(product_image5)
        self.label_img_pr5 = tkinter.Label(master=self.frame_left, image=self.image_producto5, borderwidth=0)
        product_image6= Image.open(PATH +"/img/products/"+product6.img+".png").resize((115,115))
        self.image_producto6 = ImageTk.PhotoImage(product_image6)
        self.label_img_pr6 = tkinter.Label(master=self.frame_left, image=self.image_producto6, borderwidth=0)
        product_image7= Image.open(PATH +"/img/products/"+product7.img+".png").resize((115,115))
        self.image_producto7 = ImageTk.PhotoImage(product_image7)
        self.label_img_pr7 = tkinter.Label(master=self.frame_left, image=self.image_producto7, borderwidth=0)
        product_image8= Image.open(PATH +"/img/products/"+product8.img+".png").resize((115,115))
        self.image_producto8 = ImageTk.PhotoImage(product_image8)
        self.label_img_pr8 = tkinter.Label(master=self.frame_left, image=self.image_producto8, borderwidth=0)
        product_image9= Image.open(PATH +"/img/products/"+product9.img+".png").resize((115,115))
        self.image_producto9 = ImageTk.PhotoImage(product_image9)
        self.label_img_pr9 = tkinter.Label(master=self.frame_left, image=self.image_producto9, borderwidth=0)
        product_image10= Image.open(PATH +"/img/products/"+product10.img+".png").resize((115,115))
        self.image_producto10 = ImageTk.PhotoImage(product_image10)
        self.label_img_pr10 = tkinter.Label(master=self.frame_left, image=self.image_producto10, borderwidth=0)
        product_image11= Image.open(PATH +"/img/products/"+product11.img+".png").resize((115,115))
        self.image_producto11 = ImageTk.PhotoImage(product_image11)
        self.label_img_pr11 = tkinter.Label(master=self.frame_left, image=self.image_producto11, borderwidth=0)
        self.label_img_pr0.place(x=219,y=100)
        self.label_img_pr1.place(x=360,y=100)
        self.label_img_pr2.place(x=500,y=100)
        self.label_img_pr3.place(x=641,y=100)
        self.label_img_pr4.place(x=214,y=316)
        self.label_img_pr5.place(x=359,y=316)
        self.label_img_pr6.place(x=505,y=316)
        self.label_img_pr7.place(x=648,y=316)
        self.label_img_pr8.place(x=212,y=531)
        self.label_img_pr9.place(x=353,y=531)
        self.label_img_pr10.place(x=494,y=531)
        self.label_img_pr11.place(x=635,y=531)
        self.label_price_pr0 = customtkinter.CTkLabel(master= self.frame_left,text=str(product0.price), borderwidth=0, width=60)
        self.label_price_pr1 = customtkinter.CTkLabel(master= self.frame_left,text=str(product1.price), borderwidth=0, width=60)
        self.label_price_pr2 = customtkinter.CTkLabel(master= self.frame_left,text=str(product2.price), borderwidth=0, width=60)
        self.label_price_pr3 = customtkinter.CTkLabel(master= self.frame_left,text=str(product3.price), borderwidth=0, width=60)
        self.label_price_pr4 = customtkinter.CTkLabel(master= self.frame_left,text=str(product4.price), borderwidth=0, width=60)
        self.label_price_pr5 = customtkinter.CTkLabel(master= self.frame_left,text=str(product5.price), borderwidth=0, width=60)
        self.label_price_pr6 = customtkinter.CTkLabel(master= self.frame_left,text=str(product6.price), borderwidth=0, width=60)
        self.label_price_pr7 = customtkinter.CTkLabel(master= self.frame_left,text=str(product7.price), borderwidth=0, width=60)
        self.label_price_pr8 = customtkinter.CTkLabel(master= self.frame_left,text=str(product8.price), borderwidth=0, width=60)
        self.label_price_pr9 = customtkinter.CTkLabel(master= self.frame_left,text=str(product9.price), borderwidth=0, width=60)
        self.label_price_pr10 = customtkinter.CTkLabel(master= self.frame_left,text=str(product10.price), borderwidth=0, width=60)
        self.label_price_pr11 = customtkinter.CTkLabel(master= self.frame_left,text=str(product11.price), borderwidth=0, width=60)
        self.label_price_pr0.place(x=243, y=230)
        self.label_price_pr1.place(x=387, y=230)
        self.label_price_pr2.place(x=527, y=230)
        self.label_price_pr3.place(x=673, y=230)
        self.label_price_pr4.place(x=243, y=450)
        self.label_price_pr5.place(x=386, y=450)
        self.label_price_pr6.place(x=526, y=450)
        self.label_price_pr7.place(x=674, y=450)
        self.label_price_pr8.place(x=230, y=671)
        self.label_price_pr9.place(x=380, y=671)
        self.label_price_pr10.place(x=529, y=671)
        self.label_price_pr11.place(x=667, y=671)
        
        #============ Title bar =================
        image_close = Image.open(PATH+"/img/products/Close.png").resize((50,50))
        self.image_Close = ImageTk.PhotoImage(image_close)
        image_max = Image.open(PATH+"/img/products/Engrane.png").resize((50,50))
        self.image_Max = ImageTk.PhotoImage(image_max)
        self.close_button =  customtkinter.CTkButton(image= self.image_Close, border_width=0, master=self.frame_top, text="", width=50, height=50, corner_radius=0, compound="left", fg_color=theme["red"], bg_color=theme["red"], hover_color=theme["red"], command=self.on_closing)
        self.admin_button =  customtkinter.CTkButton(image= self.image_Max, border_width=0, master=self.frame_top, text="", width=50, height=50, corner_radius=0, compound="left", fg_color=theme["red"], bg_color=theme["red"], hover_color=theme["red"], command=self.administration)
        self.close_button.place(x=0, y=0)
        self.admin_button.place(x=1870, y=0)
        
        #========== Administration =============
        self.login_frame = customtkinter.CTkFrame(master=self, width=1200,height=1030, corner_radius=0, fg_color=theme["lg_blue"])
        self.admin_frame = customtkinter.CTkFrame(master=self, width=1200,height=1030, corner_radius=0, fg_color=theme["white"])
        self.entry_username = customtkinter.CTkEntry(master= self.login_frame, fg_color=theme["dg_blue"], width=1000, height=70, corner_radius=30, border_width=0, placeholder_text="Usuario", text_color=theme["white"])
        self.entry_password = customtkinter.CTkEntry(master= self.login_frame, fg_color=theme["dg_blue"], width=1000, height=70, corner_radius=30, border_width=0, placeholder_text="Contrasena", text_color=theme["white"], show="*") 
        self.Log_in_button = customtkinter.CTkButton(master = self.login_frame, fg_color=theme["dg_blue"], width=1000, height=70, corner_radius=30, border_width=0, text="Iniciar Sesion", command=self.adminpanel, text_color=theme["white"])
        self.entry_username.grid(row=0,column=0, pady= 100, padx = 100, sticky="nwse")
        self.entry_password.grid(row=1,column=0, pady= 100, padx = 100, sticky="nwse")
        self.Log_in_button.grid(row=2,column=0, pady= 300, padx = 100, sticky="nwse")
        
        #========= Adminpanel ========= 
        self.admin_frame.grid_rowconfigure(17, weight= 1)
        self.admin_frame.grid_columnconfigure(3, minsize = 300)
        self.table_admin_quantity = customtkinter.CTkLabel(master= self.admin_frame, text="Cantidad", borderwidth=0)
        self.table_admin_price = customtkinter.CTkLabel(master= self.admin_frame, text="Cantidad", borderwidth=0)
        ad_product_image0= Image.open(PATH +"/img/products/"+product0.img+".png").resize((50,50))
        self.ad_image_producto0 = ImageTk.PhotoImage(ad_product_image0)
        ad_product_image1= Image.open(PATH +"/img/products/"+product1.img+".png").resize((50,50))
        self.ad_image_producto1 = ImageTk.PhotoImage(ad_product_image1)
        ad_product_image2= Image.open(PATH +"/img/products/"+product2.img+".png").resize((50,50))
        self.ad_image_producto2 = ImageTk.PhotoImage(ad_product_image2)
        ad_product_image3= Image.open(PATH +"/img/products/"+product3.img+".png").resize((50,50))
        self.ad_image_producto3 = ImageTk.PhotoImage(ad_product_image3)
        ad_product_image4= Image.open(PATH +"/img/products/"+product4.img+".png").resize((50,50))
        self.ad_image_producto4 = ImageTk.PhotoImage(ad_product_image4)
        ad_product_image5= Image.open(PATH +"/img/products/"+product5.img+".png").resize((50,50))
        self.ad_image_producto5 = ImageTk.PhotoImage(ad_product_image5)
        ad_product_image6= Image.open(PATH +"/img/products/"+product6.img+".png").resize((50,50))
        self.ad_image_producto6 = ImageTk.PhotoImage(ad_product_image6)
        ad_product_image7= Image.open(PATH +"/img/products/"+product7.img+".png").resize((50,50))
        self.ad_image_producto7 = ImageTk.PhotoImage(ad_product_image7)
        ad_product_image8= Image.open(PATH +"/img/products/"+product8.img+".png").resize((50,50))
        self.ad_image_producto8 = ImageTk.PhotoImage(ad_product_image8)
        ad_product_image9= Image.open(PATH +"/img/products/"+product9.img+".png").resize((50,50))
        self.ad_image_producto9 = ImageTk.PhotoImage(ad_product_image9)
        ad_product_image10= Image.open(PATH +"/img/products/"+product10.img+".png").resize((50,50))
        self.ad_image_producto10 = ImageTk.PhotoImage(ad_product_image10)
        ad_product_image11= Image.open(PATH +"/img/products/"+product11.img+".png").resize((50,50))
        self.ad_image_producto11 = ImageTk.PhotoImage(ad_product_image11)
        
        self.label_admin_img_pr0 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto0, borderwidth=0)
        self.label_admin_img_pr1 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto1, borderwidth=0)
        self.label_admin_img_pr2 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto2, borderwidth=0)
        self.label_admin_img_pr3 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto3, borderwidth=0)
        self.label_admin_img_pr4 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto4, borderwidth=0)
        self.label_admin_img_pr5 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto5, borderwidth=0)
        self.label_admin_img_pr6 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto6, borderwidth=0)
        self.label_admin_img_pr7 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto7, borderwidth=0)
        self.label_admin_img_pr8 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto8, borderwidth=0)
        self.label_admin_img_pr9 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto9, borderwidth=0)
        self.label_admin_img_pr10 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto10, borderwidth=0)
        self.label_admin_img_pr11 = tkinter.Label(master=self.admin_frame, image=self.ad_image_producto11, borderwidth=0)
        
        product_coin10= Image.open(PATH +"/img/products/Moneda_10.png").resize((50,50))
        self.image_coin10 = ImageTk.PhotoImage(product_coin10)
        product_coin5= Image.open(PATH +"/img/products/Moneda_05.png").resize((50,50))
        self.image_coin5 = ImageTk.PhotoImage(product_coin5)
        product_coin2= Image.open(PATH +"/img/products/Moneda_02.png").resize((50,50))
        self.image_coin2 = ImageTk.PhotoImage(product_coin2)
        product_coin1= Image.open(PATH +"/img/products/Moneda_01.png").resize((50,50))
        self.image_coin1 = ImageTk.PhotoImage(product_coin1)
        
        self.label_admin_img_coin10 = tkinter.Label(master=self.admin_frame, image=self.image_coin10, borderwidth=0)
        self.label_admin_img_coin5 = tkinter.Label(master=self.admin_frame, image=self.image_coin5, borderwidth=0)
        self.label_admin_img_coin2 = tkinter.Label(master=self.admin_frame, image=self.image_coin2, borderwidth=0)
        self.label_admin_img_coin1 = tkinter.Label(master=self.admin_frame, image=self.image_coin1, borderwidth=0)
        
        self.quantity_entry_pr0 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr1 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr2 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr3 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr4 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr5 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr6 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr7 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr8 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr9 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr10 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_pr11 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        
        self.price_entry_pr0 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr1 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr2 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr3 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr4 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr5 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr6 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr7 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr8 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr9 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr10 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
        self.price_entry_pr11 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["lg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Precio", text_color=theme["black"])
           
        self.quantity_entry_coin10 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_coin5 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_coin2 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        self.quantity_entry_coin1 = customtkinter.CTkEntry(master= self.admin_frame, fg_color=theme["dg_blue"], width=300, height=50, corner_radius=10, border_width=0, placeholder_text="Cantidad", text_color=theme["white"])
        
        self.button_add_items = customtkinter.CTkButton(master = self.admin_frame, fg_color=theme["dg_blue"], width=1200, height=70, corner_radius=30, border_width=0, text="Anadir Items y Monedas", command=lambda:self.add_items(), text_color=theme["white"])
        
        self.label_admin_img_pr0.grid(row=1,column=1,padx=30,pady=5)
        self.label_admin_img_pr1.grid(row=2,column=1,padx=30,pady=5)
        self.label_admin_img_pr2.grid(row=3,column=1,padx=30,pady=5)
        self.label_admin_img_pr3.grid(row=4,column=1,padx=30,pady=5)
        self.label_admin_img_pr4.grid(row=5,column=1,padx=30,pady=5)
        self.label_admin_img_pr5.grid(row=6,column=1,padx=30,pady=5)
        self.label_admin_img_pr6.grid(row=7,column=1,padx=30,pady=5)
        self.label_admin_img_pr7.grid(row=8,column=1,padx=30,pady=5)
        self.label_admin_img_pr8.grid(row=9,column=1,padx=30,pady=5)
        self.label_admin_img_pr9.grid(row=10,column=1,padx=30,pady=5)
        self.label_admin_img_pr10.grid(row=11,column=1,padx=30,pady=5)
        self.label_admin_img_pr11.grid(row=12,column=1,padx=30,pady=5)
        self.label_admin_img_coin10.grid(row=13,column=1,padx=30,pady=5)
        self.label_admin_img_coin5.grid(row=14,column=1,padx=30,pady=5)
        self.label_admin_img_coin2.grid(row=15,column=1,padx=30,pady=5)
        self.label_admin_img_coin1.grid(row=16,column=1,padx=30,pady=5)
        
        self.button_add_items.grid(row=17, column=1,padx=5, pady=10, columnspan=3, sticky = "NW")
        
        self.quantity_entry_pr0.grid(row=1,column=2,padx=5,pady=5)
        self.quantity_entry_pr1.grid(row=2,column=2,padx=5,pady=5)
        self.quantity_entry_pr2.grid(row=3,column=2,padx=5,pady=5)
        self.quantity_entry_pr3.grid(row=4,column=2,padx=5,pady=5)
        self.quantity_entry_pr4.grid(row=5,column=2,padx=5,pady=5)
        self.quantity_entry_pr5.grid(row=6,column=2,padx=5,pady=5)
        self.quantity_entry_pr6.grid(row=7,column=2,padx=5,pady=5)
        self.quantity_entry_pr7.grid(row=8,column=2,padx=5,pady=5)
        self.quantity_entry_pr8.grid(row=9,column=2,padx=5,pady=5)
        self.quantity_entry_pr9.grid(row=10,column=2,padx=5,pady=5)
        self.quantity_entry_pr10.grid(row=11,column=2,padx=5,pady=5)
        self.quantity_entry_pr11.grid(row=12,column=2,padx=5,pady=5)
        
        self.price_entry_pr0.grid(row=1,column=3,padx=5,pady=5)
        self.price_entry_pr1.grid(row=2,column=3,padx=5,pady=5)
        self.price_entry_pr2.grid(row=3,column=3,padx=5,pady=5)
        self.price_entry_pr3.grid(row=4,column=3,padx=5,pady=5)
        self.price_entry_pr4.grid(row=5,column=3,padx=5,pady=5)
        self.price_entry_pr5.grid(row=6,column=3,padx=5,pady=5)
        self.price_entry_pr6.grid(row=7,column=3,padx=5,pady=5)
        self.price_entry_pr7.grid(row=8,column=3,padx=5,pady=5)
        self.price_entry_pr8.grid(row=9,column=3,padx=5,pady=5)
        self.price_entry_pr9.grid(row=10,column=3,padx=5,pady=5)
        self.price_entry_pr10.grid(row=11,column=3,padx=5,pady=5)
        self.price_entry_pr11.grid(row=12,column=3,padx=5,pady=5)
        
        self.quantity_entry_coin10.grid(row=13,column=2,padx=5,pady=5)
        self.quantity_entry_coin5.grid(row=14,column=2,padx=5,pady=5)
        self.quantity_entry_coin2.grid(row=15,column=2,padx=5,pady=5)
        self.quantity_entry_coin1.grid(row=16,column=2,padx=5,pady=5)
        self.checkinventory()
    
    def add_items (self):
        qt_pr0=self.quantity_entry_pr0.get()
        qt_pr1=self.quantity_entry_pr1.get()
        qt_pr2=self.quantity_entry_pr2.get()
        qt_pr3=self.quantity_entry_pr3.get()
        qt_pr4=self.quantity_entry_pr4.get()
        qt_pr5=self.quantity_entry_pr5.get()
        qt_pr6=self.quantity_entry_pr6.get()
        qt_pr7=self.quantity_entry_pr7.get()
        qt_pr8=self.quantity_entry_pr8.get()
        qt_pr9=self.quantity_entry_pr9.get()
        qt_pr10=self.quantity_entry_pr10.get()
        qt_pr11=self.quantity_entry_pr11.get()
        qt_co10=self.quantity_entry_coin10.get()
        qt_co5=self.quantity_entry_coin5.get()
        qt_co2=self.quantity_entry_coin2.get()
        qt_co1=self.quantity_entry_coin1.get()
        
        pr_pr0 = self.price_entry_pr0.get()
        pr_pr1 = self.price_entry_pr1.get()
        pr_pr2 = self.price_entry_pr2.get()
        pr_pr3 = self.price_entry_pr3.get()
        pr_pr4 = self.price_entry_pr4.get()
        pr_pr5 = self.price_entry_pr5.get()
        pr_pr6 = self.price_entry_pr6.get()
        pr_pr7 = self.price_entry_pr7.get()
        pr_pr8 = self.price_entry_pr8.get()
        pr_pr9 = self.price_entry_pr9.get()
        pr_pr10 = self.price_entry_pr10.get()
        pr_pr11 = self.price_entry_pr11.get()
        
        if(pr_pr0 != "" and int(pr_pr0) != 0 ):
            product0.setPrice(int(pr_pr0))
        if(pr_pr1 != "" and int(pr_pr1) != 0 ):
            product1.setPrice(int(pr_pr1))
        if(pr_pr2 != "" and int(pr_pr2) != 0 ):
            product2.setPrice(int(pr_pr2))
        if(pr_pr3 != "" and int(pr_pr3) != 0 ):
            product3.setPrice(int(pr_pr3))
        if(pr_pr4 != "" and int(pr_pr4) != 0 ):
            product4.setPrice(int(pr_pr4))
        if(pr_pr5 != "" and int(pr_pr5) != 0 ):
            product5.setPrice(int(pr_pr5))
        if(pr_pr6 != "" and int(pr_pr6) != 0 ):
            product6.setPrice(int(pr_pr6))
        if(pr_pr7 != "" and int(pr_pr7) != 0 ):
            product7.setPrice(int(pr_pr7))
        if(pr_pr8 != "" and int(pr_pr8) != 0 ):
            product8.setPrice(int(pr_pr8))
        if(pr_pr9 != "" and int(pr_pr9) != 0 ):
            product9.setPrice(int(pr_pr9))
        if(pr_pr10 != "" and int(pr_pr10) != 0 ):
            product10.setPrice(int(pr_pr10))
        if(pr_pr11 != "" and int(pr_pr11) != 0 ):
            product11.setPrice(int(pr_pr11))              
        if(qt_pr0 == ""):
            qt_pr0 = 0 
        if(qt_pr1 == ""):
            qt_pr1 = 0
        if(qt_pr2 == ""):
            qt_pr2 = 0
        if(qt_pr3 == ""):
            qt_pr3 = 0
        if(qt_pr4 == ""):
            qt_pr4 = 0
        if(qt_pr5== ""):
            qt_pr5 = 0
        if(qt_pr6 == ""):
            qt_pr6 = 0
        if(qt_pr7 == ""):
            qt_pr7 = 0
        if(qt_pr8 == ""):
            qt_pr8 = 0
        if(qt_pr9 == ""):
            qt_pr9 = 0
        if(qt_pr10 == ""):
            qt_pr10 = 0
        if(qt_pr11 == ""):
            qt_pr11 = 0
        if(qt_co10 == ""):
            qt_co10 = 0
        if(qt_co5 == ""):
            qt_co5 = 0
        if(qt_co2 == ""):
            qt_co2 = 0
        if(qt_co1 == ""):
            qt_co1 = 0
        adding_coins_trace = [int(qt_co10), int(qt_co5), int(qt_co2), int(qt_co1)]
        change_coins.add_coins(adding_coins_trace)
        product0.addquantity(int(qt_pr0))
        product1.addquantity(int(qt_pr1))
        product2.addquantity(int(qt_pr2))
        product3.addquantity(int(qt_pr3))
        product4.addquantity(int(qt_pr4))
        product5.addquantity(int(qt_pr5))
        product6.addquantity(int(qt_pr6))
        product7.addquantity(int(qt_pr7))
        product8.addquantity(int(qt_pr8))
        product9.addquantity(int(qt_pr9))
        product10.addquantity(int(qt_pr10))
        product11.addquantity(int(qt_pr11))
        self.label_price_pr0.configure(text=str(product0.price))
        self.label_price_pr1.configure(text=str(product1.price))
        self.label_price_pr2.configure(text=str(product2.price))
        self.label_price_pr3.configure(text=str(product3.price))
        self.label_price_pr4.configure(text=str(product4.price))
        self.label_price_pr5.configure(text=str(product5.price))
        self.label_price_pr6.configure(text=str(product6.price))
        self.label_price_pr7.configure(text=str(product7.price))
        self.label_price_pr8.configure(text=str(product8.price))
        self.label_price_pr9.configure(text=str(product9.price))
        self.label_price_pr10.configure(text=str(product10.price))
        self.label_price_pr11.configure(text=str(product11.price))
        self.entry_password.configure(text="")
        self.entry_username.configure(text="")
        self.checkinventory()
        self.admin_frame.grid_forget()
        self.login_frame.grid_forget()
        self.frame_left.grid(row=1, column=0, sticky="nw")

    def adminpanel (self):
        user = self.entry_username.get()
        password = self.entry_password.get()
        if(user == "Tanner" and password == "Ulises1319@"):
           self.admin_frame.grid(row=1, column=0, sticky="nw")
        else:
            self.entry_password.delete(0,300)
            self.entry_username.delete(0,300)
            self.entry_username.configure(placeholder_text="Usuario o contrasena incorrecta")
            self.entry_password.configure(placeholder_text="Usuario o contrasena incorrecta")
    def administration(self):
        self.login_frame.grid(row=1, column=0, sticky="nw")
    
    
    
    def button_code(self, code):
        self.entry_price.delete(0,5)
        self.entry_money.delete(0,5)
        if(code == "1A"):
            price =  product0.getPrice()
        elif(code == "1B"):
            price = product1.getPrice()
        elif(code == "1C"):
            price = product2.getPrice()
        elif(code == "1D"):
            price = product3.getPrice()
        elif(code == "2A"):
            price = product4.getPrice()
        elif(code == "2B"):
            price = product5.getPrice()
        elif(code == "2C"):
            price = product6.getPrice()
        elif(code == "2D"):
            price = product7.getPrice()
        elif(code == "3A"):
            price = product8.getPrice()
        elif(code == "3B"):
            price = product9.getPrice()
        elif(code == "3C"):
            price = product10.getPrice()
        elif(code == "3D"):
            price = product11.getPrice()
        else:
            price = 0
        self.entry_price.insert(0,code)
        self.entry_money.insert(0,str(price))
        
    def button_money(self, value):
        global coins
        actual_money=  int(self.entry_money.get())
        if(value == 10):
            actual_money += 10
            self.entry_money.delete(0,4)
            self.entry_money.insert(0,str(actual_money))
            coins10 = coins[0]
            coins10 += 1 
            coins[0] = coins10
        if(value == 5):
            actual_money += 5
            self.entry_money.delete(0,4)
            self.entry_money.insert(0,str(actual_money))
            coins5 = coins[1]
            coins5 += 1 
            coins[1] = coins5
        if(value == 2):
            actual_money += 2
            self.entry_money.delete(0,4)
            self.entry_money.insert(0,str(actual_money))
            coins2 = coins[2]
            coins2 += 1 
            coins[2] = coins2
        if(value == 1):
            actual_money += 1
            self.entry_money.delete(0,4)
            self.entry_money.insert(0,str(actual_money))
            coins1 = coins[3]
            coins1 += 1 
            coins[3] = coins1
        
            
           
    def confirm(self):
        if(self.Confirm_button.text == "Confirmar"):
            price = self.entry_money.get()
            self.product_code = self.entry_price.get()
            self.entry_price.delete(0,4)
            self.entry_money.delete(0,4)
            self.entry_price.insert(0,price)
            money = self.entry_money.insert(0,"0")
            self.label_price.configure(text="Precio") 
            self.label_money.configure(text="Creditos") 
            self.Confirm_button.configure(text="Pagar")
            self.add_10_button.configure(state="ENABLED")
            self.add_5_button.configure(state="ENABLED")
            self.add_2_button.configure(state="ENABLED")
            self.add_1_button.configure(state="ENABLED")
        else:
            price = int(self.entry_price.get())
            money = int(self.entry_money.get())
            if(price <= money):
                global coins
                change_coins.add_coins(coins)
                coins_change = change_coins.exchange(price, money) 
                logic_coins = change_coins.logic_coins(coins_change)
                change_coins.pop_coins(logic_coins)
                
                if(logic_coins != [3444,3444,3444,3444]):
                    string_change = ("Cambio: "+str(logic_coins[0])+": $10 "+str(logic_coins[1])+": $5 "+str(logic_coins[2])+": $2 "+str(logic_coins[3])+": $1")
                    self.label_price.configure(text=string_change)
                    self.label_money.configure(text="Gracias por tu compra")
                    self.Cancel_button.configure(text="Reset")
                    self.add_10_button.configure(state=tkinter.DISABLED)
                    self.add_5_button.configure(state=tkinter.DISABLED)
                    self.add_2_button.configure(state=tkinter.DISABLED)
                    self.add_1_button.configure(state=tkinter.DISABLED)
                    if(self.product_code == "1A"):
                        product0.pop_prudct()
                    elif(self.product_code == "1B"):
                        product1.pop_prudct()
                    elif(self.product_code == "1C"):
                        product2.pop_prudct()
                    elif(self.product_code == "1D"):
                        product3.pop_prudct()
                    elif(self.product_code == "2A"):
                        product4.pop_prudct()
                    elif(self.product_code == "2B"):
                        product5.pop_prudct()
                    elif(self.product_code == "2C"):
                        product6.pop_prudct()
                    elif(self.product_code == "2D"):
                        product7.pop_prudct()
                    elif(self.product_code == "3A"):
                        product8.pop_prudct()
                    elif(self.product_code == "3B"):
                        product9.pop_prudct()
                    elif(self.product_code == "3C"):
                        product10.pop_prudct()
                    elif(self.product_code == "3D"):
                        product11.pop_prudct()
                    self.checkinventory()
                    self.Confirm_button.configure(state=tkinter.DISABLED)
                else: 
                    self.label_price.configure(text="No tenemos cambio, para tu compra")
                    self.label_money.configure(text="")
                    self.Cancel_button.configure(text="Reset")
                               
            
    def checkinventory(self):
        if (product0.quantity == 0 ):
            self.label_img_pr0.configure(state=tkinter.DISABLED)
            self.code_button0.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr0.configure(state="active")
            self.code_button0.configure(state="ENABLED")
        if (product1.quantity == 0 ):
            self.label_img_pr1.configure(state=tkinter.DISABLED)
            self.code_button1.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr1.configure(state="active")
            self.code_button2.configure(state="ENABLED")
        if (product2.quantity == 0 ):
            self.label_img_pr2.configure(state=tkinter.DISABLED)
            self.code_button2.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr2.configure(state="active")
            self.code_button2.configure(state="ENABLED")
        if (product3.quantity == 0 ):
            self.label_img_pr3.configure(state=tkinter.DISABLED)
            self.code_button3.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr3.configure(state="active")
            self.code_button3.configure(state="ENABLED")
        if (product4.quantity == 0 ):
            self.label_img_pr4.configure(state=tkinter.DISABLED)
            self.code_button4.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr4.configure(state="active")
            self.code_button4.configure(state="ENABLED")
        if (product5.quantity == 0 ):
            self.label_img_pr5.configure(state=tkinter.DISABLED)
            self.code_button5.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr5.configure(state="active")
            self.code_button5.configure(state="ENABLED")
        if (product6.quantity == 0 ):
            self.label_img_pr6.configure(state=tkinter.DISABLED)
            self.code_button6.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr6.configure(state="active")
            self.code_button6.configure(state="ENABLED")
        if (product7.quantity == 0 ):
            self.label_img_pr7.configure(state=tkinter.DISABLED)
            self.code_button7.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr7.configure(state="active")
            self.code_button7.configure(state="ENABLED")
        if (product8.quantity == 0 ):
            self.label_img_pr8.configure(state=tkinter.DISABLED)
            self.code_button8.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr8.configure(state="active")
            self.code_button8.configure(state="ENABLED")
        if (product9.quantity == 0 ):
            self.label_img_pr9.configure(state=tkinter.DISABLED)
            self.code_button9.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr9.configure(state="active")
            self.code_button9.configure(state="ENABLED")
        if (product10.quantity == 0 ):
            self.label_img_pr10.configure(state=tkinter.DISABLED)
            self.code_button10.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr10.configure(state="active")
            self.code_button10.configure(state="ENABLED")
        if (product11.quantity == 0 ):
            self.label_img_pr11.configure(state=tkinter.DISABLED)
            self.code_button11.configure(state=tkinter.DISABLED)
        else:
            self.label_img_pr11.configure(state="active")
            self.code_button11.configure(state="ENABLED")    
        
    def cancelar(self):
        global coins
        coins= [0,0,0,0]
        self.entry_price.delete(0,10)
        self.entry_money.delete(0,10)
        self.label_price.configure(text="Codigo") 
        self.label_money.configure(text="Precio") 
        self.Confirm_button.configure(text="Confirmar")
        self.Cancel_button.configure(text="Cancelar")
        self.Confirm_button.configure(state="ENABLED")
        self.add_10_button.configure(state=tkinter.DISABLED)
        self.add_5_button.configure(state=tkinter.DISABLED)
        self.add_2_button.configure(state=tkinter.DISABLED)
        self.add_1_button.configure(state=tkinter.DISABLED)
        
    
    def on_closing(self, event=0):
        self.destroy()
        


if __name__ == "__main__":
    app = App()
    app.mainloop()