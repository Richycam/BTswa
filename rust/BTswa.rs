use std::process::Command;
use std::process::Stdio;

fn clear_terminal(){
let system_command = "clear";
   let argument = "Hello World";
      let command_clear: std::process::Output = Command::new(system_command)
         .arg(argument)                 
            .stdout(Stdio::piped())                     
               .stderr(Stdio::piped())
                  .output()
                     .expect("Failed to run");
}

//#      user inputs 
//## input for the tool  
fn read_string_tool() -> String {
   let mut tool = String::new();
      std::io::stdin()
         .read_line(&mut tool)
            .expect("not read user input");
   tool
}
//##
fn read_string_link() -> String {
   let mut link = String::new();
      std::io::stdin()
         .read_line(&mut link)
            .expect("not read user input");
   link
}
//## 
fn read_string_choose() -> String {
   let mut choose = String::new();
      std::io::stdin()
         .read_line(&mut choose)
            .expect("not read user input");
   choose

}


fn inital(){

   println!("what is your siem?");
      let tool = read_string_tool();
   println!("What is the siem link?");
      let link = read_string_link(); 
   println!("--------------------------------------------"); 
   println!("{}", tool);  
   println!("1 ) siem link ");
   println!("2) siem documents");
   println!("3) Nmap");
   println!("--------------------------------------------");
   
//TODO      im doing somethiing wrong here
   read_string_choose();  
      let choose = read_string_choose();
         if choose.as_str() == "1" {
            println!("link");
         }
}
fn main(){
   clear_terminal();
      inital();

}
