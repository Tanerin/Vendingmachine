# Equipo 6
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
from PIL import Image, ImageTk
class MainWindow():
    def __init__(self, root, title, geometry, message):
        pass

class Widget_Canva ():
    def __init__(self,  size, row, column, master):
        myFrame = Frame(master)
        myFrame.grid(row= row, column = column)       
        

class Widget_Button_IMG():
    def __init__(self, row, column, master, size, image, command, text, width, height, compound, fg_color, bg_color, hover_color):
        button_img = ImageTk.PhotoImage(Image.open("img/"+image).resize((size), Image.ANTIALIAS))
        myButton = customtkinter.CTkButton(master= master, image=button_img, text= text, width = width, height = height, compound= compound,
            fg_color=fg_color, bg_color=bg_color, hover_color= hover_color)
        myButton.grid(row = row, column = column)

class Widget_Button():
    def __init__(self, row, column, master, size, command, text, width, height, fg_color, bg_color, hover_color):
        myButton = customtkinter.CTkButton(master= master, text= text, width = width, height = height, fg_color=fg_color, bg_color=bg_color, 
            hover_color= hover_color)
        myButton.grid(row = row, column = column)
        

class Entry():
    def __init__(self, row, column, master, image):
        pass
class Icon():
    def __init__(self, row, column, master, image):
        pass

e = Widget_Canva("500x500", 1, 1,root)
b = Widget_Canva("200x200", 2, 1,root)

root.mainloop()