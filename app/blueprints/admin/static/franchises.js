document.querySelector('#city').addEventListener('blur', validateCity);
document.querySelector('#firstName').addEventListener('blur', validateFirstName);
document.querySelector('#lastName').addEventListener('blur', validateLastName);
document.querySelector('#patronymic').addEventListener('blur', validatePatronymic);
document.querySelector('#email').addEventListener('blur', validateEmail);
document.querySelector('#phone').addEventListener('blur', validatePhone);
document.querySelector('#password').addEventListener('blur', validatePassword);

document.querySelectorAll("[name='cancel']").forEach((el) => {el.addEventListener('blur', clearInput)});

const reSpaces = /^\S*$/;


function validateCity(e) {
  const city = document.querySelector('#city');
  const re = /^[а-яА-ЯЁё\u0080-\u024F\s\/\-\)\(\`\.\"\']+$/
  if (re.test(city.value) && re.test(city.value)) {
    city.classList.remove('is-invalid');
    city.classList.add('is-valid');

    return true;
  } else {
    city.classList.add('is-invalid');
    city.classList.remove('is-valid');

    return false;
  }
}

function validateFirstName(e) {
  const firstName = document.querySelector('#firstName');
  const re = /[ЁёА-я]/
  if (reSpaces.test(firstName.value) && re.test(firstName.value)) {
    firstName.classList.remove('is-invalid');
    firstName.classList.add('is-valid');

    return true;
  } else {
    firstName.classList.add('is-invalid');
    firstName.classList.remove('is-valid');

    return false;
  }
}

function validateLastName(e) {
  const lastName = document.querySelector('#lastName');
  const re = /[ЁёА-я]/
  if (reSpaces.test(lastName.value) && re.test(lastName.value)) {
    lastName.classList.remove('is-invalid');
    lastName.classList.add('is-valid');

    return true;
  } else {
    lastName.classList.add('is-invalid');
    lastName.classList.remove('is-valid');

    return false;
  }
}

function validatePatronymic(e) {
  const patronymic = document.querySelector('#patronymic');
  const re = /[ЁёА-я]/
  if (reSpaces.test(patronymic.value) && re.test(patronymic.value)) {
    patronymic.classList.remove('is-invalid');
    patronymic.classList.add('is-valid');

    return true;
  } else {
    patronymic.classList.add('is-invalid');
    patronymic.classList.remove('is-valid');

    return false;
  }
}


function validateEmail(e) {
  const email = document.querySelector('#email');
  const re = /^([a-zA-Z0-9_\-?\.?]){3,}@([a-zA-Z]){3,}\.([a-zA-Z]){2,5}$/;

  if (reSpaces.test(email.value) && re.test(email.value)) {
    email.classList.remove('is-invalid');
    email.classList.add('is-valid');

    return true;
  } else {
    email.classList.add('is-invalid');
    email.classList.remove('is-valid');

    return false;
  }
}

function validatePhone(e) {
  const phone = document.querySelector('#phone');
  const re = /[0-9]{11}/
  if (reSpaces.test(phone.value) && re.test(phone.value)) {
    phone.classList.remove('is-invalid');
    phone.classList.add('is-valid');

    return true;
  } else {
    phone.classList.add('is-invalid');
    phone.classList.remove('is-valid');

    return false;
  }
}

function validatePassword() {
  const password = document.querySelector('#password');
  const re = /(.)/;
  if (re.test(password.value) && reSpaces.test(password.value)) {
    password.classList.remove('is-invalid');
    password.classList.add('is-valid');

    return true;
  } else {
    password.classList.add('is-invalid');
    password.classList.remove('is-valid');

    return false;
  }
}

(function () {
  const forms = document.querySelectorAll('.needs-validation');

  for (let form of forms) {
    form.addEventListener(
      'submit',
      function (event) {
        if (
          // !form.checkValidity() ||
          !validateCity() ||
          !validateFirstName() ||
          !validateLastName() ||
          !validatePatronymic() ||
          !validateEmail() ||
          !validatePhone() ||
          !validatePassword()
        ) {
          event.preventDefault();
          event.stopPropagation();
        } else {
          form.classList.add('was-validated');
          $('#form').on('submit', function(e){
            $('#staticBackdrop').modal('show');
            e.preventDefault();
          });

        }
      },
      false
    );
  }
})();

function clearInput() {
  document.getElementById('city').value = '';
  document.querySelector('#city').classList.remove('is-invalid', 'is-valid', 'was-validated');
  document.getElementById('lastName').value = '';
  document.querySelector('#lastName').classList.remove('is-invalid', 'is-valid', 'was-validated');
  document.getElementById('firstName').value = '';
  document.querySelector('#firstName').classList.remove('is-invalid', 'is-valid', 'was-validated');
  document.getElementById('patronymic').value = '';
  document.querySelector('#patronymic').classList.remove('is-invalid', 'is-valid', 'was-validated');
  document.getElementById('email').value = '';
  document.querySelector('#email').classList.remove('is-invalid', 'is-valid', 'was-validated');
  document.getElementById('phone').value = '';
  document.querySelector('#phone').classList.remove('is-invalid', 'is-valid', 'was-validated');
  document.getElementById('password').value = '';
  document.querySelector('#password').classList.remove('is-invalid', 'is-valid', 'was-validated');



  flashMessage = document.getElementById("flashMessage");
  if (flashMessage) {
    // Remove the flashed message element from the DOM
    flashMessage.parentNode.removeChild(flashMessage);
  }

}


$(document).ready(function() {
  if ($("#flashMessage *").length > 0){
    $("#staticBackdrop").modal("show");
  }
});