import speech_recognition as sr
import os

while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hello! I am your Personal Assistant:\n")
        print("My name is J.A.R.V.I.S\n")
        print("What do you want me to do ?\n")
        print("I can perform the following commands:\n")
        print("\t1.Open Google Chrome")
        print("\t2.Open Mozilla Firefox")
        print("\t3.Play Music")
        print("\t4.Open the current projects directory")
        print("\t5.Shutdown")

        n=input("Press 'S' to talk to me: ")
        if n=='S' or 's':
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                if text == "open Google Chrome":
                    os.startfile('1.bat')
                    print("Done")
                elif text == "open Mozilla Firefox":
                    os.startfile('2.bat')
                    print("Done")
                elif text == "play music":
                    os.startfile('3.bat')
                    print("Done")
                elif text ==  "open the current projects directory":
                    os.startfile('4.bat')
                    print("Done")
                elif text == "shutdown":
                    print("See you soon, Bye.....")
                    break
                else:
                    print("You said", text)
                    print("Say that again I didn't get that")
            except:
                print("Sorry! Can't hear you")
                break



