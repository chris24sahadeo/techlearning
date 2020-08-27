const sideNav = document.querySelector('.sidenav');
console.log(sideNav);
M.Sidenav.init(sideNav, {});

// autocomplete
const ac = document.querySelector('.autocomplete');
M.Autocomplete.init(ac, {
  data: {
    "Harry Potter": null;
    "Lord of the Rings": null;
    "Peter Pan": null;
    "The Lion King": null;
  }
});