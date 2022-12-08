
fn read_file(filepath: &str) -> String {
    let data = std::fs::read_to_string(filepath).expect("File not found");
    data
}

pub fn part1_read() {
    let s = read_file("input");
    dbg!(&s[..32]);
    let mut calories: Vec<u32> = Vec::new();
    for elf in s.split("\n\n") {
        let mut values = Vec::new();
        for line in elf.lines() {
            values.push(line.parse::<u32>().unwrap());
        }
        calories.push(values.iter().sum::<u32>());
    }
    println!(
        " part1_read : {}",
        calories.iter().max().unwrap()
    );
}

pub fn part1() {
    println!(
        "{}",
        include_str!("input")
            .split("\n\n")
            .map(|elf| elf.lines().map(|c| c.parse::<u32>().unwrap()).sum::<u32>())
            .max()
            .unwrap(),
    );
}

pub fn part2() {
    let mut calories = include_str!("input")
            .split("\n\n")
            .map(|elf| elf.lines().map(|c| c.parse::<u32>().unwrap()).sum::<u32>())
            .collect::<Vec<u32>>();
    calories.sort_unstable();
    println!( "{}", calories.into_iter().rev().take(3).sum::<u32>());

}

fn main() {
    part1_read();
    print!(" part 1 answer: ");
    part1();
    print!(" part 2 answer: ");
    part2();
}
