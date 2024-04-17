$(document).ready(function() {
    $('#example').DataTable({
        "ajax": {
            "url": "http://localhost:3000/tabla",
            "type": "GET",
            "dataSrc": function(json) {
                let data = [];

                // Agregar pacientes
                if (json.pacientes) {
                    data = data.concat(json.pacientes.map(function(paciente) {
                        return {
                            "id": paciente.id,
                            "nombre": paciente.nombre ?? "", // Establecer como cadena vacía si es null
                            "identificacion": paciente.identificacion ?? "", // Establecer como cadena vacía si es null
                            "correo_institucional": paciente.correo_institucional ?? "" // Establecer como cadena vacía si es null
                        };
                    }));
                }

                // Agregar psicologos
                if (json.psicologos) {
                    data = data.concat(json.psicologos.map(function(psicologo) {
                        return {
                            "id": psicologo.id,
                            "nombre": psicologo.nombre ?? "", // Establecer como cadena vacía si es null
                            "identificacion": psicologo.identificacion ?? "", // Establecer como cadena vacía si es null
                            "correo_institucional": psicologo.correo_institucional ?? "" // Establecer como cadena vacía si es null
                        };
                    }));
                }

                return data;
            }
        },
        "columns": [
            { "data": "id" },
            { "data": "nombre" },
            { "data": "identificacion" },
            { "data": "correo_institucional" }
        ],
        "initComplete": function(settings, json) {
            console.log("Datos recibidos:", json);
        }
    });
});
