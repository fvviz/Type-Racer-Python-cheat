from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pynput.keyboard import Controller , Key
import time
import pyfiglet

OnlineRace_ID = "#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a"
PracticeGame_ID = "#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a"
PlayWithFriends_ID = "#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a"

Text_ID = ".inputPanel > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)"


driver = webdriver.Chrome(executable_path=r"C:\Users\home\PycharmProjects\TypeRacer Hack\webdrivers\chromedriver.exe")
driver.get("http://play.typeracer.com/")


def Game(Game_ID,Text_ID):
    start = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_css_selector(Game_ID))
    start.click()
    TextBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(Text_ID))

header = pyfiglet.figlet_format(text="TYPERACER HACKER")
print(header)

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

option = input("Select an option (1/2/3):")

if option == "1":
    Game(OnlineRace_ID,Text_ID)
if option == "2":
    Game(PracticeGame_ID,Text_ID)
if option == "3":
    Game(PracticeGame_ID, Text_ID)


TextBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(Text_ID))


print(""
      ""
      "obtained text")

keyboard = Controller()
print(""
      ""
      "keyboard configured")

GameStart = input(""
                  ""
                  ""
                  "Do you want to start(y/n):")

if GameStart == "y":
    time.sleep(3)
    for i in TextBox.text:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.08)
    print(TextBox.text)

else:
    driver.quit()
