from pynput.keyboard import Key, Controller
keyboard = Controller()
import os

def ifFunc(xx, bcolors):
    if(xx == 1):
        keyboard.tap(Key.pause)

    if(serIN == 2):
        os.system('taskkill /f /im Teams.exe')
    if(serIN == 3):
        os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile2')
    if(serIN == 4):
        os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile1')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU Stock done")

