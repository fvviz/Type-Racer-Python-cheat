from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pynput.keyboard import Controller , Key
import time
import pyfiglet

# GET ALL THE CSS SELECTORS
OnlineRace_ID = "#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a"
PracticeGame_ID = "#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a"
PlayWithFriends_ID = "#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a"
Text_ID = ".inputPanel > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)"

#SET UP THE WEB DRIVER
driver = webdriver.Chrome(executable_path=r"C:\Users\home\PycharmProjects\TypeRacer Hack\webdrivers\chromedriver.exe") #PATH TO YOUR CHROMEDRIVER.EXE
driver.get("http://play.typeracer.com/")

# DEFINE A FUNCTION TO START A GAME AND COPY THE TEXT
def Game(Game_ID,Text_ID):
    start = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_css_selector(Game_ID)) # FIND THE GAME MODE USING THE CSS SELECTOR CODE
    start.click() # CLICK ON THE GAME MODE
    TextBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(Text_ID)) # FIND THE TEXT USING THE CSS SELECTOR CODE OF THE TEXT

# PRINT A HUGE BANNER
header = pyfiglet.figlet_format(text="TYPERACER HACKER")
print(header)

# PRINT OPTIONS
print("(1): Start a typerace // "
      "Get matched up with online opponents")
print(""
      ""
      ""
      "(2): Practice mode // "
      "Improve your typing skills on your own")
print(""
      ""
      ""
      "(3): Race with friends // "
      "Invite people to a private race with chat")

# LET THE USER SELECT AN OPTION BY ENTERING A NUMBER
option = input("Select an option (1/2/3):")

# START THE SELECTED GAME MODE 
if option == "1":
    Game(OnlineRace_ID,Text_ID)
if option == "2":
    Game(PracticeGame_ID,Text_ID)
if option == "3":
    Game(PracticeGame_ID, Text_ID)

# GET THE TEXT FROM THE TYPE RACE
Text = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(Text_ID))


print(""
      ""
      "obtained text")

# SET UP THE KEYBOARD
keyboard = Controller()
print(""
      ""
      "keyboard configured")

# ASK THE USER IF THEY ARE READY TO START THE GAME
GameStart = input(""
                  ""
                  ""
                  "Do you want to start(y/n):")

# IF THE USER TYPES IN Y , START TYPING THE TEXT GIVEN IN THE TYPERACER GAME 

if GameStart == "y":
    time.sleep(3) # START TYPING WITHIN 3 SECONDS
    for i in Text.text:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.08) # TYPE ALL THE CHRARACTERS WITH AN INTERVAL OF 0.08 SECONDS , THIS TIME CAN BE CHANGED ACCORDING TO YOUR NEEDS . DONT MAKE IT TOO SMALL OR THE GAME WILL DETECT THE HACK
    print(TextBox.text)

else:
    driver.quit()
