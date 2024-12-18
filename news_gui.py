import tkinter as tk
from tkinter import messagebox
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

# GUI setup
app = tk.Tk()
app.title("News Summarizer")
app.geometry("600x400")

# Welcome message
welcome_label = tk.Label(app, text="Welcome to News Summarizer!", font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=10)

# Input field
query_label = tk.Label(app, text="Enter a topic:")
query_label.pack()
query_input = tk.Entry(app, width=50)
query_input.pack(pady=5)

# Submit button
submit_button = tk.Button(app, text="Get News Summary", command=on_submit, bg="blue", fg="white")
submit_button.pack(pady=10)

# Output text area
output_text = tk.Text(app, wrap="word", height=15, width=70)
output_text.pack(pady=10)

# Run the app
app.mainloop()
