from transformers import pipeline

def summarize_text(text):
    ## We are using google pegasus x-sum
    summarizer = pipeline("summarization", model="google/pegasus-xsum")
    
    # Generate the summary
    def summarize_text(text):
    summarizer = pipeline("summarization", model="google/pegasus-xsum", device=-1)
    input_length = len(text.split())
    # Set max_length dynamically, ensuring it's proportionate to input length
    max_length = min(60, int(1.5 * input_length))  # Example: 1.5x input length
    min_length = max(10, int(0.5 * input_length))  # Example: 0.5x input length
    summary = summarizer(text, max_length=max_length, min_length=min_length, truncation=True)
    return summary[0]['summary_text']
