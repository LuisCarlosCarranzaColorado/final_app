//const getCustomerUrl = 'https://mintic-bancoproj-g2.herokuapp.com/getOneCustomer/';
//const getCustomerUrl = 'http://127.0.0.1:8000/getOneCustomer/';
const getMedicoUrl = 'http://127.0.0.1:8000/getOneMedico/';

function getMedico() {
  const parsedUrl = new URL(window.location.href);
  //console.log("que hay en window.location.href: "+window.location.href);
  //console.log("URL guardada  "+parsedUrl);
  const id = parsedUrl.searchParams.get("id");
  //console.log("busco id en URL: "+id);
  const accessToken = sessionStorage.getItem("accessToken");
  const refreshToken = sessionStorage.getItem("refreshToken");
  const clientId = sessionStorage.getItem("clientId");
  const nombre = sessionStorage.getItem("primer_nombre");
  //console.log("token guardado en login: " + accessToken);
  //console.log("refresh guardado en login: " + refreshToken);
  //console.log("id_guardada guardado en login: " + clientId);
  //console.log("nombre guardado en login: " + nombre);

  fetch(getMedicoUrl + id, {
    headers: {
      "Authorization": "Bearer " + accessToken
    }
  })
    .then(response => {
      //console.log("repuesta promesa: "+response);
      if (response.ok || response.status == 400)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      //console.log("Datos en la promesa: " + data);
      if (data.includes("No existe cliente con esa cédula")) {
        handleError(data);
      }
      Medico = JSON.parse(data);
      handleMedico(Medico);
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      handleError();
    });
}

function handleMedico(Medico) {
  const accInfo = [];
  Medico.Pacientes.forEach(paciente => {
    const pacientes = `
      <li>nombres: ${paciente.nombres}</li>
      <li>cedula: ${paciente.cedula}</li>
      <li>enfermero: ${paciente.enfermero}</li>
      <li>------------------------------------</li>
      `;
    //console.log(paciente)
    accInfo.push(pacientes);
  });
  console.log(accInfo)
  const usuarios = document.createElement("div");
  //div.style.backgroundColor = "#6ab150";
  usuarios.innerHTML = `
    <h3>Nombre: ${Medico.Nombre_medico}</h3>
    <h3>rol: ${Medico.rol}</h3>
    <h3>especialidad: ${Medico.especialidad}</h3>
    <h4>PACIENTES ASIGNADOS:</h4>`;
  console.log(usuarios)
  accInfo.forEach(x => usuarios.innerHTML += x);
  console.log(accInfo)
  document.getElementById("cargando").remove();
  const info = document.getElementById("info-customers");
  info.appendChild(usuarios);

  sessionStorage.setItem("nombre_medico", Medico.Nombre_medico);
  sessionStorage.setItem("medico_rol", Medico.rol);
  sessionStorage.setItem("medico_especialidad", Medico.especialidad);
  const especialidad = sessionStorage.getItem("medico_especialidad");
  //console.log("especialidad guardada: "+especialidad)

}

function handleError(err) {
  document.getElementById("cargando").remove();
  const message = document.createElement("p");
  if (err)
    message.innerText = err;
  else
    message.innerText = "Aún no se ha asociado un médico tratante, intente más tarde o póngase en contacto con su hospital.";
  const info = document.getElementById("info-customers");
  info.appendChild(message);
}

//-----------------------------------

document.addEventListener("DOMContentLoaded", getMedico);