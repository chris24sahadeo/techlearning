fn print_my_name(name: &str) {
  println!("{}", name);
}

fn add(a: i32, b: i32) -> i32 {
  a+b
}

struct Person{
  name: &str,
  dob: &str,
  fav_color: &str,
  pet_names: Vec<&str>
}

fn main() {
    println!("Hello, world!");
    let x;
    x = 1;
    println!("My name is chris! x = {}", x);
    let y: u8;
    y = 22;
    println!("{}", y);
    let tuple = ('f', 2, 3);
    println!("{:#?}",tuple);
    print_my_name("chris");
    println!("{}", add(2, 4));

    let v: Vec<i32> = Vec::new();
    println!("{:?}", v);
    let v = vec![1, 2, 3];
    println!("{:?}", v);
}

