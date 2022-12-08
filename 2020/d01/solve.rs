use std::env;
use std::fs;

type  Point = (i32, i32);

fn solve_p1(data: &Vec<i32>) -> Vec<Point> {

    let mut v: Vec<Point> = Vec::new();
    let mut solved: bool = false;

    for i in data {
        let diff = 2020 - i;
        if data.contains(&diff) {
            println!("[*] P1: ({}, {}) \t= {}", i, diff, i * diff);
            break;
        }
    }

    for i in data {
        for j in data {
            if !solved && i + j == 2020 {
                println!("[*] P1: ({}, {}) \t= {}", i, j, i * j);
                solved = true;
            }
            if i + j < 2020 {
                v.push((*i, *j));
            }
        }
    }

    v
}

fn solve_p2(data: &Vec<i32>, v: &Vec<Point>) {
    println!("    # pairs < 2020 =  {}", v.len());
    for i in data {
        for p in v {
            let (x, y) = p;
            if i + x + y == 2020 {
                println!("[*] P2: ({}, {}, {}) \t=  {} ", x, y, i, i * x * y);
                return;
            }
        }
    }
}

fn read_input(filename: &String) -> Vec<i32> {

    let contents = fs::read_to_string(filename)
        .expect("Couldn't read the file.");

    let data: Vec<i32> = contents
        .split_whitespace()
        .map(|s| s.parse().expect(r"parse error"))
        .collect();

    data
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("[*] reading file {}", filename);
    
    let data: Vec<i32> = read_input(filename);

    println!("[*] length={} \t first line `{}`", data.len(), &data[0]);

    let v: Vec<Point> = solve_p1(&data);

    solve_p2(&data, &v);
}
