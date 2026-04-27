// Before: Fighting the borrow checker with excessive cloning.
// The goal is to build a formatted string from a list of words,
// but ownership issues cause unnecessary allocations.

struct StringBuilder {
    parts: Vec<String>,
}

impl StringBuilder {
    fn new() -> Self {
        StringBuilder { parts: Vec::new() }
    }

    fn add(&mut self, word: String) {
        self.parts.push(word);
    }

    fn build(&self, separator: &str) -> String {
        let mut result = String::new();
        for i in 0..self.parts.len() {
            if i > 0 {
                result.push_str(separator);
            }
            // Clone because we can't move out of &self
            result.push_str(&self.parts[i].clone());
        }
        result
    }
}

fn main() {
    let mut builder = StringBuilder::new();
    builder.add("hello".to_string());
    builder.add("world".to_string());
    builder.add("foo".to_string());
    builder.add("bar".to_string());

    let result = builder.build(", ");
    println!("{}", result);

    // Can't use builder after build because build takes &self,
    // but we also can't consume the parts
    builder.add("baz".to_string());
    let result2 = builder.build(" ");
    println!("{}", result2);
}
