from pynput.keyboard import Key, Controller
keyboard = Controller()
import os

def ifFunc(serIN, bcolors):
    if(serIN == "0"):
        keyboard.tap(Key.pause)
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Mute/Unmute Discord")
    if(serIN == "."):
        keyboard.tap(Key.media_play_pause)
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Play/pause media button")
    if(serIN == "3"):
        keyboard.tap(Key.media_next)
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Next media button")
    if(serIN == "B"):
        os.system('taskkill /f /im Teams.exe')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Killed Teams")
    if(serIN == "+"):
        os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile2')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU OC")
    if(serIN == "-"):
        os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile1')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU Stock")
    if(serIN == "N"):
        os.system('shutdown -h')
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Hibernating, app will probably not work afterwards...")
    if(serIN == "1"):
        os.system("start cmd") 
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" opened CMD")
    if(serIN == "4"):
        os.system("start explorer") 
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" opened explorer")
    if(serIN == "2"):
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.tap('m')
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Mute/Unmute Teams")
    if(serIN == "6"):
        keyboard.press(Key.cmd)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.cmd)
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" WIN-TABbed")