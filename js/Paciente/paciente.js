let tu = JSON.parse(localStorage.getItem('tu'));
if (tu && tu.rol) {
    if (tu.rol === "paciente") {
        console.log("Bienvenido, paciente. Acceso permitido.");
    } else {
        localStorage.removeItem('tu');
        window.location.href = '../registrarse.html';
        alert("No ha iniciado sesión como Paciente. \nIngrese nuevamente.");
    }
} else {
    window.location.href = '../registrarse.html';
    alert("No has iniciado sesión. Acceso denegado.");
}

const cerrarsesion = () => {
    localStorage.removeItem("tu")
    window.location = "../../index.html";
}

function registrarAvancePersonal() {
    const contenido = document.getElementById('avance').value;
    if (!contenido.trim()) {
        alert('Por favor ingrese contenido para el avance personal.');
        return;
    }
    if (!tu.correo_institucional) {
        alert('No se ha detectado un correo válido para el paciente. Por favor, inicie sesión nuevamente.');
        return;
    }

    const avanceData = {
        contenido: contenido,
        correo_paciente: tu.correo_institucional 
    };  
    console.log(avanceData.correo_paciente)

    axios.post('http://localhost:3000/registrar_avance_personal', avanceData)
    .then(response => {
        console.log("Respuesta del servidor:", response);
        alert(response.data.mensaje);
        document.getElementById('avance').value = '';
        obtenerAvancesPersonales(); 
        })
    .catch(error => {
        console.error('Error al registrar el avance personal:', error);
        alert('Error al registrar el avance personal.');
        });
}


function obtenerAvancesPersonales() {
    if (tu.correo_institucional) {
        axios.get(`http://localhost:3000/obtener_avances?correo=${tu.correo_institucional}`)
            .then(function(response) {
                console.log(tu.correo_institucional); 
                const avances = response.data;
                mostrarAvances(avances); 
            })
            .catch(function(error) {
                console.error('Error al obtener los avances personales:', error);
            });
    } else {
        console.error('No se pudo obtener el correo electrónico del usuario.');
    }
}


function mostrarAvances(avances) {
    const avancesContainer = document.getElementById('avances-container');
    avancesContainer.innerHTML = '';
    avances.sort((a, b) => new Date(b.fecha_avance) - new Date(a.fecha_avance));
    if (avances.length > 0) {
        avances.forEach(function(avance) {
            const avanceElement = document.createElement('div');
            avanceElement.innerHTML = `
                <p>${avance.contenido}</p>
                <small>${avance.fecha_avance}</small>
                <button class="btn btn-danger btn-sm float-end" onclick="eliminarAvance('${avance.id_avance}')">Eliminar</button>
                <hr>
            `;
            avanceElement.style.backgroundColor = '#f0f0f0';
            avanceElement.style.border = '1px solid #ccc';
            avanceElement.style.padding = '10px';
            avanceElement.style.marginBottom = '10px';
            avancesContainer.appendChild(avanceElement);
        });
    } else {
        avancesContainer.innerHTML = "<p>No hay avances registrados.</p>";
    }
}

function eliminarAvance(idAvance) {
    if (confirm('¿Estás seguro de que deseas eliminar este avance?')) {
        axios.delete(`http://localhost:3000/eliminar_avance?id=${idAvance}`)
            .then(function(response) {
                alert(response.data.mensaje);
                obtenerAvancesPersonales(); 
            })
            .catch(function(error) {
                console.error('Error al eliminar el avance:', error);
                alert('Error al eliminar el avance.');
            });
    }
}

function sendFormData() {
    // Capturar los valores de los campos del formulario
    var sadness = document.getElementById("Sadness").value;
    var exhausted = document.getElementById("Euphoric").value;
    var agotamiento = document.getElementById('agotamiento').value;
    var insomnio = document.getElementById('insomnio').value;
    var actividad_sexual = document.getElementById('actividad_sexual').value;
    var concentracion = document.getElementById('concentracion').value;
    var optimismo = document.getElementById('optimismo').value;
    var cambio_humor = document.getElementById('cambio_humor').value;
    var pensamientos_suicidas = document.getElementById('pensamientos_suicidas').value;
    var anorexia = document.getElementById('anorexia').value;
    var respeto_autoridad = document.getElementById('respeto_autoridad').value;
    var intentado_explicar = document.getElementById('intentado_explicar').value;
    var respuesta_agresiva = document.getElementById('respuesta_agresiva').value;
    var ignorar_problemas = document.getElementById('ignorar_problemas').value;
    var colapso_emocional = document.getElementById('colapso_emocional').value;
    var admitir_errores = document.getElementById('admitir_errores').value;
    var sobreanalizar = document.getElementById('sobreanalizar').value;
  
    // Obtener el correo del paciente desde la variable `tu`
    const correoUsuario = tu.correo_institucional;
  
    // Crear un objeto con los valores capturados, incluyendo el correo del paciente
    var formData = {
      "Sadness": sadness,
      "Euphoric": agotamiento,
      "Exhausted": exhausted,
      "Sleep dissorder": insomnio,
      "Mood Swing": cambio_humor,
      "Suicidal thoughts":pensamientos_suicidas,
      "Anorxia": anorexia,
      "Authority Respect": respeto_autoridad,
      "Try-Explanation": intentado_explicar,
      "Aggressive Response": respuesta_agresiva,
      "Ignore & Move-On": ignorar_problemas,
      "Nervous Break-down": colapso_emocional,
      "Admit Mistakes": admitir_errores,
      "Overthinking": sobreanalizar,
      "Sexual Activity": actividad_sexual,
      "Concentration": concentracion,
      "Optimisim": optimismo,
    };
  
    // Enviar los datos al servidor utilizando Axios
    axios.post('http://localhost:3000/prediccion', formData)
    .then(function (response) {
      console.log(response.data.predicted_disorder);
      actualizarPrediccion(response.data.predicted_disorder); // Aquí se llama a actualizarPrediccion()
      alert("Sus resultados han sido enviado con exito a los psicologos!!");
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  function actualizarPrediccion(prediccion) {
    const correoPaciente = tu.correo_institucional; 
    const data = {
        correo_paciente: correoPaciente,
        prediccion_ia: prediccion
    };
    
    axios.post('http://localhost:3000/actualizar_prediccion', data)
        .then(response => {
            console.log(response.data.mensaje);
        })
        .catch(error => {
            console.error('Error al actualizar la predicción:', error);
        });
    
}


window.onload = function() {
    obtenerAvancesPersonales();
};