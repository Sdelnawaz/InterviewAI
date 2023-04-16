import speech_recognition as sr
from gtts import gTTS
import os

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Cloud Speech
try:
    # OPENAPI - Make API call to Google Cloud Speech API
    text = r.recognize_google(audio)
    print("You said: " + text)
    
    # convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    
    # play the audio file
    os.system("mpg321 output.mp3")

except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
