#//     CREDS https://github.com/vpwl -> Merged animations
#//     CREDS https://github.com/IanUmney -> Code suggestions

#// unhash ai parts to use them 
#// BTSWA with AI 
import time
import os
import random
import sys
#from openai import OpenAI
#api_keyai = 
#you need a openai api key to make this work 

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


         __________-------____                 ____-------__________
         \------____-------___--__---------__--___-------____------/
          \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/
            \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/
              --//// / /  /  //|| (O)\ /(O) ||\\  \  \ \ \\\\--
                   ---__/  // /| \_  /V\  _/ |\ \\  \__---
                       -//  / /\_ ------- _/\ \  \\-
                          \_/_/ /\---------/\ \_\_/
                              ----\   |   /----
                                   | -|- |
                                  /   |   \      
                           |-._`-._ :| |: _.-'_.-|
                           |   `-._`:| |:`_.-'   |
                           |-------`-' '-'-------|
                           |------_.-. .-._------|
                           |  _.-'_.:| |:._`-._  |
                           |-'_.-'  :| |:  `-._`-|
    """

banner.Banner2 = """


         __________-------____                 ____-------__________
         \------____-------___--__---------__--___-------____------/
          \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/
            \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/
              --//// / /  /  //|| (-)\ /(-) ||\\  \  \ \ \\\\--
                   ---__/  // /| \_  /V\  _/ |\ \\  \__---
                       -//  / /\_ ------- _/\ \  \\-
                          \_/_/ /\---------/\ \_\_/
                              ----\   |   /----
                                   | -|- |
                                  /   |   \      
                           |-._`-._ :| |: _.-'_.-|
                           |   `-._`:| |:`_.-'   |
                           |-------`-' '-'-------|
                           |------_.-. .-._------|
                           |  _.-'_.:| |:._`-._  |
                           |-'_.-'  :| |:  `-._`-|
    """
   
banner.Header = """
    ############          Blue Team Swiss Army Knife       ############
    ############            ===||:::::::::::::::>          ############
    ############         https://github.com/Richycam       ############
"""


def animation():

    frames = [    """


               8      go~~~os   go~~~os      8
               8    ,8`     '8_8`     '8.    8
               8    8`   _   '8`   _   '8    8
               8    8   !@!   8   !@!   8    8
               8    8i       /8\       i8    8
               8     8s     g8 8s     s8     8
               8      dooooo`8_8'ooooob      8
               8     d!      'V`      !b     8
               8     8        ~        8     8
               8     8                 8     8
               8   ] 8                 8 [   8
               8 [ ] 8                 8 [ ] 8
               8 [ ] !8               8| [ ] 8

    """,
    """
               8      go~~~os   go~~~os      8
               8    ,8`     '8_8`     '8.    8
               8    8`   _   '8`   _   '8    8
               8    8   !@!   8   !@!   8    8
               8    8i       /8\       i8    8
               8     8s     g8 8s     s8     8
               8      dooooo`8_8'ooooob      8
               8     d!      'V`      !b     8
               8     8        ~        8     8
               8     8                 8     8
               8   ] 8                 8 [   8
               8 [ ] 8                 8 [ ] 8
               8 [ ] !8               8| [ ] 8
                            BTSWA
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
    print("--------------------------------------------")
    print(siem.get_tool())    
    print("1) siem link ")
    print("2) siem documents")
    print("3) Nmap (Linux)")
    print("4) Open Wireshark(linux)")
    print("5) AI Tool ")
    print("6) World map")
    print("--------------------------------------------")


def main():
    ban_ani = True
    while ban_ani:
        print(banner.Banner1)
        time.sleep(0.5)
        clear()
        print(banner.Banner2)
        time.sleep(0.5)
        print(banner.Banner1)
        clear()
        ban_ani = False
        continue
    loop_all = True
    while loop_all:
        clear()
        print(banner.Header)
        menu()
        main_cntrl = input("choose usage \n")
        match main_cntrl:
            case "1":
                clear()
                print(siem.get_tool())
                print ("\n")
                back = input("go back? Y/N? \n ").lower
                if back == "y":
                    clear()
                    continue

            case "2":
                docs = siem.get_tool()
                if docs == "kibana" or docs == "elastic": 
                        print("https://www.elastic.co/guide/index.html?utm_campaign=Google-B-EMEA-UKI-Exact&utm_content=Brand-Core-Documentation&utm_source=google&utm_medium=cpc&device=c&utm_term=elastic%20documentation&gad_source=1&gclid=EAIaIQobChMIsuHa15OuiAMV6JtQBh2tHgypEAAYASAAEgKobvD_BwE") 
                        print ("\n")
                        back = input("go back? Y/N?")
                        if back == "y":
                            clear()
                            continue
                elif docs == "splunk":
                        print("https://docs.splunk.com/Documentation") 
                        print ("\n")
                        back = input("go back? Y/N?").lower()
                        if back == "y":
                            clear()
                            continue
                elif docs == "velociraptor":
                    print("https://docs.velociraptor.app/docs/")
                    print ("\n")
                    back = input("go back? Y/N?").lower()
                    if back == "y":
                        clear()
                        continue

            case "3":
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
                        back = input("want to go back? Y/N? \n").lower()
                        if back == "y":
                            clear()
                            continue
                    case "2":
                        clear()
                        ver_scan = "nmap {0} -A".format(ip)
                        os.system(ver_scan)
                        print ("\n")
                        back = input("want to go back Y/N? \n")
                        if back == "y":
                            clear()
                            continue                            
            case "4":
                clear()
                os.system("wireshark")
                print ("\n")
                back = input("want to go back Y/N? \n").lower
                if back == "y":
                    clear()
                    continue
            case "5":
                ai = True
                while ai:
                    clear()
                    print("(y to return)")
                    askai = input("ChatGPT 3.5 Turbo>>  ")
                    if askai == "y":
                        ai = False
                        clear()
                        continue  
                    client = OpenAI(
                        #api_key=api_keyai,
                    )
                    completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content":askai,
                            }
                        ],
                        model="gpt-3.5-turbo",
                    )
                    print("GPT:",completion.choices[0].message.content)
                    print ("\n")
                    back = input("want to go back Y/N? \n").lower
                    if back == "y":
                        clear()
                        ai = False
                        continue  
                    else:
                        continue
            case "6":
                clear()
                print(map.map1)
                print("\n")
                back = input("want to go back Y/N? \n").lower
                if back == "y":
                    continue          

clear() 
animation()
tool = input(str("tool name? \n")).lower()
link = input("tool link? \n").lower()
siem = siem(tool,link)
clear()
main()
