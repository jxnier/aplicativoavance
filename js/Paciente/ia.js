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

  // Crear un objeto con los valores capturados
  var formData = {
    "Sadness": sadness,
    "Euphoric": agotamiento,
    "Exhausted": exhausted,
    "Sleep dissorder": insomnio,
    "Mood Swing": cambio_humor,
    "Suicidal thoughts":pensamientos_suicidas,
    "Anorxia": anorexia,
    "Authority Respect": respeto_autoridad,
    "Try-Explanation": intentado_explicar,
    "Aggressive Response": respuesta_agresiva,
    "Ignore & Move-On": ignorar_problemas,
    "Nervous Break-down": colapso_emocional,
    "Admit Mistakes": admitir_errores,
    "Overthinking": sobreanalizar,
    "Sexual Activity": actividad_sexual,
    "Concentration": concentracion,
    "Optimisim": optimismo
  };
  console.log(formData)
  // Enviar los datos al servidor utilizando Axios
  axios.post('http://localhost:3000/prediccion', formData)
    .then(function (response) {
      console.log(response.data.predicted_disorder);
      // Mostrar el trastorno mental predicho en la interfaz de usuario
      alert(`Trastorno mental predicho: ${response.data.predicted_disorder}`);
    })
    .catch(function (error) {
      console.log(error);
    });
}