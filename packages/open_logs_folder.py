import os
import tkinter as tk
from tkinter import ttk


def open_logs_folder(self):
        # Open the logs folder in the file explorer
        os.startfile(self.logs_dir)