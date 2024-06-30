"""a voice recognition program thanks 
to which we can understand several commands
create by: Feliks Voskanyan
date: 29.06.2024"""
import os
import sys
import speech_recognition as sr


def speech_rec(rec,status):
    """This is created for recognizing and doing the commands."""
    try:
        while status:
            with sr.Microphone() as source:
                print("Say something...")
                audio = rec.listen(source)
            try:
                command = rec.recognize_google(audio).lower()
                print("You have said: " + command)
                if "end the process" in command:
                    print("You ended the process")
                    status = False
                elif "open firefox" in command:
                    os.system('firefox')
                elif "open settings" in command:
                    os.system("gnome-control-center")
                elif "open writer" in command:
                    os.system("libreoffice --writer")
                elif "open librewriter" in command:
                    os.system("libreoffice")
                elif "open camera" in command:
                    os.system("cheese")
                elif "open calculator" in command:
                    os.system("gnome-calculator")
                elif "open text editor" in command:
                    os.system("gnome-text-editor")
                else:
                    print("There is no such command.")
            except sr.UnknownValueError:
                print("Speech not recognized")
            except sr.RequestError:
                print("Error in process of recognition")
    except KeyboardInterrupt:
        print("\nYou ended the code")
        sys.exit()

def main():
    """
        This is the main.
    """
    recognizer = sr.Recognizer()
    process = True
    speech_rec(recognizer,process)
main()
