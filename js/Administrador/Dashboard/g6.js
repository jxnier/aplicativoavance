document.addEventListener('DOMContentLoaded', function() {
  const grafica6 = document.getElementById("grafica6").getContext("2d");
  const etiquetas6 = ["Malo ", "Regular", "Bueno", "Muy bueno"];
  const datosVentas20203 = {
      label: "Satisfacción por el aplicativo",
      data: [10, 50, 40, 100],
      backgroundColor: 'rgba(0, 102, 204, 0.5)',
      borderColor: 'rgba(0, 51, 102, 1)',
      borderWidth: 1,
  };
  new Chart(grafica6, {
      type: 'bar',
      data: {
          labels: etiquetas6,
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