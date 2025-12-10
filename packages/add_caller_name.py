import os
import tkinter as tk
from tkinter import ttk

def add_caller_name(self): 
        # Add Caller Name placeholder to the log
        self.text_editor.insert(tk.END, "Caller Name: ")
        self.text_editor.see(tk.END)
        self.text_editor.focus_set()