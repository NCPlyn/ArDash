# ArDash

## A python script that I made to do this:
* Run in background with tray icon, where you can show console output, launch Binding creator app and exit entire script.
* It finds COM device with PID of Arduino Nano (you can change it in the python file) and connects to it. If connection is lost, it retries, after 5 failed attempts it kills it self.
* Waits for data to come from the Arduino serial, reads it and runs your 'if's that you generated and in the Bindind creator app.

## How to use
1. Download this repository from releases.
2. Extract it somewhere, where it will stay. (Best probs is you user folder)
3. [Download](http://go.microsoft.com/fwlink/?LinkId=863262) and install this .net framework for the Binding app
### Arduino side
1. Open the .ino file in Arduino IDE (or anywhere else where you can compile it and upload it)
2. Edit it to your desires (On default for now it has only four buttons) (Add more "if"s and print commands(print needs to have two numbers - like "01" or "84"))
3. Upload it to your Arduino and connect all buttons. (For now, in future it will have matrix for numpad)
### Python side
1. Install python3 + pip3 and add python to your PATH.
2. Install needed packages. (For now - "pip3 install pyserial pynput ansicon")
3. (Optional) Run the "createTask.bat" as ADMINISTRATOR, which makes the script run after user login with Administrator priviliges (to disable UAC when starting app using os.system for example)
4. Start the main python file - "ArDash.py". Click right on the tray icon and click on the "Launch Bindings app". Which kills the pyhton script to free the serial connection.
5. Continue to the [Wiki](https://github.com/NCPlyn/ArDash/wiki/How-to-use-Binding-creator-app) to setup the bindings.
6. Start the ArDash again using the app and close the app
7. Now you are ready to use ArDash!

## TODO
* Make the arduino use matrix from USB NumPad
* Create wiki pages
* Comment code
* Make the python code look better and *run maybe better*?
* Add new features and make ArDash more user friendly.
* Fix spelling mistakes if I did some
* ~~Make PID easily changeable~~
* ~~Properly close python when opening Binding app~~

## Videos
* Emulating keyboard: [Link](http://imgload.hys.cz/ardash/keypress.mp4)
* os.system CMD command: [Link](http://imgload.hys.cz/ardash/oscommand.mp4)
* CMD launch UAC program: [Link](http://imgload.hys.cz/ardash/programuac.mp4)
