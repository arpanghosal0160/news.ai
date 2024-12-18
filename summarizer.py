from transformers import pipeline

def summarize_text(text, max_length=50000000000):
    """
    Summarize text using a pre-trained summarization model.
    :param text: The text to summarize
    :param max_length: Max length of the summary
    :return: Summary text
    """
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
