// // Exercise XP
// 5 + "34" // =534
// 5 - "4" = // I don't understand why it's a subtract.
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

// // Ninja Exercise 1: find Nemo
// let nemo = prompt("Which one is a fish?- Nemo or Simba?");
// nemo=nemo.search("nemo")+1;
// if (nemo != 0){
//   console.log("I found Nemo in the "+ nemo+ "'st word !");
// }
// else{
//   console.log("Couldn't find Nemo !");
// }

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

   // // Ninja Exercises: Evaluation(2)
   // let c;
   // let a = 34;
   // let b = 21;
   // a = 2;
   // a + b;
   // // The outcome will be: 23;
   // // The value of c is undefined.
   // // The outcome of console.log(3 + 4 + '5') will be: 75.
   // console.log(a+b);
   // console.log(3 + 4 + '5');

   // // Ninja Exercise 3 : Ask For Numbers
   //    let sumOfNumbers = prompt("Please enter some numbers separated by commas");
   //    numbersArray = [sumOfNumbers.split(" ")];
   //    console.log(sumOfNumbers);
   //    // let numbersArray= [];
   //    //
   //    // console.log(numbersArray);
   //    // let bu= Number(sumOfNumbers);
   //
   //    // numbersArray.push(sumOfNumbers);



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

// // Daily Challenge- EX 2
// let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// console.log(moreFruits[1][1]);
