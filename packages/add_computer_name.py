import os
import tkinter as tk
from tkinter import ttk

def add_computer_name(self): 
        # Add Computer Name placeholder to the log
        self.text_editor.insert(tk.END, "Computer Name: ")
        self.text_editor.see(tk.END)
        self.text_editor.focus_set()