#include <iostream>
#include <string>
#include <unistd.h>
using namespace std;

class menu
{
    public:
    string start1;
    string start2;
    string start3;
    string start4;
    string start5;       
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

void return_back() {
    system("clear");
    // return to main menu
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
the_menu_obj.start5 = "--------------------------------------------";
// i lost my sanity ok




bool looping = true;
while(looping == true){
cout << the_menu_obj.start1 <<endl; 
cout << the_menu_obj.start2 <<endl; 
cout << the_menu_obj.start3 <<endl; 
cout << the_menu_obj.start4 <<endl; 
cout << the_menu_obj.start5 <<endl; 





int choose;
    cout << "choose : "; 
        cin >> choose; 

if (choose == 1){ 
    system("clear");
        cout << siem_obj.link <<endl;
        cout << "\n";
        sleep(10);
        system("clear");
        continue;

} else if (choose == 2){   
        system("clear");
        if (siem_obj.tool == "kibana"){
                cout << "https://www.elastic.co/guide/en/kibana/current/index.html"<<endl;
                sleep(10);
                system("clear");
                continue;
                


        } else if (siem_obj.tool == "splunk"){
            cout << "https://docs.splunk.com/Documentation" <<endl;
            sleep(10);
            system("clear");
            continue;
} else if (siem_obj.tool == 3){
        int nmap;
            cout << "scan type?" <<endl;
            cout << "1) simple " <<endl;
            cout << "2) version scan" <<endl; 
                cin >> nmap;
        int ip; 
            cout << "ip address to scan?"<<endl;
                cin >> ip;

        sleep(10);
        system("clear");
        continue;
            
        }
}//while loop 
return 0;
    }
}           



