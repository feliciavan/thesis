document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('.logout').onclick = logout;

  document.querySelector('#button').disabled = true;

  // Enable button only if there is text in the input field
  document.querySelector('#uname').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
        document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

  document.querySelector('#pwd').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
      document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }


  document.querySelector('#degree').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
      document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

  document.querySelector('#title').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
        document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

  document.querySelector('#major').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
        document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

  document.querySelector('#uni').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
        document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

  document.querySelector('#email').onkeyup = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
        document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

  document.querySelector('#image').onchange = () => {
    if ((document.querySelector('#degree').value.length > 0) ||
    (document.querySelector('#title').value.length > 0) ||
    (document.querySelector('#major').value.length > 0) ||
    (document.querySelector('#uni').value.length > 0) ||
    (document.querySelector('#email').value.length > 0) ||
    (document.querySelector('#uname').value.length > 0) ||
    (document.querySelector('#pwd').value.length > 0) ||
    (document.querySelector('#image').files.length > 0))
        document.querySelector('#button').disabled = false;
    else
        document.querySelector('#button').disabled = true;
  }

});

function logout() {
  alert('You will log out.');
}
