const publicar = (event) => {    
    event.preventDefault();
    let tu = JSON.parse(localStorage.getItem('tu'));
    const titulo = document.getElementById("titulo").value;
    const contenido = document.getElementById("contenido").value;
    const tipo = document.getElementById("tipo").value;

    if (!contenido.trim()) {
        document.getElementById("error-message").style.display = "block";
        return;
    } else {
        document.getElementById("error-message").style.display = "none";
    }

    const data = {
        correo_institucional: tu.correo_institucional,
        titulo: titulo,
        contenido: contenido,
        tipo: tipo
    };
    axios.post("http://localhost:3000/Publicar", data)
        .then(() => {
            alert("Publicación creada correctamente");
            document.getElementById("publicarEventoForm").reset();
        })
        .catch((error) => {
            console.error("Error al publicar evento:", error);
            alert("Error al publicar evento. Por favor, inténtelo de nuevo más tarde.");
        });
};
