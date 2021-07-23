import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

IBM_USERNAME = "apikey"
IBM_PASSWORD = "the password provided from IBM"
result = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)

try:
    print("I think you said: " + result)
except sr.UnknownValueError:
    print("I did not understand..")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

with open('recording_result.txt', mode='w') as file:
    file.write("The recognized text is :")
    file.write("\n")
    file.write(result)
print("process completed")
