//const getMedicosUrl = 'http://127.0.0.1:8000/getAllMedicos';
//const getMedicosUrl = 'https://minticreto3.herokuapp.com/getAllMedicos';
const getUsuariosUrl = 'http://127.0.0.1:8000/getPacientes';

usuario = [];

function getPacientes() {
  // Petición HTTP
  fetch(getUsuariosUrl)
    .then(response => {
      //console.log(response);
      if (response.ok)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(text => {
      //console.log("Datos: " + data);
      usuario = JSON.parse(text);
      console.log(usuario);
      handleUsuarios();
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      //handleError();
    });
}

function handleUsuarios() {
 
  const divs = [];

  usuario.forEach((paciente) => {
    const div = document.createElement("li");
    div.innerHTML = paciente.primer_nombre + " " + paciente.primer_apellido 
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

document.addEventListener("DOMContentLoaded", getPacientes);