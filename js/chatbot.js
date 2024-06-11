document.addEventListener('DOMContentLoaded', function () {
    // TOGGLE CHATBOX
    const chatboxToggle = document.querySelector('.chatbox-toggle');
    const chatboxMessage = document.querySelector('.chatbox-message-wrapper');

    if (chatboxToggle && chatboxMessage) {
        chatboxToggle.addEventListener('click', function () {
            chatboxMessage.classList.toggle('show');
        });

        // Close chatbox when clicking outside
        document.addEventListener('click', function (e) {
            if (!chatboxMessage.contains(e.target) && !chatboxToggle.contains(e.target)) {
                chatboxMessage.classList.remove('show');
            }
        });
    }

    // DROPDOWN TOGGLE
    const dropdownToggle = document.querySelector('.chatbox-message-dropdown-toggle');
    const dropdownMenu = document.querySelector('.chatbox-message-dropdown-menu');

    if (dropdownToggle && dropdownMenu) {
        dropdownToggle.addEventListener('click', function () {
            dropdownMenu.classList.toggle('show');
        });

        document.addEventListener('click', function (e) {
            if (!e.target.matches('.chatbox-message-dropdown, .chatbox-message-dropdown *')) {
                dropdownMenu.classList.remove('show');
            }
        });
    }

    // CHATBOX MESSAGE
    const chatboxMessageWrapper = document.querySelector('.chatbox-message-content');
    const chatboxNoMessage = document.querySelector('.chatbox-message-no-message');
    const chatboxForm = document.querySelector('.chatbox-message-form'); // Correct variable name

    if (chatboxForm && chatboxMessageWrapper && chatboxNoMessage) {
        const textarea = chatboxForm.querySelector('.chatbox-message-input'); // Find textarea within chatboxForm

        // Add event listener to textarea for sending message on "Enter" press
        textarea.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault(); // Prevent default behavior of Enter key
                sendMessage(); // Call sendMessage function to send the message
            }
        });

        chatboxForm.addEventListener('submit', function (e) {
            e.preventDefault();
            sendMessage();
        });

        function sendMessage() {
            const userMessage = textarea.value.trim();
            if (isValid(userMessage)) {
                writeMessage(userMessage);
                const lowerCaseUserMessage = userMessage.toLowerCase();
                setTimeout(() => autoReply(lowerCaseUserMessage), 1000);
            }
        }

        function writeMessage(userMessage) {
            const today = new Date();
            let message = `
                <div class="chatbox-message-item sent">
                    <span class="chatbox-message-item-text">
                        ${userMessage.replace(/\n/g, '<br>\n')}
                    </span>
                    <span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
                </div>
            `;
            chatboxMessageWrapper.insertAdjacentHTML('beforeend', message);
            chatboxForm.style.alignItems = 'center';
            textarea.rows = 1;
            textarea.focus();
            textarea.value = '';
            chatboxNoMessage.style.display = 'none';
            scrollBottom();
        }

        function isValid(value) {
            let text = value.replace(/\n/g, '');
            text = text.replace(/\s/g, '');
            return text.length > 0;
        }

        function autoReply(lowerCaseUserMessage) {
            const today = new Date();
            const respuestas = [
                {
                    "preguntas": ["hola", "saludos", "buenos días", "ayuda","buenas","ayudenme","holi","ola", "hol", "ayudame", "necesito ayuda"],
                    "respuesta": "¡Hola! Soy Psique, su asistente virtual. ¿En qué puedo ayudarle?    1. ¿Dónde puedo pedir una cita?  2. ¿Para qué es la IA de predicción?  3. ¿Qué son las tareas?  4. ¿Como contactar con soporte sobre algun PQR ?  5. ¿Qué más actividades brinda la universidad para los estudiantes?    Por favor, elija el número de la pregunta que desea hacer."
                },
                {
                    "preguntas": ["1", "pedir citas", "cita", "citas",  "necesito una cita","quiero una cita"],
                    "respuesta": "Existen dos opciones para pedir una cita:  1. De manera presencial, acercándote hacia Bienestar institucional en las sedes Soledad o Barranquilla plaza de la paz.  2. De manera virtual, registrándote e iniciando sesión para pedir una cita.    Además, para solicitar atención médica o asesorías en salud, escríbe a salud@unibarranquilla.edu.co"
                },
                {
                    "preguntas": ["2", "IA", "predicción"],
                    "respuesta": "Cuando inicies sesión encontrarás el apartado de la IA 'amibot', que tiene un formulario el cual va a hacer una predicción, no un 100% certera, de tu estado, el cual será enviado a los psicólogos."
                },
                {
                    "preguntas": ["3", "tareas"],
                    "respuesta": "Las tareas son actividades que les irán dejando sus psicólogos y usted debería realizar, ya que esto le va a ayudar en sus avances."
                },
                {
                    "preguntas": ["4", "dudas", "quejas", "reclamos", "sugerencia"],
                    "respuesta": "Si usted tiene alguna queja, petición, reclamo o sugerencia (PQRS), en la parte final de la pagina INICIO existe un apartado de 'PQRS' donde nos puede contactar, o ya sea directamente al correo infoaplicativoiub@gmail.com."
                },
                {
                    "preguntas": ["5", "bienestar", "alternativas"],
                    "respuesta": "Bienestar institucional es el conjunto de acciones que propenden por el desarrollo físico, psico-afectivo, espiritual y social que contribuye al mejoramiento de la calidad de vida de los estudiantes, docentes y personal administrativo.  Desarrollo de actividades intencionalmente formativas que permitan la construcción de estilos de vida saludables, condiciones y hábitos alimentarios, prevención de uso de drogas, promoción de la salud sexual y reproductiva, en el contexto de la promoción de la salud y la prevención de la enfermedad.    Para más información, visita el siguiente link: www.unibarranquilla.edu.co/bienestar o contacta al responsable de Bienestar Universitario mfernandez@unibarranquilla.edu.co o bienestar@unibarranquilla.edu.co."
                },
                {
                    "preguntas": ["psicologo", "psico", "asesoramiento", "sesiones", "sugerencia", "ayuda emocional", "terapia", "psicoterapia", "consejería", "apoyo psicológico", "orientación emocional", "tratamiento psicológico", "recursos de salud y bienestar", "atención médica", "servicios de salud", "salud estudiantil", "nutrición", "bienestar general", "psicolgo", "psicologa"],
                    "respuesta": "Si usted necesita atención psicológica puede hacerlo con los psicólogos de la institución y su vez, puede ingresar al apartado de lineas de ayuda y canales de atención (que existen en esta misma página) que brindan asesorías psicológicas o emocionales."
                },
                {
                    "preguntas": ["ansiedad", "depresión", "estrés", "angustia", "trastornos emocionales", "tristeza", "desgaste mental", "cansancio", "me quiero matar", "me quiero morir"],
                    "respuesta": "¿Estás experimentando ansiedad, depresión, estrés, angustia u otros emociones que te están afectando? Nuestros profesionales de la salud mental están capacitados para ayudarte a manejar y superar estos desafíos. No estás solo, estamos aquí para apoyarte en tu proceso de recuperación. Te invitamos a ingresar al aplicativo o visita las lineas de ayuda."
                },
                {
                    "preguntas": ["costo", "cobertura", "pagar", "precio", "pago", "dinero", "hay que pagar?", "toca pagar", "tiene algun costo?", "toca pagar",  "hay que pagar",  "hay q pagar", "paga"],
                    "respuesta": "Nuestras asesorías psicológicas no tienen ningún valor o costo. ¡Son totalmente gratuitas!"
                },
                {
                    "preguntas": ["apoyo académico", "recursos académicos", "tutorías", "asistencia de estudio", "ayuda con los estudios", "soporte académico", "voy mal", "ayuda con los modulos", "voy perdiendo"],
                    "respuesta": "Unibarranquilla ofrece una variedad de servicios de apoyo académico, que incluyen tutorías individuales, talleres de estudio, asesoramiento académico, monitorias y padrinazos. Puedes obtener más información sobre estos servicios en nuestro sitio web o contactando a la oficina de bienestar académico y directamente en la página de la IUB."
                },
                {
                    "preguntas": ["actividades extracurriculares", "clubes estudiantiles", "grupos estudiantiles", "participación estudiantil", "eventos estudiantiles", "deporte", "musica", "baile", "danza"],
                    "respuesta": "Tenemos una amplia gama de actividades extracurriculares para que los estudiantes participen, que van desde clubes académicos hasta deportes y actividades de danza. Visita la página web de bienestar estudiantil para obtener más información sobre cómo involucrarte.   Para más información, visita el siguiente link: [https://www.unibarranquilla.edu.co/bienestar](https://www.unibarranquilla.edu.co/bienestar)"
                },
                {
                    "preguntas": ["atención médica", "enfermería prioritaria", "consulta médica"],
                    "respuesta": "Ofrecemos atención médica y de enfermería prioritaria para estudiantes. Esto incluye consultas médicas externas y asesorías sobre temas de salud. Te invitamos a acercarte presencialmente a Bienestar para recibir estos servicios."
                },
                {
                    "preguntas": ["evaluación de peso", "hábitos alimenticios"],
                    "respuesta": "Realizamos evaluaciones de peso y ofrecemos asesoramiento sobre hábitos alimenticios saludables para promover un estilo de vida equilibrado. Para obtener estos servicios, visita Bienestar en la universidad."
                },
                {
                    "preguntas": ["talleres de estilos de vida saludables"],
                    "respuesta": "Organizamos talleres periódicos sobre estilos de vida saludables, donde los estudiantes pueden aprender hábitos y prácticas que promuevan su bienestar físico y mental. ¡Acércate a Bienestar para participar en estos talleres!"
                },
                {
                    "preguntas": ["jornadas de promoción de salud", "prevención de enfermedades"],
                    "respuesta": "Realizamos jornadas de promoción de salud para concientizar a los estudiantes sobre la prevención de enfermedades y fomentar hábitos saludables. Te esperamos en Bienestar para participar en estas actividades."
                },
                {
                    "preguntas": ["seguro contra accidentes"],
                    "respuesta": "Contamos con un seguro contra accidentes que cubre a los estudiantes en caso de lesiones o accidentes durante su tiempo en la universidad. Puedes obtener más información y activar tu seguro en la oficina de Bienestar."
                },
                {
                    "preguntas": ["enfermedades de transmisión sexual", "embarazos no deseados"],
                    "respuesta": "Ofrecemos actividades y asesorías sobre la prevención de enfermedades de transmisión sexual y embarazos no deseados para promover la salud sexual y reproductiva de los estudiantes. Visítanos en Bienestar para obtener asesoramiento y apoyo."
                },
                {
                    "preguntas": ["incapacidades", "transcripción de incapacidades"],
                    "respuesta": "Brindamos servicios de transcripción de incapacidades para estudiantes que lo requieran. Si necesitas este servicio, acércate a Bienestar para solicitarlo y recibir ayuda."
                },
                {
                    "preguntas": ["actividades de prevención", "promoción en salud"],
                    "respuesta": "Realizamos diversas actividades y talleres de prevención y promoción en salud para educar a los estudiantes sobre la importancia de cuidar su bienestar y prevenir enfermedades. ¡Ven a participar en nuestras actividades en Bienestar!"
                },
                {
                    "preguntas": ["valoración de deportistas", "seguimiento a artistas"],
                    "respuesta": "Proporcionamos valoración y seguimiento a deportistas y artistas para garantizar su salud y bienestar mientras practican su actividad. Si eres deportista o artista, te invitamos a visitarnos en Bienestar para recibir estos servicios."
                },
                {
                    "preguntas": ["solicitud de atención médica", "asesorías en salud", "contacto"],
                    "respuesta": "Para solicitar atención médica, asesorías en salud o más información, escríbenos a salud@unibarranquilla.edu.co. También puedes visitarnos en la oficina de Bienestar en la universidad. Estaremos encantados de ayudarte."
                },
                {
                    "preguntas": ["default"],
                    "respuesta": "Escriba 'Hola' para poder empezar a socializar contigo "
                }    
            ];
            let responseMessage = respuestas.find(respuesta => respuesta.preguntas.includes(lowerCaseUserMessage));
            if (!responseMessage) {
                responseMessage = respuestas.find(respuesta => respuesta.preguntas.includes('default'));
            }

            let message = `
                <div class="chatbox-message-item received">
                    <span class="chatbox-message-item-text">
                        ${responseMessage.respuesta}
                    </span>
                    <span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
                </div>
            `;

            chatboxMessageWrapper.insertAdjacentHTML('beforeend', message);

            const links = chatboxMessageWrapper.querySelectorAll('a');
            links.forEach(link => {
                link.addEventListener('click', function(event) {
                    event.preventDefault();
                    window.location.href = link.getAttribute('href');
                });
            });

            scrollBottom();
        }

        function addZero(num) {
            return num < 10 ? '0' + num : num;
        }

        function scrollBottom() {
            chatboxMessageWrapper.scrollTo(0, chatboxMessageWrapper.scrollHeight);
        }
    }
});            