#include <iostream>
#include <string>
#include <unistd.h>
#include <termios.h> 
#include <cctype>
using namespace std;

class menu
{
    public:
    string start1;
    string start2;
    string start3;
    string start4;
    string start5;       
    string start6;
    string start7;
    string start9;
};

class siem
{
    public:
    string tool;
    string link;
};

class choose {

    public:
    int choice;
};


void banner() {
    std::cout << R"(
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
                                   | -|- |
                                  /   |   \  
    ############          Blue Team swiss army knife       ############
    ############              lightweight version 
                                    C++                    ############
    ############        https://github.com/Richycam        ############
     )" << "\n";
};



void animation() {
    std::cout << R"(    
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
                                   | -|- |
                                  /   |   \  

    )" << "\n";
    sleep(1);
    system("clear");
    std::cout << R"(
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
                                   | -|- |
                                  /   |   \   

    )" << "\n";
    sleep(1);
    system("clear");



};

void flw_ctrl(){
    string check;
    cout << "y) to go back \n";
    cin >> check;      
    if (check == "y"){    
    system("clear");
}
};

int main() {

string tool_type_impt;
    cout << "Siem Name \n";
        cin >> tool_type_impt;

string link_impt;
    cout << "Siem Link? \n";
        cin >> link_impt;

//create object
siem siem_obj;
//attribites
siem_obj.tool = tool_type_impt;
siem_obj.link = link_impt;
animation();

menu the_menu_obj; // create object 
//attribites
 
the_menu_obj.start1 = "--------------------------------------------"; 
the_menu_obj.start2 = "1) siem link";        
the_menu_obj.start3 = "2) siem documents";
the_menu_obj.start4 = "3) Nmap";
the_menu_obj.start5 = "4) Wireshark";
the_menu_obj.start6 = "5) world map";
the_menu_obj.start7 = "6) Password checker";

// i lost my sanity ok


bool looping = true;
// START WHILE LOOP 
while(looping == true){

banner();

            cout << siem_obj.tool <<endl;
            cout << the_menu_obj.start1 <<endl; 
            cout << the_menu_obj.start2 <<endl; 
            cout << the_menu_obj.start3 <<endl; 
            cout << the_menu_obj.start4 <<endl; 
            cout << the_menu_obj.start5 <<endl; 
            cout << the_menu_obj.start6 <<endl;
            
int choose;
    cout << "choose : "; 
        cin >> choose; 

switch(choose){
  case 1: 
    system("clear");
        cout << siem_obj.link <<endl;
        flw_ctrl();
        break;
        continue;

    case 2:  
        system("clear");
        if (siem_obj.tool == "kibana"){
                cout << "https://www.elastic.co/guide/en/kibana/current/index.html"<<endl;}
                    string check;
                    flw_ctrl();         
                    continue;
                    }else if (siem_obj.tool == "splunk"){
                    cout << "https://docs.splunk.com/Documentation" <<endl;
                    }
                    flw_ctrl();
                    continue;
    break;
    case 3:
        string ip;
            cout << "ip to nmap?";
                cin >> ip;
        int nmap;
            cout << "scan type?" <<endl;
            cout << "1) simple " <<endl;
            cout << "2) version scan" <<endl;  
            cout << "3) vuln scan" <<endl;
                            cin >> nmap;
                        system("clear");
                                switch(nmap){
                                case 1:
                                    system("nmap");
                                break;
                                case 2:
                                    system("nmap");
                                break;
                                flw_ctrl();
                                continue;
                                }
break;
    case 4:
    system("wireshark");
    flw_ctrl();
break;
    case 5:
    std::cout << R"(

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
        
        
        FOR THE INTERACTIVE MAP
        you@you> telnet mapscii.me
        in another terminal  
 
 
 
 )" << "\n";
 flw_ctrl();
 
continue;
break;


}


return 0;
} 
