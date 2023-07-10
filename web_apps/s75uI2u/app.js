/*
 * For more information, refer to the "Javascript API" documentation:
 * https://doc.dataiku.com/dss/latest/api/js/index.html
 */
function submitForm(event) {
  var formData = new FormData(form);

  for (var pair of formData.entries()) {
    console.log(pair[0] + ": " + pair[1]);
  }
    
    event.preventDefault();
}

const form = document.getElementById("mainForm");
form.addEventListener("submit", submitForm);