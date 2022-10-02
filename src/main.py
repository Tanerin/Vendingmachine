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
    "green":"#5CE639"
}
PATH = os.path.dirname(os.path.realpath(__file__))
class product:
    def __init__ (self,name,img, price,code, quantity):
        self.name = name
        self.img = img
        self.price = price
        self.quantity = quantity
product0= product("agua-simple","Botella_01",15,"1A",5)
product1= product("agua-naranja","Botella_02",20,"1B",5)
product2= product("agua-limon","Botella_03",20,"1C",5)
product3= product("agua-uva","Botella_04",20,"1D",5)
product4= product("chocolate","Chocolate_01",12,"2A",5)
product5= product("Chocolate-fresa","Chocolate_02",12,"2B",5)
product6= product("Papas-chile","Papitas_03",18,"2C",5)
product7= product("Papas-Sal","Papitas_01",15,"2D",5)
product8= product("Cocacola","Lata_01",24,"3A",5)
product9= product("Sprite","Lata_04",24,"3B",5)
product10= product("Papas-Queso","Papitas_02",18,"3C",5)
product11= product("Papas-Picantes","Papitas_04",22,"3D",5)
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
        self.Cancel_button = customtkinter.CTkButton(master= self.frame_right, fg_color=theme["red"], width=200, height=50, corner_radius=50, border_width=0, text="Cancelar")
        self.Cancel_button.grid(row=2, column=0, pady=5, padx=20, sticky="nw")
        self.Confirm_button = customtkinter.CTkButton(master= self.frame_right, fg_color=theme["green"], width=200, height=50, corner_radius=50, border_width=0, text="Confirmar")
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

        
        self.code_button0=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1A",text_color=theme["white"])
        self.code_button0.grid(row= 1, column= 1, pady=5, padx=5, sticky="nwes")
        self.code_button1=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1B",text_color=theme["white"])
        self.code_button1.grid(row= 1, column= 2, pady=5, padx=5, sticky="nwes")
        self.code_button2=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1C",text_color=theme["white"])
        self.code_button2.grid(row= 1, column= 3, pady=5, padx=5, sticky="nwes")
        self.code_button3=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="1D",text_color=theme["white"])
        self.code_button3.grid(row= 1, column= 4, pady=5, padx=5, sticky="nwes")
        self.code_button4=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2A",text_color=theme["white"])
        self.code_button4.grid(row= 2, column= 1, pady=5, padx=5, sticky="nwes")
        self.code_button5=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2B",text_color=theme["white"])
        self.code_button5.grid(row= 2, column= 2, pady=5, padx=5, sticky="nwes")
        self.code_button6=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2C",text_color=theme["white"])
        self.code_button6.grid(row= 2, column= 3, pady=5, padx=5, sticky="nwes")
        self.code_button7=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="2D",text_color=theme["white"])
        self.code_button7.grid(row= 2, column= 4, pady=5, padx=5, sticky="nwes")
        self.code_button8=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3A",text_color=theme["white"])
        self.code_button8.grid(row= 3, column= 1, pady=5, padx=5, sticky="nwes")
        self.code_button9=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3B",text_color=theme["white"])
        self.code_button9.grid(row= 3, column= 2, pady=5, padx=5, sticky="nwes")
        self.code_button10=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3C",text_color=theme["white"])
        self.code_button10.grid(row= 3, column= 3, pady=5, padx=5, sticky="nwes")
        self.code_button11=  customtkinter.CTkButton(master= self.pad_frame, fg_color=theme["dg_blue"], width=60, height=60, corner_radius=60, border_width=0, text="3D", text_color=theme["white"])
        self.code_button11.grid(row= 3, column= 4, pady=5, padx=5, sticky="nwes")
        
        #=========== Create buttons for add money ==========
        self.add_10_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$10", text_color=theme["white"])
        self.add_10_button.grid(row=4, column=0, pady=40, padx= 40, sticky="nw")
        self.add_5_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$5", text_color=theme["white"])
        self.add_5_button.grid(row=5, column=0, pady=40, padx= 40, sticky="nw")
        self.add_2_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$2", text_color=theme["white"])
        self.add_2_button.grid(row=4, column=1, pady=40, padx= 40, sticky="ne")
        self.add_1_button= customtkinter.CTkButton(master=self.frame_right, fg_color=theme["blue"], width=100, height=100, corner_radius=100, border_width=0, text="$1", text_color=theme["white"])
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
        
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()