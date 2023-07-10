function getData(form) {
  var formData = new FormData(form);
    
  console.log(obj2FormData(formData));

  console.log(Object.fromEntries(formData));
}

function obj2FormData(obj, formData = new FormData()){
    
    console.log(obj);

    this.formData = formData;

    this.createFormData = function(obj, subKeyStr = ''){
        for(let i in obj){
            let value          = obj[i];
            let subKeyStrTrans = subKeyStr ? subKeyStr + '[' + i + ']' : i;

            if(typeof(value) === 'string' || typeof(value) === 'number'){

                this.formData.append(subKeyStrTrans, value);

            } else if(typeof(value) === 'object'){

                this.createFormData(value, subKeyStrTrans);

            }
        }
    }

    this.createFormData(obj);

    return this.formData;
}


document.getElementById("mainForm").addEventListener("submit", function (e) {
    alert("Show me");
    console.log(e.target);
    e.preventDefault();
    getData(e.target);
});
