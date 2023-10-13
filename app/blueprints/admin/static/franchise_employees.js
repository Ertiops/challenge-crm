document.querySelector('#firstName').addEventListener('blur', validateFirstName);
document.querySelector('#lastName').addEventListener('blur', validateLastName);
document.querySelector('#patronymic').addEventListener('blur', validatePatronymic);
document.querySelector('#email').addEventListener('blur', validateEmail);
document.querySelector('#phone').addEventListener('blur', validatePhone);
document.querySelector('#password').addEventListener('blur', validatePassword);
document.querySelector('#role').addEventListener('blur', validateRole);

document.querySelectorAll("[name='cancel']").forEach((el) => {el.addEventListener('blur', clearInput)});

const reSpaces = /^\S*$/;


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

function validateRole() {
  const role = document.querySelector('#role');
  if (role.value) {
    role.classList.remove('is-invalid');
    role.classList.add('is-valid');
    return true;
  } else {
    role.classList.add('is-invalid');
    role.classList.remove('is-valid');
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
          !form.checkValidity() && (
          !validateRole() ||
          !validateLastName() ||
          !validateFirstName() ||
          !validatePatronymic() ||
          !validateEmail() ||
          !validatePhone() ||
          !validatePassword()
)
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
  document.getElementById('role').value = '';
  document.querySelector('#role').classList.remove('is-invalid', 'is-valid', 'was-validated');  

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






//  toggle navigation of employees groups
$(document).ready(function () {
    $('#myTab a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
});