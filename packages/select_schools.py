import os
import tkinter as tk
from tkinter import ttk

def select_school(self, school): 
        # Update selected school and add to log
        self.school_var.set(school)
        self.text_editor.insert(tk.END, f"School: {school}\n")
        self.text_editor.see(tk.END)


