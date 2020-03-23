# Type-Racer-Python-cheat
**CHEAT type racer using python .**

> This project cheats typeracer (http://play.typeracer.com) using Python libraries such as Selenium and Pynput

# INSTALLATION

> You will need 2 Python libraries : **Selenium** and **Pynput**
you can download them using pip

```
pip install selenium
pip install pynput
```

I've also used **PYFIGLET** but it is not really necessary as all it does is add ASCII text. You can delete that command if you want but if you really want ascii text , go ahead and download pyfiglet as well using pip

Selenium requires an additional chrome driver for running chrome . I have used chrome driver in this project because i prefer chrome , If you prefer some other browser you can download that specific selenium webdriver for that browser

Chromedriver can be downloaded from here : https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/

I prefer chromedriver version 80 as i use google chrome version 80 .If you use some other version of chrome , download that specific driver from here : https://chromedriver.chromium.org/downloads

Once chrome driver is downloaded , create a folder called **webdrivers** in the same directory as your python file, Like i've done in mine.

<img src="https://imgur.com/visLlH8.png>

Once you've done that , you're all good to go

# USAGE 

(1) First you gotta select which mode you want to use, There are 3 modes in typeracer 
<img src = "https://imgur.com/8l1xQ3n.png">

You have to select them in your console , **NOT IN THE BROWSER**
<img src = "https://imgur.com/KoSV1S6.png">

Type in 1,2 or 3 to select a mode

(2) Once you've selected the mode , The typerace will be loading and the console will ask you another input 
<img src = "https://imgur.com/1JYDRrf.png">

type in y and hit ENTER just before the race is about to begin

the program will take 3 seconds to start typing , so you must click on the typing box before that . If you want to inscrease or decrease this time , You can always do that by messing with the code 

<img src = "https://imgur.com/Tq7ghbc.png">

(3) Switch to the browser that the program opened and click on the typing box 
<img src = "https://imgur.com/HqlEUp1.png">

(4) Sit back and watch the program type out everything for you. If you want to increase the typing speed , Go back to the code and decrease this time
<img src = "https://imgur.com/gseZgfr.png">

# PLAYING WITH FRIENDS

if you selected MODE 2 : RACE WITH YOUR FRIENDS , then do not enter y immediately when the program asks you `Do you want to start(y/n):`
Send the invite link to your friends and wait for them to join. Once they have , click join race and when the race is about to begin , Go back to the console and enter y. once you've done that , immediatly switch back to the browser and click on the typing box (the box where you type stuff in the race)
