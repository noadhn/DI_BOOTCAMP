// // Exercise 1 : Information
// //PART 1
// let infoAboutMe= () => console.log("I'm 20 years old");
// infoAboutMe();
// //PART 2+3
// function infoAboutPerson (personName, personAge, personFavoriteColor, personHobbies){
//   console.log('You name is '+ personName+ ' ,you are '+personAge+ ' years old , your favorite color is '
//   + personFavoriteColor+ ' and your hobbies are '+ personHobbies);
// }
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"]);
//
// // Exercise 2 : Keyless Car
// //Part 1
// let userAge= parseInt(prompt("What's your age?"));
// function checkDriverAge(){
//   if (userAge< 18) alert("Sorry, you are too young to drive this car. Powering off");
//   if (userAge> 18) alert("You are old enough to drive, Powering On. Enjoy the ride!");
//   if (userAge===18) alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// checkDriverAge();
// //Part 2
// function checkDriverAge(age){
//   if (age< 18) alert("Sorry, you are too young to drive this car. Powering off");
//   if (age> 18) alert("You are old enough to drive, Powering On. Enjoy the ride!");
//   if (age===18) alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// checkDriverAge(32);

// // Exercise 3 : Odd or Even
// function checkNumber(){
//   for (var i = 1; i < 101; i++) {
//     if(i%2===0) console.log("the number "+i+ " is even");
//     else console.log("the number "+i+ " is odd");
//   }
// }
// checkNumber();

// // Exercise 4: Find The Numbers Divisible By 23
// function isDivisible(){
//   let sum=0;
//   for (var i = 0; i < 501; i++) {
//     if (i%23===0) {
//           console.log(i);
//           sum +=i;
//         }
//       }
// console.log("the sum is "+sum);
// }
// isDivisible();
// // Bonus
// function isDivisible(divisor){
//   let sum=0;
//   for (var i = 0; i < 501; i++) {
//     if (i%divisor===0){
//       console.log(i);
//       sum +=i;
//     }
//   }
//   console.log("the sum is "+sum);
// }
// isDivisible(52);

// // Exercise 5: Amazon Shopping
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
//   };
// function checkBasket(){
//   let item= prompt("please enter an item");
//   if ('item' in amazonBasket) console.log("this item is in the basket");
//   else console.log("this item is not in the basket");
// }
// checkBasket();

// // Exercise 6 : What’s In My Wallet ? ---- Didnt understand how
// quarters  = 0.25;
// dimes = 0.10;
// nickels = 0.05;
// pennies = 0.01;
// let money= [quarters,dimes,nickels,pennies];
// function changeEnough(price,change){
//   change=[i/4,i/10,i/20,i/100];
//   if (price<change) console.log("enough");
//   else console.log("not enough")
// }
// changeEnough(2, [10, 200, 0, 0]);


// Exercise 7 : Shopping List
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}
let shoppingList= ["banana", "orange", "apple"];
function myBill(){
  let sum=0;
  for (var i = 0; i < shoppingList.length; i++) {
    if (Object.keys(shoppingList)[i] in Object.keys(prices)) {
      let add=Object.values(shoppingList[i])=> Object.values(prices);
      sum+= add;
    }
    console.log(sum);
  };

myBill();

//
// Bonus: If the item is in stock, decrease the item’s stock by 1
