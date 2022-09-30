//const getCustomerUrl = 'https://mintic-bancoproj-g2.herokuapp.com/getOneCustomer/';
//const getCustomerUrl = 'http://127.0.0.1:8000/getOneCustomer/';
const getMedicoUrl = 'http://127.0.0.1:8000/getOneMedico/';

function getMedico() {
  const parsedUrl = new URL(window.location.href);
  console.log(parsedUrl+" ***URL PARSEADA");
  const id = parsedUrl.searchParams.get("id");
  console.log(id);
  const accessToken = sessionStorage.getItem("accessToken");
  const refreshToken = sessionStorage.getItem("refreshToken");
  console.log("Acá en el otro archivo: " + accessToken);
  console.log("Acá en el otro archivo: " + refreshToken);

  fetch(getMedicoUrl + id, {
    headers: {
      "Authorization": "Bearer " + accessToken
    }
  })
    .then(response => {
      console.log(response);
      if (response.ok || response.status == 400)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      console.log("Datos: " + data);
      if (data.includes("No existe cliente con esa cédula")) {
        handleError(data);
      }
      Medico = JSON.parse(data);
      handleCustomer(Medico);
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      handleError();
    });
}

function handleCustomer(Medico) {
  const accInfo = [];
  Medico.Pacientes.forEach(acc => {
    const singleAccInfo = `
      <li>nombres: ${acc.nombres}</li>
      <li>cedula: ${acc.cedula}</li>
      <li>enfermero: ${acc.enfermero}</li>
      `;
    accInfo.push(singleAccInfo);
  });
  const custDiv = document.createElement("div");
  custDiv.innerHTML = `
    <h3>Nombre: ${Medico.Nombre_medico}</h3>
    <h3>rol: ${Medico.rol}</h3>
    <h3>PACIENTES ASIGNADOS:</h3>`;
  accInfo.forEach(acc => custDiv.innerHTML += acc);
  document.getElementById("cargando").remove();
  const info = document.getElementById("info-customers");
  info.appendChild(custDiv);

  sessionStorage.setItem("fname", Medico.primer_nombre);
  sessionStorage.setItem("lname", Medico.primer_apellido);
  sessionStorage.setItem("email", Medico.email);
}

function handleError(err) {
  document.getElementById("cargando").remove();
  const message = document.createElement("p");
  if (err)
    message.innerText = err;
  else
    message.innerText = "No se pudo cargar la información. Intente más tarde.";
  const info = document.getElementById("info-customers");
  info.appendChild(message);
}

//-----------------------------------

document.addEventListener("DOMContentLoaded", getMedico);