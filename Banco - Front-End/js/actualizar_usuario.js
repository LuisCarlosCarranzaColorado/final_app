//const updateCustomerUrl = 'https://mintic-bancoproj-g2.herokuapp.com/updateCustomer/';
const updateCustomerUrl = 'http://127.0.0.1:8000/updateUsuario/';

const userId = sessionStorage.getItem("clientId");

function validate_names(val) {
    const letters = /^[A-Z a-zÁÉÍÓÚáéíóúñ]+$/;
    if (val.match(letters))
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
    console.log(userId)
    evt.preventDefault();
    const primer_nombre = document.actualizar.primer_nombre.value.trim();
    const primer_apellido = document.actualizar.primer_apellido.value.trim();
    const email = document.actualizar.email.value.trim();
    const password = document.actualizar.password.value;

    let rasult = true;
    if (primer_nombre) {
        let result = validate_names(primer_nombre);
        if (!result) {
            alert('Nombre no es válido');
            return;
        }
    }
    if (primer_apellido) {
        result = validate_names(primer_apellido);
        if (!result) {
            alert('Apellido no es válido');
            return;
        }
    }
    if (password) {
        result = validate_password(password);
        if (!result) {
            alert('Contraseña no es válida. Debe tener al menos 5 caracteres.');
            return;
        }
    }

    const usuario = {}
    if (primer_nombre)
        usuario.primer_nombre = primer_nombre;
    if (primer_apellido)
        usuario.primer_apellido = primer_apellido;
    if (email)
        usuario.email = email;
    if (password)
        usuario.password = password;
    console.log(usuario);
    const dataToSend = JSON.stringify(usuario);
    updateCustomer(dataToSend);
}

function updateCustomer(data) {
    const accessToken = sessionStorage.getItem("accessToken");
    // Petición HTTP
    fetch(updateCustomerUrl + userId, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + accessToken
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
            alert('Datos actualizados');
            goBack();
        })
        .catch(error => {
            console.error("ERROR: ", error.message);
            alert('Error al actualizar datos');
            goBack();
        });
}

function goBack() {
    window.location.href = './cliente.html?id=' + userId;
}

function showOldData() {
    const oldFName = sessionStorage.getItem('primer_nombre');
    const oldLName = sessionStorage.getItem('primer_apellido');
    const oldEmail = sessionStorage.getItem('email');

    document.actualizar.primer_nombre.placeholder = oldFName;
    document.actualizar.primer_apellido.placeholder = oldLName;
    document.actualizar.email.placeholder = oldEmail;
}

// --------------------
document.actualizar.addEventListener("submit", collectData);
//document.addEventListener('DOMContentLoaded', showOldData);