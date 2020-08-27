// function Person(firstName, lastName, dob){
//   this.firstName = firstName;
//   this.lastName = lastName;
//   this.dob = new Date(dob);
//   this.getBirthYear = function(){
//     return this.dob.getFullYear();
//   }
//   this.getFullName = function(){
//     return `${this.firstName} ${this.lastName}`;
//   }
// }

// Person.prototype.getDob = function(){
//   return this.dob;
// }

// const person = new Person('chris', 'sahadeo', '11/28/1997');

// console.log(person);

// class Person{
//   constructor(firstName, lastName, dob){
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.dob = new Date(dob);
//   }

//   getBirthYear(){
//     return this.dob.getFullYear();
//   }

//   getFullName(){
//     return `${this.firstName} ${this.lastName}`;
//   }
// }

// const person = new Person('Chris', 'Sahadeo', '11-28-1997');
// console.log(person.getBirthYear());

// const form = document.getElementById('my-form');
// const query = document.querySelector('.container');
// const items = document.querySelectorAll('.items li');

// const ul = document.querySelector('.items');

// const btn = document.querySelector('.btn');
// btn.addEventListener('click', (e) => {
//   e.preventDefault();
//   document.querySelector('#my-form').style.background = "#ccc";
//   document.querySelector('body').classList.add("bg-dark");
//   document.querySelector('.items').lastElementChild.innerHTML = "<h1>Hello</h1>";
// })

const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');

myForm.addEventListener('submit', onSubmit);

function onSubmit(e){
  e.preventDefault();

  msg.classList.add('error');
  if(nameInput.value === '' || emailInput.value === ''){
    msg.innerHTML = "You retard!";
    setTimeout(() => msg.remove(), 2000);
  }
  else{
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(`${nameInput.value}: ${emailInput.value}`));
    userList.appendChild(li);
    nameInput.value='';
    emailInput.value='';
  }
}