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
from bindings import ifFunc
ansicon.load()

console_toggle = True

USBPID = "B534" #if your arduinos PID is different, change it here

class bcolors:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    
print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Import done")

def raise_console(): #Show/Hide console function
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Toggling console window")
    global console_toggle
    if console_toggle:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4) #Show console
    else:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) #Hide console
    console_toggle = not console_toggle

def threadBindApp(): #Function for thread to start Binding app
    os.system('ArDashBind.exe')

def bindApp(): #Start Binding app and kill itself function
    thread3 = threading.Thread(target=threadBindApp)
    thread3.daemon = True
    thread3.start()
    print(bcolors.PURPLE+"[WARN]"+bcolors.ENDC+" Started ArDashBind app, killing ArDash to open COM port.")
    os.system('taskkill /f /pid ' + str(os.getpid()))

def trayIcon(): #Function for tray icon
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Started tray icon")
    def init_icon():
        icon = pystray.Icon('ArDash')
        icon.menu = Menu(
            item('Show console', lambda : raise_console()), item('Launch Bindings app', lambda : bindApp()), item('Exit', lambda : icon.stop()), 
        )
        icon.icon = Image.open("image.png")
        icon.title = 'ArDash'
        icon.run()
    init_icon()

thread = threading.Thread(target=trayIcon)
print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Starting tray icon thread")
thread.start()

def comConnect(): #Function to find COM port
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Finding PID & COM port")
    x=50
    while x!=0:
        for port in serial.tools.list_ports.comports():
            if(port.pid == int(USBPID, 16)):
                print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Found valid PID, connecting...")
                return(port.device)
        print(bcolors.PURPLE+"[WARN]"+bcolors.ENDC+" Did not found valid PID, retrying " + str(x) + " times in 10s")
        x -= 1;
        time.sleep(10)
        if(x==0):
            print(bcolors.RED+"[ERROR]"+bcolors.ENDC+" Failed to find valid PID, terminating...")
            sys.exit()

def  doMain():
    re = comConnect() #Get COM port
    ser = serial.Serial(re, 9600) #Connect to it - you can change baud rate here
    print(bcolors.GREEN+"[INFO]"+bcolors.ENDC+" Serial connected")
    time.sleep(0.5)

    while True:
        try:
            ifFunc(ser.read(1).decode('utf-8'), bcolors) #read 2bytes from serial and pass that to function in bindings file
        except serial.serialutil.SerialException: #if something happens with serial connection, break out of while loop
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
    if(thread.is_alive() == False or thread2.is_alive() == False): #watches threads and kills ArDash
        print(bcolors.PURPLE+"[WARN]"+bcolors.ENDC+" One of the threads is dead, killing entire script...")
        os.system('taskkill /f /pid ' + str(os.getpid()))
