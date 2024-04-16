const grafica4 = document.getElementById("grafica4").getContext("2d");
const etiquetas4 = ["Enero", "Febrero", "Marzo", "Abril"]
const datosVentas20204 = {
    label: "Ingreso al aplicativo - Mujeres",
    data: [5000, 1700, 8000, 722], // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
    backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de fondo
    borderColor: 'rgba(54, 162, 235, 1)', // Color del borde
    borderWidth: 1,// Ancho del borde
};
const datosVentas20214 = {
    label: "Ingreso al aplicativo - Hombres",
    data: [4000, 1700, 5000, 589], // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
    backgroundColor: 'rgba(255, 159, 64, 0.2)',// Color de fondo
    borderColor: 'rgba(255, 159, 64, 1)',// Color del borde
    borderWidth: 1,// Ancho del borde
};

new Chart(grafica4, {
    type: 'bar',// Tipo de gráfica
    data: {
        labels: etiquetas4,
        datasets: [
            datosVentas20204,
            datosVentas20214,
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