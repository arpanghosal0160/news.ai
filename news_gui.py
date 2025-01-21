import tkinter as tk
from tkinter import messagebox, scrolledtext
from main import handle_query
import pyttsx3
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_welcome():
    engine.say("Welcome to the News Summarizer! Please enter a topic to get started.")
    engine.runAndWait()

def fetch_and_summarize():
    # Get the query from the user input
    query = query_input.get()
    if not query.strip():
        messagebox.showwarning("Input Error", "Please enter a topic to search!")
        return

    try:
        # Update status
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Fetching news...\n")
        result_label.config(text="Fetching news, please wait...")

        # Fetch and summarize news
        summary = handle_query(query)
        output_text.insert(tk.END, f"\nSummary:\n{summary}")
        result_label.config(text="Summarization complete!")

        # Read summary aloud
        engine.say(summary)
        engine.runAndWait()
    except Exception as e:
        output_text.insert(tk.END, f"\nError: {str(e)}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        result_label.config(text="An error occurred!")

def on_submit():
    # Run summarization in a separate thread to avoid freezing the GUI
    thread = threading.Thread(target=fetch_and_summarize)
    thread.start()

# Function to clear input and output
def clear_text():
    query_input.delete(0, tk.END)
    output_text.delete(1.0, tk.END)
    result_label.config(text="")

# GUI setup
app = tk.Tk()
app.title("News Summarizer")
app.geometry("700x500")
app.configure(bg="#f2f2f2")

# Fonts and Colors
title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
bg_color = "#ffffff"
button_color = "#0078D7"
button_text_color = "#ffffff"

# Main Frame
main_frame = tk.Frame(app, bg=bg_color, padx=10, pady=10)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Welcome message
welcome_label = tk.Label(
    main_frame, text="Welcome to News Summarizer!", font=title_font, bg=bg_color, fg="#333333"
)
welcome_label.pack(pady=10)

# Input field
query_label = tk.Label(main_frame, text="Enter a topic to search:", font=label_font, bg=bg_color)
query_label.pack(anchor="w", padx=5)

query_input = tk.Entry(main_frame, width=50, font=("Helvetica", 12))
query_input.pack(pady=5, padx=5)

# Button Frame
button_frame = tk.Frame(main_frame, bg=bg_color)
button_frame.pack(pady=10)

submit_button = tk.Button(
    button_frame, text="Get News Summary", font=button_font, bg=button_color, fg=button_text_color,
    command=on_submit, padx=20, pady=5
)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame, text="Clear", font=button_font, bg="#d9534f", fg=button_text_color,
    command=clear_text, padx=20, pady=5
)
clear_button.grid(row=0, column=1, padx=10)

# Output text area
output_label = tk.Label(main_frame, text="Summary:", font=label_font, bg=bg_color)
output_label.pack(anchor="w", padx=5, pady=5)

output_text = scrolledtext.ScrolledText(main_frame, wrap="word", font=("Helvetica", 12), height=15, width=70)
output_text.pack(pady=5, padx=5)

# Status Label
result_label = tk.Label(main_frame, text="", font=("Helvetica", 10), bg=bg_color, fg="#666666")
result_label.pack(pady=5)

# Footer
footer_label = tk.Label(
    app, text="Created by [Your Name] | Powered by GNews API & Hugging Face",
    font=("Helvetica", 10), bg="#f2f2f2", fg="#666666"
)
footer_label.pack(side="bottom", pady=10)

# Speak welcome message
threading.Thread(target=speak_welcome).start()

# Run the app
app.mainloop()
