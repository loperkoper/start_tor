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

    mouse.position = (17, 519)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (112, 370)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (247, 389)
    mouse.click(Button.left, 1)
    sleep(1.5)

        # #select on terminal

    mouse.position = (641, 342)
    mouse.click(Button.left, 1)
    sleep(1)
#cd /root/Desktop/tor1/tor-browser_en-US/Browser/
##minimize Terminal
mouse.position = (968, 34)
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
mouse.position = (592, 249)
mouse.click(Button.left, 1)
##sleep
sleep(21)
##select searchbar
mouse.position = (404, 76)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('a')
sleep(0.09)
keyboard.type('b')
sleep(0.09)
keyboard.type('o')
sleep(0.09)
keyboard.type('u')
sleep(0.09)
keyboard.type('t')
sleep(0.09)
keyboard.type(':')
sleep(0.09)
keyboard.type('c')
sleep(0.09)
keyboard.type('o')
sleep(0.09)
keyboard.type('n')
sleep(0.09)
keyboard.type('f')
sleep(0.09)
keyboard.type('i')
sleep(0.09)
keyboard.type('g')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##select to accept risk
mouse.position = (355, 316)
mouse.click(Button.left, 1)
sleep(1)
##select to type
mouse.position = (467, 118)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('extensions.torlauncher.start_tor')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##change to false
mouse.position = (930, 171)
mouse.click(Button.left, 1)
sleep(1.5)
##close tor
mouse.position = (991, 11)
mouse.click(Button.left, 1)
sleep(1.5)
##close Terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (1001, 34)
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
mouse.position = (766, 252)
mouse.click(Button.left, 1)
sleep(1)
##click on connect
mouse.position = (934, 476)
mouse.click(Button.left, 1)
##sleep
sleep(21)
##select searchbar
mouse.position = (404, 76)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('a')
sleep(0.09)
keyboard.type('b')
sleep(0.09)
keyboard.type('o')
sleep(0.09)
keyboard.type('u')
sleep(0.09)
keyboard.type('t')
sleep(0.09)
keyboard.type(':')
sleep(0.09)
keyboard.type('c')
sleep(0.09)
keyboard.type('o')
sleep(0.09)
keyboard.type('n')
sleep(0.09)
keyboard.type('f')
sleep(0.09)
keyboard.type('i')
sleep(0.09)
keyboard.type('g')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##select to accept risk
mouse.position = (355, 316)
mouse.click(Button.left, 1)
sleep(1)
##select to type
mouse.position = (467, 118)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('extensions.torlauncher.start_tor')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##change to false
mouse.position = (930, 171)
mouse.click(Button.left, 1)
sleep(1.5)
##close tor
mouse.position = (991, 11)
mouse.click(Button.left, 1)
sleep(1.5)
##close Terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (1001, 34)
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
mouse.position = (766, 252)
mouse.click(Button.left, 1)
sleep(1)
##click on connect
mouse.position = (934, 476)
mouse.click(Button.left, 1)
##sleep
sleep(21)
##select searchbar
mouse.position = (404, 76)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('a')
sleep(0.09)
keyboard.type('b')
sleep(0.09)
keyboard.type('o')
sleep(0.09)
keyboard.type('u')
sleep(0.09)
keyboard.type('t')
sleep(0.09)
keyboard.type(':')
sleep(0.09)
keyboard.type('c')
sleep(0.09)
keyboard.type('o')
sleep(0.09)
keyboard.type('n')
sleep(0.09)
keyboard.type('f')
sleep(0.09)
keyboard.type('i')
sleep(0.09)
keyboard.type('g')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##select to accept risk
mouse.position = (355, 316)
mouse.click(Button.left, 1)
sleep(1)
##select to type
mouse.position = (467, 118)
mouse.click(Button.left, 1)
sleep(0.5)
##type
keyboard.type('extensions.torlauncher.start_tor')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
##change to false
mouse.position = (930, 171)
mouse.click(Button.left, 1)
sleep(1.5)
##close tor
mouse.position = (991, 11)
mouse.click(Button.left, 1)
sleep(1.5)
##close Terminal
mouse.position = (570, 408)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (1001, 34)
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
mouse.position = (766, 252)
mouse.click(Button.left, 1)
sleep(1)
##click on connect
mouse.position = (934, 476)
mouse.click(Button.left, 1)
##sleep
sleep(21)



def first():
    url = ['gestyy.com/ey2pMV','gestyy.com/eyR2QO','gestyy.com/eyETAR']
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)
    ##go to second page
    mouse.position = (194, 517)
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
    sleep(15)
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)

    ##go to third page
    mouse.position = (279, 515)
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
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)

    ##go to fourth page
    mouse.position = (322, 516)
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
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(3)
first()

def reset():
    ##go to first page
    mouse.position = (152, 517)
    mouse.click(Button.left, 1)
    sleep(3)
    ##close Terminal
    mouse.position = (576, 519)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (518, 490)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (576, 519)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (518, 490)
    mouse.click(Button.left, 1)
    sleep(0.5)


    ##scond page
    mouse.position = (209, 520)
    mouse.click(Button.left, 1)
    sleep(3)
    ##close Terminal
    mouse.position = (401, 517)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (370, 495)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (401, 517)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (370, 495)
    mouse.click(Button.left, 1)
    sleep(0.5)


    ##third page
    mouse.position = (259, 517)
    mouse.click(Button.left, 1)
    sleep(3)
    ##close Terminal
    mouse.position = (401, 517)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (370, 495)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (401, 517)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (370, 495)
    mouse.click(Button.left, 1)
    sleep(0.5)
    


    ##fourth page
    mouse.position = (318, 515)
    mouse.click(Button.left, 1)
    sleep(3)
    ##close Terminal
    mouse.position = (401, 517)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (370, 495)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (401, 517)
    mouse.click(Button.right, 1)
    sleep(0.5)
    mouse.position = (370, 495)
    mouse.click(Button.left, 1)
    sleep(0.5)
    





    ##go to first page
    mouse.position = (150, 518)
    mouse.click(Button.left, 1)
    terminal()
    ##type
    keyboard.type('cd /root/Desktop/tor-browser_en-US/Browser && ./firefox')
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(5)
    ##click on configure
    mouse.position = (766, 252)
    mouse.click(Button.left, 1)
    sleep(1)
    ##click on connect
    mouse.position = (934, 476)
    mouse.click(Button.left, 1)
    sleep(15)



    url = ['gestyy.com/ey2pMV','gestyy.com/eyR2QO','gestyy.com/eyETAR']
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)





    
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)
    ##go to second page
    mouse.position = (210, 519)
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
    sleep(15)
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)

    ##go to third page
    mouse.position = (258, 514)
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
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)

    ##go to fourth page
    mouse.position = (327, 515)
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
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(3)

i = 0
while True:
   i = i+1
   if i == 15:
    reset()
    i = 0
   else:
    url = ['gestyy.com/ey2pMV','gestyy.com/eyR2QO','gestyy.com/eyETAR']
    ##go to first page
    mouse.position = (156, 518)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click on skip add
    mouse.position = (1198, 121)
    mouse.click(Button.left, 1)
    sleep(12)
    ##new identity
    mouse.position = (1306, 75)
    mouse.click(Button.left, 1)
    sleep(2)
    ##never ask again
    mouse.position = (466, 281)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click yes
    mouse.position = (918, 314)
    mouse.click(Button.left, 1)
    sleep(4.5)
    ##click yes2
    mouse.position = (961, 301)
    mouse.click(Button.left, 1)
    sleep(6)
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)


    ##scond page
    mouse.position = (211, 517)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click on skip add
    mouse.position = (1198, 121)
    mouse.click(Button.left, 1)
    sleep(12)
    ##new identity
    mouse.position = (1306, 75)
    mouse.click(Button.left, 1)
    sleep(2)
    ##never ask again
    mouse.position = (466, 281)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click yes
    mouse.position = (918, 314)
    mouse.click(Button.left, 1)
    sleep(4.5)
    ##click yes2
    mouse.position = (961, 301)
    mouse.click(Button.left, 1)
    sleep(6)
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)



    ##third page
    mouse.position = (269, 520)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click on skip add
    mouse.position = (1198, 121)
    mouse.click(Button.left, 1)
    sleep(12)
    ##new identity
    mouse.position = (1306, 75)
    mouse.click(Button.left, 1)
    sleep(2)
    ##never ask again
    mouse.position = (466, 281)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click yes
    mouse.position = (918, 314)
    mouse.click(Button.left, 1)
    sleep(4.5)
    ##click yes2
    mouse.position = (961, 301)
    mouse.click(Button.left, 1)
    sleep(6)
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)



    ##fourth page
    mouse.position = (319, 514)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click on skip add
    mouse.position = (1198, 121)
    mouse.click(Button.left, 1)
    sleep(12)
    ##new identity
    mouse.position = (1306, 75)
    mouse.click(Button.left, 1)
    sleep(2)
    ##never ask again
    mouse.position = (466, 281)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click yes
    mouse.position = (918, 314)
    mouse.click(Button.left, 1)
    sleep(4.5)
    ##click yes2
    mouse.position = (961, 301)
    mouse.click(Button.left, 1)
    sleep(6)
    ##max tor
    mouse.position = (975, 10)
    mouse.click(Button.left, 1)
    mouse.position = (1339, 40)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click search bar
    mouse.position = (595, 74)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type url
    c = random.choice(url)
    keyboard.type(c)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1)

