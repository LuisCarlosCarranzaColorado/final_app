const newUsuarioUrl = 'http://127.0.0.1:8000/newUsuario';
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
    const primer_nombre = document.registro.primer_nombre.value;
    const segundo_nombre = document.registro.segundo_nombre.value;
    const primer_apellido = document.registro.primer_apellido.value;
    const segundo_apellido = document.registro.segundo_apellido.value;
    const email = document.registro.email.value;
    const no_celular = document.registro.no_celular.value;
    const rol = document.registro.rol.value;
    const contrasena = document.registro.contrasena.value;
    const fecha_nacimiento = document.registro.fecha_nacimiento.value;
    const ubicacion_gps_latitud = document.registro.ubicacion_gps_latitud.value;
    const ubicacion_gps_longitud = document.registro.ubicacion_gps_longitud.value;

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

    const usuario = {
        no_cedula: no_cedula,
        primer_nombre: primer_nombre,
        segundo_nombre: segundo_nombre,
        primer_apellido: primer_apellido,
        segundo_apellido: segundo_apellido,
        email: email,
        no_celular: no_celular,
        rol: rol,
        contrasena: contrasena,
        fecha_nacimiento: fecha_nacimiento,
        ubicacion_gps_latitud: ubicacion_gps_latitud,
        ubicacion_gps_longitud: ubicacion_gps_longitud,
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