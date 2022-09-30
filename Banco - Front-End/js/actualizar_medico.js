//const updateCustomerUrl = 'https://mintic-bancoproj-g2.herokuapp.com/updateCustomer/';
const updateCustomerUrl = 'http://127.0.0.1:8000/updateMedico/';

const clientId = sessionStorage.getItem("clientId");
//console.log(clientId)

function collectData(evt) {
    //console.log(clientId)
    evt.preventDefault();
    const especialidad = document.actualizar.especialidad.value.trim();

    const medico = {}
    medico.especialidad = especialidad;
    console.log(medico);
    const dataToSend = JSON.stringify(medico);
    updateMedico(dataToSend);
}

function updateMedico(data) {
    const accessToken = sessionStorage.getItem("accessToken");
    // Petición HTTP
    fetch(updateCustomerUrl + clientId, {
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
            //console.log("datos devueltos a la promesa:  "+data);
            goBack();
            alert(data);
            
        })
        .catch(error => {
            console.error("ERROR: ", error.message);
            alert('Error al actualizar datos');
            goBack();
        });
}

function goBack() {
    //window.location.href = './medico.html?id=' + data.clientId;
    window.location.href = './medico.html?id=' + clientId;
}

function showOldData() {
    const especialidad = sessionStorage.getItem('medico_especialidad');
    document.actualizar.especialidad.placeholder = especialidad;
}

// --------------------
document.actualizar.addEventListener("submit", collectData);
document.addEventListener('DOMContentLoaded', showOldData);