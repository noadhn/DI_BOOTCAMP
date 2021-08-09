// // Exercise 1: Simple If/Else Statement
// let x= 8;
// let y= 10;
// if (x >y){
//   console.log("x is bigger");
// }
// else {
//   console.log("y is bigger");
// }
// // Exercise 2: Chihuahua
// var newDog= "Chihuahua";
// console.log('There are '+newDog.length+ ' letters in Chihuahua');
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());
// if (newDog==='Chihuahua'){
//   console.log("I love Chihuahuas, it’s my favorite dog breed");
// }
// else {
//   console.log("I dont care, I prefer cats");
// }
// // Exercise 3: Even Or Odd
// var userNum= parseInt(prompt("Please enter a number"));
// if (userNum%2==0){
//   console.log("the number you choose is an even number");
// }
// else {
//   console.log("the number you choose is an odd number");
// }
// //Exercise 4: Group Chat
// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
// if (users.length===0)
// {
//   console.log("no one online");
// }
// if (users.length===1) {
//     console.log(users[0]+" is online");
// }
// if (users.length===2) {
//     console.log(users[0]+users[1]+" are online");
// }
// else {
//     console.log(users[0]+" , "+users[1]+ " and "+ users.length+ " other users are online");
// }
// //XP GOLD: Exercise 1 : The World Translator
// let lang= (prompt("what language do you speak?")).toLowerCase();
// switch (lang) {
//   case "french":
//     console.log("Bonjour");
//     break;
//
//     case "english":
//       console.log("Hello");
//       break;
//
//     case "hebrew":
//       console.log("Shalom");
//       break;
//
//   default:
//   console.log("01110011 01101111 01110010 01110010 01111001");
// }
// //XP GOLD: Exercise 2 : The Grade Assigner
// let grade= parseInt(prompt("what is your grade?"));
// if (grade> 90){
//   console.log("A");
// }
// if (80<grade && grade<=90){
//   console.log("B");
// }
// if (70<=grade && grade<=80){
//   console.log("C");
// }
// if (grade< 70){
//   console.log("D");
// }
// //XP GOLD: Exercise 3 : Verbing
// let verb= prompt("please enter a verb");
// if (verb.length>=3 && verb.slice(-3)!='ing') {
// console.log(verb+"ing");
// }
// if (verb.length>=3 && verb.slice(-3)==='ing') {
// console.log(verb+"ly");
// }
// if (verb.length<3) {
//   console.log(verb);
// }

const array1 = 'bones';
for (let value of array1) {
  console.log(value);
}
