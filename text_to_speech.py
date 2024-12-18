import pyttsx3

def read_aloud(text):
    """
    Read the given text aloud using pyttsx3 text-to-speech engine.
    :param text: The text to read aloud
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust speaking speed
    engine.say(text)
    engine.runAndWait()

# Test text-to-speech
if __name__ == "__main__":
    read_aloud("Hello! This is a test of the text-to-speech functionality.")
