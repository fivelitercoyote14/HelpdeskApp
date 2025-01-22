import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog, messagebox
import os


# Main Application Class
class HelpdeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Helpdesk Call Companion App")
        self.root.geometry("1024x768")

        # Apply sage green theme
        self.apply_theme()

        # Create logs directory if it doesn't exist
        self.logs_dir = os.path.join(os.getcwd(), "Logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create GUI elements
        self.create_widgets()

        # Initialize call count
        self.call_count = 0

    def apply_theme(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#556B2F")  # Sage green background
        style.configure("TLabel", background="#556B2F", foreground="white", font=("Arial", 10))
        style.configure("TButton", background="#404040", foreground="white", font=("Arial", 10), relief="flat")  # Dark gray accents
        style.map("TButton", background=[("active", "#606060")])  # Lighter gray on hover
        style.configure("TOptionMenu", background="#404040", foreground="white", relief="flat")

    def create_widgets(self):
        # Banner Section
        banner_frame = ttk.Frame(self.root)
        banner_frame.pack(fill="x")

        # Add logo/banner (Replace 'district_logo.png' and 'personal_logo.png' with your image files)
        try:
            self.logo_image = tk.PhotoImage(file="scslogo.png")
            logo_label = ttk.Label(banner_frame, image=self.logo_image, background="#556B2F")
            logo_label.pack(side="left", padx=10, pady=10)
        except Exception as e:
            print("Error loading logo:", e)

        title_label = ttk.Label(banner_frame, text="Helpdesk Call Companion", font=("Arial", 16, "bold"))
        title_label.pack(side="left", padx=10)

        created_by_label = ttk.Label(banner_frame, text="Created by Emilio Acuna-Reyes", font=("Arial", 10))
        created_by_label.pack(side="left", padx=10)

        try:
            self.personal_logo = tk.PhotoImage(file="personal_logo.png")
            personal_logo_label = ttk.Label(banner_frame, image=self.personal_logo, background="#556B2F")
            personal_logo_label.pack(side="right", padx=10, pady=10)
        except Exception as e:
            print("Error loading personal logo:", e)

        # Buttons Frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10)

        # Add Buttons
        ttk.Button(buttons_frame, text="New Call Log", command=self.new_call_log).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Save Log", command=self.save_log).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Open Logs Folder", command=self.open_logs_folder).grid(row=0, column=2, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Caller Name", command=self.add_caller_name).grid(row=0, column=3, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Computer Name", command=self.add_computer_name).grid(row=0, column=4, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Exit", command=self.root.quit).grid(row=0, column=5, padx=10, pady=5)

        # Dropdowns Frame
        dropdowns_frame = ttk.Frame(self.root)
        dropdowns_frame.pack(pady=10)

        # Dropdown menus with default value handling
        self.town_var = tk.StringVar(value="Select Town")
        self.device_var = tk.StringVar(value="Select Device")
        self.problem_var = tk.StringVar(value="Select Problem")
        self.location_var = tk.StringVar(value="Select Location")
        self.user_type_var = tk.StringVar(value="Select User Type")

        # Town Dropdown
        ttk.Label(dropdowns_frame, text="Town:").grid(row=0, column=0, padx=5, pady=5)
        self.towns = ["Select Town", "Central Office", "SSF", "Gallatin", "Hendersonville", "White House", "Portland", "Westmoreland", "Bethpage", "Goodlettsville", "Millersville", "Cottontown"]
        self.town_menu = ttk.OptionMenu(dropdowns_frame, self.town_var, self.towns[0], *self.towns, command=self.update_schools)
        self.town_menu.grid(row=0, column=1, padx=5, pady=5)

        # School Dropdown
        ttk.Label(dropdowns_frame, text="School:").grid(row=0, column=2, padx=5, pady=5)
        self.school_var = tk.StringVar(value="Select School")
        self.school_menu = ttk.OptionMenu(dropdowns_frame, self.school_var, "Select Town First")
        self.school_menu.grid(row=0, column=3, padx=5, pady=5)

        # Device Dropdown
        ttk.Label(dropdowns_frame, text="Device:").grid(row=1, column=0, padx=5, pady=5)
        devices = ["Select Device", "Windows PC", "Windows Laptop", "MacBook", "iPad", "Chromebook", "Apple TV", "Projector", "TV", "Printer", "Yodeck",
                   "Newline Display", "TV Display", "Mitel Phone", "Cameras", "SmartBoard"]
        self.device_menu = ttk.OptionMenu(dropdowns_frame, self.device_var, devices[0], *devices, command=self.add_to_log_with_newline)
        self.device_menu.grid(row=1, column=1, padx=5, pady=5)

        # Problem Dropdown
        ttk.Label(dropdowns_frame, text="Problem:").grid(row=1, column=2, padx=5, pady=5)
        problems = ["Select Problem", "Password Reset", "Add Printer", "Printer Issues", "Device Needs Set Up", "Log In Issue", "Cameras", "Warranty Request", "Phone Issue", "Adobe",
                    "Update Needed/Issues", "Network Issues","Tyler Account - Payroll", "Tyler Account - Munis", "Trust Issues", "Raptor Kiosk", "Display", "change ipad settings",
                    "Software/Apps Needed", "Reimage Needed", "account access"]
        self.problem_menu = ttk.OptionMenu(dropdowns_frame, self.problem_var, problems[0], *problems, command=self.add_to_log_with_newline)
        self.problem_menu.grid(row=1, column=3, padx=5, pady=5)

        # Location Dropdown
        ttk.Label(dropdowns_frame, text="Location:").grid(row=2, column=0, padx=5, pady=5)
        locations = ["Select Location", "Front Office", "Principal Office", "Nurse", "AP Office", "Teacher Workroom",
                     "Library", "Classroom", "Cafeteria", "Lab", "Guidance"]
        self.location_menu = ttk.OptionMenu(dropdowns_frame, self.location_var, locations[0], *locations, command=self.add_to_log_with_newline)
        self.location_menu.grid(row=2, column=1, padx=5, pady=5)

        # User Type Dropdown
        ttk.Label(dropdowns_frame, text="User Type:").grid(row=2, column=2, padx=5, pady=5)
        user_types = ["Select User Type", "Staff", "Admin", "Teacher", "Student"]
        self.user_type_menu = ttk.OptionMenu(dropdowns_frame, self.user_type_var, user_types[0], *user_types, command=self.add_to_log_with_newline)
        self.user_type_menu.grid(row=2, column=3, padx=5, pady=5)

        # Resolution Dropdown
        ttk.Label(dropdowns_frame, text="Resolution:").grid(row=3, column=0, padx=5, pady=5)
        self.resolution_var = tk.StringVar(value="Select Resolution")
        resolutions = [
            "Select Resolution",
            "Resolved on Call",
            "Waiting for Client Follow-Up",
            "Work Order Sent to Technician"
        ]
        self.resolution_menu = ttk.OptionMenu(dropdowns_frame, self.resolution_var, resolutions[0], *resolutions,
                                              command=self.add_resolution_to_log)
        self.resolution_menu.grid(row=3, column=1, padx=5, pady=5)

        # Text Editor
        self.text_editor = tk.Text(self.root, wrap="word", font=("Courier", 12), bg="#404040", fg="white", bd=2, relief="flat")
        self.text_editor.pack(expand=1, fill="both", padx=10, pady=10)

        # Add scrollbar to text editor
        self.text_scroll = tk.Scrollbar(self.text_editor, command=self.text_editor.yview)
        self.text_scroll.pack(side="right", fill="y")
        self.text_editor.config(yscrollcommand=self.text_scroll.set)

    def new_call_log(self):
        # Add a new call log entry
        self.call_count += 1
        self.text_editor.insert(tk.END, f"\n--- Call {self.call_count} ---\n")
        self.text_editor.see(tk.END)  # Auto-scroll to the end

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

    def add_to_log_with_newline(self, value):
        # Add dropdown selection to the log with a newline
        if value and value not in ["Select Town", "Select Device", "Select Problem", "Select Location", "Select User Type"]:
            self.text_editor.insert(tk.END, f"{value}\n")
            self.text_editor.see(tk.END)  # Auto-scroll to the end

    def add_caller_name(self):
        # Add Caller Name placeholder to the log
        self.text_editor.insert(tk.END, "Caller Name: ")
        self.text_editor.see(tk.END)
        self.text_editor.focus_set()

    def add_computer_name(self):
        # Add Computer Name placeholder to the log
        self.text_editor.insert(tk.END, "Computer Name: ")
        self.text_editor.see(tk.END)
        self.text_editor.focus_set()

    def update_schools(self, selected_town):
        # Update the school dropdown based on the selected town
        schools_by_town = {
            "Central Office": ["Administration", "Archives/Family Resource", "Attendance", "Benefits", "CTE", "School Health", "Finance", "Human Resources", "Instruction", "Nursing", "Nutrition", "Pupil Services", "Safe Schools", "Teacher Center", "Unity"],
            "SSF": ["Technology", "Maintenance", "Transportation", "Lawn Center", "Operations"],
            "Gallatin": ["Benny Bills Elementary", "Howard Elementary", "Guild Elementary", "Liberty Creek Elementary", "R.T. Fisher Alternative", "Station Camp Elementary", "Union STEM Elementary", "Vena Stewart Elementary", "Liberty Creek Middle", "Shafer Middle", "Rucker-Stewart Middle", "Station Camp Middle", "Gallatin High School", "Liberty Creek High School"],
            "Hendersonville": ["Beech Elementary", "George Whitten Elementary", "Gene Brown Elementary", "Indian Lake Elementary", "Jack Anderson Elementary", "Lakeside Park Elementary", "Merrol Hyde Magnet", "Nannie Berry Elementary", "Walton Ferry Elementary", "William Burrus Elementary", "Ellis Middle", "Hawkins Middle", "Knox Doss Middle", "T.W. Hunter Middle", "Hendersonville High School"],
            "White House": ["H.B. Williams Elementary", "White House Middle", "White House Intermediate", "White House High School (Main)", "White House High School (Annex)"],
            "Portland": ["Clyde Riggs Elementary", "J.W. Wiseman Elementary", "Portland Gateview Elementary", "Watt Hardison Elementary", "Portland East Middle", "Portland West Middle", "Portland High School"],
            "Westmoreland": ["North Sumner Elementary", "Westmoreland Elementary", "Westmoreland Middle", "Westmoreland High School"],
            "Bethpage": ["Bethpage Elementary"],
            "Goodlettsville": ["Madison Creek Elementary"],
            "Millersville": ["Millersville Elementary"],
            "Cottontown": ["Oakmont Elementary"]
        }

        schools = schools_by_town.get(selected_town, [])

        self.school_var.set("Select School")
        self.school_menu['menu'].delete(0, 'end')

        for school in schools:
            self.school_menu['menu'].add_command(label=school, command=lambda s=school: self.select_school(s))

        # Update the selected town without adding to the log
        if selected_town != "Select Town":
            self.town_var.set(selected_town)

    def select_school(self, school):
        # Update selected school and add to log
        self.school_var.set(school)
        self.text_editor.insert(tk.END, f"School: {school}\n")
        self.text_editor.see(tk.END)

    def add_resolution_to_log(self, resolution):
        if resolution and resolution != "Select Resolution":
            self.text_editor.insert(tk.END, f"Resolution: {resolution}\n")
            self.text_editor.see(tk.END)  # Auto-scroll to the end


# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpdeskApp(root)
    root.mainloop()
