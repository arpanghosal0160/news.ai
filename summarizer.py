from transformers import pipeline

def summarize_text(text):
    ## We are using google pegasus x-sum
    summarizer = pipeline("summarization", model="google/pegasus-xsum")
    
    # Generate the summary
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]['summary_text']
