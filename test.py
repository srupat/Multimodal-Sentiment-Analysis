import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            text = recognizer.recognize_google(audio_data=C:\Users\sruja\OneDrive\Documents\Sound recordings)
            text = text.lower()

            print(f'Recognized {text}')

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()   
        continue  