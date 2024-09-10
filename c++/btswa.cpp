#include <iostream>
#include <string>
#include <unistd.h>
using namespace std;

int main() {

    

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
     _______________clear____
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

string tool, link;
    cout << "siem tool type : ";
        cin >> tool;

    cout << "link to siem : ";
        cin >> link;


    cout << "--------------------------------------------" <<endl;   
    cout << "1) siem link "<<endl;
    cout << "2) siem documents"<<endl;
    cout << "3) Nmap"<<endl;
    cout << "--------------------------------------------"<<endl;
    
    int choose; 
        cout << "choose : "; 
            cin >> choose; 

switch (choose){
    case 1: 
    system("clear");
        cout << link <<endl;
    case 2:
    system("clear");
        if (tool == "kibana"){
            cout << "https://www.elastic.co/guide/en/kibana/current/index.html" ;
    }
            else if (tool == "splunk"){
                cout << "https://docs.splunk.com/Documentation";
    }
    case 3:
        int nmap;
            cout << "scan type?" <<endl;
            cout << "1) simple " <<endl;
            cout << "2) version scan" <<endl; 
                cin >> nmap;
        int ip; 
            cout << "ip address to scan?"<<endl;
                cin >> ip;
        
        if (nmap == 1){   
            string args = "nmap" + ip ;
            system(args.c_str());
            

    }


    }


return 0;

}

