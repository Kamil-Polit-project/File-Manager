#!/usr/bin/env python3
from tkinter import ttk
import tkinterDnD

# Window configuration
root = tkinterDnD.Tk()
root.title("File Manager")  # Set the title of the window
root.geometry('300x380')  # Set window size to 300x380
root.resizable(False, False)  # Disable window resizing
style = ttk.Style()  # Create main app style

# Tabs Controler
tabControl = ttk.Notebook(root, padding=6)
style.configure('My.TFrame', background='white')  # Set tabs background color to white

# Create tabs
general_tab = ttk.Frame(tabControl, padding=2, style='My.TFrame')
security_tab = ttk.Frame(tabControl, padding=2, style='My.TFrame')
metadata_tab = ttk.Frame(tabControl, padding=2, style='My.TFrame')
details_tab = ttk.Frame(tabControl, padding=2, style='My.TFrame')

# Add tabs to the app
tabControl.add(general_tab, text='General')
tabControl.add(security_tab, text='Security')
tabControl.add(metadata_tab, text='Metadata')
tabControl.add(details_tab, text='Details')

# Make tabs visible
tabControl.pack(expand=1, fill="both")

if __name__ == '__main__':
    root.mainloop()
