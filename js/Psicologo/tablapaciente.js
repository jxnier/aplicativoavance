$(document).ready(function() {
    $('#example').DataTable({
        "ajax": {
            "url": "http://localhost:3000/psico", 
            "type": "GET",
            "dataSrc": "" 
        },
        "columns": [
            { "data": "nombre" },
            { "data": "tipo_documento" },
            { "data": "identificacion" },
            { "data": "correo_institucional" },
            { "data": "grado_salud" }
        ],
        "initComplete": function(settings, json) {
            console.log("Datos recibidos:", json);
        }
    });
});
