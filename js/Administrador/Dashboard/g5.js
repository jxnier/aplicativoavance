document.addEventListener('DOMContentLoaded', function() {
    const grafica5 = document.getElementById("grafica5").getContext("2d");
    const etiquetas5 = ["Pedir cita", "Prediagnostico por la IA", "Lineas de atención", "Avances"];
    const datosVentas20203 = {
        label: "Funciones más utilizadas del aplicativo",
        data: [50, 70, 60, 41],
        backgroundColor: 'rgba(173, 216, 230, 0.5)', // Color de fondo
        borderColor: 'rgba(100, 230, 100, 1)',
        borderWidth: 1
    };
    new Chart(grafica5, {
        type: 'bar',
        data: {
            labels: etiquetas5,
            datasets: [
                datosVentas20203,
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
            },
        }
    });
});