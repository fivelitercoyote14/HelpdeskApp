import os
import tkinter as tk
from tkinter import ttk


def new_call_log(self):
        # Add a new call log entry
        self.call_count += 1
        self.text_editor.insert(tk.END, f"\n--- Call {self.call_count} ---\n")
        self.text_editor.see(tk.END)  # Auto-scroll to the end
