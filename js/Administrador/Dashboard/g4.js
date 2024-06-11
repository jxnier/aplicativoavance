fetch('http://localhost:3000/grafica_tipos_publicaciones')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('grafica_tipos_publicaciones').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Cantidad de publicaciones',
          data: data.valores,
          backgroundColor: ['#F1AA2FF', '#36A2EB', '#FFCE56', '#8BC34A']
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Distribución de publicaciones por tipo'
          }
        }
      }
    });
  })
  .catch(error => console.error(error));