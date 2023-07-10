/*
 * For more information, refer to the "Javascript API" documentation:
 * https://doc.dataiku.com/dss/latest/api/js/index.html
 */
function submitForm(event) {
    var value = `Form Submitted! Timestamp: ${event.timeStamp}`;
    alert(value);
    alert(event);
    console.log(event);
}

const form = document.getElementById("mainForm");
form.addEventListener("submit", submitForm);