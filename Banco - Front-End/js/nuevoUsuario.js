const newUsuarioUrl = 'http://127.0.0.1:8000/newUsuario';
//const newCustomerUrl = 'http://127.0.0.1:8000/newCustomer';

function validate_names(val) {
    const letters = /^[A-Z a-z]+$/;
    if (val.match(letters))
        return true;
    else
        return false;
}

function validate_cedula(val) {
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
}

function collectData(evt) {
    evt.preventDefault();

    const id = document.registro.id.value;
    const primer_nombre = document.registro.primer_nombre.value.trim();
    const segundo_nombre = document.registro.segundo_nombre.value.trim();
    const primer_apellido = document.registro.primer_apellido.value.trim();
    const segundo_apellido = document.registro.segundo_apellido.value.trim();
    const email = document.registro.email.value.trim();
    const no_celular = document.registro.no_celular.value.trim();
    const rol = document.registro.rol.value;
    const password = document.registro.password.value;

    let result = validate_cedula(id);
    if (!result) {
        alert('Cédula no es válida');
        return;
    }
    result = validate_names(primer_nombre);
    if (!result) {
        alert('Nombre no es válido');
        return;
    }
    result = validate_names(primer_apellido);
    if (!result) {
        alert('Apellido no es válido');
        return;
    }
    result = validate_password(password);
    if (!result) {
        alert('Contraseña no es válida. Debe tener al menos 5 caracteres.');
        return;
    }

    const usuario = {
        id: id,
        primer_nombre: primer_nombre,
        segundo_nombre: segundo_nombre,
        primer_apellido: primer_apellido,
        segundo_apellido: segundo_apellido,
        email: email,
        no_celular: no_celular,
        rol: rol,
        password: password
    }
    console.log(usuario);
    const dataToSend = JSON.stringify(usuario);
    saveUsuario(dataToSend);
}

function saveUsuario(data) {
    // Petición HTTP
    fetch(newUsuarioUrl, {
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
    message.innerText = "Usuario creado exitosamente.";
    const info = document.getElementById("info");
    info.appendChild(message);
    console.log("usuario creado");
    window.location.href = './login2.html';
    window.alert("usuario creado ok");
}

function handleError(msg) {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerText = "No se pudo crear el usuario. Intente luego. " + msg;
    const info = document.getElementById("info");
    info.appendChild(message);
}

// --------------------
document.registro.addEventListener("submit", collectData);