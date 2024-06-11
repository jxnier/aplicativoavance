fetch('http://localhost:3000/tareas_completadas_por_psicologo')
  .then(response => response.json())
  .then(data => {
    // Datos recibidos
    const nombresPsicologos = data.nombres_psicologos;
    const cantidades = data.cantidades;

    // Configuración del gráfico
    const ctx = document.getElementById('grafica2').getContext('2d');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: nombresPsicologos,
        datasets: [{
          label: 'Cantidad de tareas completadas por psicólogo',
          data: cantidades,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  .catch(error => {
    console.error('Error al obtener los datos:', error);
  });
