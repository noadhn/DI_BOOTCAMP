let time=10;
function endSalesMessage() {
  let endSales= document.createElement('p');
  banner.appendChild(endSales);
  endSales.textContent= "Sales end in "+time+" minutes!";
}
setTimeout(endSalesMessage,2000);

setInterval(function() {


      // Do something every 5 seconds
}, 1000);
