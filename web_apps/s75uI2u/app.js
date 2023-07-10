/*
 * For more information, refer to the "Javascript API" documentation:
 * https://doc.dataiku.com/dss/latest/api/js/index.html
 */
function submitForm(event) {
  var formData = new FormData(event.target);

  for (var pair of formData.entries()) {
    console.log(pair[0] + ": " + pair[1]);
  }
}

const form = document.getElementById("mainForm");
form.addEventListener("submit", submitForm);