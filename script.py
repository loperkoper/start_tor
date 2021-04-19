from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from time import sleep
import random
sleep(5)

url = ['gestyy.com/ey2pMV','gestyy.com/eyR2QO','gestyy.com/eyETAR']

def terminal():
        # #select terminal

    mouse.position = (10, 712)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (58, 491)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (251, 519)
    mouse.click(Button.left, 1)
    sleep(1.5)

        # #select on terminal

    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(1)
#cd /root/Desktop/tor1/tor-browser_en-US/Browser/
##minimize Terminal
mouse.position = (968, 94)
mouse.click(Button.left, 1) 
sleep(1)  
terminal()
sleep(2)
##write command
keyboard.type('cd /root/Desktop/tor1/tor-browser_en-US/Browser/ && ./firefox')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
sleep(5)
##click on connect
mouse.position = (592, 300)
mouse.click(Button.left, 1)
##sleep
sleep(12)
##select searchbar
mouse.position = (404, 75)
mouse.click(Button.left, 1)
##type
keyboard.type('a')
keyboard.type('b')
keyboard.type('o')
keyboard.type('u')
keyboard.type('t')
keyboard.type(':')
keyboard.type('c')
keyboard.type('o')
keyboard.type('n')
keyboard.type('f')
keyboard.type('i')
keyboard.type('g')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##select to accept risk
mouse.position = (265, 413)
mouse.click(Button.left, 1)
sleep(1)
##select to type
mouse.position = (301, 121)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('extensions.torlauncher.start_tor')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##change to false
mouse.position = (933, 168)
mouse.click(Button.left, 1)
sleep(1.5)
##close tor
mouse.position = (990, 10)
mouse.click(Button.left, 1)
sleep(1.5)
##close Terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (999, 94)
mouse.click(Button.left, 1)
sleep(0.5)
terminal()
###second time
sleep(5)
##click on terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(1)
##write command
keyboard.type('cd /root/Desktop/tor2/tor-browser_en-US/Browser/ && ./firefox')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
sleep(5)
##click on configure
mouse.position = (760, 297)
mouse.click(Button.left, 1)
sleep(1)
##click on connect
mouse.position = (914, 556)
mouse.click(Button.left, 1)
##sleep
sleep(12)
##select searchbar
mouse.position = (404, 75)
mouse.click(Button.left, 1)
##type
keyboard.type('about:config')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##select to accept risk
mouse.position = (265, 413)
mouse.click(Button.left, 1)
sleep(1)
##select to type
mouse.position = (301, 121)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('extensions.torlauncher.start_tor')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##change to false
mouse.position = (933, 168)
mouse.click(Button.left, 1)
sleep(1.5)
##close tor
mouse.position = (990, 10)
mouse.click(Button.left, 1)
sleep(1.5)
##close Terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (999, 94)
mouse.click(Button.left, 1)
sleep(0.5)
terminal()
##third time
sleep(5)
##click on terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(1)
##write command
keyboard.type('cd /root/Desktop/tor3/tor-browser_en-US/Browser/ && ./firefox')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
sleep(5)
##click on configure
mouse.position = (760, 297)
mouse.click(Button.left, 1)
sleep(1)
##click on connect
mouse.position = (914, 556)
mouse.click(Button.left, 1)
##sleep
sleep(12)
##select searchbar
mouse.position = (404, 75)
mouse.click(Button.left, 1)
##type
keyboard.type('about:config')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##select to accept risk
mouse.position = (265, 413)
mouse.click(Button.left, 1)
sleep(1)
##select to type
mouse.position = (301, 121)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('extensions.torlauncher.start_tor')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##change to false
mouse.position = (933, 168)
mouse.click(Button.left, 1)
sleep(1.5)
##close tor
mouse.position = (990, 10)
mouse.click(Button.left, 1)
sleep(1.5)
##close Terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (999, 94)
mouse.click(Button.left, 1)
sleep(0.5)
terminal()
##type
keyboard.type('cd /root/Desktop/tor1/tor-browser_en-US/Browser/TorBrowser/Data/Tor && rm -r torrc-defaults && wget https://raw.githubusercontent.com/loperkoper/start_tor/main/torrc-defaults && cd /root/Desktop/tor2/tor-browser_en-US/Browser/TorBrowser/Data/Tor && rm -r torrc-defaults && wget https://raw.githubusercontent.com/loperkoper/torrc2/main/torrc-defaults && cd /root/Desktop/tor3/tor-browser_en-US/Browser/TorBrowser/Data/Tor && rm -r torrc-defaults && wget https://raw.githubusercontent.com/loperkoper/torrc3/main/torrc-defaults')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(9)
##type
keyboard.type('cd /root/Desktop/tor-browser_en-US/Browser && ./firefox')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(5)
##click on configure
mouse.position = (760, 297)
mouse.click(Button.left, 1)
sleep(1)
##click on connect
mouse.position = (914, 556)
mouse.click(Button.left, 1)
##sleep
sleep(12)
def first():
	url = ['gestyy.com/ey2pMV','gestyy.com/eyR2QO','gestyy.com/eyETAR']
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    ##go to second page
    mouse.position = (190, 642)
    mouse.click(Button.left, 1)  
    sleep(1.5)
    terminal()
    ##click on terminal
    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(1)
    ##write command
    keyboard.type('cd /root/Desktop/tor1/tor-browser_en-US/Browser/ && ./firefox')
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)
    sleep(5) 
    sleep(12)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    ##go to third page
    mouse.position = (238, 642)
    mouse.click(Button.left, 1)  
    sleep(1.5)
    terminal()
    ##click on terminal
    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(1)
    ##write command
    keyboard.type('cd /root/Desktop/tor2/tor-browser_en-US/Browser/ && ./firefox')
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)
    sleep(5) 
    sleep(12)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    ##go to fourth page
    mouse.position = (238, 642)
    mouse.click(Button.left, 1)  
    sleep(2)
    terminal()
    ##click on terminal
    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(1)
    ##write command
    keyboard.type('cd /root/Desktop/tor3/tor-browser_en-US/Browser/ && ./firefox')
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)
    sleep(5) 
    sleep(12)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

first()

while True:
    url = ['gestyy.com/ey2pMV','gestyy.com/eyR2QO','gestyy.com/eyETAR']
    ##go to first page
    mouse.position = (142, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##click on skip add
    mouse.position = (1222, 121)
    mouse.click(Button.left, 1)
    ##scond page
    mouse.position = (190, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##click on skip add
    mouse.position = (1222, 121)
    mouse.click(Button.left, 1)
    ##third page
    mouse.position = (238, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##click on skip add
    mouse.position = (1222, 121)
    mouse.click(Button.left, 1)
    ##fourth page
    mouse.position = (280, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##click on skip add
    mouse.position = (1222, 121)
    mouse.click(Button.left, 1)


    ##go to first page
    mouse.position = (142, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##new identity
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(1)
    ##never ask again
    mouse.position = (466, 342)
    mouse.click(Button.left, 1)
    ##click yes
    mouse.position = (919, 380)
    mouse.click(Button.left, 1)
    sleep(3)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    ##go to scond page
    mouse.position = (190, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##new identity
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(1)
    ##never ask again
    mouse.position = (466, 342)
    mouse.click(Button.left, 1)
    ##click yes
    mouse.position = (919, 380)
    mouse.click(Button.left, 1)
    sleep(3)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    ##go to third page
    mouse.position = (238, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##new identity
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(1)
    ##never ask again
    mouse.position = (466, 342)
    mouse.click(Button.left, 1)
    ##click yes
    mouse.position = (919, 380)
    mouse.click(Button.left, 1)
    sleep(3)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    ##go to fourth page
    mouse.position = (280, 642)
    mouse.click(Button.left, 1)
    sleep(2)
    ##new identity
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(1)
    ##never ask again
    mouse.position = (466, 342)
    mouse.click(Button.left, 1)
    ##click yes
    mouse.position = (919, 380)
    mouse.click(Button.left, 1)
    sleep(3)
    ##max tor
    mouse.position = (975, 11)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (365, 72)
    mouse.click(Button.left, 1)
    sleep(0.1)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
