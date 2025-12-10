import os
import tkinter as tk
from tkinter import ttk

def add_to_log_with_newline(self, value): 
        # Add dropdown selection to the log with a newline
        if value and value not in ["Select Town", "Select Device", "Select Problem", "Select Location", "Select User Type"]:
            self.text_editor.insert(tk.END, f"{value}\n")
            self.text_editor.see(tk.END)  # Auto-scroll to the end