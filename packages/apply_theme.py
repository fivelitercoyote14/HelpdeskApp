from tkinter import ttk


def apply_theme(self): #Typically called as a method of some class. It doesn’t require arguments beyond self, which gives it access to the instance context if needed elsewhere.
        style = ttk.Style() #Instantiates a ttk.Style object, which lets you configure theme elements in a Tkinter application.
        style.theme_use("clam") #Tells Tkinter to use the built-in “clam” theme as a base.
        style.configure("TFrame", background="#669999")  # Mostly desaturated dark cyan | TFrame is the ttk.Frame widget style name.
        style.configure("TLabel", background="#669999", foreground="white", font=("Arial", 10)) #Background set to the same Mostly desaturated dark cyan.Text (foreground) set to white
        style.configure("TButton", background="#404040", foreground="white", font=("Arial", 10), relief="flat")  # Dark gray accents A relief="flat" look, which removes the typical 3D border effect.
        style.map("TButton", background=[("active", "#606060")])  # Lighter gray on hover .map allows you to specify different style options depending on widget states (e.g., active, disabled, pressed).
        #This line sets the button’s background to a lighter gray (#606060) when hovered or clicked (“active”).
        style.configure("TOptionMenu", background="#404040", foreground="white", relief="flat")

        """Tweak the ttk.OptionMenu widget style:
        Dark gray background.
        White text.
        Flat look (no 3D border)"""

