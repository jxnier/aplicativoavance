fetch('http://localhost:3000/grafica_tipo_documento')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('grafica_tipo_documento').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Tipo de documento',
          data: data.values,
          backgroundColor: [
            '#FF6384',
            '#36A2EB'
          ]
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Distribución de pacientes por tipo de documento'
          }
        }
      }
    });
  })
  .catch(error => console.error(error));



  