function publicar(){

    const obtenerYMostrarEventos = () => {
        axios.get("http://localhost:3000/obtener_eventos")  
            .then((response) => {
    
                const eventos = response.data;
                const eventosContainer = document.getElementById("eventosContainer");
    
                eventosContainer.innerHTML = ""; 
    
                eventos.forEach((evento) => {
                    const eventoHTML = `
                        <div class="col-md-6">
                            <div class="card mb-3">
                                <div class="card-body">
                                    <h3 class="card-title">${evento.titulo}</h3>
                                    <p class="card-text">${evento.contenido}</p>
                                    <p class="card-text">${evento.fecha}</p>
                                    <p class="card-text">${evento.nombre}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    eventosContainer.innerHTML += eventoHTML; 
                });
            })
            .catch((error) => {
                console.error("Error al obtener eventos:", error);
            });
    };
    
    const obtenerYMostrarConsejos = () => {
        axios.get("http://localhost:3000/obtener_consejos")  
            .then((response) => {
    
                const consejos = response.data;
                const consejosContainer = document.getElementById("ConsejosContainer");
    
                consejosContainer.innerHTML = ""; 
    
                consejos.forEach((consejo) => {
                    const consejoHTML = `
                        <div class="col-md-6">
                            <div class="card mb-3">
                                <div class="card-body">
                                    <h3 class="card-title">${consejo.titulo}</h3>
                                    <p class="card-text">${consejo.contenido}</p>
                                    <p class="card-text">${consejo.fecha}</p>
                                    <p class="card-text">${consejo.nombre}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    consejosContainer.innerHTML += consejoHTML; 
                });
            })
            .catch((error) => {
                console.error("Error al obtener consejos:", error);
            });
    };

    const obtenerYMostrarAnuncios = () => {
        axios.get("http://localhost:3000/obtener_anuncios")  
            .then((response) => {
    
                const anuncios = response.data;
                const anunciosContainer = document.getElementById("AnunciosContainer");
    
                anunciosContainer.innerHTML = ""; 
    
                anuncios.forEach((anuncio) => {
                    const eventoHTML = `
                        <div class="col-md-6">
                            <div class="card mb-3">
                                <div class="card-body">
                                    <h3 class="card-title">${anuncio.titulo}</h3>
                                    <p class="card-text">${anuncio.contenido}</p>
                                    <p class="card-text">${anuncio.fecha}</p>
                                    <p class="card-text">${anuncio.nombre}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    anunciosContainer.innerHTML += eventoHTML; 
                });
            })
            .catch((error) => {
                console.error("Error al obtener anuncio:", error);
            });
    };


    return { obtenerYMostrarConsejos, obtenerYMostrarEventos, obtenerYMostrarAnuncios};
};

window.onload = () => {
    const { obtenerYMostrarConsejos, obtenerYMostrarEventos, obtenerYMostrarAnuncios } = publicar();
    obtenerYMostrarConsejos();
    obtenerYMostrarEventos();
    obtenerYMostrarAnuncios();
};