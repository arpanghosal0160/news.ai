from transformers import pipeline

def summarize_text(text):
    # Initialize the summarizer pipeline with Pegasus-XSum
    summarizer = pipeline("summarization", model="google/pegasus-xsum", device=-1)
    
    # Calculate input length and adjust max and min lengths dynamically
    input_length = len(text.split())
    max_length = min(60, int(1.5 * input_length))  # Max length proportional to input
    min_length = max(10, int(0.5 * input_length))  # Min length proportional to input
    
    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=min_length, truncation=True)
    return summary[0]['summary_text']
