# TCMLobbyBBQ v1.1
# by 7 Minute Security (https://7minsec.com) with tons of help from hackern0v1c3
# A tool for making it more efficient to get into Texas Chain Saw Massacre games that ACTUALLY start (what a concept!)

# Import all the necessary python pre-reqs
import argparse
import os
import pyautogui
import requests 
import smtplib
import sys
import time

# Import date/time module
from datetime import datetime

# Import some email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

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
duration = 30
can_webhook = True
can_webhook_matchstart = False
matchstart = False
start_time = time.time()

# Define email config
def send_email(subject, body, attachment_path=None):
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    
    # Define sender and recipient email addresses
    sender_email = "alerts@braimee.com"  # Replace with your email address
    recipient_email = "braimee@gmail.com"  # Replace with the recipient's email address

    # Create MIMEMultipart object
    message = MIMEMultipart()

    # Attach body as plain text
    message.attach(MIMEText(body, "plain"))

    # Define structure of email message
    message["Subject"] = f"{subject} - {thetime}" 
    message["From"] = sender_email
    message["To"] = recipient_email

    # Attach file if provided
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part["Content-Disposition"] = f"attachment; filename={os.path.basename(attachment_path)}"
            message.attach(part)

    # Connect to the SMTP server    
    with smtplib.SMTP(smtp_server, smtp_port) as server:  # Use port 587 for TLS. FIX AND PASS PORT VARIABLE!
        server.starttls()
        server.login(email_user, email_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

# Define a file attachment (in this case it's the pics/temp.jpg file that will be captured once you actually get into a lobby)
file_path = "pics/temp.jpg"

# Defining multiple .env variables so we can check later to see if email alerts should fire
mail_vars = ["EMAIL_USER", "EMAIL_PASSWORD"]
mail_send = True

for mail_var in mail_vars:
    if os.getenv(mail_var) is not None:
        mail_check = True
    else:
        mail_check = False

# pyautogui has a failsafe that, when enabled, will NOT take pyautogui actions if your mouse is in the corner of the screen.
# I personally don't care about this so I'm setting it to 'False'.  If you're having issues, you might want to set to 'True'.
pyautogui.FAILSAFE = False

# Display a menu with two choices: Family or Victim
print("")
print("\033[0;34mTCMLobbyBBQ v1.1 - by 7MinSec with tons of help from hackern0v1c3.\033[m")
print("\033[0;34mThis python script will help you get into lobby queues more efficiently.\033[m")
print("")
print("\033[0;34mFirst, select if you want to play as family or victim:\033[m")
print("")
print("\033[0;34m1. Family\033[0;34m")
print("\033[0;34m2. Victim\033[m")
print("")
# Get user input
user_input = input("Enter the number of your choice: ")
print("")

# Initialize a variable to store the user's choice
chosen_option = None

# Process the user's choice
if user_input == "1":
    chosen_option = "family"
    print(f"\033[0;93mYou chose: {chosen_option}! (Kill Leland first OK?  He's annoying.  And when you do, yell 'BARGE THIS!' LOL)\033[0;34m")
    print(f"")
    time.sleep(3)
elif user_input == "2":
    chosen_option = "victim"
    print(f"\033[0;93mYou chose: {chosen_option}! (Maybe pick Danny or Virginia - they're P2W FTW, amirite?  LOL)\033[0;34m")
    print(f"")
    time.sleep(3)
else:
    print("Ehhhh...that's not a valid choice. Please enter 1 or 2 next time.")
    sys.exit(1)  # Exit the script with an error code

# Here's where the script actually starts doing stuff
print("\033[0;34mOk the TCMLobbyBBQ is about to begin!\033[m")
print("")
print("\033[0;34mMake sure that TCM is running, and that your mouse is actively 'clicked' on the monitor where TCM is running.\033[m")
print("")
print("\033[0;34mI'll give you 7 seconds to do that, then I'm starting automatically!\033[m")
print("")
time.sleep(7)

# In case we ever need to completely restart the loop, we call "restart_program"
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

while True:
# Get the current time
    thetime = datetime.now().strftime('%I:%M:%S %p').lstrip('0')

# Set an initial player value of none
    player = None

    if can_webhook:
        try:
            pyautogui.locateOnScreen('pics/autosave.jpg', confidence=0.8)
            print("\033[1;32mThe 'Auto Save' box was found!!\033[m")
            print("\033[1;32mPressing 'E' key to continue now...\033[m")
            print("")
            time.sleep(.5)
            pyautogui.press('e')
            time.sleep(5)
            print("\033[1;32mPressing E again to get past the cool voiceover.\033[m")
            print("\033[1;32mLove it but probably heard it a bunch LOL.\033[m")
            print("")
            pyautogui.press('e')
            time.sleep(5)
            print("\033[1;32mWaiting another 5 seconds to hit the main TCM menu.\033[m")

        except pyautogui.ImageNotFoundException:
            print("\033[0;31mThe 'Auto Save' box was NOT found, which means you must be on another screen within TCM.\033[m")
            print("\033[0;31mMoving on!\033[m")
            print("")
            time.sleep(.5)
        
        try:
            pyautogui.locateOnScreen('pics/thetexascsm.jpg', confidence=0.8)
            print("\033[1;32mThe main TCM splash screen was found.\033[m")
            print("\033[1;32mPressing 'E' to continue now...\033[m")
            print("")
            pyautogui.press('e')
            time.sleep(5)
   
        except pyautogui.ImageNotFoundException:
            print("\033[0;31mThe main TCM splash screen was not found.\033[m")
            print("\033[0;31mMoving on to see if you're perhaps at the main menu.\033[m")
            print("")
            time.sleep(.5)

        try:
            pyautogui.locateOnScreen('pics/mainmenu.jpg', confidence=0.8)
            print("\033[1;32mYou're at the main menu.\033[m")
            print("\033[1;32mPressing up a bunch of times and then 'E' to continue now...\033[m")
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
            print("\033[0;31mHuh...you're not at the main TCM menu either.\033[m")
            print("\033[0;31mMoving on to see if you're perhaps at something else...\033[m")
            print("")
            time.sleep(.5)

        try:
            pyautogui.locateOnScreen('pics/windmill.jpg', confidence=0.8)
            print("\033[1;32mYou're just about ready to start a game!\033[m")
            print("")
            print("\033[1;32mI'll choose to play as family or victim now, based on what you told me earlier!\033[m")
            print("")
            
         
            if chosen_option == "family":
                print("\033[1;32mLet's get you ready to play family!\033[m")
                print("\033[1;32mI'm going to hit 'Up' arrow a bunch of times, and then 'Enter'.\033[m")
                print("\033[1;32mGood luck!\033[m")
                print("")
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('down')
                pyautogui.press('Enter')
                time.sleep(.5)
                print("\033[1;32mI'm also going to just snooze for like 30 seconds because match-making takes a while...\033[m")
                print("")
                time.sleep(30)

            if chosen_option == "victim":
                print("\033[1;32mLets get you setup to play victim.  I'm going to hit 'Up' a bunch of times, then 'Down' two times, then 'Enter.'\033[m")
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('Enter')
                time.sleep(.5)
                print("\033[1;32mI'm also going to just snooze for like 30 seconds because match-making takes a while...\033[m")
                time.sleep(30)
                
        except pyautogui.ImageNotFoundException:
            print("\033[0;31mI don't see the windmill on your screen!\033[m")
            print("\033[0;31mMoving on to see if you're perhaps at something else...\033[m")
            print("")
            time.sleep(.5)   
        
        try:
            pyautogui.locateOnScreen('pics/unabletofindsuitableplayers.jpg', confidence=0.8)
            print("\033[1;32mOh noes, your match didn't start? I'll press 'E' to keep this party going.\033[m")
            time.sleep(2)
            pyautogui.press('e')
            time.sleep(5)
        
        except pyautogui.ImageNotFoundException:
            print("\033[0;31mDoesn't seem like you're having a network error, so I'm moving on to see if you're somewhere else...\033[m")
            print("")
            time.sleep(.5)
            
        try:
            pyautogui.locateOnScreen('pics/findingmatch.jpg', confidence=0.8)
            print("\033[1;32mLooks like you're waiting to get into a lobby.  I'm going to sleep for like 15 seconds to give myself a breather.\033[m")
            print("")
            time.sleep(15)
        
        except pyautogui.ImageNotFoundException:
            print("\033[0;31mDoesn't seem like you're at the matchmaking screen, so I'll keep trying to find you...\033[m")
            print("")
            time.sleep(.5)
        
# This section is for character-specific Webhook alerts 
        if chosen_option == "victim":
        # Try Ana
            try:
                pyautogui.locateOnScreen('pics/ana.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Ana"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Ana!")
                can_webhook_matchstart = True

            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Ana, so I'm moving on.\033[m")
                print("")
            
        # Try Connie
            try:
                pyautogui.locateOnScreen('pics/connie.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Connie"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Connie!")
                can_webhook_matchstart = True
            
            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Connie, so I'm moving on.\033[m")
                print("")
                                
        # Try Julie
            try:    
                pyautogui.locateOnScreen('pics/julie.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Julie"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Julie!")
                can_webhook_matchstart = True

            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Julie, so I'm moving on.\033[m")
                print("")    
            
        # Try Leland
            try:
                pyautogui.locateOnScreen('pics/leland.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Leland"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Leland!")
                can_webhook_matchstart = True

            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Leland, so I'm moving on.\033[m")
                print("")    
            
        # Try Sonny
            try:    
                pyautogui.locateOnScreen('pics/sonny.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Sonny"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Sonny!")
                can_webhook_matchstart = True
        
            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Sonny, so I'm moving on.\033[m")
                print("")    
            
        if chosen_option == "family":  
        
        # Try Cook
            try:
                pyautogui.locateOnScreen('pics/cook.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Cook"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Cook!")
                can_webhook_matchstart = True
            
            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Cook, so I'm moving on.\033[m")
                print("")        
            
        # Try Leatherface
            try:
                pyautogui.locateOnScreen('pics/leatherface.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Leatherface"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Leatherface!")
                can_webhook_matchstart = True

            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Leatherface, so I'm moving on.\033[m")
                print("")

        # Try Sissy
            try:    
                pyautogui.locateOnScreen('pics/sissy.jpg', confidence=0.9)
                pyautogui.screenshot('pics/temp.jpg')
                player = "Sissy"
                print(f"\033[1;32mYou're {player}!\033[m")
                print("")
                send_webhook("You're Sissy!")
                can_webhook_matchstart = True
        
            except pyautogui.ImageNotFoundException:
                print(f"\033[0;31mYou don't seem to be Sissy, so I'm moving on.\033[m")
                print("")


    if player is not None and can_webhook and mail_check:
        try:
            print(f"\033[0;33mEmail is configured, sending you an email letting you know you're {player}!\033[m")
            print("")
            custom_subject = f"You're {player}!!"
            custom_body = "Good luck!"
            send_email(custom_subject, custom_body, file_path)
            can_webhook = False
        
        except NameError:
            print("Player not defined properly  ...moving on.")
    
# This section is for when the match is actually starting! 
         
    if player is not None and not matchstart:
        duration = 180
        start_time = time.time()
        while time.time() - start_time < duration:
            try:
                remaining_time = duration - (time.time() - start_time)
                pyautogui.locateOnScreen('pics/matchstart.jpg', confidence=0.4)            
                print("\033[1;32mYour match is going to start soon!\033[m")
                print("")
                send_webhook("Your match is about to start as of:")
                matchstart = True
                break
            
            except pyautogui.ImageNotFoundException:
                print("\033[0;33mWelp, you've been in a lobby and selected a character, but I don't think your match has started.\033[m")
                print("")
                print(f"\033[0;33mI'm going to keep waiting for 3 minutes to see if the match starts.\033[m")
                print("")
                print(f"\033[0;33mEvery 10 seconds I'll check to see if your match is starting,\033[m") 
                print(f"\033[0;33mand give you an update on how much time we have left to wait.\033[m")
                print("")
                print(f"\033[0;33mAfter 3 minutes is up, if the match STILL hasn't started, I'll restart the script entirely.\033[m")
                print("")
                print("\033[0;33m---\033[m")
                print(f"\033[0;33mTime left to wait before script starts over: {remaining_time:.2f} seconds.\033[m")
                print("")
                print("")
                print("")
                print("")
                time.sleep(10)
                
            if time.time() - start_time >= duration:
                print(f"\033[0;33mHmmm, that's a mystery.  Doesn't seem like your match started in {duration} seconds.  I'm going to start completely fresh and run through the script again.\033[m")
                print("")
                can_webhook = True
                player = None
            
    if matchstart and mail_check:
        custom_subject = "OMg your match is starting!"
        custom_body = "If you're a victim, be sure to make lots of noise right away so grandpa wakes up immediately, amirite?"
        send_email(custom_subject,custom_body)
            
    if matchstart:
        try:
            print("\033[1;32mNow that your match is starting,\033[m")
            print("\033[1;32mI'm going to pause the script until the match is over.\033[m")
            print("\033[1;32mThat way your PC isn't wasting cycles for no reason.\033[m")
            print("")   
            print("\033[1;32mWhen your match is over, please go ahead and\033[m")
            input("\033[1;32mpress ENTER to continue.  That will start this script loop over!\033[m") 
            print("")
            print("\033[1;32mOk make sure you are clicked into the monitor where TCM is running!\033[m")
            print("\033[1;32mWe will fire the script back up again in 10 seconds!\033[m")
            print("")
            can_webhook = True
            matchstart = False
            countdown_duration = 10
            print("")
 
            # Display a 10-second countdown
            for seconds in range(countdown_duration, 0, -1):
                print(f"\033[1;32mStarting again in...{seconds}\033[m")
                print("")
                time.sleep(1)
          
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")