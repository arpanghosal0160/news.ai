import speech_recognition as sr
import pyttsx3

def get_voice_input():
    """
    Capture voice input from the user.
    :return: Recognized text
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your query...")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Error connecting to speech recognition service.")
            return None

def speak_text(text):
    """
    Convert text to speech.
    :param text: The text to speak
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
