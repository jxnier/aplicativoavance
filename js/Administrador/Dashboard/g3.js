fetch('http://localhost:3000/grafica_predicciones_ia')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('grafica_predicciones_ia').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Cantidad de pacientes',
          data: data.valores,
          backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Distribución de pacientes por predicción de IA'
          }
        }
      }
    });
  })
  .catch(error => console.error(error));