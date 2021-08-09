let solarPlanets= ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'];
solarPlanets.forEach(element => {
  let planetName=element;
  let newPlanetDiv= document.createElement('div');
  newPlanetDiv.classList.add(planetName, 'planet');
  document.getElementById('listPlanets').appendChild(newPlanetDiv); //how to refer to class and not to id ?
});
 //Bonus
 var moons = {
    earth: 'moon',
    Jupiter: ['Amalthea','Callisto','Europa','Ganymede','Io'],
};
moons.Mars = ['Deimos','Phobos'];
console.log(moons);

// do the same as for the planets using DOM
