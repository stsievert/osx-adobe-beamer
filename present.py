from __future__ import division
import Tkinter as tk
from applescript import AppleScript

def nextSlide(keycode):
    scpt = """
    on send_key()
            delay 0.3
            tell application "System Events" to key code {0}
    end send_key

    on switch_windows()
            delay 0.3
            tell application "System Events" to key code 50 using """.format(keycode)\
            +r'{command down}'+"""
    end switch_windows

    activate application "Adobe Reader"
    tell application "Adobe Reader" to activate

    send_key()
    switch_windows()
    send_key()

    tell application "System Events" to key code 48 using {command down}

    #activate application "python"
    """
    AppleScript(scpt).run()

def onKeyPress(event):
    # space, arrows, return, shift
    keys = {'space'   : 49,
            'Return'  : 36,
            'Tab'     : 48,
            'Shift_L' : 56,
            'Shift_R' : 56,
            'Left'    : 123,
            'Right'   : 124,
            'Down'    : 125,
            'Up'      : 126}
    key = event.keysym
    if key in keys.keys():
        #text.insert('end', 'You pressed {0} resulting in {1}\n'.format(event.keysym, keys[event.keysym]))
        print key
        nextSlide(keys[key])

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x400')
    text = tk.Text(root)
    text.pack()

    text.insert('end', """
    # osx-adobe-beamer
    ## Usage directions
    1. Open up notes.pdf and presentation.pdf in Adobe Reader 
       (and nothing else!)
    2. Run command `python present.py`
    3. Make the window that pops up in front/active
    4. User standard keybindings for Adobe Reader
        (arrows/space/return supported)
    
    ## Tips
    1. You can fix any errors (ie notes/presentation off)in this script; 
       when the osx-adobe-beamer window is open it only sends your keys to Adobe.
    2. Don't put the notes in full screen -- the window of osx-adobe-beamer
       needs to be active!

    ## Notes:
    1. Keep osx-adobe-beamer (aka python) and Adobe Reader the last 
       two application open (don't open other applications)
    2. Do not open other files with Adobe Reader.
    3. Set up and test this script before hand! If you run into a problem,
       adbondon this script.
    """)

    root.bind('<KeyPress>', onKeyPress)
    root.mainloop()
