const mumAge_me= 2;
const dadAge_mom= 1.2;
// function displayParentsAge(myAge){
//   let mumAge= myAge*mumAge_me;
//   let dadAge= mumAge*dadAge_mom;
//   console.log("My mum's age is "+ mumAge + " my dad's age is "+ dadAge);
// }
// displayParentsAge(20);

// function mom (myAge){
//   return myAge*mumAge_me;
// }
// console.log(mom (20));

// // function mom (myAge){
// //   return myAge*2;
// // }
// // console.log("My mom's age is "+ mom (20));
//
// //Arrow func
// let doubleAge= myAge =>myAge*2;
// console.log(doubleAge(15));
//
let person= {
    firstName : "Sarah",
    eyeColor: "blue",
    eat : function () {
      let eat= prompt("what you eat?");
      return eat;
    }
};
console.log(person.eat());
