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




void banner()  {
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
    ############          Blue Team swiss army knife       ############
    /|\/|\/|\/|\             lightweight version           /|\/|\/|\/|\
    ############                    C++                    ############
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
the_menu_obj.start2 = "     1) Siem link";        
the_menu_obj.start3 = "     2) Siem documents";
the_menu_obj.start4 = "     3) Nmap (not finished)";
the_menu_obj.start5 = "     4) Wireshark";
the_menu_obj.start6 = "     5) World map";
the_menu_obj.start7 = "     6) Python Server ";

// i lost my sanity ok


bool looping = true;
// START WHILE LOOP 
while(looping == true){
system("clear");
banner();

            cout << siem_obj.tool <<endl;
            cout << the_menu_obj.start1 <<endl; 
            cout << the_menu_obj.start2 <<endl; 
            cout << the_menu_obj.start3 <<endl; 
            cout << the_menu_obj.start4 <<endl; 
            cout << the_menu_obj.start5 <<endl; 
            cout << the_menu_obj.start6 <<endl;
            cout << the_menu_obj.start7 <<endl;
            
int choose;
    cout << "choose : "; 
        cin >> choose; 

switch(choose){
    case 1:
    { 
    system("clear");
    cout << siem_obj.link <<endl;
    flw_ctrl();
    break;
    }
continue;
    case 2:  
    {
    system("clear");
        if (siem_obj.tool == "kibana"){
                cout << "https://www.elastic.co/guide/en/kibana/current/index.html"<<endl;
                    flw_ctrl();         
                    continue;
        }else if (siem_obj.tool == "splunk"){
                    cout << "https://docs.splunk.com/Documentation" <<endl;
                    flw_ctrl();
                    continue;
        }else if (siem_obj.tool == "tensable")
                    cout << "https://docs.tenable.com/" <<endl;
                    flw_ctrl();
                    continue;



    break;   
    }               
continue;
    case 3:
    {    
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
    }
    case 4:
    {
    system("wireshark");
    flw_ctrl();
    break;
    }
    case 5:
    {

    int ok; 
    cout << "press enter to open the ascii map "<<endl;
    cout << "use q to exit the map"<<endl;
    cin >> ok;
    system("mapscii");
    break;
    }
    case 6:
    {
    cout << " ctrl + c to shut down server"<<endl;
    system("python3 -m http.server 8000");
    flw_ctrl();
    }
continue;
return 0;
}
}
}



