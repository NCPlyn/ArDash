from pynput.keyboard import Key, Controller
keyboard = Controller()
import os

def ifFunc(serIN, bcolors):
    if(serIN == "1"):
        keyboard.tap(Key.pause)
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Mute/Unmute discord")
    if(serIN == "2"):
        os.system('taskkill /f /im Teams.exe')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Killed Spotify")
    if(serIN == "3"):
        os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile2')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU OC done")
    if(serIN == "4"):
        os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile1')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU Stock done")
