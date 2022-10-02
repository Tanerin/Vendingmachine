# Equipo 6
import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
theme= {
    "red":"#E63946",
    "lg_blue":"#A8DADC",
    "dg_blue":"#1D3557",
    "blue":"#457B9D",
    "green":"#5CE639"
}

class App(customtkinter.CTk):

    WIDTH = 1920
    HEIGHT = 1080

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry("1920x1080")
        

        # ============ create two frames ============

        # configure grid layout (2x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=1200,height=1030, corner_radius=0, fg_color=theme["lg_blue"])
        self.frame_left.grid(row=1, column=0, sticky="nw")
        
        self.frame_right = customtkinter.CTkFrame(master=self, width=720,height=1030, corner_radius=0, fg_color=theme["green"])
        self.frame_right.grid(row=1, column=1, sticky="nwse")
        
        self.frame_top = customtkinter.CTkFrame(master=self, width=1920,height=50, corner_radius=0, fg_color=theme["red"])
        self.frame_top.grid(row=0, column=0, sticky="nw")

        


if __name__ == "__main__":
    app = App()
    app.mainloop()