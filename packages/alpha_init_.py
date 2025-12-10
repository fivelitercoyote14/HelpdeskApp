import os                                       # THIS IS HOW YOU CREATE A CLASS THAT UTILIZES ALL THE PACKAGES IN THE PACKAGE FOLDER 
import tkinter as tk
from tkinter import ttk

#class HelpdeskApp:
# This class (in the example, named HelpdeskApp) is initialized with a root parameter, presumably a tk.Tk root window that’s passed in from outside.
def alpha__init__(self, root):
        
        self.root = root #Binds the provided root window to the instance for later reference.
        self.root.title("Helpdesk Call Companion App") # Sets the title bar of the main application window.
        self.root.geometry("1024x768") # Defines the default size of the window (width x height in pixels).

        # Apply sage green theme
        self.apply_theme() #Calls an internal method (not shown in detail here)
                           #that presumably sets up a “sage green” color scheme or other style attributes for widgets in the application.


        # Create logs directory if it doesn't exist
        self.logs_dir = os.path.join(os.getcwd(), "Logs") #Constructs a path for a directory named "Logs" inside the current working directory (os.getcwd()).
        #Uses os.makedirs(..., exist_ok=True) to create that directory if it does not already exist
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create GUI elements
        self.create_widgets() #Invokes a method called create_widgets()
        #Centralizes widget creation logic instead of cluttering the constructor.

        # Initialize call count
        self.call_count = 0 #Sets up a simple integer counter (starting at zero) to track the number of helpdesk calls or interactions within the app.