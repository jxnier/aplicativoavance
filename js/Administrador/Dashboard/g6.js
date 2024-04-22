fetch('http://localhost:3000/pacientes_por_tipo_documento_y_prediccion_ia')
  .then(response => response.json())
  .then(data => {
    // Datos recibidos
    const resultados = data.resultados;

    // Agrupación de datos por tipo de documento
    const tiposDocumento = {};
    resultados.forEach(resultado => {
      if (!tiposDocumento[resultado.tipo_documento]) {
        tiposDocumento[resultado.tipo_documento] = {};
      }
      tiposDocumento[resultado.tipo_documento][resultado.prediccion_ia] = resultado.cantidad_pacientes;
    });

    // Configuración del gráfico
    const ctx = document.getElementById('grafica6').getContext('2d');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: Object.keys(tiposDocumento),
        datasets: Object.keys(tiposDocumento['CC']).map(prediccionIA => ({
          label: prediccionIA,
          data: Object.values(tiposDocumento).map(obj => obj[prediccionIA] || 0),
          backgroundColor: getRandomColor(),
          borderColor: getRandomColor(),
          borderWidth: 1
        }))
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

// Función para generar colores aleatorios
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
