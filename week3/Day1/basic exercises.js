// // Exercise XP
// 5 + "34" // =534
// 5 - "4" = // I don't understand why it's a subtract
// 10 % 5 // 0
// 5 % 10 // =5
// "Java" + "Script" //= JavaScript
// " " + " "  //= two spaces
// " " + 0 //= space then 0
// true + true //= 2
// true + false //= 1
// false + true //= 1
// false - true //= -1
// 3 - 4 //= -1
// "Bob" - "bill" //= NaN
// console.log(5 + "34");
// console.log(5 - "4");
// console.log(10 % 5);
// console.log(5 % 10);
// console.log("Java" + "Script");
// console.log(" " + " ");
// console.log(" " + 0);
// console.log(true + true);
// console.log(true + false);
// console.log(false + true);
// console.log(false - true);
// console.log(3 - 4);
// console.log("Bob" - "bill");
//
//
//
// // Exercise 1: Favorite color
// let me = ["my","favorite","color","is","blue"];
// me.push("and", "my","name","is","noa");
// console.log(me);
//
// // Exercise 2: Mixup
// let str1 = "maya";
// let str2 = "liam";
// str1=str1.slice(2, 4) + str1.slice(0, 2);
// str2=str2.slice(2, 4) + str2.slice(0, 2);
// let neWord= (str1 + " " + str2);
// console.log(str1);
// console.log(str2);
// console.log(neWord);
//
// // Exercise 3: calculator
// let num1 = parseInt(prompt('Choose a number please'));
// let num2 = parseInt(prompt('Choose another number please'));
// let sum= num1 + num2;
// let subtract= num1 - num2;
// let multiply= num1 * num2;
// let division= num1 / num2;
// alert('The sum is: '+sum);
// alert('The subtraction is: '+subtract);
// alert('The multiplication is: '+multiply);
// alert('The division is: '+division);
//
// // Ninja Exercise 1: find Nemo
// let nemo = prompt("Which one is a fish?- Nemo or Simba?");
// nemo=nemo.search("nemo")+1;
// if (nemo != 0){
//   console.log("I found Nemo in the "+ nemo+ "'st word !");
// }
// else{
//   console.log("Couldn't find Nemo !");
// }
//
// // Ninja Exercise 1: Evaluation
//    5 >= 1 // true
//    0 === 1 // false
//    4 <= 1 // false
//    1 != 1 // false
//    "A" > "B" // false
//    "B" < "C" // true
//    "a" > "A" // true
//    "b" < "A" // false
//    true === false // false
//    true != true // false
//
//    // Ninja Exercises: Evaluation(2)
//    let c;
//    let a = 34;
//    let b = 21;
//    a = 2;
//    a + b;
//    // The outcome will be: 23;
//    // The value of c is undefined.
//    // The outcome of console.log(3 + 4 + '5') will be: 75.
//    console.log(a+b);
//    console.log(3 + 4 + '5');
//
//    // Ninja Exercise 3 : Ask For Numbers
//       var inputNumbers = prompt("Please enter some numbers separated by commas");
//       var numbersArray = inputNumbers.split(",");
//       let numbersLength= numbersArray.length;
//       let sum=0;
//       for(var i=0; i<numbersArray.length;i++) {
//         numbersArray[i] = +numbersArray[i];
//         sum += numbersArray[i];
//       }
//       console.log("your numbers sum is "+ sum);

// Ninja Exercise 4 :   Boom
let oLetter= 'o';
let addOLetter=0;
let bLetter='b';
let mLetter='m';
let number= parseInt(prompt("please enter a number"));
if (number<2) return "boom";
if (number>2) {
  addOLetter= number; // if i entered 3, there are 3 o
let boom= bLetter.concat(addOLetter).concat(mLetter);
}
console.log(boom);
// //Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:
// If the number given is less than 2 : return “boom”
// If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
// If the number given is evenly divisible by 2, add a exclamation mark to the end.
// If the number given is evenly divisible by 5, return the string in ALL CAPS.
// If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// Examples
// 4 ➞ "Boooom!"
// // There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// // 1 is lower than 2, so we return "boom"





// // Daily Challenge- EX 1
// let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// fruits.shift();
// console.log(fruits);
// fruits.sort();
// console.log(fruits);
// fruits.push("Kiwi");
// console.log(fruits);
// fruits.splice(0,1);
// console.log(fruits);
// fruits.reverse();
// console.log(fruits);
//
// // Daily Challenge- EX 2
// let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// console.log(moreFruits[1][1]);
