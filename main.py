import speech_recognition as sr
from news_fetcher import fetch_news
from summarizer import summarize_text
from text_to_speech import read_aloud

def recognize_voice():
    """
    Capture voice input and convert it into text using speech recognition.
    :return: Recognized text query
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        read_aloud("Listening for your query now. Please speak your topic.")
        print("Listening for your query...")
        try:
            audio = recognizer.listen(source, timeout=8)
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            read_aloud("Sorry, I could not understand. Please try again.")
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            read_aloud("Check your internet connection and try again.")
            print("Could not request results; check your internet connection.")
        return None

def main():
    # Welcome the user
    read_aloud("Hello! Welcome to news.ai.")
    print("Welcome to news.ai!")
    read_aloud("Please tell me what topic you want the latest news on.")
    
    # Capture voice query
    query = recognize_voice()
    if query:
        print(f"Searching news for: {query}")
        read_aloud(f"Searching for the latest news about {query}.")
        
        # Fetch and summarize news
        news_articles = fetch_news(query, max_results=3)
        if not news_articles:
            read_aloud("Sorry, no news articles were found for your topic.")
            print("No news articles found.")
            return
        
        for idx, article in enumerate(news_articles):
            print(f"\nArticle {idx+1}: {article['title']}")
            read_aloud(f"Here is article {idx+1}.")
            print("Summarizing...")
            summary = summarize_text(article['content'])
            print(f"Summary: {summary}")
            
            print("Reading aloud...")
            read_aloud(f"Article {idx+1}: {summary}")
    else:
        read_aloud("No query detected. Please try again.")
        print("No query recognized. Please try again.")

if __name__ == "__main__":
    main()
