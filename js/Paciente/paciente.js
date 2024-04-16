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

// Función para registrar un avance personal
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


window.onload = function() {
    obtenerAvancesPersonales();
};