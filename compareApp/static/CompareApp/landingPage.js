let h3Elements = document.querySelectorAll('h3');
h3Elements.forEach(element => {
  let dateString = element.textContent;
  let date = new Date(dateString);
  let options = { month: 'short', day: 'numeric', year: 'numeric' };
  let formattedDate = date.toLocaleDateString('en-US', options);
  element.textContent = formattedDate;
});
