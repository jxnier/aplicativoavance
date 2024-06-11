// Registrar Paciente
const registrar_paciente = (event) => {
    event.preventDefault();

    var nombre = document.getElementById('nombreregister').value;
    var tipoDocumento = document.getElementById('tipodocumentoregister').value;
    var numeroDocumento = document.getElementById('documentoregister').value;
    var correo = document.getElementById('correoregister').value;
    var contraseña = document.getElementById('contraseñaregister').value;

    var errores = [];

    if (!/^\d{7,13}$/.test(numeroDocumento)) {
        errores.push('El número de documento debe contener entre 7 y 13 números.');
    }

    if (!correo.endsWith('@unibarranquilla.edu.co') || correo.indexOf('@') === -1 || correo.indexOf('@') === 0) {
        errores.push('El correo institucional debe tener el dominio "@unibarranquilla.edu.co" y contener texto antes del "@".');
    }

    if (!/(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W|_]).{8,}/.test(contraseña)) {
        errores.push('La contraseña debe contener al menos 8 caracteres combinados entre caracteres especiales, números y letras mayúsculas y minúsculas.');
    }

    if (errores.length > 0) {
        alert('Debe corregir lo siguiente:\n' + errores.join('\n'));
    } else {
        var pacienteNuevo = {
            nombre: nombre,
            tipo_documento: tipoDocumento,
            documento: numeroDocumento,
            correo: correo,
            contraseña: contraseña
        };
        axios.post("http://localhost:3000/registrar_paciente", pacienteNuevo)
            .then((response) => {
                url = response.data.link;
                window.location.replace(url)
                alert('¡Registro exitoso!, ahora inicie sesión con su correo institucional y contraseña')
            })
            .catch((error) => {
                console.error('Error al enviar datos al servidor:', error);
                alert('Error al registrarse. Por favor, inténtelo de nuevo más tarde.');
            });
    }
};

document.getElementById('register-form').addEventListener('submit', registrar_paciente);

// Iniciar sesión

const login = () => {
    const rol = document.getElementById('rol').value;
    const correo_institucional = document.getElementById('correo_institucional').value;
    const contraseña = document.getElementById('contraseña').value;
    const nombre = document.getElementById('nombreregister').value;

    if (!correo_institucional || !contraseña || !rol) {
        alert('Por favor, complete todos los campos.');
        return;
    }

    const nuevoingreso = {
        nombre: nombre,
        rol: rol,
        correo_institucional: correo_institucional,
        contraseña: contraseña
    };

    axios.post("http://localhost:3000/iniciar_sesion", nuevoingreso)
        .then((response) => {
            if (response.data.mensaje == "Credenciales de administrador incorrectas") {
                alert("Credenciales de administrador incorrectas");
            } else {
                if (response.data.mensaje == "Paciente: Correo institucional o contraseña incorrecta") {
                    alert("Paciente: Correo institucional o contraseña incorrecta");
                } else {
                    if (response.data.mensaje == "Psicólogo: Correo institucional o contraseña incorrecta") {
                        alert("Psicólogo: Correo institucional o contraseña incorrecta");
                    } else {
                        const url = response.data.link;
                        window.location.replace(url);
                        const tu = {
                            rol: rol,
                            correo_institucional: correo_institucional,
                            nombre: response.data.nombre
                        };
                        localStorage.setItem("tu", JSON.stringify(tu));
                    }
                }
            }
        })
        .catch((error) => {
            console.error('Error al iniciar sesión:', error);
            alert('Error al iniciar sesión. Por favor, inténtelo de nuevo más tarde.');
        });
};

document.getElementById('login').addEventListener('click', login);