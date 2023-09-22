const greeting = (name) => {
    console.log(`Hello ${name}, welcome to nodejs`);
};
// greeting(name)

const hello = (name) => {
    console.log(`Hello ${name}!!!`);
};

module.exports = {
    greeting,
    hello
}