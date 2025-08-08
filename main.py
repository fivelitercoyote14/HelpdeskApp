import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

# Import all functions from your packages
from packages.apply_theme import apply_theme
from packages.create_widgets import create_widgets
from packages.new_call_log import new_call_log
from packages.save_log import save_log
from packages.open_logs_folder import open_logs_folder
from packages.add_to_log_with_newline import add_to_log_with_newline
from packages.add_caller_name import add_caller_name
from packages.add_computer_name import add_computer_name
from packages.add_asset_tag import add_asset_tag
from packages.add_studentID import add_studentID
from packages.update_schools import update_schools
from packages.select_schools import select_school
from packages.add_resolution_to_log import add_resolution_to_log

# Main Application Class
class HelpdeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Helpdesk Call Companion App")
        self.root.geometry("1024x768")

        # Create logs directory if it doesn't exist
        self.logs_dir = os.path.join(os.getcwd(), "Logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        # Apply sage green theme
        apply_theme(self)

        # Create GUI elements
        create_widgets(self)

        # Initialize call count
        self.call_count = 0

    # All methods are imported and "bound" to the class
    apply_theme = apply_theme
    create_widgets = create_widgets
    new_call_log = new_call_log
    save_log = save_log
    open_logs_folder = open_logs_folder
    add_to_log_with_newline = add_to_log_with_newline
    add_caller_name = add_caller_name
    add_computer_name = add_computer_name
    add_asset_tag = add_asset_tag
    update_schools = update_schools
    select_school = select_school
    add_resolution_to_log = add_resolution_to_log
    add_studentID = add_studentID

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpdeskApp(root)
    root.mainloop()