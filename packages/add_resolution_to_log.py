import os
import tkinter as tk
from tkinter import ttk

def add_resolution_to_log(self, resolution): 
        if resolution and resolution != "Select Resolution":
            self.text_editor.insert(tk.END, f"Resolution: {resolution}\n")
            self.text_editor.see(tk.END)  # Auto-scroll to the end
