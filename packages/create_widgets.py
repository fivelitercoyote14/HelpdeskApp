import os
import tkinter as tk
from tkinter import ttk



def create_widgets(self):
        # Banner Section
        banner_frame = ttk.Frame(self.root) #Creates a ttk.Frame named banner_frame and packs it horizontally (fill="x") at the top of self.root.
        banner_frame.pack(fill="x") #Serves as a “banner area” for logos, a title, and creator info.

        # Add logo/banner (Replace 'district_logo.png' and 'personal_logo.png' with your image files)
        try:
            self.logo_image = tk.PhotoImage(file="scslogo.png") #Attempts to load an image ("scslogo.png") into a tk.PhotoImage object.
            logo_label = ttk.Label(banner_frame, image=self.logo_image, background="#669999") #If successful, creates a ttk.Label that displays the image with a Mostly desaturated dark cyan background ("#556B2F").
            logo_label.pack(side="left", padx=10, pady=10) 
        except Exception as e:
            print("Error loading logo:", e) #If the file is missing or fails to load, prints an error message to the console instead of crashing.

        #Title and Creator Labels
        title_label = ttk.Label(banner_frame, text="Helpdesk Call Companion", font=("Arial", 16, "bold")) #title_label: Large, bold text for the application title.
        title_label.pack(side="left", padx=10) 

        created_by_label = ttk.Label(banner_frame, text="Created by Emilio Acuna-Reyes", font=("Arial", 10))
        created_by_label.pack(side="left", padx=10) #A smaller font label with the author name.

        try:
            self.personal_logo = tk.PhotoImage(file="personal_logo.png")
            personal_logo_label = ttk.Label(banner_frame, image=self.personal_logo, background="#556B2F")
            personal_logo_label.pack(side="right", padx=10, pady=10)
        except Exception as e:
            print("Error loading personal logo:", e)

        # Buttons Frame
        buttons_frame = ttk.Frame(self.root)# Each ttk.Button is placed on buttons_frame using the grid layout manager.
        buttons_frame.pack(pady=10)

        # Add Buttons
        ttk.Button(buttons_frame, text="New Call Log", command=self.new_call_log).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Save Log", command=self.save_log).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Open Logs Folder", command=self.open_logs_folder).grid(row=0, column=2, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Caller Name", command=self.add_caller_name).grid(row=0, column=3, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Computer Name", command=self.add_computer_name).grid(row=0, column=4, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Asset tag", command=self.add_asset_tag).grid(row=0, column=5, padx=10, pady=5)
        ttk.Button(buttons_frame, text="StudentID", command=self.add_studentID).grid(row=0, column=6, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Exit", command=self.root.quit).grid(row=0, column=7, padx=10, pady=5)

        
        # Dropdowns Frame
        dropdowns_frame = ttk.Frame(self.root)
        dropdowns_frame.pack(pady=10)

        # Dropdown menus with default value handling
        self.town_var = tk.StringVar(value="Select Town")
        self.device_var = tk.StringVar(value="Select Device")
        self.problem_var = tk.StringVar(value="Select Problem")
        self.location_var = tk.StringVar(value="Select Location")
        self.user_type_var = tk.StringVar(value="Select User Type")
        self.printer_var = tk.StringVar(value="Select Printer Issue")

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
                    "Update Needed/Issues", "Network Issues","Tyler Account - Payroll", "Tyler Account - Munis", "Trust Issues", "Raptor Kiosk", "Display", "ipad issues",
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
        user_types = ["Select User Type", "Staff", "Admin", "Teacher", "Student", "subsitute",]
        self.user_type_menu = ttk.OptionMenu(dropdowns_frame, self.user_type_var, user_types[0], *user_types, command=self.add_to_log_with_newline)
        self.user_type_menu.grid(row=2, column=3, padx=5, pady=5)

        # Resolution Dropdown
        ttk.Label(dropdowns_frame, text="Resolution:").grid(row=3, column=0, padx=5, pady=5)
        self.resolution_var = tk.StringVar(value="Select Resolution")
        resolutions = [
            "Select Resolution",
            "Resolved on Call",
            "Waiting for Client Follow-Up",
            "Work Order Sent to Technician",
            "Client will call back"
        ]
        self.resolution_menu = ttk.OptionMenu(dropdowns_frame, self.resolution_var, resolutions[0], *resolutions,
                                              command=self.add_resolution_to_log)
        self.resolution_menu.grid(row=3, column=1, padx=5, pady=5)

        # Printer Dropdown
        ttk.Label(dropdowns_frame, text="Printer Issues:").grid(row=3, column=2, padx=5, pady=5)
        self.printer_var = tk.StringVar(value="Select Issues")
        resolutions = [
            "need printer added",
            "printer has errors",
            "printer does not connect",
            "printer wont print",
            "not printing correctly"
        ]
        self.printer_menu = ttk.OptionMenu(dropdowns_frame, self.printer_var, resolutions[0], *resolutions,
                                              command=self.add_to_log_with_newline)
        self.printer_menu.grid(row=3, column=3, padx=5, pady=5)


        # Text Editor
        self.text_editor = tk.Text(self.root, wrap="word", font=("Courier", 12), bg="#404040", fg="white", bd=2, relief="flat")
        self.text_editor.pack(expand=1, fill="both", padx=10, pady=10)

        # Add scrollbar to text editor
        self.text_scroll = tk.Scrollbar(self.text_editor, command=self.text_editor.yview)
        self.text_scroll.pack(side="right", fill="y")
        self.text_editor.config(yscrollcommand=self.text_scroll.set)