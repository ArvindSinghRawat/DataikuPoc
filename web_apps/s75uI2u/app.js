function getData(form) {
  var formData = new FormData(form);

  for (var pair of formData.entries()) {
    console.log(pair[0] + ": " + pair[1]);
  }

  console.log(Object.fromEntries(formData));
}

document.getElementById("mainForm").addEventListener("submit", function (e) {
    alert("Show me");
  e.preventDefault();
  getData(e.target);
});
