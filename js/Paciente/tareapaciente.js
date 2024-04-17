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
                const listaTareasPendientes = document.getElementById('tareaspendientes');
                tareasAsignadas.forEach(tarea => {
                    const tareaElemento = document.createElement('li');
                    tareaElemento.innerHTML = `
                        <strong>Título:</strong> ${tarea.titulo}<br>
                        <strong>Descripción:</strong> ${tarea.descripcion}<br>
                        <strong>Psicólogo asignado:</strong> ${tarea.nombre_psicologo}<br>
                        <button class="btn btn-primary marcar-completada" data-id="${tarea.id}" >Marcar como completada</button>
                        <hr>
                    `;
                    listaTareasPendientes.appendChild(tareaElemento);
                });

                document.querySelectorAll('.marcar-completada').forEach(boton => {
                    boton.addEventListener('click', function () {
                        const tareaId = boton.dataset.id;
                        console.log(tareaId)
                        
                        axios.post('http://localhost:3000/marcar_como_completada', { tarea_id: tareaId })
                            .then(function(response) {
                                
                                const tareaCompletada = boton.parentNode;
                                const listaTareasCompletadas = document.getElementById('tareascompletadas');
                                listaTareasCompletadas.appendChild(tareaCompletada);
                            })
                            .catch(function (error) {
                                console.error('Error al marcar la tarea como completada:', error);
                            });
                    });
                });
            })
            .catch(function (error) {
                console.error('Error al obtener las tareas:', error);
            });
    } else {
        console.log('No hay usuario logueado');
    }
});
