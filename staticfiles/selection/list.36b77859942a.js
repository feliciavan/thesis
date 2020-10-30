var content;
document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('.logout').onclick = logout;
  document.querySelectorAll('.form-check-input').forEach(function(input) {
    input.addEventListener("click", () => {
      content = input.value;
    });
  });

  document.querySelector('.btn.btn-info').onclick = verify;

  document.querySelector('#button-addon2').disabled = true;

  // Enable button only if there is text in the input field
  document.querySelector('#search_input').onkeyup = () => {
      if (document.querySelector('#search_input').value.length > 0)
          document.querySelector('#button-addon2').disabled = false;
      else
          document.querySelector('#button-addon2').disabled = true;
  };

});

function logout() {
  alert('You will log out.');
}

function verify() {
    alert(`You have selected \"${content}\".`);
}
