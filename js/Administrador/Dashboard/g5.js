fetch('http://localhost:3000/grafica_tareas_psicologos')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('grafica_tareas_psicologos').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Cantidad de tareas',
          data: data.valores,
          backgroundColor: '#36A2EB'
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Distribución de tareas por psicólogo'
          }
        }
      }
    });
  })
  .catch(error => console.error(error));