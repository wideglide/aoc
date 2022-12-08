
use std::collections::HashSet;


fn read_file(filepath: &str) -> String {
    let data = std::fs::read_to_string(filepath).expect("File not found");
    data
}

pub fn part_solve(part: usize, length: usize) {
    let s = read_file("input");
    for i in length..s.len() {
        let mut start = HashSet::new();
        for j in i - length..i {
            start.insert(&s[j..j+1]);
        }
        if start.len() == length {
            println!(
                " part{}, characters received = {}, {}", 
                part, i, &s[i-length..i]);
            return;
        }
    }
}

fn main() {
    part_solve(1, 4);
    part_solve(2, 14);
}
