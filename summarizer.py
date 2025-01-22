from transformers import pipeline

from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="google/pegasus-xsum")

    # Handle cases where input is a list
    if isinstance(text, list):
        text = " ".join(
            item.get("content", "") if isinstance(item, dict) else str(item)
            for item in text
        )

    # Ensure text is a string after processing
    if not isinstance(text, str):
        raise ValueError("Expected input to be a string after processing.")

    # Dynamically set max_length and min_length based on input length
    input_length = len(text.split())
    max_length = min(60, int(1.5 * input_length))
    min_length = max(10, int(0.5 * input_length))

    # Summarize the text
    summary = summarizer(text, max_length=max_length, min_length=min_length, truncation=True)
    return summary[0]['summary_text']
