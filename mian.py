import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox
import os


# Main Application Class
class HelpdeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Helpdesk Call Companion App")
        self.root.geometry("800x600")

        # Create logs directory if it doesn't exist
        self.logs_dir = os.path.join(os.getcwd(), "Logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Helpdesk Call Companion", font=("Arial", 16))
        title_label.pack(pady=10)

        # Buttons Frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        # Add Buttons
        tk.Button(buttons_frame, text="New Call Log", command=self.new_call_log).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(buttons_frame, text="Save Log", command=self.save_log).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(buttons_frame, text="Open Logs Folder", command=self.open_logs_folder).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(buttons_frame, text="Exit", command=self.root.quit).grid(row=0, column=3, padx=10, pady=5)

        # Dropdowns Frame
        dropdowns_frame = tk.Frame(self.root)
        dropdowns_frame.pack(pady=20)

        # School Dropdown
        tk.Label(dropdowns_frame, text="School:").grid(row=0, column=0, padx=5, pady=5)
        self.school_var = tk.StringVar(value="Select School")
        schools = ["School A", "School B", "School C"]
        school_menu = tk.OptionMenu(dropdowns_frame, self.school_var, *schools, command=self.add_to_log)
        school_menu.grid(row=0, column=1, padx=5, pady=5)

        # Device Dropdown
        tk.Label(dropdowns_frame, text="Device:").grid(row=0, column=2, padx=5, pady=5)
        self.device_var = tk.StringVar(value="Select Device")
        devices = ["Windows PC", "Windows Laptop", "MacBook", "iPad", "Chromebook"]
        device_menu = tk.OptionMenu(dropdowns_frame, self.device_var, *devices, command=self.add_to_log)
        device_menu.grid(row=0, column=3, padx=5, pady=5)

        # Problem Dropdown
        tk.Label(dropdowns_frame, text="Problem:").grid(row=0, column=4, padx=5, pady=5)
        self.problem_var = tk.StringVar(value="Select Problem")
        problems = ["Network Issue", "Hardware Failure", "Software Bug"]
        problem_menu = tk.OptionMenu(dropdowns_frame, self.problem_var, *problems, command=self.add_to_log)
        problem_menu.grid(row=0, column=5, padx=5, pady=5)

        # Text Editor
        self.text_editor = tk.Text(self.root, wrap="word", font=("Courier", 12))
        self.text_editor.pack(expand=1, fill="both", padx=10, pady=10)

    def new_call_log(self):
        # Add a new call log entry
        current_text = self.text_editor.get("1.0", tk.END).strip()
        call_number = current_text.count("Call") + 1
        self.text_editor.insert(tk.END, f"\n--- Call {call_number} ---\n")


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

    def open_logs_folder(self):
        # Open the logs folder in the file explorer
        os.startfile(self.logs_dir)

    def add_to_log(self, value):
        # Add dropdown selection to the log
        self.text_editor.insert(tk.END, f"{value}\n")

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpdeskApp(root)
    root.mainloop()
