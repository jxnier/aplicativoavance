let tu = JSON.parse(localStorage.getItem('tu'));
if (tu && tu.rol) {
    if (tu.rol === "psicologo") {
        console.log("Bienvenido, psicólogo(a). Acceso permitido.");
    } else {
        localStorage.removeItem('tu');
        window.location.href = '../registrarse.html';
        alert("No ha iniciado sesión como Psicólogo(a). \nIngrese nuevamente.");
    }
} else {
    window.location.href = '../registrarse.html';
    alert("No has iniciado sesión. Acceso denegado.");
}

const cerrarsesion = () =>{
    localStorage.removeItem("tu")
    window.location="../../index.html";
}

document.addEventListener("DOMContentLoaded", function () {
    axios.get('http://localhost:3000/allpaciente')
        .then(function (response) {
            response.data.forEach(function (paciente) {
                var option = document.createElement('option');
                option.value = paciente.id;
                option.text = paciente.nombre + ' - ' + paciente.identificacion;
                document.getElementById('paciente').appendChild(option);
            });
        })
        .catch(function (error) {
            console.error('Error fetching patients:', error);
        });
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("tareaForm").addEventListener("submit", function (event) {
        event.preventDefault();

        var titulo = document.getElementById("titulo").value;
        var descripcion = document.getElementById("descripcion").value;
        var pacienteId = document.getElementById("paciente").value;

        var tarea = {
            psicologo_id: tu.correo_institucional,
            paciente_id: pacienteId,
            titulo: titulo,
            descripcion: descripcion
        };

        axios.post('http://localhost:3000/registrar_tarea', tarea)
            .then(function (response) {
                console.log('Tarea registrada con éxito:', response.data);
                document.getElementById("modalMessage").innerText = "Tarea registrada con éxito";
                $('#resultadoModal').modal('show');
                // Limpiar los campos del formulario
                document.getElementById("titulo").value = "";
                document.getElementById("descripcion").value = "";
            })
            .catch(function (error) {
                console.error('Error al registrar la tarea:', error);
                document.getElementById("modalMessage").innerText = "Error al registrar la tarea";
                $('#resultadoModal').modal('show');
            });
    });
});