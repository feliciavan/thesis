document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('.logout').onclick = logout;
  document.querySelector('#button').disabled = true;

  // Enable button only if there is text in the input field
  document.querySelector('#title').onkeyup = () => {

  if ((document.querySelector('#title').value.length > 0) &&
  (document.querySelector('#req').value.length > 0) &&
  (document.querySelector('#output').value.length > 0) &&
  (document.querySelector('#tool').value.length > 0))
      document.querySelector('#button').disabled = false;
  else
      document.querySelector('#button').disabled = true;
}

document.querySelector('#req').onkeyup = () => {
  if ((document.querySelector('#title').value.length > 0) &&
  (document.querySelector('#req').value.length > 0) &&
  (document.querySelector('#output').value.length > 0) &&
  (document.querySelector('#tool').value.length > 0))
      document.querySelector('#button').disabled = false;
  else
      document.querySelector('#button').disabled = true;
}

document.querySelector('#output').onkeyup = () => {
  if ((document.querySelector('#title').value.length > 0) &&
  (document.querySelector('#req').value.length > 0) &&
  (document.querySelector('#output').value.length > 0) &&
  (document.querySelector('#tool').value.length > 0))
      document.querySelector('#button').disabled = false;
  else
      document.querySelector('#button').disabled = true;
}

document.querySelector('#tool').onkeyup = () => {
  if ((document.querySelector('#title').value.length > 0) &&
  (document.querySelector('#req').value.length > 0) &&
  (document.querySelector('#output').value.length > 0) &&
  (document.querySelector('#tool').value.length > 0))
      document.querySelector('#button').disabled = false;
  else
      document.querySelector('#button').disabled = true;
}
});


function email() {
  var els = document.querySelectorAll('input:checked');
  var content = els[0].value;
  alert(`You have chosen Student No. ${content}. All the involved students will receive notification emails.`);
}

function logout() {
  alert('You will log out.');
}
