import pyttsx3
import wikipedia

voice = pyttsx3.init()
In = input("Searching wikipedia/google:")
result = wikipedia.summary(In , sentence = 3)
print(result)
voice.say(result)
voice.runAndWait()
