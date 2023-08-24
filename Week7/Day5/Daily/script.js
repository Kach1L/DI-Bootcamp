function isAnagram(str1, str2) {
    // Remove whitespace and convert both strings to lowercase
    str1 = str1.replace(/\s/g, "").toLowerCase();
    str2 = str2.replace(/\s/g, "").toLowerCase();

    // Check if the sorted characters of the two strings are equal
    return str1.split("").sort().join("") === str2.split("").sort().join("");
}

// Test cases
console.log(isAnagram("Astronomer", "Moon starer"));  // true
console.log(isAnagram("School master", "The classroom"));  // true
console.log(isAnagram("The Morse Code", "Here come dots"));  // true
console.log(isAnagram("Hello", "World"));  // false
