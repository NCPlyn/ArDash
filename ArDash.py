#python script to comunicate with arduino and performs actions
#pip3 install pyserial pynput ansicon
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
print("Hiding console window quickly")
import serial
import serial.tools.list_ports
import os
import time
import sys
import ansicon
import threading
from pystray import MenuItem as item,Menu
import pystray
from PIL import Image
from pynput.keyboard import Key, Controller
keyboard = Controller()
ansicon.load()

console_toggle = True

class bcolors:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    
print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Import done")

def raise_console():
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Toggling console window")
    global console_toggle
    if console_toggle:
        # Show console
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    else:
        # Hide console
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    console_toggle = not console_toggle

def trayIcon():
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Started tray icon")
    def init_icon():
        icon = pystray.Icon('ArDash')
        icon.menu = Menu(
            item('Show console', lambda : raise_console()), item('Exit', lambda : icon.stop()), 
        )
        icon.icon = Image.open("image.png")
        icon.title = 'ArDash'
        icon.run()
    init_icon()

thread = threading.Thread(target=trayIcon)
print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Starting tray icon thread")
thread.start()

def comConnect():
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Finding PID & COM port")
    x=5
    while x!=0:
        for port in serial.tools.list_ports.comports():
            if(port.pid == 46388):
                print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Found valid PID, connecting...")
                return(port.device)
        print(bcolors.PURPLE+"[WARN]"+bcolors.ENDC+" Did not found valid PID, retrying " + str(x) + " times in 2s")
        x -= 1;
        time.sleep(2)
        if(x==0):
            print(bcolors.RED+"[ERROR]"+bcolors.ENDC+" Failed to find valid PID, terminating...")
            sys.exit()

def  doMain():
    re = comConnect()
    ser = serial.Serial(re, 9600)
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Serial connected")
    time.sleep(0.5)

    while True:
        try:
            x = ser.read(1)
            xx = x.decode('utf-8')
            if(xx == "1"):
                keyboard.press(Key.pause)
                keyboard.release(Key.pause)
                print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Discord Mute/Unmute")
            if(xx == "2"):
                os.system('taskkill /f /im Teams.exe')
                print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" Teams killed")
            if(xx == "3"):
                os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile2')
                print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU OC done")
            if(xx == "4"):
                os.system('start "" "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe" -Profile1')
                print(bcolors.CYAN+"[INFO]"+bcolors.ENDC+" GPU Stock done")
                
        except serial.serialutil.SerialException:
            print(bcolors.RED+"[ERROR]"+bcolors.ENDC+" Device disconnected, braking out of loop")
            break
    
    while True:
        print(bcolors.PURPLE+"[WARN]"+bcolors.ENDC+" We shouldn\'t be here, trying to reconnect...")
        time.sleep(0.5)
        doMain()
    
thread2 = threading.Thread(target=doMain)
print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Starting main thread")
thread2.start()

while True:
    time.sleep(1)
    if(thread.is_alive() == False or thread2.is_alive() == False):
        print(bcolors.PURPLE+"[WARN]"+bcolors.ENDC+" One of the threads is dead, killing entire script...")
        os.system('taskkill /f /pid ' + str(os.getpid()))