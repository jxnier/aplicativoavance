const obtenerPerfilUsuario = () => {
    const url = '/obtener_perfil';
    const correoUsuario = localStorage.getItem('correo');

    axios.get(url, { params: { correo: correoUsuario } })
        .then(response => {
            const perfil = response.data;
            console.log('Perfil del usuario:', perfil);
            document.getElementById('nombre').innerText = perfil.nombre;
            document.getElementById('tipo_documento').innerText = perfil.tipo_documento;
            document.getElementById('identificacion').innerText = perfil.identificacion;
            document.getElementById('correo_institucional').innerText = perfil.correo_institucional;
        })
        .catch(error => {
            console.error('Error:', error);
        });
};

obtenerPerfilUsuario();
