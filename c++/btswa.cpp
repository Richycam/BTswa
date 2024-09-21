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
    ############          Blue Team swiss army knife       ############
    ############           --for Blue teamers--            ############
    ############        https://github.com/Richycam        ############
     )" << "\n";
};



void animation() {
    std::cout << R"(    
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

    )" << "\n";
    sleep(1);
    system("clear");
    std::cout << R"(
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

    )" << "\n";
    sleep(1);
    system("clear");
    std::cout << R"(
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

    )" << "\n";
    sleep(1); 
    system("clear");
    std::cout << R"(
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

    )" << "\n";
    sleep(1);
    system("clear");
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
the_menu_obj.start6 = "--------------------------------------------";
// i lost my sanity ok


bool looping = true;
// START WHILE LOOP 
while(looping == true){

banner();


            cout << the_menu_obj.start1 <<endl; 
            cout << the_menu_obj.start2 <<endl; 
            cout << the_menu_obj.start3 <<endl; 
            cout << the_menu_obj.start4 <<endl; 
            cout << the_menu_obj.start5 <<endl; 
            cout << the_menu_obj.start6 <<endl;
            
int choose;
    cout << "choose : "; 
        cin >> choose; 

if (choose == 1){ 
    system("clear");
        cout << siem_obj.link <<endl;
        string check;
        cout << "y) to go back \n";
           cin >> check;      
        if (check == "y"){    
        system("clear");
        continue;
        }


} else if (choose == 2){   
        system("clear");
        if (siem_obj.tool == "kibana"){
                cout << "https://www.elastic.co/guide/en/kibana/current/index.html"<<endl;
                    string check;
                        cout << "y) to go back \n";
                         cin >> check;
                        if (check == "y"){
                            system("clear");
                            continue;
                    }
                        
                
                    } else if (siem_obj.tool == "splunk"){
                        cout << "https://docs.splunk.com/Documentation" <<endl;
                        string check;
                        cout << "y) to go back \n";
                            cin >> check;
                        system("clear");
                        continue;


} else if (choose == 3){
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
                                continue;
                                }

}else if(choose == 4){
    system("wireshark");
}
}//while loop 
return 0;
}
}//main


