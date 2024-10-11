#//     CREDS https://github.com/vpwl -> Merged animations
#//     CREDS https://github.com/IanUmney -> Code suggestions

### // dependancies 
## // map
# // sudo snap install mapscii


import time
import os
import random
import sys


class siem:
    def __init__(self , tool, link):
        self.tool = tool
        self.link = link

    def get_tool(self):
        return self.tool
    def get_link(self):
        return self.link

class map:
    def __init__(self,map1):
        self.map1 = map1

class banner:
    def __init__(self,Banner1,Banner2,Header):
        self.Banner1 = Banner1 
        self.Banner2 = Banner2
        self.Header = Header


banner.Banner1 = """
                           |-._`-._ :| |: _.-'_.-|
                           |   `-._`:| |:`_.-'   |
                           |-------`-' '-'-------|
                           |------_.-. .-._------|
                           |  _.-'_.:| |:._`-._  |
                           |-'_.-'  :| |:  `-._`-|
         __________-------____                 ____-------__________
         \------____-------___--__---------__--___-------____------/
          \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/
            \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/
              --//// / /  /  //|| (O)\ /(O) ||\\  \  \ \ \\\\--
                   ---__/  // /| \_  /V\  _/ |\ \\  \__---
                       -//  / /\_ ------- _/\ \  \\-
                          \_/_/ /\---------/\ \_\_/
                              ----\   |   /----     
    """

banner.Banner2 = """
                           |-._`-._ :| |: _.-'_.-|
                           |   `-._`:| |:`_.-'   |
                           |-------`-' '-'-------|
                           |------_.-. .-._------|
                           |  _.-'_.:| |:._`-._  |
                           |-'_.-'  :| |:  `-._`-|
         __________-------____                 ____-------__________
         \------____-------___--__---------__--___-------____------/
          \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/
            \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/
              --//// / /  /  //||  - \ / - ||\\  \  \ \ \\\\--
                   ---__/  // /| \_  /V\  _/ |\ \\  \__---
                       -//  / /\_ ------- _/\ \  \\-
                          \_/_/ /\---------/\ \_\_/
                              ----\   |   /----  
    """
   
banner.Header = """
    ############          Blue Team Swiss Army Knife       ############
    ############                     .py                   ############
    ############         https://github.com/Richycam       ############
"""


def animation():

    frames = [ 
    """
    BTSWA 
    """,
    """
    BTSWA - Blue Team Swiss Army Knife
    """,
    """
    BTSWA - Blue Team Swiss Army Knife
                            https://github.com/Richycam
    """,
 ]
    for frame in frames:
        print(frame)
        time.sleep(round(random.uniform(0.6,0.9),1)) 
        clear()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def exit():
    sys.exit()

## create obj 
map.map1 = """
            180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
            |     |     |     |     |     |     |     |     |     |     |     |     |
        90N-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90N
            |           . _..::__:  ,-"-"._        |7       ,     _,.__             |
            |   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|
            |>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                mt-2_|
        60N-+  \_.:--.       `._ )`^-. "'       , [_/(                       __,/-' +-60N
            | '"'     \         "    _L        oD_,--'                )     /. (|   |
            |          |           ,'          _)_.\\._<> 6              _,' /  '   |
            |          `.         /           [_/_'` `"(                <'}  )      |
        30N-+           \\    .-. )           /   `-'"..' `:._          _)  '       +-30N
            |    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |
            |              `._,   ""         |           \`'   \|   ?_)  {\         |
            |                 `=.---.        `._._       ,'     "`  |' ,- '.        |
        000-+                   |    `-._         |     /          `:`<_|h--._      +-000
            |                   (        >        .     | ,          `=.__.`-'\     |
            |                    `.     /         |     |{|              ,-.,\     .|
            |                     |   ,'           \   / `'            ,"     \     |
        30S-+                     |  /              |_'                |  __  /     +-30S
            |                     | |                                  '-'  `-'   \.|
            |                     |/                                         "    / |
            |                     \.                                             '  |
        60S-+                                                                       +-60S
            |                      ,/            ______._.--._ _..---.---------._   |
            |     ,-----"-..?----_/ )      __,-'"             "                  (  |
            |-.._(                  `-----'                                       `-|
        90S-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90S
            Map 1998 Matthew Thomas.|Freely usable as long as this|line is included.|
            |     |     |     |     |     |     |     |     |     |     |     |     |
        180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
        -----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----
        
        
        """

def menu():

    print(banner.Banner1)
    print(banner.Header)
    print("\n")    
    print("tool ->" , siem.get_tool()) 
    print("       ---------------------------------------------------------------")
    print("                      1) SIEM link ")
    print("                      2) SIEM documents")
    print("                      3) Nmap (Linux)")
    print("                      4) Open Wireshark (Linux)")
    print("                      5) TCPDump (Linux) ")
    print("                      6) Interactive World map (Linux)")
    print("                      7) World map")
    print("                      8) Password to wordlist checking tool")
    print("                      9) Start Python HTTP Sever ")
    print("        ---------------------------------------------------------------")

def ban_animate():
        print(banner.Banner1)
        time.sleep(0.5)
        clear()
        print(banner.Banner2)
        time.sleep(0.5)
        print(banner.Banner1)
        clear()

def go_home():
    back = input("go back? Y/N? \n ").lower
    if back == "y":
        clear()

def check(word, list):
    if word in list:
        print("The word is in the list!")
    else:
        print("The password is not in the list!")


def choose_1():
    clear()
    print(siem.get_tool())
    print ("\n")
    go_home()
  
def choose_2():
    docs = siem.get_tool()
    if docs == "kibana" or docs == "elastic": 
        print("https://www.elastic.co/guide/index.html?utm_campaign=Google-B-EMEA-UKI-Exact&utm_content=Brand-Core-Documentation&utm_source=google&utm_medium=cpc&device=c&utm_term=elastic%20documentation&gad_source=1&gclid=EAIaIQobChMIsuHa15OuiAMV6JtQBh2tHgypEAAYASAAEgKobvD_BwE") 
        print ("\n")
        go_home()
    elif docs == "splunk":
        print("https://docs.splunk.com/Documentation") 
        print ("\n")
        go_home()
    elif docs == "velociraptor":
        print("https://docs.velociraptor.app/docs/")
        print ("\n")
        go_home()

def choose_3():
    clear()
    ip = input("ip to scan \n")
    print("scan type") 
    print("1) simple scan")
    print("2) version detector")
    scan_type = input("")
    match scan_type:
        case "1":
            clear()
            simple_scan = "nmap {0}".format(ip)
            os.system(simple_scan)
            print ("\n")
            go_home()
                       
        case "2":
            clear()
            ver_scan = "nmap {0} -A".format(ip)
            os.system(ver_scan)
            print ("\n")
            go_home()

def choose_4():
    clear()
    os.system("wireshark")
    print ("\n")
    go_home()

def choose_5():                    
    clear()
    os.system("sudo tcpdump -c 30 --interface any")
    go_home()

def choose_6():
    clear()
    print("Keyboard shortcuts \n \n")
    print("Arrows up, down, left, right to scroll around\n")
    print("Press a or z to zoom in and out\n")
    print("Press c to switch to block character mode\n")
    print("\nPress q to quit")
    input("\nEnter start interactive map").lower   
    clear()
    os.system("mapscii")

    

def choose_7():
    clear()
    print(map.map1)
    print("\n")
    go_home()

def choose_8():
    paswd = input("password to check \n")
    wrdlist = input("Wordlist to check against \n")
    clear()
    check (paswd,wrdlist)
    print("\n")
    go_home()

def choose_9():
    srv_start = "python3 -m http.server 9000"
    print(" ctrl + c to shut down server ")
    print ("check http://localhost:9000")
    os.system(srv_start)
    ("\n")
    go_home()
def main():
    ban_ani = True
    
    while ban_ani:
        ban_animate()
        ban_ani = False
    
    loop_all = True
    
    while loop_all:
        clear()
        menu()
        main_cntrl = input("choose usage \n")
      
        match main_cntrl:
            case "1":
                choose_1()
                continue
            case "2":
                choose_2()
                continue
            case "3":
                choose_3()
                continue                            
            case "4":
                choose_4()
                continue
            case "5":  
                choose_5()
                continue
            case "6":
                choose_6()
                continue          
            case "7":
                choose_7()
                continue
            case "8":
                choose_8()
                continue 
            case "9":
                choose_9()               
clear() 
animation()
tool = input(str("SIEM tool name? \n")).lower()
link = input("SIEM tool link? \n").lower()
siem = siem(tool,link)
clear()
main()
