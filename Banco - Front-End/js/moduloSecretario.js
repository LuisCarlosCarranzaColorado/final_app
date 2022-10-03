//const getMedicosUrl = 'http://127.0.0.1:8000/getAllMedicos';
//const getMedicosUrl = 'https://minticreto3.herokuapp.com/getAllMedicos';
const getUsuariosUrl = 'http://127.0.0.1:8000/getAllUsuarios';

usuario = [];

function getUsuarios() {
  // Petición HTTP
  fetch(getUsuariosUrl)
    .then(response => {
      //console.log(response);
      if (response.ok){
        //console.log("respuesta del JSON: "+response.ok)
        return response.text()
      }
        else{
        throw new Error(response.status);
        }
    })
    .then(
    data => {
            //console.log("Datos: " + data);
            Usuario = JSON.parse(data);
            //console.log("datos del json:\n"+Usuario);
            handleUsuarios(Usuario);
            }
        )
    .catch(error => {
      console.error("ERROR: ", error.message);
      //handleError();
    });
}

function handleUsuarios(Usuario) {
  arrayUsuarios = []
  
  Usuario.forEach(user => {
    let info = 
    `<table id="usuarios">
    <tr>
      <td>${user.primer_nombre}</td>
      <td>${user.primer_apellido}</td>
      <td>${user.id}</td>
      <td>${user.rol}</td>
    </tr>
    </table>`
  arrayUsuarios.push(info)
  });
  const usuarios = document.createElement("div");
  arrayUsuarios.forEach(x => usuarios.innerHTML += x);
  document.getElementById("contenedorCargando").remove();
  const contenedor = document.getElementById("contenedor1");
  contenedor.appendChild(usuarios);

}

function handleError() {
  document.getElementById("contenedorCargando").remove();
  const message = document.createElement("p");
  message.innerText = "No se pudo cargar la información. Intente más tarde.";
  const info = document.getElementById("contenedor1");
  info.appendChild(message);
}

//-----------------------------------

document.addEventListener("DOMContentLoaded", getUsuarios);