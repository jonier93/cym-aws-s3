document.querySelector("#btn-consult").addEventListener('click', consult_user)

function consult_user() {
    var obj = {
        "id": document.getElementById("id").value
    }
    fetch("/consult_user", {
        "method": "post",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(obj)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message == "OK") {
            document.getElementById("txt-data").innerHTML = data.name + "\n" + data.lastname + "\n" + data.birthday
            document.getElementById("image").src = "https://test-s3-jonier.s3.amazonaws.com/" + data.photo
        }
        else {
            alert("Usuario no existe")
            document.getElementById("txt-data").innerHTML = ""
            document.getElementById("image").src = ""
        }
            
        })
    .catch(err => {
        alert("error " + err)
        document.getElementById("txt-data").value = ""
    })
}

    
