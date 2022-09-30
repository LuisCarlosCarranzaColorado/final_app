const newMedicoUrl = 'http://127.0.0.1:8000/newMedico';
//const newCustomerUrl = 'http://127.0.0.1:8000/newCustomer';

/*function validate_names(val) {
    const letters = /^[A-Z a-z]+$/;
    if (val.match(letters))
        return true;
    else
        return false;
}

function validate_id(val) {
    if (Number(val) > 1000)
        return true;
    else
        return false;
}

function validate_password(val) {
    if (val.length >= 5)
        return true;
    else
        return false;
}*/

function collectData(evt) {
    evt.preventDefault();

    const no_cedula = document.registro.no_cedula.value;
    const especialidad = document.registro.especialidad.value;

    /*let result = validate_id(id);
    if (!result) {
        alert('Cédula no es válida');
        return;
    }
    result = validate_names(firstName);
    if (!result) {
        alert('Nombre no es válido');
        return;
    }
    result = validate_names(lastName);
    if (!result) {
        alert('Apellido no es válido');
        return;
    }
    result = validate_password(password);
    if (!result) {
        alert('Contraseña no es válida. Debe tener al menos 5 caracteres.');
        return;
    }*/

    const medico = {
        no_cedula: no_cedula,
        especialidad: especialidad,
    }
    console.log(medico);
    const dataToSend = JSON.stringify(medico);
    saveCustomer(dataToSend);
}

function saveCustomer(data) {
    // Petición HTTP
    fetch(newMedicoUrl, {
        method: "POST",
        headers: {
            "Content-Type": "text/json"
        },
        body: data
    })
        .then(response => {
            console.log(response);
            if (response.ok)
                return response.text()
            else
                throw new Error(response.text());
        })
        .then(data => {
            console.log(data);
            handleSuccess();
        })
        .catch(error => {
            console.error("ERROR: ", error.message);
            handleError(error.message);
        });
}

function handleSuccess() {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerText = "Medico creado exitosamente.";
    const info = document.getElementById("info");
    info.appendChild(message);
}

function handleError(msg) {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerText = "No se pudo crear el medico. Intente luego. " + msg;
    const info = document.getElementById("info");
    info.appendChild(message);
}

// --------------------
document.registro.addEventListener("submit", collectData);