# TCMLobbyBBQ v1.0
# by 7 Minute Security (https://7minsec.com) with tons of help from hackern0v1c3
# A tool for making it more efficient to get into Texas Chain Saw Massacre games that ACTUALLY start

# Import all the necessary python pre-reqs
import argparse
import os
import pyautogui
import requests 
import sys
import time

# Import date/time module
from datetime import datetime

# Load ability to call the .env file with Webhook URL
from dotenv import load_dotenv
load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Defining the Webhooks
def send_webhook(message):
    my_json = {
        "content": f"{message} ({datetime.now().strftime('%I:%M:%S %p').lstrip('0')})",
        "username" : "TCMLobbyBBQ says:"
	}
    result = requests.post(WEBHOOK_URL, json = my_json)
    result.raise_for_status()
    return result

# Webhook timeout stuff
skip_time = 240
gettingstarted = True
can_webhook = True
can_webhook_matchstart = True

# pyautogui has a failsafe that, when enabled, will NOT take pyautogui actions if your mouse is in the corner of the screen.
# I personally don't care about this so I'm setting it to 'False'.  If you're having issues, you might want to set to 'True'.
pyautogui.FAILSAFE = False

# Display a menu with two choices
print("")
print("TCMLobbyBBQ v1.0 - by 7MinSec with tons of help from hackern0v1c3.")
print("This python script will help you get into lobby queues more efficiently.")
print("")
print("First, select if you want to play as family or victim:")
print("")
print("1. Family")
print("2. Victim")
print("")
# Get user input
user_input = input("Enter the number of your choice: ")

# Initialize a variable to store the user's choice
chosen_option = None

# Process the user's choice
if user_input == "1":
    chosen_option = "family"
    print(f"You chose: {chosen_option}! - kill Leland first OK?  He's annoying.  And when you do, yell 'BARGE THIS!' LOL.")
    print(f"")
elif user_input == "2":
    chosen_option = "victim"
    print(f"You chose: {chosen_option}! - Pick Danny - he's P2W FTW, amirite?  LOL.")
    print(f"")
else:
    print("Ehhhh...that's not a valid choice. Please enter 1 or 2 next time.")
    sys.exit(1)  # Exit the script with an error code

# Here's where the script actually starts doing stuff
print("Ok the TCMLobbyBBQ is about to begin!")
print("")
print("Make sure that TCM is running, and that your mouse is actively 'clicked' on the monitor where TCM is running.")
print("Otherwise basically none of this will work.")
print("")
print("I'll give you 7 seconds to do that, then I'm starting automatically!")
print("")
time.sleep(7)

while True:
# Get the current time
    thetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        pyautogui.locateOnScreen('pics/autosave.jpg', confidence=0.8)
        print("The 'Auto Save' box was found!!")
        print("Pressing 'E' key to continue now...")
        print("")
        time.sleep(.5)
        pyautogui.press('e')
        time.sleep(5)
        print("Pressing E again to get past the cool voiceover.")
        print("Love it but probably heard it a bunch LOL.")
        print("")
        pyautogui.press('e')

    except pyautogui.ImageNotFoundException:
        print("The 'The 'Auto Save' box was NOT found, which means you must be on another screen within TCM.")
        print("Moving on to see if you're at the 'A gun interactive...' screen.")
        print("")
        time.sleep(.5)
        
    try:
        pyautogui.locateOnScreen('pics/thetexascsm.jpg', confidence=0.8)
        print("The main TCM splash screen was found.")
        print("Pressing 'E' to continue now...")
        print("")
        pyautogui.press('e')
        time.sleep(5)
   
    except pyautogui.ImageNotFoundException:
        print("The main TCM splash screen was not found.")
        print("Moving on to see if you're perhaps at the main menu.")
        print("")
        time.sleep(.5)

    try:
        pyautogui.locateOnScreen('pics/mainmenu.jpg', confidence=0.8)
        print("You're at the main menu!")
        print("Pressing up a bunch of times and then 'E' to continue now...")
        print("")
        print("Then I'll pause for 5 seconds so we can get ready to choose victim or family from the next menu...")
        pyautogui.press('up')
        #time.sleep(1)
        pyautogui.press('up')
        #time.sleep(1)
        pyautogui.press('up')
        #time.sleep(1)
        pyautogui.press('up')
        #time.sleep(1)
        pyautogui.press('up')
        #time.sleep(1)
        pyautogui.press('up')
        #time.sleep(1)
        pyautogui.press('Enter')
        time.sleep(5)

    except pyautogui.ImageNotFoundException:
        print("Huh...you're not at the main TCM menu either.")
        print("Moving on to see if you're perhaps at something else...")
        print("")
        time.sleep(.5)

    try:
        pyautogui.locateOnScreen('pics/windmill.jpg', confidence=0.8)
        print("You're just about ready to start a game!")
        print("I'll choose to play as family or victim now, based on what you told me earlier!")
        print("")
        
        if chosen_option == "family":
#        if fov == "family":
            print("Let's get you setup to play family.")
            print("I'm going to hit 'up' arrow a bunch of times, and then enter.")
            print("Good luck")
            print("")
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('down')
            #time.sleep(1)
            pyautogui.press('Enter')
            time.sleep(.5)

        if chosen_option == "victim":
            print("Lets get you setup to play victim.  I'm going to hit 'up' a bunch of times, then down two times, then enter.")
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('up')
            #time.sleep(1)
            pyautogui.press('down')
            #time.sleep(1)
            pyautogui.press('down')
            #time.sleep(1)
            pyautogui.press('Enter')
            time.sleep(1)

    except pyautogui.ImageNotFoundException:
        print("I don't see the windmill on your screen!")
        print("Moving on to see if you're perhaps at something else...")
        print("")
        time.sleep(.5)

    try:
        pyautogui.locateOnScreen('pics/lobby.jpg', confidence=0.8)
        print("Oh cool!  Looks like you're in a lobby.")
        print("Good luck!")
        print("")
        time.sleep(5)
   
    except pyautogui.ImageNotFoundException:
        print("Huh, you don't seem to be waiting in a lobby.")
        print("Moving on to see if you're somewhere else...")
        print("")
        time.sleep(.5)
        
    try:
        pyautogui.locateOnScreen('pics/unabletofindsuitableplayers.jpg', confidence=0.8)
        print("Oh noes, your match didn't start? I'll press 'E' to keep this party going.")
        pyautogui.press('e')
        time.sleep(5)
        
    except pyautogui.ImageNotFoundException:
        print("Bizarre.  You didn't seem to have a network error, so what the heck is happening?")
        print("Moving on to see if you're somewhere else...")
        print("")
        time.sleep(.5)

# This section is for when the match is actually starting! 
       
    try:
        if can_webhook_matchstart:
            pyautogui.locateOnScreen('pics/matchstart.jpg', confidence=0.4)
            print("Your match is going to start soon!")
            print("")
            send_webhook("Your match is about to start as of:")
            last_webhook = time.time()
            can_webhook_matchstart = False
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")        
          
    except pyautogui.ImageNotFoundException:
        print("Huh, you don't seem to be waiting for a match to start.  That's weird.  Moving on.")
        print("")
    finally:
        if not can_webhook_matchstart and time.time() - last_webhook >= skip_time:
            can_webhook_matchstart = True


# This section is for character-specific Webhook alerts 

## Ana        
    try:
        if can_webhook:
            pyautogui.locateOnScreen('pics/ana.jpg', confidence=0.9)
            print("You're Ana!  Good luck!")
            print("")
            send_webhook("You're Ana!")
            last_webhook = time.time()
            time.sleep(0.1)
            can_webhook = False
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")        
          
    except pyautogui.ImageNotFoundException:
        print("You're not playing as Ana.  Moving on.")
        print("")
    finally:
        if not can_webhook and time.time() - last_webhook >= skip_time:
            can_webhook = True

## Connie        
    try:
        if can_webhook:
            pyautogui.locateOnScreen('pics/connie.jpg', confidence=0.9)
            print("You're playing as Connie - good luck!!")
            print("")
            send_webhook("You're Connie!")
            last_webhook = time.time()
            time.sleep(0.1)
            can_webhook = False
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        
          
    except pyautogui.ImageNotFoundException:
        print("You're not playing as Connie.  Moving on.")
        print("")
    finally:
        if not can_webhook and time.time() - last_webhook >= skip_time:
            can_webhook = True

## Julie        
    try:
        if can_webhook:
            pyautogui.locateOnScreen('pics/julie.jpg', confidence=0.9)
            print("You're playing as Julie - good luck!!")
            print("")
            send_webhook("You're Julie!!")
            last_webhook = time.time()
            time.sleep(0.1)
            can_webhook = False
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        
          
    except pyautogui.ImageNotFoundException:
        print("You're not playing as Julie.  Moving on.")
        print("")
    finally:
        if not can_webhook and time.time() - last_webhook >= skip_time:
            can_webhook = True
            
## Leland        
    try:
        if can_webhook:
            pyautogui.locateOnScreen('pics/leland.jpg', confidence=0.9)
            print("You're Leland!  Go shoulder-barge some family!!")
            print("")
            send_webhook("You're Leland!")
            last_webhook = time.time()
            time.sleep(0.1)
            can_webhook = False
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        
          
    except pyautogui.ImageNotFoundException:
        print("You're not playing as Leland.  Moving on.")
        print("")
    finally:
        if not can_webhook and time.time() - last_webhook >= skip_time:
            can_webhook = True

## Sonny        
    try:
        if can_webhook:
            pyautogui.locateOnScreen('pics/sonny.jpg', confidence=0.9)
            print("You're Sonny!  Go do...you know...whatever he does.")
            print("")
            send_webhook("You're Sonny!")
            last_webhook = time.time()
            time.sleep(0.1)
            can_webhook = False
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        
          
    except pyautogui.ImageNotFoundException:
        print("You're not playing as Sonny.  Moving on.")
        print("")
    finally:
        if not can_webhook and time.time() - last_webhook >= skip_time:
            can_webhook = True