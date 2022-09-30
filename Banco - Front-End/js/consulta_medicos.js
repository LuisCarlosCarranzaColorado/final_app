const getMedicosUrl = 'http://127.0.0.1:8000/getAllMedicos';
//const getMedicosUrl = 'https://minticreto3.herokuapp.com/getAllMedicos';
//const getCustomersUrl = 'http://127.0.0.1:8000/getAllCustomers';

medicos = [];

function getAllMedicos() {
  // Petición HTTP
  fetch(getMedicosUrl)
    .then(response => {
      console.log(response);
      if (response.ok)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      console.log("Datos: " + data);
      medicos = JSON.parse(data);
      handleMedicos();
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      handleError();
    });
}

function handleMedicos() {
  const divs = [];
  medicos.forEach((cust) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <h3>Especialidad: ${cust.especialidad}</h3>
      <h3>No_cedula: ${cust.no_cedula}</h3>
      `;
    divs.push(div);
  });
  document.getElementById("cargando").remove();
  const info = document.getElementById("info-medicos");
  divs.forEach(div => info.appendChild(div));
}

function handleError() {
  document.getElementById("cargando").remove();
  const message = document.createElement("p");
  message.innerText = "No se pudo cargar la información. Intente más tarde.";
  const info = document.getElementById("info-customers");
  info.appendChild(message);
}

//-----------------------------------

document.addEventListener("DOMContentLoaded", getAllMedicos);