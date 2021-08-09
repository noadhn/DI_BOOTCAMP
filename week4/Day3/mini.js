function playTheGame(){
  if (!(confirm('Would you like to play the game?'))) {
    alert('No problem, Goodbye');
    return;
  }
    let computerNumber= Math.round(Math.floor(Math.random() * 11));
    //console.log(computerNumber);
    let userGuess;
    for (var i = 0; i < 3; i++) {
      userGuess= validNumber ();
      if (!userGuess) return;
      if(test(userGuess,computerNumber)) return;
      }
    alert('out of chances');
    return;
   }

function validNumber (){
  answer= parseInt(prompt('Please enter a number between 0 and 10'));
  if (answer > 10 || answer < 0) alert('Sorry not a good number, Goodbye');
  if(!answer) alert('Sorry not a number, Goodbye');
}

function test(userNumber,computerNumber){
  if (userNumber===computerNumber){
    alert ('WINNER');
    return;
  }
  if (userNumber>computerNumber){
    alert ('Your number is bigger then the computer’s, guess again');
    return;
  }
  if (userNumber<computerNumber){
    alert ('Your number is smaller then the computer’s, guess again');
    return;
 }
}
