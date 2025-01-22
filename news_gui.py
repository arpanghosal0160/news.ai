import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from main import handle_query
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def on_submit():
    # Get the query from the user input
    query = query_input.get()
    if not query.strip():
        messagebox.showwarning("Input Error", "Please enter a topic to search!")
        return

    try:
        # Fetch and summarize news
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Fetching news...\n")
        summary = handle_query(query)
        output_text.insert(tk.END, f"\nSummary:\n{summary}")
        
        # Read summary aloud
        engine.say(summary)
        engine.runAndWait()
    except Exception as e:
        output_text.insert(tk.END, f"\nError: {str(e)}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to clear input and output
def clear_text():
    query_input.delete(0, tk.END)
    output_text.delete(1.0, tk.END)

# GUI setup
app = tk.Tk()
app.title("News Summarizer")
app.geometry("800x600")
app.configure(bg="#2C2F33")

# Fonts and Colors
title_font = ("Helvetica", 20, "bold")
label_font = ("Helvetica", 14)
button_font = ("Helvetica", 12, "bold")
bg_color = "#2C2F33"
input_color = "#23272A"
text_color = "#FFFFFF"
button_color = "#7289DA"
button_text_color = "#FFFFFF"

# Main Frame
main_frame = tk.Frame(app, bg=bg_color, padx=10, pady=10)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Welcome message
welcome_label = tk.Label(
    main_frame, text="Welcome to News Summarizer!", font=title_font, bg=bg_color, fg="#99AAB5"
)
welcome_label.pack(pady=10)

# Input field
query_label = tk.Label(main_frame, text="Enter a topic to search:", font=label_font, bg=bg_color, fg=text_color)
query_label.pack(anchor="w", padx=5)

query_input = tk.Entry(main_frame, width=50, font=("Helvetica", 14), bg=input_color, fg=text_color, insertbackground=text_color)
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
    button_frame, text="Clear", font=button_font, bg="#99AAB5", fg=button_text_color,
    command=clear_text, padx=20, pady=5
)
clear_button.grid(row=0, column=1, padx=10)

# Output text area
output_label = tk.Label(main_frame, text="Summary:", font=label_font, bg=bg_color, fg=text_color)
output_label.pack(anchor="w", padx=5, pady=5)

output_text = scrolledtext.ScrolledText(main_frame, wrap="word", font=("Helvetica", 14), height=15, width=70, bg=input_color, fg=text_color, insertbackground=text_color)
output_text.pack(pady=5, padx=5)

# Footer
footer_label = tk.Label(
    app, text="Created by [Your Name] | Powered by GNews API & Hugging Face",
    font=("Helvetica", 10), bg=bg_color, fg="#99AAB5"
)
footer_label.pack(side="bottom", pady=10)

# Run the app
app.mainloop()
