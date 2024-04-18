document.querySelector("#btn-consult").addEventListener('click', consult_user)

function consult_user() {
    let obj_data = { "id": document.getElementById("id").value }
    fetch("/consult_user", { 
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(obj_data)
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.status == "OK") {
            let user = data.name + "\n" + data.lastname + "\n" + data.birthday
            document.getElementById("txt-data").value = user
        }
        else {
            alert("The user doesn't exist")
            document.getElementById("txt-data").value = ""
        }
    })
}

    
