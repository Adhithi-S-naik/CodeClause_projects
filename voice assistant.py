import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        command = listen()

        if "stop" in command:
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hi there!")
        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
