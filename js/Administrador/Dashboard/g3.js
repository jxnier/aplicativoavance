const grafica3 = document.getElementById("grafica3").getContext("2d");
const etiquetas3 = ["Administrador", "Paciente", "Psicologo",]
const datosVentas20203 = {
    label: "Indice de registro al aplicativo",
    data: [2, 15,10], 
    backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de fondo
    borderColor: 'rgba(54, 162, 235, 1)', // Color del borde
    borderWidth: 1,// Ancho del borde
};
new Chart(grafica3, {
    type: 'bar',// Tipo de gráfica
    data: {
        labels: etiquetas3,
        datasets: [
            datosVentas20203,
            // Aquí más datos...
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