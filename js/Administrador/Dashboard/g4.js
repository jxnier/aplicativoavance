const grafica4 = document.getElementById("grafica4").getContext("2d");
const etiquetas4 = ["Depresion", "Bipolar tipo-1", "Bipolar tipo-2","Normal"]
const datosVentas20204 = {
    label: "Diagnosticos Mas comunes",
    data: [3, 4, 5, 7], // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
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