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