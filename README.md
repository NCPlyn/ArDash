# ArDash

## A python script that I made to do this:
* Run in background with tray icon, where you can show console output, launch Binding creator app and exit entire script.
* It finds COM device with PID of Arduino Nano (you can change it in the python file) and connects to it. If connection is lost, it retries, after 50 failed attempts it kills it self.
* Waits for data to come from the Arduino serial, reads it and runs your 'if's that you generated in the Bindind creator app.
* Support for two layouts (or more). (So far it's not in releases because I have to update Binding creator)

## How to use
1. Download this repository from releases.
2. Extract it somewhere, where it will stay. (Best is probably you user folder)
3. [Download](http://go.microsoft.com/fwlink/?LinkId=863262) and install this .net framework for the Binding app
### Arduino side
1. Open the .ino file in Arduino IDE (or anywhere else where you can compile it and upload it)
2. Edit it to your desires (On default for now it uses NumPad - more info at bottom)
3. Upload it to your Arduino and connect all wires.
### Python side
1. Install python3 + pip3 and add python to your PATH.
2. Install needed packages. (For now - "pip3 install pyserial pynput ansicon pystray")
3. (Optional) Run the "createTask.bat" as ADMINISTRATOR, which makes the script run after user login with Administrator priviliges (to disable UAC when starting app using os.system for example) (WARNING: IT'S BROKEN, WILL HAVE TO UPDATE TO POWERSHELL WAY)
4. Start the main python file - "ArDash.py". Click right on the tray icon and click on the "Launch Bindings app". Which kills the pyhton script to free the serial connection.
5. Continue to the [Wiki](https://github.com/NCPlyn/ArDash/wiki/How-to-use-Binding-creator-app) (TBD) to setup the bindings.
6. Start the ArDash again using the app and close the app
7. Now you are ready to use ArDash!

## Arduino wiring
* The default Arduino Code is configured for [this](https://www.aliexpress.com/item/1005001743404535.html) keyboard.
* I have connected the pins of the membrane to Arduino and put the right pins to ROWS/COLS arrays by reverse engineering the membrane.
* The original board had to be cut to fit the Arduino NANO and not cause problems while detecting keypresses.
![Soldered ArDash](http://imgload.hys.cz/ardash/IMG_20210427_181650.jpg)
### The connections points are as follow from the picture:
1. First 5 points from left are COLS, connect them to Arduino pins from 12-8
2. Then one point from the membrane connector is left out and then the last 6 points are ROWS, connect them to Arduino pins from 7-2
3. (Optional) Solder external LED to pin 13 and GND for active layout indicator.

## TODO
* ~~Make the arduino use matrix from USB NumPad~~
* Create wiki pages
* ~~Comment code~~
* Make the python code look better and *run maybe better*?
* Add more features and make ArDash more user friendly.
* Fix spelling mistakes if I did some
* ~~Make PID easily changeable~~
* ~~Properly close python when opening Binding app~~
* Fix the Binding creator app
* Fix createTask.bat

## Videos
* Emulating keyboard: [Link](http://imgload.hys.cz/ardash/keypress.mp4)
* os.system CMD command: [Link](http://imgload.hys.cz/ardash/oscommand.mp4)
* CMD launch UAC program: [Link](http://imgload.hys.cz/ardash/programuac.mp4)
* NumPad version - Final: [Link](http://imgload.hys.cz/ardash/final.mp4)
