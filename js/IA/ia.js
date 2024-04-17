function sendFormData() {
    // Capturar los valores de los campos del formulario
    var sadness = document.getElementById("Sadness").value;
    var exhausted = document.getElementById("Euphoric").value;
    var agotamiento = document.getElementById('agotamiento').value;
    var insomnio = document.getElementById('insomnio').value; 
    var actividad_sexual = document.getElementById('actividad_sexual').value; 
    var concentracion = document.getElementById('concentracion').value; 
    var optimismo = document.getElementById('optimismo').value; 
    var cambio_humor = document.getElementById('cambio_humor').value; 
    var pensamientos_suicidas = document.getElementById('pensamientos_suicidas').value; 
    var anorexia = document.getElementById('anorexia').value;
    var respeto_autoridad = document.getElementById('respeto_autoridad').value;
    var intentado_explicar = document.getElementById('intentado_explicar').value;
    var respuesta_agresiva = document.getElementById('respuesta_agresiva').value;
    var ignorar_problemas = document.getElementById('ignorar_problemas').value;
    var colapso_emocional = document.getElementById('colapso_emocional').value;
    var admitir_errores = document.getElementById('admitir_errores').value;
    var sobreanalizar = document.getElementById('sobreanalizar').value;
    // Captura los demás valores de la misma forma
  
    // Crear un objeto con los valores capturados
    var formData = {
      Sadness: sadness,
      Exhausted: exhausted,
      agotamiento:agotamiento,
      insomnio:insomnio,
      actividad_sexual:actividad_sexual,
      concentracion:concentracion,
      optimismo:optimismo,
      cambio_humor:cambio_humor,
      pensamientos_suicidas:pensamientos_suicidas,
      anorexia:anorexia,
      respeto_autoridad:respeto_autoridad,
      intentado_explicar:intentado_explicar,
      respuesta_agresiva:respuesta_agresiva,
      ignorar_problemas:ignorar_problemas,
      colapso_emocional:colapso_emocional,
      admitir_errores:admitir_errores,
      sobreanalizar:sobreanalizar
    };

    
    axios.post('http://localhost:3000/prediccion', formData)
      .then(function(response) {
        console.log('Trastorno mental predicho:', response.predicted_disorder);
      })
      .catch(function(error) {
        console.error('Error:', error);
      });
}
