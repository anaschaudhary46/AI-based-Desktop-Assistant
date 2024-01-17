import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from ttkthemes import ThemedTk  # Import ThemedTk from ttkthemes
import subprocess  # Import the subprocess module for opening the web browser

# Importing the functions from the original code
from marcvoice import wishMe, takeCommand, playMusic, getWeather

# Variable to track whether the assistant is running
assistant_running = False

# Function to handle button click event
def execute_code():
    global assistant_running
    try:
        # Call the main functions from the original code
        wishMe()
        query = takeCommand().lower()
        if 'play music' in query:
            playMusic()
        elif 'weather' in query:
            getWeather()
        elif 'open google' in query:
            subprocess.run(['start', 'https://www.google.com'], shell=True)  # Use subprocess to open the default web browser
        elif 'open youtube' in query:
            subprocess.run(['start', 'https://www.youtube.com'], shell=True)
        elif 'open chat gpt' in query:
            subprocess.run(['start', 'https://chat.openai.com'], shell=True)
        elif 'open code' in query:
            subprocess.run(['start', 'C:\\Users\\Kaleem\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'], shell=True)
        
        # Stop the assistant after executing one command
        assistant_running = False

    except Exception as e:
        # Display an error message if an exception occurs
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Schedule the function to run again after 100 milliseconds (adjust as needed)
    if assistant_running:
        root.after(100, execute_code)

# Function to handle stop button click event
def stop_execution():
    global assistant_running
    # Set the flag to stop the assistant
    assistant_running = False

# Create the main GUI window using ThemedTk
root = ThemedTk(theme="equilux")  # Use the "equilux" theme
root.set_theme("arc")  # Set the "arc" theme for the white and parrot green color

root.title("Marc Assistant GUI")

# Create a button to execute the code
execute_button = ttk.Button(root, text="Start", command=lambda: execute_code())
execute_button.pack(pady=10)

# Create a button to stop execution
stop_button = ttk.Button(root, text="Stop", command=stop_execution)
stop_button.pack(pady=10)

# Create a scrolled text widget to display output (if needed)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
output_text.pack(padx=10, pady=10)

# Run the ThemedTk main loop
root.mainloop()
