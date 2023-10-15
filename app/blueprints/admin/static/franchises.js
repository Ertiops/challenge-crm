document.querySelector('#city').addEventListener('blur', validateCity);

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


(function () {
  const forms = document.querySelectorAll('.needs-validation');

  for (let form of forms) {
    form.addEventListener(
      'submit',
      function (event) {
        if (
          // !form.checkValidity() ||
          !validateCity()
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

// $(document).ready(function() {
//   // Copy to clipboard function
//   $(".copy-button").click(function() {
//       const textToCopy = $(this).parents("tr").find("input.form-control");

//       const tempInput = document.createElement("input");
//       tempInput.style = "position: absolute; left: -1000px";
//       tempInput.value = textToCopy.val();
//       document.body.appendChild(tempInput);
//       tempInput.select();
//       document.execCommand("copy");
//       document.body.removeChild(tempInput);

//       textToCopy.addClass("is-valid");

//   });
// });

$(document).ready(function() {
  // Copy to clipboard function
  $(".copy-button").click(function() {
    // Remove is-valid class from all text fields except the current one
    $(".form-control").not($(this).parents("tr").find("input.form-control")).removeClass("is-valid");

    const textToCopy = $(this).parents("tr").find("input.form-control");

    const tempInput = document.createElement("input");
    tempInput.style = "position: absolute; left: -1000px";
    tempInput.value = textToCopy.val();
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);

    textToCopy.addClass("is-valid");
  });
});

