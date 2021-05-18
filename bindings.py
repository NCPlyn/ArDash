from pynput.keyboard import Key, Controller
keyboard = Controller()
import os
layout = 0

def ifFunc(serIN, bcolors, ser):
    if(serIN == "E"): #layout switcher
        ser.write('1'.encode('utf-8'))
        global layout
        if(layout == 0):
            layout = 1
        else:
            layout = 0
        print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Changing layout to "+str(layout))
    if(layout == 0):
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
    elif(layout == 1):
        if(serIN == "0"):
            print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" You pressed '0' using second layout")
        if(serIN == "4"):
            os.system("start chrome") 
            print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" opened google chrome")