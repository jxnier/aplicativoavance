function RegistrarPsicologo(event) {
    event.preventDefault(); 

    const nombre = document.getElementById("nombre").value;
    const contraseña = document.getElementById("contraseña").value;
    const correo_institucional = document.getElementById("correo_institucional").value;
    const identificacion = document.getElementById("identificacion").value;

    const errores = [];

    if (!/^\d{7,13}$/.test(identificacion)) {
        errores.push('El número de documento debe contener entre 7 y 13 números.');
    }

    if (!correo_institucional.endsWith('@unibarranquilla.edu.co') || correo_institucional.indexOf('@') === -1 || correo_institucional.indexOf('@') === 0) {
        errores.push('El correo institucional debe tener el dominio "@unibarranquilla.edu.co" y contener texto antes del "@".');
    }

    if (!/(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W|_]).{8,}/.test(contraseña)) {
        errores.push('La contraseña debe contener al menos 8 caracteres combinados entre caracteres especiales, números y letras mayúsculas y minúsculas.');
    }

    if (errores.length > 0) {
        alert('Debe corregir lo siguiente:\n' + errores.join('\n'));
    } else {
        const NuevoPsicologo = {
            nombre: nombre,
            contraseña: contraseña,
            correo_institucional: correo_institucional,
            identificacion: identificacion
        };
        axios.post("http://localhost:3000/registrar_psicologo", NuevoPsicologo)
            .then((response) => {
                alert("Mensaje: "+response.data.mensaje);
            })
            .catch((error) => {
                console.error('Error al enviar datos al servidor:', error);
                alert('Error al registrar Psicologo(a). Por favor, inténtelo de nuevo más tarde.');
            });
    }
}