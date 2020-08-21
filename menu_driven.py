"""
Convert the OS based program into a menu driven program using Python Code which will execute
 the required user query when user will give the input as a text.
"""

import os
import pyttsx3
import webbrowser
path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Menu Function for user to enter choices
def Menu():
    """
    Menu Function
    :return:
    """
    print("Enter your Requirements : ")
    print("1. CHROME \n 2. MEDIA PLAYER \n 3. NOTEPAD \n 4. eMAIL \n 5. CODING SITES \n 6. ONLINE GAMES ")
    print(" 7. DOWNLOAD MOVIES \n 8. YOUTUBE \n 9. VIDEO CALL \n 10. MUSIC \n 11. Code OF THIS PROGRAM")
    x = input("Enter : ")
    y = x.lower()
    if ("chrome" in y) or ("web browser" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):             # not or don't open conditions
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            os.system("chrome")
            Menu()
    elif ("media player" in y) or ("vlc" in y) or ("windows media player" in y) or ("wmplayer" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            if ("vlc" in y):
                os.system("vlc")
                Menu()
            else:
                os.system("wmplayer")
                Menu()
    elif ("text editor" in y) or ("editor" in y) or ("notepad" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            os.system("notepad")
            Menu()
    elif ("open gmail" in y) or ("gmail" in y) or ("email" in y) or ("mail" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('https://mail.google.com/')
            Menu()
    elif ("coding" in y) or ("programming" in y) or ("python" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('w3schools.com/python/default.asp')
            Menu()
    elif ("play online games" in y) or ("games" in y) or ("game" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('https://www.arkadium.com/free-online-games/')
            Menu()
    elif ("download movies" in y) or ("movies" in y) or ("movie" in y) or ("watch movie" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('http://extramovies.casa/')
            Menu()
    elif ("open youtube" in y) or ("play youtube" in y) or ("run youtube" in y) or ("youtube" in y) or ("stream youtube" in y) or ("stream video" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('https://www.youtube.com/')
            Menu()
    elif ("video call" in y) or ("videocall" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('https://duo.google.com/')
            Menu()
    elif ("play music" in y) or ("music" in y) or ("stream music" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('https://gaana.com/')
            Menu()
    elif ("github" in y) or ("code" in y) or ("see" in y) or ("show" in y):
        if ("don't" in y) or ("dont" in y) or ("not" in y) or ("stop" in y):
            pyttsx3.speak("So what do you want me to do")
            pyttsx3.speak("let's choose again")
            Menu()
        else:
            webbrowser.get(path).open_new_tab('https://github.com/puzariZ/Menu-Driven-Function/commit/edb1eb95590f46d3b32973d00fb9b4703bd3f989')
            Menu()
    elif ("exit" in y) or ("break" in y):
        return 0
    else:
        print("Invalid input enter input Correctly\n")
        pyttsx3.speak("Invalid input")
        pyttsx3.speak("enter input Correctly")
        Menu()                     # calls function again after Incorrect Input

if __name__ == '__main__':
    pyttsx3.speak("hello users")
    pyttsx3.speak("Welcome to My tools")
    pyttsx3.speak("chat with me with your requirements")
    Menu()