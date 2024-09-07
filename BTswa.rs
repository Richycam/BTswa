//using this as a way to learn rust please dont PR on this 

fn read_string() -> String {
   let mut input = String::new();
   std::io::stdin()
       .read_line(&mut input)
       .expect("can not read user input");
   input
}
fn inital(){
   println!("what is your siem?");
   let input = read_string();
   }

fn menu(){
   println!("--------------------------------------------");   
   println!("1) siem link ");
   println!("2) siem documents");
   println!("3) Nmap");
   println!("4) ");
   println!("--------------------------------------------");
   }

fn main(){
  
inital();
menu();
}
