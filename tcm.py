# Import all the necessary python stuff
import argparse
import pyautogui
import requests 
import sys
import time

# pyautogui has a failsafe that, when enabled, will NOT take pyautogui actions if your mouse is in the corner of the screen.
# I personally don't care about this so I'm setting it to 'False'.  If you're having issues, set to 'True.'
pyautogui.FAILSAFE = False

# Display a menu with two choices
print("Select who you want to play as:")
print("1. Family")
print("2. Victim")

# Get user input
user_input = input("Enter the number of your choice: ")

# Initialize a variable to store the user's choice
chosen_option = None

# Process the user's choice
if user_input == "1":
    chosen_option = "family"
    print(f"You chose: {chosen_option}")
elif user_input == "2":
    chosen_option = "victim"
    print(f"You chose: {chosen_option}")
else:
    print("Ehhhh...that's not a valid choice. Please enter 1 or 2.")
    sys.exit(1)  # Exit the script with an error code


# Here's where the script actually starts doing stuff
print("Ok the TCMLobbySimBBQ is about to begin!")
print("")

# Helping you choose either family or victim
#while True:
#    fov = input("What do you want to play as today?  Please type 'family' or 'victim' without quotes:").lower()
#    if fov == "family":
#        print("You chose family.  Kill Leland first please LOL.\n")
#        break
#    
#
#    elif fov == "victim":
#        print("Victims!  Danny is P2W FTW, amirite?! Go tamper those valves and fuse boxes, amirite?")
#        print("")
#        break
#
#    else:
#        print("You fat-fingered something.  Please type 'family' or 'victim'")
#        print("")

print("Ok, this is important!")
print("Make sure that TCM is running, and that your mouse is actively 'clicked' on the monitor where TCM is running.")
print("Otherwise basically none of this will work.")
print("I'll give you 5 seconds to do that, then I'm starting automatically!")
print("")

while True:

    try:
        pyautogui.locateOnScreen('pics/autosave.jpg', confidence=0.8)
        print("The 'Auto Save' box was found!!")
        print("Pressing 'E' key to continue now...")
        time.sleep(1)
        pyautogui.press('e')
        time.sleep(5)
        print("Pressing E again to get past the cool voiceover.")
        print("Love it but heard it a bunch LOL.")
        pyautogui.press('e')

    except pyautogui.ImageNotFoundException:
        print("The 'The 'Auto Save' box was NOT found, which means you must be on another screen within TCM.")
        print("Moving on to see if you're at the 'A gun interactive...' screen.")
        print("")
        time.sleep(1)
        
    try:
        pyautogui.locateOnScreen('pics/thetexastcm.jpg', confidence=0.8)
        print("The main TCM splash screen was found.")
        print("Pressing 'E' to continue now...")
        print("")
        pyautogui.press('e')
   
    except pyautogui.ImageNotFoundException:
        print("The main TCM splash screen was not found.")
        print("Moving on to see if you're perhaps at the main menu.")
        print("")
        time.sleep(1)

    try:
        pyautogui.locateOnScreen('pics/mainmenu.jpg', confidence=0.8)
        print("You're at the main menu!")
        print("Pressing up a bunch of times and then 'E' to continue now...")
        print("")
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.press('Enter')
        time.sleep(1)

    except pyautogui.ImageNotFoundException:
        print("Huh...you're not at the main TCM menu either.")
        print("Moving on to see if you're perhaps at something else...")
        print("")
        time.sleep(1)

    try:
        pyautogui.locateOnScreen('pics/windmill.jpg', confidence=0.8)
        print("You're just about ready to start a game!")
        print("I'll choose family or victim based on what you told me earlier")
        print("")
        
        if chosen_option == "family":
#        if fov == "family":
            print("Let's get you setup to play family.")
            print("I'm going to hit 'up' arrow a bunch of times, and then enter.")
            print("Good luck")
            print("")
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(1)
            pyautogui.press('Enter')
            time.sleep(1)

        if chosen_option == "victim":
            print("Lets get you setup to play victim.  I'm going to hit 'up' a bunch of times, then down two times, then enter.")
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(1)
            pyautogui.press('Enter')
            time.sleep(1)

    except pyautogui.ImageNotFoundException:
        print("I don't see the windmill on your screen so you must be somewhere else!")
        print("Moving on to see if you're perhaps at something else...")
        print("")
        time.sleep(1)

    try:
        pyautogui.locateOnScreen('pics/lobby.jpg', confidence=0.8)
        print("Oh cool!  Looks like you're in a lobby.")
        print("Good luck!")
        print("")
        time.sleep(2)
        
        result = requests.post(url, json = data)
        result.raise_for_status()
        #break
        time.sleep(200)
   
    except pyautogui.ImageNotFoundException:
        print("Huh, you don't seem to be waiting in a lobby.")
        print("Moving on to see if you're somewhere else...")
        print("")
        time.sleep(1)
        
    try:
        pyautogui.locateOnScreen('pics/unabletofindsuitableplayers.jpg', confidence=0.8)
        print("Oh noes, your match didn't start? I'll press 'E' to keep this party going.")
        pyautogui.press('e')
        time.sleep(5)
        
    except pyautogui.ImageNotFoundException:
        print("Bizarre.  You didn't seem to have a network error, so what the heck is happening?")
        print("Moving on to see if you're somewhere else...")
        print("")
        time.sleep(1)