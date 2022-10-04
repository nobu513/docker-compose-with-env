use std::env;

fn main() {
    let my_name = env::var("MY_NAME").unwrap();
    println!("{}", my_name);
}
