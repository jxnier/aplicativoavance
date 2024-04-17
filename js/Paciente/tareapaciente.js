document.addEventListener("DOMContentLoaded", function () {
    // Obtener el usuario actual del almacenamiento local
    const usuario = JSON.parse(localStorage.getItem('tu'));

    if (usuario) {
        // Obtener el correo electrónico del usuario
        const correoUsuario = usuario.correo_institucional;

        // Realizar una solicitud GET a la ruta /mistareas con el correo del usuario como parámetro
        axios.get(`http://localhost:3000/mistareas?usuario=${correoUsuario}`)
            .then(function (response) {
                const tareasAsignadas = response.data;

                // Mostrar las tareas asignadas en el HTML
                const listaTareas = document.getElementById('lista-tareas');
                tareasAsignadas.forEach(tarea => {
                    const tareaElemento = document.createElement('li');
                    tareaElemento.innerHTML = `
                        <strong>Título:</strong> ${tarea.titulo}<br>
                        <strong>Descripción:</strong> ${tarea.descripcion}<br>
                        <strong>Psicólogo asignado:</strong> ${tarea.nombre_psicologo}<br>
                        <hr>
                    `;
                    listaTareas.appendChild(tareaElemento);
                });
            })
            .catch(function (error) {
                console.error('Error al obtener las tareas:', error);
            });
    } else {
        console.log('No hay usuario logueado');
    }
});
