document.querySelector('#city').addEventListener('blur', validateCity);
document.addEventListener('DOMContentLoaded', openModalsWithFlashedMessages);


const reSpaces = /^\S*$/;

function validateCity() {
  const city = document.querySelector('#city');
  const re = /^[а-яА-ЯЁё\u0080-\u024F\s\/\-\)\(\`\.\"\']+$/
  if (re.test(city.value) && reSpaces.test(city.value)) {
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
  const form = document.querySelector('.registration');

  form.addEventListener(
    'submit',
    function (event) {
      if (!validateCity()) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        form.classList.add('was-validated');
      }
    },
    false
  );
})();





function clearRegisterModalInput() {
  const modal = document.getElementById('staticBackdrop');
  const cityInput = modal.querySelector('input[type="text"]');
  cityInput.value = '';
  cityInput.classList.remove('is-valid', 'is-invalid');
}

function clearUpdateModalInput(modalId, franchiseCity) {
  const modal = document.getElementById(`staticBackdropUpdate${modalId}`);
  const cityInput = modal.querySelector('input[type="text"]');
  const flashMessage = document.getElementById('flashMessageUpdate' + modalId);
  cityInput.value = franchiseCity;
  cityInput.classList.remove('is-valid', 'is-invalid');
  if (flashMessage) {
    flashMessage.parentNode.removeChild(flashMessage);
  }
}

function clearDeleteModalInput(modalId) {
  const modal = document.getElementById('staticBackdrop' + modalId);
  const passwordInput = modal.querySelector('input[type="password"]');
  if (passwordInput) {
    passwordInput.value = '';
  }

  // const flashMessage = modal.querySelector('.form-label-group #flashMessage' + modalId);
  const flashMessage = document.getElementById('flashMessage' + modalId);
  console.log(flashMessage)
  if (flashMessage) {
    flashMessage.parentNode.removeChild(flashMessage);
  }
}




function openModalsWithFlashedMessages() {
  // Get all modal elements with the 'modal' class
  const modals = document.querySelectorAll('.modal');

  // Iterate through the modals
  modals.forEach(modal => {
    // Check if a flash message element exists for this modal
    const modalId = modal.id.replace(/(staticBackdrop|staticBackdropUpdate)/, '');

    if (document.getElementById('flashMessage' + modalId)) {
      // If a flash message exists, open the modal
      const modalInstance = new bootstrap.Modal(modal);
      modalInstance.show();
    }
  });
}









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





