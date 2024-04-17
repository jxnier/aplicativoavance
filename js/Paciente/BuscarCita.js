function buscarCitas() {
    const btnBuscarCitas = document.getElementById("buscarCitas");
    const fechaInput = document.getElementById("fecha");
    const listaCitas = document.getElementById("listaCitas");
    btnBuscarCitas.addEventListener("click", function () {
        const fecha = fechaInput.value;
        // Crear objeto con la fecha
        const requestData = { fecha: fecha };
        console.log(requestData)
        axios.get('http://localhost:3000/buscar_citas', { params: requestData })
            .then((response) => {
                console.log("entro js xd")
                const citas = response.data;
                listaCitas.innerHTML = '';
                citas.forEach(function (cita) {
                    // Crear elemento de lista para cada cita
                    const citaItem = document.createElement('li');
                    citaItem.classList.add('list-group-item');
                    citaItem.innerHTML = `
                        <strong>Psicólogo:</strong> ${cita.nombre_psicologo}<br>
                        <strong>Fecha:</strong> ${cita.fecha}<br>
                        <strong>Hora:</strong> ${cita.hora}<br>
                        <strong>Sede:</strong> ${cita.sede}<br>
                        <button class="btn btn-success mt-2">Agendar</button>
                    `;
                    listaCitas.appendChild(citaItem);
                });
            })
            .catch((error) => {
                console.error('Error al xd buscar citas:', error);
            });
    });
}

buscarCitas(); // Llamar a la función al cargar el script
