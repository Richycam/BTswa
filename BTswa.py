import time
import os
import sys
Banner = """
############          Blue Team swiss army knife       ############
############           --for Blue teamers--            ############
############        https://github.com/Richycam        ############
"""

art1 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |x           x| |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""
art2 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |x x   x   x x| |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""

art3 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""
art4 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | | Github.com  | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J    
   
"""

class siem:
    def __init__(self, tool, link):
        self.tool = tool
        self.link = link

    def call_back(tool):
        print(tool)

    def call_back(link):
        print(link)

def clear():
    os.system("clear")

def for_art():
    list = [art1, art2, art3, art4]
    for art in list:
        print(art)
        time.sleep(0.7)
        clear()

def exit():
    sys.exit()

clear()
for_art()
tool = input("tool name? \n")
link = input("tool link? \n")
siem(tool,link)
clear()
print(Banner)


def menu():

    print("--------------------------------------------")
    siem.call_back(tool)
    print("1) siem link ")
    print("2) siem documents")
    print("--------------------------------------------")

menu()

def main():
    main_cntrl = input("choose useage \n")
    if main_cntrl == "1":
        clear()
        siem.call_back(link)
        back = input("go back? Y/N?")
        if back == "y" or "Y":
            clear()
            print(Banner)
            menu()
            main()


    elif main_cntrl == "2":
        if siem.call_back(tool) == "elastic"  or "kibana" or "Elastic" or "Kibana":
            print("https://www.elastic.co/guide/index.html?utm_campaign=Google-B-EMEA-UKI-Exact&utm_content=Brand-Core-Documentation&utm_source=google&utm_medium=cpc&device=c&utm_term=elastic%20documentation&gad_source=1&gclid=EAIaIQobChMIsuHa15OuiAMV6JtQBh2tHgypEAAYASAAEgKobvD_BwE") 
            back = input("go back? Y/N?")
            if back == "y" or "Y":
                clear()
                print(Banner)
                menu()
                main()
        elif siem.call_back(tool) == "Splunk" or "splunk":
            print("https://docs.splunk.com/Documentation") 
            back = input("go back? Y/N?")
            if back == "y" or "Y":
                clear()
                print(Banner)
                menu()
                main()
main()
