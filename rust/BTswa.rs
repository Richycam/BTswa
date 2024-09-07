//using this as a way to learn rust please dont PR on this 
fn read_string_tool() -> String {
   let mut tool = String::new();
   std::io::stdin()
       .read_line(&mut tool)
       .expect("can not read user input");
   tool
}
fn read_string_link() -> String {
   let mut link = String::new();
   std::io::stdin()
       .read_line(&mut link)
       .expect("can not read user input");
   link
}



fn inital(){

   println!("what is your siem?");
   let tool = read_string_tool();
   println!("What is the siem link?");
   let link = read_string_link(); 
   println!("--------------------------------------------"); 
   println!("{}", tool);  
   println!("1) siem link ");
   println!("2) siem documents");
   println!("3) Nmap");
   println!("--------------------------------------------");
}

fn main(){
  
inital();
}
