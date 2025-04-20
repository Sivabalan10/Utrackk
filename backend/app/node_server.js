const mod1 = require('./custom_modules/add');
require('./custom_modules/iife');
const data = require("./data.json");

console.log(data.address.chennai);
console.log("Log from node_server.js");
const add = mod1.add(2,3);
console.log(add);

function test(){
    var t = 0;
}
let count = 0;
function counter() {
    count++;
    console.log(count);
    return count
}
counter(); // Calling the function separately
counter();

const obj1 = {
    name: "siva",
}
let obj2 = obj1;

obj2  = {name: "siva kumar"};
console.log(obj2.name);