import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from datetime import datetime


def save_log(self): 
        # Save the current log to a uniquely named file
        log_content = self.text_editor.get("1.0", tk.END).strip()
        if not log_content:
            messagebox.showwarning("Warning", "Log is empty. Nothing to save.")
            return

        # Generate a unique filename using the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(self.logs_dir, f"log_{timestamp}.txt")

        with open(log_file, "w") as file:
            file.write(log_content)

        messagebox.showinfo("Success", f"Log saved to {log_file}")
